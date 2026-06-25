from __future__ import annotations

import argparse
import re
import sys
from collections import Counter
from dataclasses import dataclass
from datetime import date, datetime
from pathlib import Path
from typing import Iterable, List, Sequence
from urllib.parse import urlparse

import requests


REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_INDEX = REPO_ROOT / "skills" / "provider-source-index.md"
SKILLS_ROOT = REPO_ROOT / "skills"
DATE_RE = re.compile(r"^Last refreshed:\s*(\d{4}-\d{2}-\d{2})\.", re.MULTILINE)
ROW_RE = re.compile(r"^\|\s*`([^`]+)`\s*\|\s*([^|]+?)\s*\|", re.MULTILINE)


@dataclass
class SourceEntry:
    skill: str
    source: str


@dataclass
class CheckResult:
    ok: bool
    message: str


def parse_refreshed_date(text: str) -> date | None:
    match = DATE_RE.search(text)
    if not match:
        return None
    return date.fromisoformat(match.group(1))


def parse_source_entries(text: str) -> List[SourceEntry]:
    entries = []
    for skill, source in ROW_RE.findall(text):
        if skill == "Skill" or source.strip() == "Source":
            continue
        entries.append(SourceEntry(skill=skill.strip(), source=source.strip()))
    return entries


def expected_skill_names(skills_root: Path = SKILLS_ROOT) -> List[str]:
    return sorted(path.name for path in skills_root.iterdir() if path.is_dir())


def check_source_index(
    index_path: Path = DEFAULT_INDEX,
    *,
    max_age_days: int = 30,
    today: date | None = None,
) -> List[CheckResult]:
    today = today or datetime.now().date()
    if not index_path.exists():
        return [CheckResult(False, f"missing source index: {index_path}")]

    text = index_path.read_text(encoding="utf-8")
    results: List[CheckResult] = []

    refreshed = parse_refreshed_date(text)
    if refreshed is None:
        results.append(CheckResult(False, "missing Last refreshed date"))
    else:
        age = (today - refreshed).days
        results.append(
            CheckResult(
                age <= max_age_days,
                f"Last refreshed {refreshed.isoformat()} ({age} days old)",
            )
        )

    entries = parse_source_entries(text)
    indexed_skills = {entry.skill for entry in entries}
    duplicate_entries = sorted(
        f"{skill} -> {source}"
        for (skill, source), count in Counter(
            (entry.skill, entry.source) for entry in entries
        ).items()
        if count > 1
    )
    if duplicate_entries:
        results.append(
            CheckResult(
                False,
                "duplicate source index rows: " + ", ".join(duplicate_entries),
            )
        )
    for skill_name in expected_skill_names(index_path.parent):
        results.append(
            CheckResult(
                skill_name in indexed_skills,
                f"{skill_name}: {'indexed' if skill_name in indexed_skills else 'missing'}",
            )
        )

    return results


def check_link(entry: SourceEntry, repo_root: Path = REPO_ROOT, timeout: float = 10.0) -> CheckResult:
    parsed = urlparse(entry.source)
    if parsed.scheme in {"http", "https"}:
        try:
            response = requests.get(
                entry.source,
                timeout=timeout,
                allow_redirects=True,
                headers={"User-Agent": "awesome-deep-researchers-source-check/0.1"},
            )
        except requests.RequestException as exc:
            return CheckResult(False, f"{entry.skill}: {entry.source} failed: {exc}")
        ok = 200 <= response.status_code < 400
        return CheckResult(ok, f"{entry.skill}: {entry.source} HTTP {response.status_code}")

    local_path = repo_root / entry.source
    return CheckResult(local_path.exists(), f"{entry.skill}: {entry.source} local path")


def check_links(index_path: Path = DEFAULT_INDEX) -> List[CheckResult]:
    text = index_path.read_text(encoding="utf-8")
    return [check_link(entry) for entry in parse_source_entries(text)]


def format_results(results: Iterable[CheckResult]) -> str:
    lines = []
    for result in results:
        status = "PASS" if result.ok else "FAIL"
        lines.append(f"{status}\t{result.message}")
    return "\n".join(lines)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Check provider source freshness and coverage.")
    parser.add_argument("--index", type=Path, default=DEFAULT_INDEX, help="Source index markdown file.")
    parser.add_argument("--max-age-days", type=int, default=30, help="Maximum allowed index age.")
    parser.add_argument(
        "--check-links",
        action="store_true",
        help="Also perform live HTTP/local path checks for indexed sources.",
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    results = check_source_index(args.index, max_age_days=args.max_age_days)
    if args.check_links and args.index.exists():
        results.extend(check_links(args.index))
    print(format_results(results))
    return 0 if all(result.ok for result in results) else 1


if __name__ == "__main__":
    sys.exit(main())
