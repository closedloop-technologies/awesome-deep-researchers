---
name: exa-research
description: Call Exa Search, Contents, and Exa Deep research models with bounded result and page-read counts.
---

# Exa Research

Use this skill for neural web search, source discovery, and Exa's agentic deep
research endpoint.

## Environment

```bash
op run --env-file .env.adr -- python .claude/skills/exa-research/scripts/exa_tools.py \
  search "deepresearch the deepresearchers" \
  --num-results 5 \
  --highlights
```

Required 1Password-backed variable:

- `EXA_API_KEY`

## Cost Controls

- Use the `search` command with `--num-results 5 --highlights` for under-$1 benchmark smokes.
- Use `research --model exa-research` only when the task needs Exa's agentic research endpoint.
- For search-only tasks, cap `--num-results` to 5 or fewer.
- Avoid broad content reads unless the task requires full-page extraction.

## Current Source Links

- https://exa.ai/docs/reference/search-api-guide
- https://exa.ai/docs/changelog
