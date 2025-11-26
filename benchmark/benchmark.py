"""Main benchmark runner for evaluating deep research skills."""
import argparse
import subprocess
import sys
from pathlib import Path
from typing import List, Dict, Optional
import json
from datetime import datetime

from .config import RESULTS_DIR, SKILL_TIMEOUT
from .utils import (
    discover_skills,
    parse_taxonomy_questions,
    get_skill_command_info,
    sanitize_filename,
    format_duration,
)
from .tracker import BenchmarkTracker, BenchmarkMetrics


class BenchmarkRunner:
    """Run benchmarks across skills and questions."""
    
    def __init__(self, output_dir: Optional[Path] = None, verbose: bool = False):
        self.output_dir = output_dir or RESULTS_DIR
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.verbose = verbose
        self.tracker = BenchmarkTracker()
    
    def log(self, message: str, level: str = "INFO") -> None:
        """Log a message."""
        timestamp = datetime.now().strftime("%H:%M:%S")
        print(f"[{timestamp}] [{level}] {message}", file=sys.stderr)
    
    def run_skill(
        self,
        skill: Dict[str, str],
        question: str,
        category: str
    ) -> BenchmarkMetrics:
        """
        Run a single skill on a single question.
        
        Args:
            skill: Skill information dictionary
            question: Research question
            category: Question category
            
        Returns:
            BenchmarkMetrics object with results
        """
        metrics = self.tracker.create_run(
            skill_name=skill['name'],
            category=category,
            question=question
        )
        
        metrics.start()
        
        try:
            # Get command info for this skill
            cmd_info = get_skill_command_info(skill['name'])
            
            # Check for special requirements
            if cmd_info.get('requires_server'):
                self.log(f"⚠️  {skill['name']} requires external server - skipping", "WARN")
                metrics.set_error("Requires external server (e.g., LangGraph)")
                metrics.end()
                return metrics
            
            # Build command
            command = cmd_info['command'].format(
                script=skill['script_path'],
                question=f'"{question}"'
            )
            
            if self.verbose:
                self.log(f"Running: {command}")
            
            # Run the skill
            result = subprocess.run(
                command,
                shell=True,
                capture_output=True,
                text=True,
                timeout=SKILL_TIMEOUT
            )
            
            # Capture output
            output = result.stdout
            if result.returncode != 0:
                error_output = result.stderr
                metrics.set_error(f"Exit code {result.returncode}: {error_output}")
                self.log(f"❌ {skill['name']} failed: {error_output[:100]}", "ERROR")
            else:
                metrics.set_output(output)
                
                # Extract model info and calculate cost
                model_info = BenchmarkMetrics.extract_model_info(output, result.stderr)
                metrics.add_metadata("provider", model_info["provider"])
                metrics.add_metadata("model", model_info["model"])
                metrics.calculate_cost(model_info["model"], model_info["provider"])
                
                # Extract API calls
                api_calls = BenchmarkMetrics.extract_api_calls_from_output(output)
                metrics.add_metadata("api_calls", api_calls)
                
                if self.verbose:
                    self.log(
                        f"✅ {skill['name']} completed in {format_duration(metrics.duration_seconds)}"
                    )
        
        except subprocess.TimeoutExpired:
            metrics.set_error(f"Timeout after {SKILL_TIMEOUT} seconds")
            self.log(f"⏱️  {skill['name']} timed out", "ERROR")
        
        except Exception as e:
            metrics.set_error(str(e))
            self.log(f"❌ {skill['name']} error: {str(e)}", "ERROR")
        
        finally:
            metrics.end()
        
        return metrics
    
    def save_individual_result(
        self,
        metrics: BenchmarkMetrics,
        skill_name: str,
        category: str,
        question_idx: int
    ) -> None:
        """Save individual run result to file."""
        # Create directory structure: results/{skill_name}/{category}/
        skill_dir = self.output_dir / skill_name / sanitize_filename(category)
        skill_dir.mkdir(parents=True, exist_ok=True)
        
        # Save full metrics as JSON
        metrics_file = skill_dir / f"q{question_idx + 1}_metrics.json"
        with open(metrics_file, 'w') as f:
            json.dump(metrics.to_dict(), f, indent=2)
        
        # Save output separately for easy reading
        if metrics.success:
            output_file = skill_dir / f"q{question_idx + 1}_output.txt"
            with open(output_file, 'w') as f:
                f.write(f"Question: {metrics.question}\n")
                f.write(f"Category: {category}\n")
                f.write(f"Duration: {format_duration(metrics.duration_seconds)}\n")
                f.write(f"Cost: ${metrics.estimated_cost_usd:.4f}\n")
                f.write(f"Tokens: {metrics.total_tokens}\n")
                f.write(f"\n{'='*80}\n\n")
                f.write(metrics.output)
    
    def run_benchmark(
        self,
        skills: Optional[List[str]] = None,
        categories: Optional[List[str]] = None,
        max_questions: int = 3
    ) -> None:
        """
        Run the full benchmark suite.
        
        Args:
            skills: List of skill names to test (None = all)
            categories: List of categories to test (None = all)
            max_questions: Maximum questions per category
        """
        self.log("🚀 Starting benchmark run")
        
        # Discover skills
        all_skills = discover_skills()
        if skills:
            all_skills = [s for s in all_skills if s['name'] in skills]
        
        self.log(f"📦 Found {len(all_skills)} skills to test")
        
        # Parse questions
        all_questions = parse_taxonomy_questions()
        if categories:
            all_questions = {k: v for k, v in all_questions.items() if k in categories}
        
        # Limit questions per category
        for cat in all_questions:
            all_questions[cat] = all_questions[cat][:max_questions]
        
        total_questions = sum(len(q) for q in all_questions.values())
        self.log(f"📝 Found {len(all_questions)} categories with {total_questions} total questions")
        
        # Run benchmarks
        total_runs = len(all_skills) * total_questions
        current_run = 0
        
        self.log(f"🎯 Total benchmark runs: {total_runs}")
        self.log("")
        
        for skill in all_skills:
            self.log(f"Testing skill: {skill['name']}")
            
            for category, questions in all_questions.items():
                for idx, question in enumerate(questions):
                    current_run += 1
                    
                    self.log(
                        f"[{current_run}/{total_runs}] "
                        f"{skill['name']} | {category} | Q{idx + 1}/3"
                    )
                    
                    # Run the skill
                    metrics = self.run_skill(skill, question, category)
                    
                    # Save results
                    self.save_individual_result(metrics, skill['name'], category, idx)
                    
                    # Show summary
                    if metrics.success:
                        self.log(
                            f"  ✓ Duration: {format_duration(metrics.duration_seconds)}, "
                            f"Cost: ${metrics.estimated_cost_usd:.4f}, "
                            f"Output: {metrics.output_length} chars"
                        )
                    else:
                        self.log(f"  ✗ Failed: {metrics.error[:100]}")
                    
                    self.log("")
        
        # Save aggregated results
        self.save_summary()
        
        self.log("✅ Benchmark complete!")
    
    def save_summary(self) -> None:
        """Save summary statistics and aggregated results."""
        summary_file = self.output_dir / "benchmark_summary.json"
        self.tracker.save_to_json(str(summary_file))
        self.log(f"📊 Summary saved to: {summary_file}")
        
        # Generate markdown report
        self.generate_markdown_report()
    
    def generate_markdown_report(self) -> None:
        """Generate a human-readable markdown report."""
        report_file = self.output_dir / "benchmark_report.md"
        
        summary = self.tracker.get_summary()
        
        with open(report_file, 'w') as f:
            f.write("# Deep Research Skills Benchmark Report\n\n")
            f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            
            f.write("## Overall Summary\n\n")
            f.write(f"- **Total Runs**: {summary.get('total_runs', 0)}\n")
            f.write(f"- **Successful**: {summary.get('successful', 0)}\n")
            f.write(f"- **Failed**: {summary.get('failed', 0)}\n")
            f.write(f"- **Success Rate**: {summary.get('success_rate', 0):.1%}\n")
            f.write(f"- **Total Duration**: {format_duration(summary.get('total_duration', 0))}\n")
            f.write(f"- **Total Cost**: ${summary.get('total_cost', 0):.2f}\n")
            f.write(f"- **Total Tokens**: {summary.get('total_tokens', 0):,}\n\n")
            
            f.write("## Results by Skill\n\n")
            f.write("| Skill | Runs | Success | Avg Duration | Total Cost | Tokens |\n")
            f.write("|-------|------|---------|--------------|------------|--------|\n")
            
            for skill_name in sorted(set(r.skill_name for r in self.tracker.runs)):
                skill_summary = self.tracker.get_skill_summary(skill_name)
                f.write(
                    f"| {skill_name} "
                    f"| {skill_summary['total_runs']} "
                    f"| {skill_summary['successful']}/{skill_summary['total_runs']} "
                    f"| {format_duration(skill_summary['avg_duration'])} "
                    f"| ${skill_summary['total_cost']:.2f} "
                    f"| {skill_summary['total_tokens']:,} |\n"
                )
            
            f.write("\n## Results by Category\n\n")
            f.write("| Category | Runs | Success | Avg Duration | Total Cost |\n")
            f.write("|----------|------|---------|--------------|------------|\n")
            
            for category in sorted(set(r.category for r in self.tracker.runs)):
                cat_summary = self.tracker.get_category_summary(category)
                f.write(
                    f"| {category} "
                    f"| {cat_summary['total_runs']} "
                    f"| {cat_summary['successful']}/{cat_summary['total_runs']} "
                    f"| {format_duration(cat_summary['avg_duration'])} "
                    f"| ${cat_summary['total_cost']:.2f} |\n"
                )
            
            f.write("\n---\n\n")
            f.write("*See `benchmark_summary.json` for detailed metrics.*\n")
        
        self.log(f"📄 Report saved to: {report_file}")


def main():
    """Main entry point for benchmark CLI."""
    parser = argparse.ArgumentParser(
        description="Benchmark deep research skills across taxonomy questions"
    )
    parser.add_argument(
        "--skills",
        nargs="+",
        help="Specific skills to test (default: all)"
    )
    parser.add_argument(
        "--categories",
        nargs="+",
        help="Specific categories to test (default: all)"
    )
    parser.add_argument(
        "--max-questions",
        type=int,
        default=3,
        help="Maximum questions per category (default: 3)"
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        help="Output directory for results"
    )
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Verbose output"
    )
    
    args = parser.parse_args()
    
    runner = BenchmarkRunner(
        output_dir=args.output_dir,
        verbose=args.verbose
    )
    
    try:
        runner.run_benchmark(
            skills=args.skills,
            categories=args.categories,
            max_questions=args.max_questions
        )
    except KeyboardInterrupt:
        print("\n\n⚠️  Benchmark interrupted by user")
        runner.save_summary()
        sys.exit(1)
    except Exception as e:
        print(f"\n\n❌ Benchmark failed: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
