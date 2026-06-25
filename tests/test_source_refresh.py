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


def test_parse_refreshed_date_rejects_invalid_iso_date():
    assert source_refresh.parse_refreshed_date("Last refreshed: 2026-99-99.") is None


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


def test_link_checker_resolves_local_paths_from_selected_index_repo_root(tmp_path):
    skills_root = tmp_path / "skills"
    docs_root = tmp_path / "docs"
    (skills_root / "example-skill").mkdir(parents=True)
    docs_root.mkdir()
    (docs_root / "source.md").write_text("source", encoding="utf-8")
    index_path = skills_root / "provider-source-index.md"
    index_path.write_text(
        """# Provider Source Index

Last refreshed: 2026-06-23.

| Skill | Source |
| --- | --- |
| `example-skill` | docs/source.md |
""",
        encoding="utf-8",
    )

    results = source_refresh.check_links(index_path)

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


def test_source_index_checker_fails_duplicate_sources_across_skills(tmp_path):
    skills_root = tmp_path / "skills"
    (skills_root / "example-skill").mkdir(parents=True)
    (skills_root / "other-skill").mkdir(parents=True)
    index_path = skills_root / "provider-source-index.md"
    index_path.write_text(
        """# Provider Source Index

Last refreshed: 2026-06-23.

| Skill | Source |
| --- | --- |
| `example-skill` | https://example.com |
| `other-skill` | https://example.com |
""",
        encoding="utf-8",
    )

    results = source_refresh.check_source_index(index_path, today=date(2026, 6, 23))

    assert any(
        not result.ok and "duplicate source index sources: https://example.com" in result.message
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


def test_source_index_checker_fails_invalid_skill_row_names(tmp_path):
    skills_root = tmp_path / "skills"
    (skills_root / "example-skill").mkdir(parents=True)
    index_path = skills_root / "provider-source-index.md"
    index_path.write_text(
        """# Provider Source Index

Last refreshed: 2026-06-23.

| Skill | Source |
| --- | --- |
| `Example Skill` | https://example.com |
""",
        encoding="utf-8",
    )

    results = source_refresh.check_source_index(index_path, today=date(2026, 6, 23))

    assert any(
        not result.ok and "Example Skill: skill name must be lowercase hyphen-case" in result.message
        for result in results
    ), source_refresh.format_results(results)


def test_source_index_checker_fails_untrimmed_skill_row_names(tmp_path):
    skills_root = tmp_path / "skills"
    (skills_root / "example-skill").mkdir(parents=True)
    index_path = skills_root / "provider-source-index.md"
    index_path.write_text(
        """# Provider Source Index

Last refreshed: 2026-06-23.

| Skill | Source |
| --- | --- |
| ` example-skill ` | https://example.com |
""",
        encoding="utf-8",
    )

    results = source_refresh.check_source_index(index_path, today=date(2026, 6, 23))

    assert any(
        not result.ok and " example-skill : skill name must be lowercase hyphen-case" in result.message
        for result in results
    ), source_refresh.format_results(results)


def test_source_index_checker_fails_invalid_skill_directory_names(tmp_path):
    skills_root = tmp_path / "skills"
    (skills_root / "example_skill").mkdir(parents=True)
    index_path = skills_root / "provider-source-index.md"
    index_path.write_text(
        """# Provider Source Index

Last refreshed: 2026-06-23.

| Skill | Source |
| --- | --- |
| `example_skill` | https://example.com |
""",
        encoding="utf-8",
    )

    results = source_refresh.check_source_index(index_path, today=date(2026, 6, 23))

    assert any(
        not result.ok
        and "skill directories must be lowercase hyphen-case: example_skill" in result.message
        for result in results
    ), source_refresh.format_results(results)


def test_source_index_checker_fails_blank_skill_rows(tmp_path):
    skills_root = tmp_path / "skills"
    (skills_root / "example-skill").mkdir(parents=True)
    index_path = skills_root / "provider-source-index.md"
    index_path.write_text(
        """# Provider Source Index

Last refreshed: 2026-06-23.

| Skill | Source |
| --- | --- |
| `` | https://example.com |
""",
        encoding="utf-8",
    )

    results = source_refresh.check_source_index(index_path, today=date(2026, 6, 23))

    assert any(
        not result.ok and "source index row has a blank skill name" in result.message
        for result in results
    ), source_refresh.format_results(results)


def test_source_index_checker_fails_blank_source_rows(tmp_path):
    skills_root = tmp_path / "skills"
    (skills_root / "example-skill").mkdir(parents=True)
    index_path = skills_root / "provider-source-index.md"
    index_path.write_text(
        """# Provider Source Index

Last refreshed: 2026-06-23.

| Skill | Source |
| --- | --- |
| `example-skill` |   |
""",
        encoding="utf-8",
    )

    results = source_refresh.check_source_index(index_path, today=date(2026, 6, 23))

    assert any(
        not result.ok and "example-skill: source must be non-empty" in result.message
        for result in results
    ), source_refresh.format_results(results)


def test_source_index_checker_fails_unsupported_source_schemes(tmp_path):
    skills_root = tmp_path / "skills"
    (skills_root / "example-skill").mkdir(parents=True)
    index_path = skills_root / "provider-source-index.md"
    index_path.write_text(
        """# Provider Source Index

Last refreshed: 2026-06-23.

| Skill | Source |
| --- | --- |
| `example-skill` | ftp://example.com/source.md |
""",
        encoding="utf-8",
    )

    results = source_refresh.check_source_index(index_path, today=date(2026, 6, 23))

    assert any(
        not result.ok
        and "example-skill: ftp://example.com/source.md has unsupported URL scheme"
        in result.message
        for result in results
    ), source_refresh.format_results(results)


def test_source_index_checker_fails_http_urls_without_hosts(tmp_path):
    skills_root = tmp_path / "skills"
    (skills_root / "example-skill").mkdir(parents=True)
    index_path = skills_root / "provider-source-index.md"
    index_path.write_text(
        """# Provider Source Index

Last refreshed: 2026-06-23.

| Skill | Source |
| --- | --- |
| `example-skill` | https:///source.md |
""",
        encoding="utf-8",
    )

    results = source_refresh.check_source_index(index_path, today=date(2026, 6, 23))

    assert any(
        not result.ok and "example-skill: https:///source.md must include a host" in result.message
        for result in results
    ), source_refresh.format_results(results)


def test_source_index_checker_fails_plain_http_sources(tmp_path):
    skills_root = tmp_path / "skills"
    (skills_root / "example-skill").mkdir(parents=True)
    index_path = skills_root / "provider-source-index.md"
    index_path.write_text(
        """# Provider Source Index

Last refreshed: 2026-06-23.

| Skill | Source |
| --- | --- |
| `example-skill` | http://example.com/source.md |
""",
        encoding="utf-8",
    )

    results = source_refresh.check_source_index(index_path, today=date(2026, 6, 23))

    assert any(
        not result.ok and "example-skill: http://example.com/source.md must use HTTPS"
        in result.message
        for result in results
    ), source_refresh.format_results(results)


def test_source_index_checker_fails_sources_with_whitespace(tmp_path):
    skills_root = tmp_path / "skills"
    (skills_root / "example-skill").mkdir(parents=True)
    index_path = skills_root / "provider-source-index.md"
    index_path.write_text(
        """# Provider Source Index

Last refreshed: 2026-06-23.

| Skill | Source |
| --- | --- |
| `example-skill` | https://example.com/bad path |
""",
        encoding="utf-8",
    )

    results = source_refresh.check_source_index(index_path, today=date(2026, 6, 23))

    assert any(
        not result.ok
        and "example-skill: https://example.com/bad path must not contain whitespace"
        in result.message
        for result in results
    ), source_refresh.format_results(results)


def test_source_index_checker_fails_absolute_local_source_paths(tmp_path):
    skills_root = tmp_path / "skills"
    (skills_root / "example-skill").mkdir(parents=True)
    absolute_source = tmp_path / "docs" / "source.md"
    index_path = skills_root / "provider-source-index.md"
    index_path.write_text(
        f"""# Provider Source Index

Last refreshed: 2026-06-23.

| Skill | Source |
| --- | --- |
| `example-skill` | {absolute_source} |
""",
        encoding="utf-8",
    )

    results = source_refresh.check_source_index(index_path, today=date(2026, 6, 23))

    assert any(
        not result.ok
        and f"example-skill: {absolute_source} must be repo-relative" in result.message
        for result in results
    ), source_refresh.format_results(results)


def test_source_index_checker_fails_parent_directory_source_paths(tmp_path):
    skills_root = tmp_path / "skills"
    (skills_root / "example-skill").mkdir(parents=True)
    index_path = skills_root / "provider-source-index.md"
    index_path.write_text(
        """# Provider Source Index

Last refreshed: 2026-06-23.

| Skill | Source |
| --- | --- |
| `example-skill` | ../docs/source.md |
""",
        encoding="utf-8",
    )

    results = source_refresh.check_source_index(index_path, today=date(2026, 6, 23))

    assert any(
        not result.ok
        and (
            "example-skill: ../docs/source.md must not contain parent directory references"
            in result.message
        )
        for result in results
    ), source_refresh.format_results(results)


def test_source_index_checker_fails_stale_index():
    results = source_refresh.check_source_index(max_age_days=30, today=date(2026, 8, 1))

    assert any(not result.ok and "Last refreshed" in result.message for result in results)


def test_source_index_checker_rejects_negative_max_age_days():
    results = source_refresh.check_source_index(
        max_age_days=-1,
        today=date(2026, 6, 23),
    )

    assert results == [
        source_refresh.CheckResult(False, "max_age_days must be a non-negative integer")
    ]


def test_source_index_checker_rejects_non_integer_max_age_days():
    results = source_refresh.check_source_index(
        max_age_days=True,
        today=date(2026, 6, 23),
    )

    assert results == [
        source_refresh.CheckResult(False, "max_age_days must be a non-negative integer")
    ]


def test_source_index_checker_fails_future_refresh_dates(tmp_path):
    skills_root = tmp_path / "skills"
    (skills_root / "example-skill").mkdir(parents=True)
    index_path = skills_root / "provider-source-index.md"
    index_path.write_text(
        """# Provider Source Index

Last refreshed: 2026-06-24.

| Skill | Source |
| --- | --- |
| `example-skill` | https://example.com |
""",
        encoding="utf-8",
    )

    results = source_refresh.check_source_index(index_path, today=date(2026, 6, 23))

    assert any(
        not result.ok and "Last refreshed 2026-06-24 is in the future" in result.message
        for result in results
    ), source_refresh.format_results(results)


def test_local_source_link_rejects_path_outside_repo(tmp_path):
    outside_doc = tmp_path.parent / "outside.md"
    outside_doc.write_text("outside", encoding="utf-8")

    result = source_refresh.check_link(
        source_refresh.SourceEntry("example-skill", "../outside.md"),
        repo_root=tmp_path,
    )

    assert result.ok is False
    assert "escapes repo root" in result.message


def test_local_source_link_rejects_absolute_path_outside_repo(tmp_path):
    outside_doc = tmp_path.parent / "outside.md"
    outside_doc.write_text("outside", encoding="utf-8")

    result = source_refresh.check_link(
        source_refresh.SourceEntry("example-skill", str(outside_doc.resolve())),
        repo_root=tmp_path,
    )

    assert result.ok is False
    assert "escapes repo root" in result.message


def test_source_link_rejects_unsupported_url_schemes(tmp_path):
    result = source_refresh.check_link(
        source_refresh.SourceEntry("example-skill", "ftp://example.com/source.md"),
        repo_root=tmp_path,
    )

    assert result.ok is False
    assert "unsupported URL scheme" in result.message


def test_local_source_link_rejects_directory_sources(tmp_path):
    docs_dir = tmp_path / "docs"
    docs_dir.mkdir()

    result = source_refresh.check_link(
        source_refresh.SourceEntry("example-skill", "docs"),
        repo_root=tmp_path,
    )

    assert result.ok is False
    assert "local path must be a file" in result.message
