"""Analysis utilities for benchmark results."""
import json
from pathlib import Path
from typing import Dict, List, Optional
import argparse


def load_summary(results_dir: Path) -> Dict:
    """Load benchmark summary JSON."""
    summary_file = results_dir / "benchmark_summary.json"
    if not summary_file.exists():
        raise FileNotFoundError(f"Summary file not found: {summary_file}")
    
    with open(summary_file) as f:
        return json.load(f)


def compare_skills(
    summary: Dict,
    metric: str = "avg_duration",
    top_n: int = 10
) -> List[tuple]:
    """
    Compare skills by a specific metric.
    
    Args:
        summary: Loaded benchmark summary
        metric: Metric to compare (avg_duration, total_cost, total_tokens)
        top_n: Number of top results to return
        
    Returns:
        List of (skill_name, value) tuples sorted by metric
    """
    skills_data = summary.get('skills', {})
    
    results = []
    for skill_name, skill_metrics in skills_data.items():
        if metric in skill_metrics:
            results.append((skill_name, skill_metrics[metric]))
    
    # Sort based on metric (lower is better for most metrics)
    reverse = metric in ['successful', 'total_runs']  # Higher is better for these
    results.sort(key=lambda x: x[1], reverse=reverse)
    
    return results[:top_n]


def calculate_efficiency_scores(summary: Dict) -> Dict[str, Dict]:
    """
    Calculate efficiency scores combining speed, cost, and success rate.
    
    Returns composite scores for trade-off analysis.
    """
    skills_data = summary.get('skills', {})
    
    efficiency_scores = {}
    
    for skill_name, metrics in skills_data.items():
        if metrics['total_runs'] == 0:
            continue
        
        # Normalize metrics (lower is better, scale 0-1)
        success_rate = metrics['successful'] / metrics['total_runs']
        
        # Speed score (faster = better)
        # Assume 60s is good, normalize
        speed_score = max(0, 1 - (metrics.get('avg_duration', 60) / 300))  # 300s = 5min baseline
        
        # Cost score (cheaper = better)
        # Assume $0.10 per run is baseline
        avg_cost = metrics['total_cost'] / max(metrics['total_runs'], 1)
        cost_score = max(0, 1 - (avg_cost / 0.50))  # $0.50 baseline
        
        # Composite score (weighted average)
        # Success is most important, then cost, then speed
        composite = (
            0.5 * success_rate +
            0.3 * cost_score +
            0.2 * speed_score
        )
        
        efficiency_scores[skill_name] = {
            'success_rate': success_rate,
            'speed_score': speed_score,
            'cost_score': cost_score,
            'composite_score': composite,
            'avg_duration': metrics.get('avg_duration', 0),
            'avg_cost': avg_cost,
            'total_runs': metrics['total_runs'],
        }
    
    return efficiency_scores


def print_comparison_table(results: List[tuple], metric_name: str, format_fn=None):
    """Print a formatted comparison table."""
    print(f"\n{'='*60}")
    print(f"Comparison by: {metric_name}")
    print(f"{'='*60}\n")
    print(f"{'Rank':<6} {'Skill':<30} {'Value':<20}")
    print("-" * 60)
    
    for rank, (skill, value) in enumerate(results, 1):
        if format_fn:
            value_str = format_fn(value)
        else:
            value_str = str(value)
        
        print(f"{rank:<6} {skill:<30} {value_str:<20}")


def print_efficiency_scores(efficiency_scores: Dict):
    """Print efficiency scores in a formatted table."""
    print(f"\n{'='*80}")
    print(f"Efficiency Scores (Composite: 50% success, 30% cost, 20% speed)")
    print(f"{'='*80}\n")
    print(f"{'Skill':<25} {'Success':<10} {'Cost':<10} {'Speed':<10} {'Composite':<10}")
    print("-" * 80)
    
    # Sort by composite score
    sorted_skills = sorted(
        efficiency_scores.items(),
        key=lambda x: x[1]['composite_score'],
        reverse=True
    )
    
    for skill, scores in sorted_skills:
        print(
            f"{skill:<25} "
            f"{scores['success_rate']:.3f}     "
            f"{scores['cost_score']:.3f}     "
            f"{scores['speed_score']:.3f}     "
            f"{scores['composite_score']:.3f}"
        )


