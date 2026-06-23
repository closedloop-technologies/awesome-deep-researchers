# Awesome Deep Researchers [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated list of deep research APIs, libraries, and frameworks that enable autonomous multi-step information gathering, analysis, and synthesis with citations.

Deep research agents go beyond simple Q&A—they autonomously plan research strategies, execute multi-step queries across diverse sources, and synthesize findings into comprehensive, citation-backed reports.

## Contents

- [Commercial APIs](#commercial-apis)
- [Open Source Frameworks](#open-source-frameworks)
- [Specialized Research Tools](#specialized-research-tools)
- [Search & Retrieval Infrastructure](#search--retrieval-infrastructure)
- [API Skill and Benchmark Status](#api-skill-and-benchmark-status)
- [Benchmarks & Evaluation](#benchmarks--evaluation)
- [What Makes an Agent Deep Research](#what-makes-an-agent-deep-research)
- [Domain-Specific Deep Research](#domain-specific-deep-research)
- [Codex Plugin and Skills](#codex-plugin-and-skills)

## Commercial APIs

### General Purpose Deep Research

Pricing and model availability change frequently. Use
`.agents/skills/provider-source-index.md` and `python -m
awesome_deep_research.source_refresh --check-links` before refreshing pricing
or model guidance.

| Name | Type | Under-$1 Benchmark Stance | Key Features | Best For |
|------|------|---------------------------|--------------|----------|
| [OpenAI Deep Research](https://openai.com/chatgpt) | API + Web UI | Prefer mini/deep-research models, low effort, concise prompts | reasoning models, autonomous browsing, code execution, multimodal | Strategic analysis, legal research, complex synthesis |
| [Google Gemini Deep Research](https://gemini.google.com) | Web UI + API | Use grounded low-cost mode for smoke tests; reserve Deep Research Agent for deliberate live runs | Google Search integration, workspace/file grounding, asynchronous agent flow | Corporate intelligence, internal data research |
| [Perplexity Sonar](https://perplexity.ai) | API + Web UI | Prefer the lowest Sonar model/search depth that returns citations | Real-time web index, citations, live data | Market research, news synthesis, competitive intelligence |
| [xAI Grok](https://grok.x.ai) | API + Web UI | Use the lowest-cost model that supports the needed web or X search tools | real-time web/X tools, large context, social/news coverage | Crisis monitoring, social sentiment, finance |
| [You.com Research](https://you.com) | API + Web UI | Use `research_effort=lite` for smoke tests; avoid high-depth tiers unless budgeted | research reports, source analysis, MCP/API options | Enterprise reports, analyst workflows |
| [Anthropic Claude](https://anthropic.com) | API + Web UI | Use economical model settings inside OSS frameworks | multi-agent research patterns, long-context synthesis | Production research workflows |

### Specialized Deep Research

| Name | Type | Cost-Control Stance | Domain Focus | Key Features |
|------|------|---------------------|--------------|--------------|
| [Jina Reader/Search](https://jina.ai) | API | Use for bounded retrieval/reading, not as a full report writer | Middleware agent | URL-to-markdown, search-read-reason building block |
| [Exa Search](https://exa.ai) | Search API | Cap searches and page reads | Neural search | Embedding-based retrieval, RAG-optimized content |
| [Elicit](https://elicit.org) | Web UI | Use outside API benchmark unless an API key/path is added | Academic literature | Paper analysis, research synthesis |
| [Consensus](https://consensus.app) | Web UI | Use outside API benchmark unless an API key/path is added | Scientific papers | Evidence-based answers from papers |
| [Scite](https://scite.ai) | Web + API | Use outside API benchmark unless an API key/path is added | Citation analysis | Smart citations, claim verification |

## Open Source Frameworks

### Production-Ready Frameworks

| Name | License | Language | Key Features | Architecture |
|------|---------|----------|--------------|--------------|
| [GPT Researcher](https://github.com/assafelovic/gpt-researcher) | Apache-2.0 | Python | CLI/API, Docker support, customizable agents | Planner + executor + publisher |
| [LangChain Deep Research](https://github.com/langchain-ai/open_deep_research) | MIT | Python | LangGraph UI, multi-step workflows | Summarize → research → synthesize |
| [Stanford STORM](https://github.com/stanford-oval/storm) | MIT | Python | Academic-style articles, multi-agent dialogue | Q&A agents + moderator |
| [Smolagents](https://github.com/huggingface/smolagents) | Apache-2.0 | Python | Code-as-action, 30% token efficiency gain | Python code generation, sandboxed execution |
| [DeepResearcher](https://github.com/Alibaba-NLP/DeepResearch) | Apache-2.0 | Python | RL-trained, self-reflective, citation-aware | End-to-end RL agent |

### Research & Experimental

| Name | License | Language | Key Innovation | Status |
|------|---------|----------|----------------|--------|
| [MA-RAG](https://arxiv.org/abs/2505.20096) | Research | Python | Multi-agent RAG with specialized roles | Research prototype |
| [AgentRxiv](https://agentrxiv.github.io) | MIT | Python | Collaborative agent knowledge sharing | Experimental |
| [DR-Tulu](https://allenai.org/blog/dr-tulu) | Permissive | Python | RLAER training, citation optimization | Beats GPT-4 on ScholarQA |
| [Zilliz DeepSearcher](https://github.com/zilliztech/deep-searcher) | Open Source | Python | Private vector DB research, agentic RAG | Self-hosted |
| [SPAR](https://github.com/tmgthb/Autonomous-Agents) | Open Source | Python | Scholar paper retrieval, citation-driven | OSS project |

## Specialized Research Tools

### Academic & Scientific

| Name | Access | Focus | Key Features |
|------|--------|-------|--------------|
| [Semantic Scholar](https://semanticscholar.org) | Web + API | Academic search | AI-powered paper discovery, citation graphs |
| [ResearchRabbit](https://researchrabbit.ai) | Web | Academic discovery | Visual paper networks, recommendations |
| [Documind](https://documind.chat) | Web | PDF analysis | Document-focused research |

### Enterprise & Internal Data

| Name | Type | Key Features | Best For |
|------|------|--------------|----------|
| [NVIDIA AI-Q Blueprint](https://developer.nvidia.com/blog/chat-with-your-enterprise-data-through-open-source-ai) | Platform | PDF ingestion, iterative reasoning, enterprise scale | Enterprise deployment |
| [Manus](https://manus.app) | Web Platform | Multi-agent (lead + sub-agents), multi-modal | Code + web research |

## Search & Retrieval Infrastructure

### Search APIs for Agents

| Name | Type | Benchmark Stance | Key Features |
|------|------|------------------|--------------|
| [Tavily](https://tavily.com) | Search API | Use basic/fast depth and small result counts | LLM-optimized, clean text output |
| [SerpAPI](https://serpapi.com) | Search API | Not wired into the current benchmark | Google Search scraping, structured data |
| [Exa](https://exa.ai) | Neural Search | Cap search and content-read counts | Embedding-based, meaning-aware search |

### Vector & Knowledge Bases

| Name | Type | Use Case |
|------|------|----------|
| [Milvus](https://milvus.io) | Vector DB | Private data deep research |
| [Pinecone](https://pinecone.io) | Vector DB | Context caching, RAG |
| [ChromaDB](https://trychroma.com) | Vector DB | Embeddings storage |

## API Skill and Benchmark Status

The table below tracks whether this repo has a runnable skill for each API,
whether the API has a verified live benchmark smoke, and the latest under-`$1`
benchmark cost observed for the canonical `meta-deepresearchers` task. Quality
is reported as a reproducible structural proxy: OKF bundle validity plus output
size. It is not a human preference score.

| API / Provider | Env field | Skill | Verified live smoke | Latest cost | Quality proxy |
| --- | --- | --- | --- | ---: | --- |
| Gemini grounded research | `GOOGLE_API_KEY`, optional `GOOGLE_CLOUD_PROJECT` | `gemini-deep-research` | Yes, 2026-06-23 | `$0.0034` | OKF valid; 5,679 tokens / 22,587 chars |
| Perplexity Sonar | `PERPLEXITY_API_KEY` | `perplexity-sonar` | Yes, 2026-06-23 | `$0.0072` | OKF valid; 2,269 tokens / 8,944 chars |
| You.com Research | `YOU_API_KEY` | `you-research` | Yes, 2026-06-23 | `$0.0016` | OKF valid; 435 tokens / 1,610 chars |
| Tavily Search | `TAVILY_API_KEY` | `tavily-search` | Yes, 2026-06-23 | `$0.0016` | OKF valid; 563 tokens / 2,122 chars |
| Exa Search | `EXA_API_KEY` | `exa-research` | Yes, 2026-06-23 | `$0.0111` | OKF valid; 3,732 tokens / 14,797 chars |
| Jina Reader/Search | `JINA_API_KEY` | `jina-ai` | Yes, 2026-06-23 | `$0.2856` | OKF valid; 95,219 tokens / 380,746 chars |
| OpenAI Deep Research | `OPENAI_API_KEY` | `openai-deep-research` | Not yet live-smoked in this repo | n/a | Skill and env path present |
| xAI Grok | `XAI_API_KEY` | `xai-grok` | Not yet live-smoked in this repo | n/a | Skill and env path present |
| You.com Finance Research | `YOU_API_KEY` | `you-research` with `--api finance` | Not in under-`$1` smoke suite | n/a | Domain-specific skill path present |
| GPT Researcher | `OPENAI_API_KEY`, `TAVILY_API_KEY` | `gpt-researcher` | Not yet live-smoked in this repo | n/a | OSS framework skill present |
| LangChain Open Deep Research | `OPENAI_API_KEY`, optional model/search keys | `langchain-deep-research` | Not yet live-smoked in this repo | n/a | OSS framework skill present; server workflow |
| Stanford STORM | `OPENAI_API_KEY`, `YDC_API_KEY` or `BING_SEARCH_API_KEY` | `stanford-storm` | Not yet live-smoked in this repo | n/a | OSS framework skill present |
| Smolagents | `OPENAI_API_KEY`, optional `HF_TOKEN` | `smolagents` | Not yet live-smoked in this repo | n/a | OSS framework skill present |

Live smoke reports are written under `/tmp/adr-live-*-smoke/` during local
verification. Re-run them with:

```bash
op run --env-file .env.adr -- python benchmark/live_smoke.py -v
```

To send one prompt to multiple API providers at the same time and keep the raw
responses, use the fan-out script:

```bash
op run --env-file .env.adr -- python scripts/run_api_fanout.py \
  --output-dir outputs \
  "Deepresearch the deepresearchers. Keep each answer concise."

printf '%s\n' "Compare AI-for-science research agents." | \
  op run --env-file .env.adr -- python scripts/run_api_fanout.py --output-dir outputs
```

Each run creates `outputs/yyyy-mm-dd-hh-mm-ss-xxxx/` with
`<provider>.response.txt`, `<provider>.stderr.txt`, and `summary.json`.

## Benchmarks & Evaluation

- **[Humanity's Last Exam (HLE)](https://scale.com/leaderboard/humanitys_last_exam)** — Expert-level academic testing (Gemini 3: 45.8%, o3: 26-30%).
- **[GAIA](https://huggingface.co/gaia-benchmark)** — Multi-step real-world task execution (Smolagents: 55.15%).
- **[ScholarQA](https://github.com/allenai/scholarqa)** — Academic literature synthesis (DR-Tulu beats GPT-4).
- **[ARC-AGI](https://arcprize.org)** — Abstract reasoning (o3: 87.5%).

## What Makes an Agent Deep Research

A deep research agent plans an investigation, retrieves and reads multiple
sources, cross-checks claims, synthesizes a report, and preserves enough
citations or traces for audit. A fuller architecture and build-vs-buy guide is
available in `docs/deep-research-agent.md`.

## Domain-Specific Deep Research

Deep research tools should also be categorized by domain index: general web,
finance, medicine/life sciences, AI for science, legal/regulatory,
enterprise/internal data, and social/news sentiment. Domain-specific tools can
retrieve better sources but require tighter citation and compliance checks.

See `docs/domain-specific-deep-research.md`. It includes You.com Finance
Research, which uses a finance-optimized index for earnings analysis, due
diligence, competitive benchmarking, macroeconomic research, and regulatory or
filing analysis.

## Codex Plugin and Skills

This repo is also structured as a Codex Plugin via
`.codex-plugin/plugin.json`. The Codex-facing skills live in `.agents/skills/`:

- `deep-research-api-calls` documents API-key environment names, provider call
  patterns, cost controls, and under-$1 benchmark prompt guidance.
- provider-specific skills document OpenAI, Gemini, Perplexity, xAI, You.com,
  Exa, Tavily, Jina, GPT Researcher, LangChain Open Deep Research, STORM, and
  Smolagents call patterns.
- `okf-normalize-research` converts raw deep research reports into a small
  Open Knowledge Format-style markdown bundle.

Normalization guidance is in `docs/okf-normalization.md`. Canonical low-cost
benchmark tasks are in `docs/benchmark-tasks.md`. Provider source links are in
`.agents/skills/provider-source-index.md`.

1Password setup guidance is in `docs/onepassword-env.md`, with signup URLs and
required API-key field names in `docs/api-key-signup-checklist.md`.
Custom-source research guidance for Google Docs, YouTube, local files, S3,
arXiv, and related corpora is in `docs/custom-data-sources.md`.
Domain-specific tool categorization is in `docs/domain-specific-deep-research.md`.
Live provider smoke-test guidance is in `docs/live-benchmark-runbook.md`.

Run the offline repository audit before spending API credits:

```bash
python -m awesome_deep_research.audit
python -m awesome_deep_research.op_env --template
python -m awesome_deep_research.source_refresh
```

## Claude Code Skills

This repository includes ready-to-use **Claude Code Skills** for several key deep research APIs and frameworks. These skills enable you to leverage powerful research agents directly from Claude Code with simple Python scripts.

### Available Skills

| Skill Name | Type | Description |
|------------|------|-------------|
| [perplexity-sonar](.claude/skills/perplexity-sonar) | Commercial API | Real-time, citation-backed answers using Perplexity Sonar API |
| [xai-grok](.claude/skills/xai-grok) | Commercial API | Real-time web and X (Twitter) search with Grok Agent Tools |
| [exa-research](.claude/skills/exa-research) | Commercial API | Neural search, content retrieval, and automated research |
| [tavily-search](.claude/skills/tavily-search) | Commercial API | LLM-optimized real-time web search for RAG applications |
| [jina-ai](.claude/skills/jina-ai) | Commercial API | URL to Markdown conversion and web search |
| [gpt-researcher](.claude/skills/gpt-researcher) | Open Source | Autonomous research agent for comprehensive reports |
| [stanford-storm](.claude/skills/stanford-storm) | Open Source | Wikipedia-style article generation with citations |
| [openai-deep-research](.claude/skills/openai-deep-research) | Commercial API | Launch OpenAI Deep Research (o3/o4) autonomous research runs |
| [langchain-deep-research](.claude/skills/langchain-deep-research) | Open Source | Iterative research with reflection and knowledge gap analysis |
| [smolagents](.claude/skills/smolagents) | Open Source | Code-based agentic framework with 30% token efficiency gain |

### Installation

Each skill directory contains:

- `SKILL.md` - Complete documentation and usage examples
- `scripts/` - Python implementation scripts
- `requirements.txt` - Python dependencies

To install a skill:

```bash
cd .claude/skills/<skill-name>
pip install -r requirements.txt
```

For detailed documentation on Claude Code Skills, see [CLAUDE_SKILLS.md](CLAUDE_SKILLS.md).

## Headless Claude CLI Runner

Run Claude Code skills without the IDE using the `adr` CLI (exposed via `python -m awesome_deep_research.cli`). The tool wraps the `claude` binary and saves Markdown reports to disk.

1. **Prerequisites**

   - Install the [Claude Code CLI](https://www.anthropic.com/claude)
   - Configure API keys required by each skill (see `.claude/skills/<skill>/SKILL.md`)
   - Optional: install skill-specific dependencies listed in each `requirements.txt`

2. **Usage**

   ```bash
   # List installed Claude Code skills
   python -m awesome_deep_research.cli list-skills

   # List canonical research prompts sourced from docs/taxonomy-and-examples.md
   python -m awesome_deep_research.cli list-prompts

   # Run a headless research job and store the result in outputs/
   python -m awesome_deep_research.cli run \
     --skill perplexity-sonar \
     --prompt-id domain-mapping-01 \
     --output-dir outputs
   ```

   The CLI writes successive runs to `OUTPUT-{SKILL}-{NNNN}.md`. Pass `--prompt-text "..."` for ad-hoc briefs, `--model` to target a specific Claude model, and `--extra-instructions` to append custom guidance.

## Contributing

Contributions welcome! Please read the [contribution guidelines](CONTRIBUTING.md) first. Ensure all additions:

- Include a concise description explaining why the resource is awesome.
- Are actively maintained (updated within 12 months unless historically significant).
- Follow the established formatting and category structure.
- Pass `awesome-lint` checks.

## License

[![CC0](https://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg)](https://creativecommons.org/publicdomain/zero/1.0)

To the extent possible under law, the contributors have waived all copyright and related rights to this work.
