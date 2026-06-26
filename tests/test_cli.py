import re
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from awesome_deep_research import cli
from awesome_deep_research.cli import PromptExample


def test_load_prompt_examples_contains_expected_ids():
    prompts = cli.load_prompt_examples()
    assert prompts, "Expected at least one prompt example from taxonomy file"

    prompt_ids = {prompt.identifier for prompt in prompts}
    assert "domain-mapping-01" in prompt_ids
    assert "source-retrieval-01" in prompt_ids
    assert "repository-refresh-meta-research-01" in prompt_ids


def test_next_output_path_increments(tmp_path: Path):
    first = cli.next_output_path(tmp_path, "perplexity-sonar")
    assert first.name == "OUTPUT-PERPLEXITY-SONAR-0001.md"
    first.write_text("dummy", encoding="utf-8")

    second = cli.next_output_path(tmp_path, "perplexity-sonar")
    assert second.name == "OUTPUT-PERPLEXITY-SONAR-0002.md"


def test_next_output_path_rejects_blank_skill_names(tmp_path: Path):
    with pytest.raises(ValueError, match="skill_name must be a non-empty string"):
        cli.next_output_path(tmp_path, "   ")


def test_next_output_path_rejects_punctuation_only_skill_names(tmp_path: Path):
    with pytest.raises(ValueError, match="skill_name must contain at least one"):
        cli.next_output_path(tmp_path, "!!!")


def test_next_output_path_trims_generated_tokens(tmp_path: Path):
    output_path = cli.next_output_path(tmp_path, "-perplexity-sonar-")

    assert output_path.name == "OUTPUT-PERPLEXITY-SONAR-0001.md"


def test_load_skill_infos_includes_agents_documentation_skills():
    skills = cli.load_skill_infos(include_documentation=True)

    assert "gemini-deep-research" in skills
    assert skills["gemini-deep-research"].source == "agents"
    assert skills["gemini-deep-research"].runnable is True


def test_load_skill_infos_falls_back_to_packaged_plugin_skills(tmp_path: Path, monkeypatch):
    agents_root = tmp_path / ".agents" / "skills"
    plugin_root = tmp_path / "skills"
    skill_root = plugin_root / "packaged-skill"
    scripts_root = skill_root / "scripts"
    scripts_root.mkdir(parents=True)
    (skill_root / "SKILL.md").write_text(
        "---\nname: packaged-skill\ndescription: Packaged fallback.\n---\n",
        encoding="utf-8",
    )
    (scripts_root / "run.py").write_text("print('ok')\n", encoding="utf-8")

    monkeypatch.setattr(
        cli,
        "SKILL_ROOTS",
        [("agents", agents_root), ("plugin", plugin_root)],
    )

    skills = cli.load_skill_infos(include_documentation=True)

    assert skills["packaged-skill"].source == "plugin"
    assert skills["packaged-skill"].runnable is True


def test_load_skills_only_returns_runnable_skills():
    skills = cli.load_skills()

    assert "okf-normalize-research" in skills
    assert "gemini-deep-research" in skills


def test_list_skills_command_shows_source_and_runnable_state(capsys):
    result = cli.list_skills_command(None)
    output = capsys.readouterr().out

    assert result == 0
    assert "gemini-deep-research\tagents\trunnable" in output
    assert "okf-normalize-research\tagents\trunnable" in output


def test_build_user_prompt_includes_extra_instructions():
    prompt = PromptExample(identifier="custom", category="Domain Mapping", text="Analyze the domain.")
    extra = "Prioritize regulatory perspectives."

    user_prompt = cli.build_user_prompt(prompt, extra)

    assert "## Additional Instructions" in user_prompt
    assert extra in user_prompt
    assert re.search(r"Domain Mapping", user_prompt)


def test_resolve_prompt_text_rejects_blank_custom_prompts():
    with pytest.raises(ValueError, match="--prompt-text must be a non-empty string"):
        cli.resolve_prompt_text(None, "   ")


def test_resolve_prompt_text_trims_custom_prompts():
    prompt = cli.resolve_prompt_text(None, "  Analyze this corpus.  ")

    assert prompt.identifier == "custom"
    assert prompt.category == "Custom"
    assert prompt.text == "Analyze this corpus."


@pytest.mark.parametrize("mode", ["default", "relative", "absolute"])
def test_ensure_output_dir_creates_directories(tmp_path: Path, monkeypatch, mode: str):
    monkeypatch.setattr(cli, "REPO_ROOT", tmp_path)
    monkeypatch.setattr(cli, "DEFAULT_OUTPUT_DIR", tmp_path / "default")

    if mode == "default":
        requested = None
    elif mode == "relative":
        requested = str(Path("outputs-test"))
    else:
        requested = str((tmp_path / "absolute").resolve())

    output_dir = cli.ensure_output_dir(requested)
    assert output_dir.exists()
    assert output_dir.is_dir()


@pytest.mark.parametrize(
    ("requested", "message"),
    [
        ("", "--output-dir must be a non-empty path"),
        ("   ", "--output-dir must be a non-empty path"),
        (" outputs", "--output-dir must be trimmed"),
        ("outputs\\test", "--output-dir must use forward slashes"),
        ("outputs\x7f", "--output-dir must not contain control characters"),
        ("./outputs", "--output-dir must not contain dot path segments"),
        ("outputs/../outputs2", "--output-dir must not contain dot path segments"),
        ("../outside", "--output-dir must not contain dot path segments"),
    ],
)
def test_ensure_output_dir_rejects_invalid_paths(
    tmp_path: Path, monkeypatch, requested: str, message: str
):
    monkeypatch.setattr(cli, "REPO_ROOT", tmp_path)
    monkeypatch.setattr(cli, "DEFAULT_OUTPUT_DIR", tmp_path / "default")

    with pytest.raises(ValueError, match=message):
        cli.ensure_output_dir(requested)

    assert not (tmp_path.parent / "outside").exists()


def test_ensure_output_dir_rejects_absolute_paths_outside_repo(
    tmp_path: Path, monkeypatch
):
    outside = tmp_path.parent / "outside-output"
    monkeypatch.setattr(cli, "REPO_ROOT", tmp_path)
    monkeypatch.setattr(cli, "DEFAULT_OUTPUT_DIR", tmp_path / "default")

    with pytest.raises(ValueError, match="--output-dir must stay within"):
        cli.ensure_output_dir(str(outside))

    assert not outside.exists()


def test_ensure_output_dir_rejects_existing_files(tmp_path: Path, monkeypatch):
    output_file = tmp_path / "outputs"
    output_file.write_text("not a directory", encoding="utf-8")
    monkeypatch.setattr(cli, "REPO_ROOT", tmp_path)
    monkeypatch.setattr(cli, "DEFAULT_OUTPUT_DIR", tmp_path / "default")

    with pytest.raises(ValueError, match="--output-dir must be a directory"):
        cli.ensure_output_dir(str(output_file))

    assert output_file.read_text(encoding="utf-8") == "not a directory"