def generate_analysis_report(results_dir: Path, output_file: Optional[Path] = None):
    """Generate comprehensive analysis report."""
    summary = load_summary(results_dir)
    
    report = []
    report.append("# Benchmark Analysis Report\n\n")
    
    # Overall summary
    overall = summary.get('summary', {})
    report.append("## Overall Statistics\n\n")
    report.append(f"- Total Runs: {overall.get('total_runs', 0)}\n")
    report.append(f"- Success Rate: {overall.get('success_rate', 0):.1%}\n")
    report.append(f"- Total Duration: {overall.get('total_duration', 0):.1f}s\n")
    report.append(f"- Total Cost: ${overall.get('total_cost', 0):.2f}\n\n")
    
    # Top performers by speed
    speed_rankings = compare_skills(summary, 'avg_duration', top_n=5)
    report.append("## Fastest Skills (Avg Duration)\n\n")
    for rank, (skill, duration) in enumerate(speed_rankings, 1):
        report.append(f"{rank}. **{skill}**: {duration:.1f}s\n")
    report.append("\n")
    
    # Most cost-effective
    cost_rankings = compare_skills(summary, 'total_cost', top_n=5)
    report.append("## Most Cost-Effective Skills\n\n")
    for rank, (skill, cost) in enumerate(cost_rankings, 1):
        report.append(f"{rank}. **{skill}**: ${cost:.3f}\n")
    report.append("\n")
    
    # Efficiency scores
    efficiency = calculate_efficiency_scores(summary)
    sorted_efficiency = sorted(
        efficiency.items(),
        key=lambda x: x[1]['composite_score'],
        reverse=True
    )
    
    report.append("## Composite Efficiency Scores\n\n")
    report.append("*Weighted: 50% success rate, 30% cost efficiency, 20% speed*\n\n")
    for rank, (skill, scores) in enumerate(sorted_efficiency[:10], 1):
        report.append(
            f"{rank}. **{skill}**: {scores['composite_score']:.3f} "
            f"(success: {scores['success_rate']:.2f}, "
            f"cost: ${scores['avg_cost']:.3f}, "
            f"speed: {scores['avg_duration']:.1f}s)\n"
        )
    
    report_text = ''.join(report)
    
    if output_file:
        output_file.write_text(report_text)
        print(f"✅ Analysis report saved to: {output_file}")
    
    print(report_text)


def main():
    """Main analysis CLI."""
    parser = argparse.ArgumentParser(description="Analyze benchmark results")
    parser.add_argument(
        "--results-dir",
        type=Path,
        default=Path(__file__).parent / "results",
        help="Path to benchmark results directory"
    )
    parser.add_argument(
        "--metric",
        choices=['duration', 'cost', 'tokens', 'efficiency', 'all'],
        default='all',
        help="Metric to analyze"
    )
    parser.add_argument(
        "--output",
        type=Path,
        help="Output file for analysis report"
    )
    parser.add_argument(
        "--top-n",
        type=int,
        default=10,
        help="Number of top results to show"
    )
    
    args = parser.parse_args()
    
    if not args.results_dir.exists():
        print(f"❌ Results directory not found: {args.results_dir}")
        return
    
    try:
        summary = load_summary(args.results_dir)
        
        if args.metric == 'all':
            generate_analysis_report(args.results_dir, args.output)
        else:
            if args.metric == 'duration':
                results = compare_skills(summary, 'avg_duration', args.top_n)
                print_comparison_table(
                    results,
                    "Average Duration",
                    lambda x: f"{x:.2f}s"
                )
            elif args.metric == 'cost':
                results = compare_skills(summary, 'total_cost', args.top_n)
                print_comparison_table(
                    results,
                    "Total Cost",
                    lambda x: f"${x:.4f}"
                )
            elif args.metric == 'tokens':
                results = compare_skills(summary, 'total_tokens', args.top_n)
                print_comparison_table(
                    results,
                    "Total Tokens",
                    lambda x: f"{x:,}"
                )
            elif args.metric == 'efficiency':
                efficiency = calculate_efficiency_scores(summary)
                print_efficiency_scores(efficiency)
    
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
