"""Scoring rubric for evaluating benchmark results quality."""
import json
from typing import Dict, List, Optional
from dataclasses import dataclass
from pathlib import Path


@dataclass
class QualityScore:
    """Quality evaluation score for a benchmark result."""
    
    # Objective metrics (computed automatically)
    completeness: float = 0.0  # 0-1: Output length / expected length
    structure: float = 0.0  # 0-1: Has sections, formatting
    citations: float = 0.0  # 0-1: Number and quality of citations
    
    # Subjective metrics (require human evaluation)
    accuracy: Optional[float] = None  # 0-1: Factual correctness
    relevance: Optional[float] = None  # 0-1: On-topic, addresses question
    depth: Optional[float] = None  # 0-1: Level of analysis
    
    # Overall
    objective_score: float = 0.0  # Average of objective metrics
    subjective_score: Optional[float] = None  # Average of subjective (if evaluated)
    combined_score: Optional[float] = None  # Weighted combination
    
    notes: str = ""
    
    def calculate_objective_score(self) -> float:
        """Calculate average of objective metrics."""
        metrics = [self.completeness, self.structure, self.citations]
        self.objective_score = sum(metrics) / len(metrics)
        return self.objective_score
    
    def calculate_subjective_score(self) -> Optional[float]:
        """Calculate average of subjective metrics (if available)."""
        metrics = [m for m in [self.accuracy, self.relevance, self.depth] if m is not None]
        if not metrics:
            return None
        self.subjective_score = sum(metrics) / len(metrics)
        return self.subjective_score
    
    def calculate_combined_score(
        self,
        objective_weight: float = 0.3,
        subjective_weight: float = 0.7
    ) -> Optional[float]:
        """
        Calculate weighted combination of objective and subjective scores.
        
        Args:
            objective_weight: Weight for objective metrics (default 0.3)
            subjective_weight: Weight for subjective metrics (default 0.7)
        """
        if self.subjective_score is None:
            return None
        
        self.combined_score = (
            objective_weight * self.objective_score +
            subjective_weight * self.subjective_score
        )
        return self.combined_score


