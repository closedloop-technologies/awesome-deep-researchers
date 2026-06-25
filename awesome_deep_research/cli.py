from __future__ import annotations

import argparse
import re
import subprocess
import sys
import textwrap
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Optional

REPO_ROOT = Path(__file__).resolve().parent.parent
SKILLS_ROOT = REPO_ROOT / ".agents" / "skills"
PROMPT_FILE = REPO_ROOT / "docs" / "taxonomy-and-examples.md"
DEFAULT_OUTPUT_DIR = REPO_ROOT / "outputs"


@dataclass
class PromptExample:
    identifier: str
    category: str
    text: str


@dataclass
class SkillInfo:
    name: str
    path: Path
    source: str
    runnable: bool


SKILL_ROOTS = [
    ("agents", REPO_ROOT / ".agents" / "skills"),
    ("plugin", REPO_ROOT / "skills"),
]


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return slug or "prompt"


def load_skill_infos(include_documentation: bool = True) -> Dict[str, SkillInfo]:
    skills: Dict[str, SkillInfo] = {}
    for source, root in SKILL_ROOTS:
        if not root.exists():
            continue
        for path in sorted(root.iterdir()):
            if not path.is_dir():
                continue
            scripts_dir = path / "scripts"
            runnable = scripts_dir.exists() and any(scripts_dir.glob("*.py"))
            if not include_documentation and not runnable:
                continue
            existing = skills.get(path.name)
            if existing and existing.runnable:
                continue
            skills[path.name] = SkillInfo(
                name=path.name,
                path=path,
                source=source,
                runnable=runnable,
            )
    return skills


def load_skills() -> Dict[str, Path]:
    return {name: info.path for name, info in load_skill_infos(include_documentation=False).items()}


def parse_skill_description(skill_dir: Path) -> str:
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        return ""

    description = ""
    inside_front_matter = False
    try:
        for raw_line in skill_md.read_text(encoding="utf-8").splitlines():
            line = raw_line.strip()
            if line == "---":
                if not inside_front_matter:
                    inside_front_matter = True
                    continue
                break
            if inside_front_matter and line.lower().startswith("description:"):
                description = line.split(":", 1)[1].strip()
                break
    except UnicodeDecodeError:
        return ""
    return description


def list_skills_command(_: argparse.Namespace) -> int:
    skills = load_skill_infos(include_documentation=True)
    if not skills:
        print("No skills found under .agents/skills/ or skills/", file=sys.stderr)
        return 1

    for name, skill in sorted(skills.items()):
        description = parse_skill_description(skill.path)
        runnable = "runnable" if skill.runnable else "docs"
        if description:
            print(f"{name}\t{skill.source}\t{runnable}\t{description}")
        else:
            print(f"{name}\t{skill.source}\t{runnable}")
    return 0


def load_prompt_examples() -> List[PromptExample]:
    if not PROMPT_FILE.exists():
        return []

    examples: List[PromptExample] = []
    counters: Dict[str, int] = {}
    current_category: Optional[str] = None
    current_slug: Optional[str] = None
    in_examples_section = False

    content = PROMPT_FILE.read_text(encoding="utf-8")
    for raw_line in content.splitlines():
        line = raw_line.strip()

        if not line:
            continue

        if line == "---":
            if not in_examples_section:
                continue
            # Ignore horizontal rules once inside the section
            continue

        if not in_examples_section:
            if line.startswith("##") and "Canonical" in line:
                in_examples_section = True
            continue

        if line.startswith("##") and not line.startswith("###") and "Canonical" not in line:
            # Exiting the examples section
            break

        if line.startswith("###"):
            heading = line.lstrip("#").strip()
            heading = heading.replace("**", "").strip()
            heading = re.sub(r"^\d+(\.\d+)*\s*", "", heading)
            current_category = heading
            current_slug = slugify(heading)
            continue

        if not current_category or not current_slug:
            continue

        bullet_match = re.match(r"^[-*+]\s*(.+)", line)
        if bullet_match:
            prompt_text = bullet_match.group(1).strip()
            prompt_text = prompt_text.strip('"“”')
            if not prompt_text:
                continue
            count = counters.get(current_slug, 0) + 1
            counters[current_slug] = count
            identifier = f"{current_slug}-{count:02d}"
            examples.append(
                PromptExample(identifier=identifier, category=current_category, text=prompt_text)
            )

    return examples


