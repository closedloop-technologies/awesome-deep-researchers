# Codex Skills

This directory is the Codex-facing skill bundle for the repository. The older
`.claude/skills` tree remains available for Claude Code compatibility; new
Codex-oriented skills should be added here and registered in
`benchmark/utils.py`.

## Current Skills

- `deep-research-api-calls` - provider call patterns, API-key expectations,
  cost controls, and 1Password environment guidance.
- `okf-normalize-research` - convert a deep research output into an Open
  Knowledge Format-style bundle.
- `custom-data-deep-research` - plan custom-source research across Google Docs,
  YouTube, local files, S3 buckets, arXiv papers, and similar corpora.
- Provider-specific call guides:
  - `openai-deep-research`
  - `perplexity-sonar`
  - `exa-research`
  - `tavily-search`
  - `jina-ai`
  - `xai-grok`
  - `you-research`
  - `gemini-deep-research`
  - `gpt-researcher`
  - `langchain-deep-research`
  - `stanford-storm`
  - `smolagents`

`you-research`, `gemini-deep-research`, and `okf-normalize-research` include
`.agents` runnable scripts. Several other providers reuse the legacy
`.claude/skills` scripts while keeping Codex-facing call guidance here.

## Adding a Skill

1. Add `.agents/skills/<skill-name>/SKILL.md`.
2. Add executable scripts under `.agents/skills/<skill-name>/scripts/` when the
   skill should run in the benchmark.
3. Add or confirm command wiring in `benchmark/utils.py`.
4. Add the tox environment to `tox.ini` when the skill has tests or runtime
   dependencies.
5. Keep benchmark prompts and runtime defaults below the documented `$1` per
   call budget.