class ResultScorer:
    """Score benchmark results for quality evaluation."""
    
    @staticmethod
    def score_completeness(output: str, question: str) -> float:
        """
        Score output completeness.
        
        Heuristic: ratio of output length to expected length.
        Expected length varies by question type.
        """
        if not output:
            return 0.0
        
        # Expected minimum lengths by category (characters)
        expected_lengths = {
            "source_retrieval": 500,
            "cross_validation": 800,
            "domain_mapping": 1000,
            "technical_decomposition": 1200,
            "quantitative_synthesis": 800,
            "regulatory": 700,
            "scholarly_synthesis": 1000,
            "bias_uncertainty": 800,
            "multi_domain": 1500,
            "executive_summarization": 600,
        }
        
        # Use average as default
        expected = sum(expected_lengths.values()) / len(expected_lengths)
        
        # Score: min(actual / expected, 1.0)
        return min(len(output) / expected, 1.0)
    
    @staticmethod
    def score_structure(output: str) -> float:
        """
        Score output structure and formatting.
        
        Checks for:
        - Section headers
        - Bullet points or numbered lists
        - Paragraph breaks
        - Proper formatting
        """
        score = 0.0
        
        # Check for headers (markdown style)
        if any(line.startswith('#') for line in output.split('\n')):
            score += 0.3
        
        # Check for lists
        lines = output.split('\n')
        has_bullets = any(line.strip().startswith(('*', '-', '•')) for line in lines)
        has_numbers = any(line.strip()[:3].rstrip('.').isdigit() for line in lines)
        if has_bullets or has_numbers:
            score += 0.3
        
        # Check for paragraph breaks (multiple newlines)
        if '\n\n' in output:
            score += 0.2
        
        # Check for reasonable line length (not one giant paragraph)
        avg_line_length = sum(len(line) for line in lines) / max(len(lines), 1)
        if avg_line_length < 200:  # Reasonable line breaks
            score += 0.2
        
        return min(score, 1.0)
    
    @staticmethod
    def score_citations(output: str) -> float:
        """
        Score citation quality.
        
        Checks for:
        - URLs
        - References
        - Source attributions
        """
        score = 0.0
        
        # Count URLs
        import re
        urls = re.findall(r'https?://[^\s]+', output)
        if urls:
            # Score based on number of citations (cap at 10)
            score += min(len(urls) / 10, 0.5)
        
        # Check for citation markers [1], (Source: ...), etc.
        citation_patterns = [
            r'\[\d+\]',  # [1], [2]
            r'\(Source:',  # (Source: ...)
            r'\(Ref:',  # (Ref: ...)
            r'According to',  # According to X
        ]
        
        for pattern in citation_patterns:
            if re.search(pattern, output):
                score += 0.2
                break
        
        # Check for reference section
        if re.search(r'(References?|Sources?|Citations?):', output, re.IGNORECASE):
            score += 0.3
        
        return min(score, 1.0)
    
    @staticmethod
    def score_result(output: str, question: str, category: str) -> QualityScore:
        """
        Score a benchmark result automatically (objective metrics only).
        
        Args:
            output: The skill's output text
            question: The original question
            category: Question category
            
        Returns:
            QualityScore with objective metrics computed
        """
        score = QualityScore()
        
        score.completeness = ResultScorer.score_completeness(output, question)
        score.structure = ResultScorer.score_structure(output)
        score.citations = ResultScorer.score_citations(output)
        
        score.calculate_objective_score()
        
        return score
    
    @staticmethod
    def score_benchmark_results(results_dir: Path) -> Dict:
        """
        Score all results in a benchmark results directory.
        
        Args:
            results_dir: Path to benchmark/results directory
            
        Returns:
            Dictionary with scores for all results
        """
        scores = {}
        
        # Find all metrics files
        for metrics_file in results_dir.rglob("*_metrics.json"):
            with open(metrics_file) as f:
                metrics = json.load(f)
            
            # Score the result
            quality = ResultScorer.score_result(
                output=metrics.get('output', ''),
                question=metrics.get('question', ''),
                category=metrics.get('category', '')
            )
            
            # Store score
            skill_name = metrics.get('skill_name', 'unknown')
            category = metrics.get('category', 'unknown')
            
            if skill_name not in scores:
                scores[skill_name] = {}
            if category not in scores[skill_name]:
                scores[skill_name][category] = []
            
            scores[skill_name][category].append({
                'question': metrics.get('question', ''),
                'completeness': quality.completeness,
                'structure': quality.structure,
                'citations': quality.citations,
                'objective_score': quality.objective_score,
            })
        
        return scores
    
    @staticmethod
    def generate_quality_report(results_dir: Path, output_file: Optional[Path] = None) -> str:
        """
        Generate a quality assessment report.
        
        Args:
            results_dir: Path to benchmark/results directory
            output_file: Optional path to save report
            
        Returns:
            Markdown report string
        """
        scores = ResultScorer.score_benchmark_results(results_dir)
        
        report = []
        report.append("# Benchmark Quality Assessment Report\n")
        report.append("## Objective Quality Scores\n")
        report.append("Metrics: Completeness, Structure, Citations\n\n")
        
        # Overall statistics
        all_scores = []
        for skill_scores in scores.values():
            for category_scores in skill_scores.values():
                all_scores.extend([s['objective_score'] for s in category_scores])
        
        if all_scores:
            avg_score = sum(all_scores) / len(all_scores)
            report.append(f"**Overall Average Score**: {avg_score:.3f}\n\n")
        
        # Per-skill breakdown
        report.append("## Scores by Skill\n\n")
        report.append("| Skill | Avg Completeness | Avg Structure | Avg Citations | Overall Score |\n")
        report.append("|-------|------------------|---------------|---------------|---------------|\n")
        
        for skill in sorted(scores.keys()):
            skill_results = []
            for category_scores in scores[skill].values():
                skill_results.extend(category_scores)
            
            if skill_results:
                avg_completeness = sum(r['completeness'] for r in skill_results) / len(skill_results)
                avg_structure = sum(r['structure'] for r in skill_results) / len(skill_results)
                avg_citations = sum(r['citations'] for r in skill_results) / len(skill_results)
                avg_overall = sum(r['objective_score'] for r in skill_results) / len(skill_results)
                
                report.append(
                    f"| {skill} | {avg_completeness:.3f} | {avg_structure:.3f} | "
                    f"{avg_citations:.3f} | {avg_overall:.3f} |\n"
                )
        
        report_text = ''.join(report)
        
        if output_file:
            output_file.write_text(report_text)
        
        return report_text


def main():
    """Generate quality report for existing benchmark results."""
    import argparse
    
    parser = argparse.ArgumentParser(description="Score benchmark results for quality")
    parser.add_argument(
        "--results-dir",
        type=Path,
        default=Path(__file__).parent / "results",
        help="Path to benchmark results directory"
    )
    parser.add_argument(
        "--output",
        type=Path,
        help="Output file for quality report"
    )
    
    args = parser.parse_args()
    
    if not args.results_dir.exists():
        print(f"Error: Results directory not found: {args.results_dir}")
        return
    
    report = ResultScorer.generate_quality_report(
        args.results_dir,
        args.output
    )
    
    print(report)
    
    if args.output:
        print(f"\n✅ Quality report saved to: {args.output}")


if __name__ == "__main__":
    main()
