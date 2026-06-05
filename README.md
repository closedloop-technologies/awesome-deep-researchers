# Awesome Deep Researchers [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated list of deep research APIs, libraries, and frameworks that enable autonomous multi-step information gathering, analysis, and synthesis with citations.

Deep research agents go beyond simple Q&A—they autonomously plan research strategies, execute multi-step queries across diverse sources, and synthesize findings into comprehensive, citation-backed reports.

## Contents

- [Commercial APIs](#commercial-apis)
- [Open Source Frameworks](#open-source-frameworks)
- [Specialized Research Tools](#specialized-research-tools)
- [Search & Retrieval Infrastructure](#search--retrieval-infrastructure)
- [Benchmarks & Evaluation](#benchmarks--evaluation)

## Commercial APIs

### General Purpose Deep Research

| Name | Type | Pricing | Key Features | Best For |
|------|------|---------|--------------|----------|
| [OpenAI Deep Research](https://openai.com/chatgpt) | API + Web UI | $10/1M input, $40/1M output tokens | o3-series reasoning, autonomous browsing, code execution, multimodal | Strategic analysis, legal research, complex synthesis |
| [Google Gemini Deep Research](https://gemini.google.com) | Web UI + API | $2.50/1M input, $10/1M output tokens | Google Search integration, workspace grounding, plan visibility | Corporate intelligence, internal data research |
| [Perplexity Sonar](https://perplexity.ai) | API + Web UI | $2/1M input, $8/1M output + $0.005/search | Real-time web index, sentence-level citations, live data | Market research, news synthesis, competitive intelligence |
| [xAI Grok](https://grok.x.ai) | API + Web UI | $5/1M input, $15/1M output tokens | Real-time X/Twitter data, social sentiment analysis | Crisis monitoring, social sentiment, finance |
| [You.com ARI](https://you.com) | API + Web UI | $15.00 per call | Analyzes 400+ sources, professional reports, data visualizations | Enterprise reports, analyst replacement |
| [Anthropic Claude](https://anthropic.com) | API + Web UI | Variable | Multi-agent research system, parallel agent spawning | Production research workflows |

### Specialized Deep Research

| Name | Type | Pricing | Domain Focus | Key Features |
|------|------|---------|--------------|--------------|
| [Jina DeepSearch](https://jina.ai) | API | $2/1M input, $8/1M output | Middleware agent | OpenAI-compatible endpoint, search-read-reason loop |
| [Exa Deep Search](https://exa.ai) | Search API | $5.00 per 1k searches | Neural search | Embedding-based retrieval, RAG-optimized content |
| [Elicit](https://elicit.org) | Web UI | Paid tiers | Academic literature | Paper analysis, research synthesis |
| [Consensus](https://consensus.app) | Web UI | Paid tiers | Scientific papers | Evidence-based answers from papers |
| [Scite](https://scite.ai) | Web + API | Paid tiers | Citation analysis | Smart citations, claim verification |

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

| Name | Type | Pricing | Key Features |
|------|------|---------|--------------|
| [Tavily](https://tavily.com) | Search API | $0.005/query | LLM-optimized, clean text output |
| [SerpAPI](https://serpapi.com) | Search API | Variable | Google Search scraping, structured data |
| [Exa](https://exa.ai) | Neural Search | $5/1k searches | Embedding-based, meaning-aware search |

### Vector & Knowledge Bases

| Name | Type | Use Case |
|------|------|----------|
| [Milvus](https://milvus.io) | Vector DB | Private data deep research |
| [Pinecone](https://pinecone.io) | Vector DB | Context caching, RAG |
| [ChromaDB](https://trychroma.com) | Vector DB | Embeddings storage |

## Benchmarks & Evaluation

- **[Humanity's Last Exam (HLE)](https://scale.com/leaderboard/humanitys_last_exam)** — Expert-level academic testing (Gemini 3: 45.8%, o3: 26-30%).
- **[GAIA](https://huggingface.co/gaia-benchmark)** — Multi-step real-world task execution (Smolagents: 55.15%).
- **[ScholarQA](https://github.com/allenai/scholarqa)** — Academic literature synthesis (DR-Tulu beats GPT-4).
- **[ARC-AGI](https://arcprize.org)** — Abstract reasoning (o3: 87.5%).

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


## Benchmarks

- [REFUTE](https://huggingface.co/datasets/BGPT-OFFICIAL/refute) — Apache-2.0 benchmark for scientific critique & epistemic calibration on recent science summaries. Separates critique skill from calibrated truthfulness (falsification, limitations, overclaims, missing-evidence refusal, confidence calibration, planted-flaw detection). [Leaderboard](https://huggingface.co/spaces/BGPT-OFFICIAL/refute-leaderboard) · [Technical report](https://huggingface.co/datasets/BGPT-OFFICIAL/refute/blob/main/TECHNICAL_REPORT.md) · [Integrators](https://huggingface.co/datasets/BGPT-OFFICIAL/refute/blob/main/INTEGRATORS.md)
