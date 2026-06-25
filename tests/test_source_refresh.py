from datetime import date

from awesome_deep_research import source_refresh


def test_parse_source_entries_reads_skill_rows():
    text = """# Provider Source Index

| Skill | Source |
| --- | --- |
| `openai-deep-research` | https://example.com/openai |
| `okf-normalize-research` | docs/okf-normalization.md |
"""

    entries = source_refresh.parse_source_entries(text)

    assert [entry.skill for entry in entries] == [
        "openai-deep-research",
        "okf-normalize-research",
    ]
    assert entries[1].source == "docs/okf-normalization.md"


def test_parse_refreshed_date_reads_iso_date():
    assert source_refresh.parse_refreshed_date("Last refreshed: 2026-06-23.") == date(
        2026, 6, 23
    )


def test_source_index_checker_passes_current_index():
    results = source_refresh.check_source_index(today=date(2026, 6, 23))

    assert results
    assert all(result.ok for result in results), source_refresh.format_results(results)


def test_source_index_checker_uses_selected_index_parent_for_expected_skills(tmp_path):
    skills_root = tmp_path / "skills"
    (skills_root / "example-skill").mkdir(parents=True)
    index_path = skills_root / "provider-source-index.md"
    index_path.write_text(
        """# Provider Source Index

Last refreshed: 2026-06-23.

| Skill | Source |
| --- | --- |
| `example-skill` | https://example.com |
""",
        encoding="utf-8",
    )

    results = source_refresh.check_source_index(index_path, today=date(2026, 6, 23))

    assert all(result.ok for result in results), source_refresh.format_results(results)


def test_source_index_checker_fails_duplicate_skill_rows(tmp_path):
    skills_root = tmp_path / "skills"
    (skills_root / "example-skill").mkdir(parents=True)
    index_path = skills_root / "provider-source-index.md"
    index_path.write_text(
        """# Provider Source Index

Last refreshed: 2026-06-23.

| Skill | Source |
| --- | --- |
| `example-skill` | https://example.com |
| `example-skill` | https://example.com |
""",
        encoding="utf-8",
    )

    results = source_refresh.check_source_index(index_path, today=date(2026, 6, 23))

    assert any(
        not result.ok
        and "duplicate source index rows: example-skill -> https://example.com"
        in result.message
        for result in results
    ), source_refresh.format_results(results)


def test_source_index_checker_fails_unknown_skill_rows(tmp_path):
    skills_root = tmp_path / "skills"
    (skills_root / "example-skill").mkdir(parents=True)
    index_path = skills_root / "provider-source-index.md"
    index_path.write_text(
        """# Provider Source Index

Last refreshed: 2026-06-23.

| Skill | Source |
| --- | --- |
| `example-skill` | https://example.com |
| `example-skil` | https://example.com/typo |
""",
        encoding="utf-8",
    )

    results = source_refresh.check_source_index(index_path, today=date(2026, 6, 23))

    assert any(
        not result.ok and "unknown source index skills: example-skil" in result.message
        for result in results
    ), source_refresh.format_results(results)


def test_source_index_checker_fails_stale_index():
    results = source_refresh.check_source_index(max_age_days=30, today=date(2026, 8, 1))

    assert any(not result.ok and "Last refreshed" in result.message for result in results)