def list_prompts_command(_: argparse.Namespace) -> int:
    prompts = load_prompt_examples()
    if not prompts:
        print(
            "No prompt examples were found. Ensure docs/taxonomy-and-examples.md is present.",
            file=sys.stderr,
        )
        return 1

    for prompt in prompts:
        print(f"{prompt.identifier}\t[{prompt.category}] {prompt.text}")
    return 0


def resolve_prompt_text(prompt_id: Optional[str], prompt_text: Optional[str]) -> PromptExample:
    if prompt_text is not None:
        if not prompt_text.strip():
            raise ValueError("--prompt-text must be a non-empty string.")
        return PromptExample(identifier="custom", category="Custom", text=prompt_text.strip())

    if not prompt_id:
        raise ValueError("Either --prompt-id or --prompt-text must be provided.")

    prompts = {example.identifier: example for example in load_prompt_examples()}
    if prompt_id not in prompts:
        raise KeyError(f"Prompt id '{prompt_id}' was not found in docs/taxonomy-and-examples.md.")
    return prompts[prompt_id]


def gather_skill_scripts(skill_dir: Path) -> Iterable[str]:
    scripts_dir = skill_dir / "scripts"
    if not scripts_dir.exists():
        return []
    return [str(path.relative_to(REPO_ROOT)) for path in sorted(scripts_dir.glob("*.py"))]


def build_system_prompt(skill_name: str, skill_dir: Path) -> str:
    description = parse_skill_description(skill_dir)
    scripts = list(gather_skill_scripts(skill_dir))
    scripts_section = "\n".join(f"- {script}" for script in scripts) if scripts else "(no scripts directory found)"

    requirements_path = skill_dir / "requirements.txt"
    requirements_line = (
        f"requirements: {requirements_path.relative_to(REPO_ROOT)}"
        if requirements_path.exists()
        else "requirements: (none provided)"
    )

    system_prompt = textwrap.dedent(
        f"""
        You are running inside the Awesome Deep Researchers headless CLI.
        Skill: {skill_name}
        Description: {description or 'No description available.'}
        Skill path: {skill_dir.relative_to(REPO_ROOT)}
        {requirements_line}

        Accessible helper scripts:
        {scripts_section}

        Always rely on the selected skill's tooling for external research calls.
        Verify that required environment variables and dependencies are available before execution.
        If something is missing, stop and report precise remediation steps.
        Provide outputs with clear inline citations and a final reference list.
        """
    ).strip()

    return system_prompt


def build_user_prompt(prompt: PromptExample, extra: Optional[str]) -> str:
    extra_section = f"\n\n## Additional Instructions\n{extra.strip()}" if extra else ""

    return textwrap.dedent(
        f"""
        # Research Brief

        ## Category
        {prompt.category}

        ## Core Task
        {prompt.text}
        {extra_section}

        ## Deliverable
        Produce a concise but thorough Markdown report including:
        - Executive summary (2-3 paragraphs).
        - Key findings as bulleted insights with inline citations.
        - Risks, uncertainties, or open questions.
        - Recommended next steps for a human researcher.
        - Reference list with full source URLs.

        Confirm how the selected skill was used. If the task cannot be completed, explain why and propose alternatives.
        """
    ).strip()


def ensure_output_dir(path: Optional[str]) -> Path:
    if path is not None:
        if not path.strip():
            raise ValueError("--output-dir must be a non-empty path.")
        requested_dir = Path(path)
        output_dir = requested_dir if requested_dir.is_absolute() else REPO_ROOT / requested_dir
    else:
        output_dir = DEFAULT_OUTPUT_DIR
    output_dir = output_dir.resolve()
    try:
        output_dir.relative_to(REPO_ROOT.resolve())
    except ValueError as exc:
        raise ValueError("--output-dir must stay within the repository root.") from exc
    output_dir.mkdir(parents=True, exist_ok=True)
    return output_dir


