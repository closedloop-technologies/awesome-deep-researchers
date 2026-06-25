from __future__ import annotations

import argparse
import re
import sys
from collections import Counter
from dataclasses import dataclass
from datetime import date, datetime
from pathlib import Path
from typing import Iterable, List, Sequence
from urllib.parse import unquote, urlparse

import requests


REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_INDEX = REPO_ROOT / "skills" / "provider-source-index.md"
SKILLS_ROOT = REPO_ROOT / "skills"
DATE_RE = re.compile(r"^Last refreshed:\s*(\d{4}-\d{2}-\d{2})\.", re.MULTILINE)
ROW_RE = re.compile(r"^\|\s*`([^`]*)`\s*\|\s*([^|]*?)\s*\|", re.MULTILINE)
SKILL_NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


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
    try:
        return date.fromisoformat(match.group(1))
    except ValueError:
        return None


def parse_source_entries(text: str) -> List[SourceEntry]:
    entries = []
    for skill, source in ROW_RE.findall(text):
        if skill == "Skill" or source.strip() == "Source":
            continue
        entries.append(SourceEntry(skill=skill, source=source.strip()))
    return entries


def expected_skill_names(skills_root: Path = SKILLS_ROOT) -> List[str]:
    return sorted(path.name for path in skills_root.iterdir() if path.is_dir())


