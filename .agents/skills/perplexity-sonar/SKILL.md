---
name: perplexity-sonar
description: Call Perplexity Sonar and Sonar Deep Research for web-grounded answers with citations.
---

# Perplexity Sonar

Use this skill when the research task needs current web-grounded synthesis and
source citations. The Sonar API is OpenAI-compatible.

## Environment

```bash
op run --env-file .env.adr -- python .claude/skills/perplexity-sonar/scripts/ask.py \
  --prompt "deepresearch the deepresearchers" \
  --model sonar \
  --search-context-size low
```

Required 1Password-backed variable:

- `PERPLEXITY_API_KEY`

## Cost Controls

- Prefer `sonar` or the lowest available Sonar model for smoke tests.
- Use `--search-context-size low` for under-`$1` benchmark smoke tests.
- Use Sonar Deep Research only when the benchmark task truly needs deep
  multi-source reasoning.
- Track token, citation, reasoning, request, and search-query costs when the API
  returns them.

## Current Source Links

- https://docs.perplexity.ai/docs/sonar/quickstart
- https://docs.perplexity.ai/docs/getting-started/pricing