def next_output_path(output_dir: Path, skill_name: str) -> Path:
    token = re.sub(r"[^A-Z0-9]+", "-", skill_name.upper())
    pattern = re.compile(rf"OUTPUT-{re.escape(token)}-(\d+)\.md$")
    max_index = 0
    for existing in output_dir.glob(f"OUTPUT-{token}-*.md"):
        match = pattern.match(existing.name)
        if match:
            max_index = max(max_index, int(match.group(1)))
    next_index = max_index + 1
    return output_dir / f"OUTPUT-{token}-{next_index:04d}.md"


def run_command(args: argparse.Namespace) -> int:
    skills = load_skill_infos(include_documentation=False)
    if args.skill not in skills:
        available = ", ".join(skills.keys()) or "<none>"
        print(f"Runnable skill '{args.skill}' not found. Available runnable skills: {available}", file=sys.stderr)
        return 1

    skill_dir = skills[args.skill].path

    try:
        prompt = resolve_prompt_text(args.prompt_id, args.prompt_text)
    except (ValueError, KeyError) as exc:
        print(str(exc), file=sys.stderr)
        return 1
    try:
        output_dir = ensure_output_dir(args.output_dir)
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        return 1

    system_prompt = build_system_prompt(args.skill, skill_dir)
    user_prompt = build_user_prompt(prompt, args.extra_instructions)

    cmd = ["claude", "--print", "--append-system-prompt", system_prompt]
    if args.model:
        cmd.extend(["--model", args.model])
    cmd.append(user_prompt)

    try:
        completed = subprocess.run(
            cmd,
            check=False,
            capture_output=True,
            text=True,
        )
    except FileNotFoundError:
        print("The 'claude' CLI could not be found in PATH. Install Claude Code before running.", file=sys.stderr)
        return 1

    if completed.returncode != 0:
        print("Claude CLI command failed:", file=sys.stderr)
        if completed.stderr:
            print(completed.stderr.strip(), file=sys.stderr)
        return completed.returncode

    output_text = completed.stdout.strip()
    if not output_text:
        print("Claude CLI returned empty output.", file=sys.stderr)
        return 1

    output_path = next_output_path(output_dir, args.skill)
    output_path.write_text(output_text + "\n", encoding="utf-8")

    if completed.stderr:
        print(completed.stderr.strip(), file=sys.stderr)

    print(f"Saved report to {output_path.relative_to(REPO_ROOT)}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="adr",
        description="Awesome Deep Researchers CLI wrapper for headless agent skill runs.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    list_skills = subparsers.add_parser("list-skills", help="List available .agents skills.")
    list_skills.set_defaults(func=list_skills_command)

    list_prompts = subparsers.add_parser(
        "list-prompts", help="List canned research prompts from the taxonomy examples."
    )
    list_prompts.set_defaults(func=list_prompts_command)

    run_parser = subparsers.add_parser(
        "run", help="Execute a headless Claude research run with a selected skill and prompt."
    )
    run_parser.add_argument("--skill", required=True, help="Runnable skill name to activate.")
    prompt_group = run_parser.add_mutually_exclusive_group(required=True)
    prompt_group.add_argument("--prompt-id", help="Identifier from 'adr list-prompts'.")
    prompt_group.add_argument("--prompt-text", help="Freeform research prompt text.")
    run_parser.add_argument("--model", help="Optional Claude model alias (passed through to claude CLI).")
    run_parser.add_argument(
        "--extra-instructions",
        help="Additional instructions appended to the research brief.",
    )
    run_parser.add_argument(
        "--output-dir",
        help="Directory for saving outputs (default: outputs/ in repo root).",
    )
    run_parser.set_defaults(func=run_command)

    return parser


def main(argv: Optional[List[str]] = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
