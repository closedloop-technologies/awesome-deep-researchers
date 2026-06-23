---
name: smolagents
description: Run Hugging Face Smolagents as a code-as-action research agent with optional web search.
---

# Smolagents

Use this skill when the research task benefits from tool use, code execution,
and explicit intermediate actions.

## Environment

```bash
op run --env-file .env.adr -- python .agents/skills/smolagents/scripts/agent.py \
  --task "Find current deep research APIs and summarize cost controls" \
  --model openai \
  --model-id gpt-4o-mini \
  --web-search
```

Common 1Password-backed variables:

- `HF_TOKEN`
- `OPENAI_API_KEY`
- `ANTHROPIC_API_KEY`

## Cost Controls

- Use economical model IDs for benchmark tasks.
- Keep `max_steps` low in the script configuration.
- Enable web search only when the prompt requires current sources.

## Source Link

- https://github.com/huggingface/smolagents