def normalized_skill_name(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", name.casefold()).strip("-")


def validate_source_reference(entry: SourceEntry) -> CheckResult | None:
    if any(character.isspace() for character in entry.source):
        return CheckResult(
            False,
            f"{entry.skill}: {entry.source} must not contain whitespace",
        )
    parsed = urlparse(entry.source)
    if parsed.scheme == "http":
        return CheckResult(False, f"{entry.skill}: {entry.source} must use HTTPS")
    if parsed.scheme and parsed.scheme not in {"http", "https"}:
        return CheckResult(
            False,
            f"{entry.skill}: {entry.source} has unsupported URL scheme",
        )
    if parsed.scheme in {"http", "https"} and not parsed.netloc:
        return CheckResult(False, f"{entry.skill}: {entry.source} must include a host")
    if parsed.scheme in {"http", "https"} and (
        parsed.username is not None or parsed.password is not None
    ):
        return CheckResult(
            False,
            f"{entry.skill}: {entry.source} must not include credentials",
        )
    if not parsed.scheme and parsed.query:
        return CheckResult(
            False,
            f"{entry.skill}: {entry.source} local source must not include query parameters",
        )
    local_path = unquote(parsed.path) if not parsed.scheme else entry.source
    if not parsed.scheme and not local_path:
        return CheckResult(
            False,
            f"{entry.skill}: {entry.source} local source must include a path",
        )
    if not parsed.scheme and "\\" in local_path:
        return CheckResult(
            False,
            f"{entry.skill}: {entry.source} local source must use forward slashes",
        )
    if not parsed.scheme and Path(local_path).is_absolute():
        return CheckResult(
            False,
            f"{entry.skill}: {entry.source} must be repo-relative",
        )
    if not parsed.scheme and ".." in Path(local_path).parts:
        return CheckResult(
            False,
            f"{entry.skill}: {entry.source} must not contain parent directory references",
        )
    return None


def check_source_index(
    index_path: Path = DEFAULT_INDEX,
    *,
    max_age_days: int = 30,
    today: date | None = None,
) -> List[CheckResult]:
    today = today or datetime.now().date()
    if isinstance(max_age_days, bool) or not isinstance(max_age_days, int):
        return [CheckResult(False, "max_age_days must be a non-negative integer")]
    if max_age_days < 0:
        return [CheckResult(False, "max_age_days must be a non-negative integer")]
    if not index_path.exists():
        return [CheckResult(False, f"missing source index: {index_path}")]

    text = index_path.read_text(encoding="utf-8")
    results: List[CheckResult] = []
    if "| Skill | Source |" not in text:
        results.append(CheckResult(False, "source index table must include Skill and Source header"))

    refreshed = parse_refreshed_date(text)
    if refreshed is None:
        results.append(CheckResult(False, "missing Last refreshed date"))
    else:
        age = (today - refreshed).days
        if age < 0:
            results.append(
                CheckResult(
                    False,
                    f"Last refreshed {refreshed.isoformat()} is in the future",
                )
            )
        else:
            results.append(
                CheckResult(
                    age <= max_age_days,
                    f"Last refreshed {refreshed.isoformat()} ({age} days old)",
                )
            )

    entries = parse_source_entries(text)
    for entry in entries:
        if not entry.skill:
            results.append(CheckResult(False, "source index row has a blank skill name"))
        elif not SKILL_NAME_RE.fullmatch(entry.skill):
            results.append(
                CheckResult(False, f"{entry.skill}: skill name must be lowercase hyphen-case")
            )
        if not entry.source:
            results.append(
                CheckResult(False, f"{entry.skill or '<blank>'}: source must be non-empty")
            )
        else:
            source_result = validate_source_reference(entry)
            if source_result is not None:
                results.append(source_result)
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
    duplicate_sources = sorted(
        source
        for source, count in Counter(entry.source for entry in entries if entry.source).items()
        if count > 1
    )
    if duplicate_sources:
        results.append(
            CheckResult(
                False,
                "duplicate source index sources: " + ", ".join(duplicate_sources),
            )
        )
    expected_skills = set(expected_skill_names(index_path.parent))
    invalid_skill_dirs = sorted(
        skill_name for skill_name in expected_skills if not SKILL_NAME_RE.fullmatch(skill_name)
    )
    if invalid_skill_dirs:
        results.append(
            CheckResult(
                False,
                "skill directories must be lowercase hyphen-case: "
                + ", ".join(invalid_skill_dirs),
            )
        )
    normalized_directory_counts = Counter(
        normalized_skill_name(skill_name) for skill_name in expected_skills
    )
    duplicate_normalized_dirs = sorted(
        skill_name for skill_name, count in normalized_directory_counts.items() if count > 1
    )
    if duplicate_normalized_dirs:
        results.append(
            CheckResult(
                False,
                "skill directories collide after normalization: "
                + ", ".join(duplicate_normalized_dirs),
            )
        )
    for skill_name in sorted(expected_skills):
        results.append(
            CheckResult(
                skill_name in indexed_skills,
                f"{skill_name}: {'indexed' if skill_name in indexed_skills else 'missing'}",
            )
        )
    unknown_skills = sorted(indexed_skills - expected_skills)
    if unknown_skills:
        results.append(
            CheckResult(
                False,
                "unknown source index skills: " + ", ".join(unknown_skills),
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
    if parsed.scheme:
        return CheckResult(False, f"{entry.skill}: {entry.source} has unsupported URL scheme")

    local_source_path = unquote(parsed.path)
    if not local_source_path:
        return CheckResult(False, f"{entry.skill}: {entry.source} local source must include a path")
    local_path = (repo_root / local_source_path).resolve()
    try:
        local_path.relative_to(repo_root.resolve())
    except ValueError:
        return CheckResult(False, f"{entry.skill}: {entry.source} escapes repo root")
    if not local_path.exists():
        return CheckResult(False, f"{entry.skill}: {entry.source} local path missing")
    if not local_path.is_file():
        return CheckResult(False, f"{entry.skill}: {entry.source} local path must be a file")
    return CheckResult(True, f"{entry.skill}: {entry.source} local path")


def check_links(index_path: Path = DEFAULT_INDEX) -> List[CheckResult]:
    text = index_path.read_text(encoding="utf-8")
    repo_root = index_path.parent.parent
    return [check_link(entry, repo_root=repo_root) for entry in parse_source_entries(text)]


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
