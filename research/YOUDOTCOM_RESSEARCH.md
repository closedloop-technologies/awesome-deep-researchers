# 🧠 Comprehensive Catalog of Deep Research APIs & Locally Hosted Systems (2025)

> **Key Takeaway:**
> The Deep Research API landscape in 2025 features a rich ecosystem of commercial (private/paid) and open-source (locally hosted) systems. These platforms automate multi-step research, leverage language models to orchestrate tool calls (web search, file, database, code, and more), and generate high-quality, citation-rich reports with full provenance tracking.

---

## What Is a Deep Research API?

A **Deep Research API** is a system that:

- Accepts a user prompt and may ask clarifying questions.
- Orchestrates multiple tool calls (web search, file/database access, code execution, etc.) using one or more language models.
- Compiles a well-cited, high-quality research document, with citations tied to each tool call or source.
- Supports provenance tracking, allowing users to trace claims back to their origins.

---

## 1. Commercial & Private-Paid Deep Research APIs

| Platform/API                | Key Features                                                                 | Pricing/Access                  | Notable Integrations                |
|-----------------------------|------------------------------------------------------------------------------|----------------------------------|-------------------------------------|
| **OpenAI Deep Research API** | Multi-step agentic research, prompt clarification, web & private data, full citation, tool orchestration, async/webhook | $10/1M input, $40/1M output tokens | Web search, MCP (private docs), code exec |
| **Microsoft Azure AI Foundry Deep Research** | Modular agentic workflows, Bing Search grounding, enterprise connectors, auditability | $10/1M input, $40/1M output tokens | Bing, Azure Logic Apps, MCP, custom tools |
| **Google Gemini Deep Research (API & Workspace)** | Multi-step planning, web & internal (Gmail, Drive) search, cited reports, audio summaries | $19.99/mo (Adv.), $20–$30/user/mo (Biz/Ent.), API: $2–$4/1M input, $12–$18/1M output | Google Search, Workspace, custom connectors |
| **Anthropic Claude API**    | Multi-step research, tool use, RAG, cited reports, enterprise features       | $3–$15/1M input, $15–$75/1M output | Web, files, Google/Microsoft 365, Slack |
| **Perplexity AI API**       | Autonomous research, real-time web/file search, cited reports, Copilot mode  | $20/mo Pro, $40/mo/user Ent., API: $0.002–$0.015/1K tokens | Web, file upload, Copilot, API      |
| **Grok DeepSearch (xAI)**   | Multi-step, cited research, real-time news/science, visual browser           | Beta, API upcoming               | Web, news feeds, Wikipedia, X       |
| **Aomni Deep Research**     | Web scraping, CRM/productivity integration, cited reports                    | Commercial, API                  | Web, Salesforce, HubSpot, Gmail     |
| **Elicit (Ought)**          | Systematic review automation, customizable, citation-rich reports            | Web, API in dev, free/paid       | Academic search, data extraction    |
| **NotebookLM (Google)**     | Multi-doc research, citation tracking, Google Drive integration              | Beta, API in dev                 | Google Drive, web                   |
| **CustomGPT**               | Source-linked responses, document/file search, citation management           | Commercial, API                  | Web, file system, custom docs       |

---

## 2. Open-Source & Locally Hosted Deep Research Systems

| System/Framework            | Key Features                                                                 | Installation/Hosting             | Community/Support                  |
|-----------------------------|------------------------------------------------------------------------------|----------------------------------|------------------------------------|
| **GPT Researcher**          | Multi-agent, web/local docs, citations, MCP, deep/recursive, export, frontend | Python, Docker, FastAPI/NextJS   | 7K+ GitHub stars, active           |
| **DeepResearchAgent (SkyworkAI)** | Hierarchical agents, browser ops, MCP, async, secure exec, local/remote LLMs | Python, Docker, vLLM/HF          | Modular, open-source               |
| **Langchain Open Deep Research** | Multi-model, modular, MCP, GUI config, benchmarking                        | Python, LLM APIs, Tavily         | LangChain, active                  |
| **Deep-Research (dzhng)**   | Iterative, recursive, markdown, concurrent, local LLM                        | Python, Docker, Firecrawl, LLM   | MIT, open                          |
| **Deep Research Agent (tarun7r)** | Multi-agent, credibility scoring, citation formatting, UI, local/cloud LLMs | Python, LangGraph, LangChain     | New, open                          |
| **RAGFlow**                 | Deep doc parsing, citation Q&A, visual block mgmt                             | Python, Docker, vector DB        | Enterprise, OSS                    |
| **Open Deep Research (nickscamara)** | Real-time web data, structured extraction, reasoning model                | Node.js, Python, Firecrawl, LLM  | 3K+ stars, active                   |
| **Enterprise Deep Research (SalesforceAIResearch)** | Multi-agent, real-time, citation mgmt, parallel, HITL                    | Python, Slack, LangGraph         | Salesforce, OSS                    |
| **Agentic Browser**         | Planner/browser/critique agents, web scraping, API/server                     | Python, uv, Docker               | PydanticAI, OSS                    |
| **Langchain Local Deep Researcher** | Iterative search/summarize, markdown, citations                            | Python, uv                       | LangChain, OSS                     |
| **Suna**                    | Browser automation, modular, multi-format output                               | Open-source, self-hosted         | Active development                  |
| **Manus AI**                | Chromium-based browser agent, multimodal, code execution                       | Commercial/open-source           | Modular, API/local                  |
| **ByteDance DeerFlow**      | Multi-agent, web search/crawling, code exec, RAG, MCP, human-in-loop          | CLI, FastAPI, Docker-compose     | Open-source, modular                |

---

## 3. Multi-Agent Frameworks & Developer Toolkits

| Framework/Platform          | Research Automation Features                                                  | Cited Output | Hosting/Integration         |
|-----------------------------|-------------------------------------------------------------------------------|--------------|----------------------------|
| **LangChain/LangGraph**     | Multi-agent, graph-based orchestration, 600+ tools, RAG, memory, LangSmith    | Yes          | Local/cloud, Python        |
| **Microsoft AutoGen**       | Conversation-driven, async multi-agent, code exec, DB, web, custom tools      | Yes          | Local/cloud, Python        |
| **CrewAI**                  | Role-based, multi-agent, RAG, LLMs, memory, task delegation                  | Yes          | Local/cloud, Python        |
| **LlamaIndex**              | RAG pipelines, vector DB, doc Q&A, analytics                                 | Yes          | Local/cloud, Python        |
| **OpenAI Agents SDK**       | Provider-agnostic, 100+ LLMs, self-host, OpenAI tools                        | Yes          | Local/cloud, Python        |
| **Google Agent Dev Kit**    | Model-agnostic, multi-agent, audio/video, tracing, safety                    | Yes          | Local/cloud, Python        |
| **n8n, Activepieces, Huginn, Node-RED** | Visual workflow automation, LLM integration, self-hosted                | Yes          | Local, open-source         |

---

## 4. Academic & Research Institution Systems

| System/Project              | Institution(s)                | Research Focus/Background                                  | Availability/Access                |
|-----------------------------|-------------------------------|-----------------------------------------------------------|------------------------------------|
| **Agentic AI & Deep Research Projects** | MIT CSAIL                     | Agentic AI, interpretability, multi-modal research agents  | Publications, some tools via partnership |
| **Virtual Scientists, Agentic Frameworks** | Stanford                      | Multi-agent research automation, data analysis, AlphaFold  | Publications, platform via collaboration |
| **AI Co-Scientist**         | Google DeepMind, Stanford     | Multi-agent hypothesis generation, web search, recursive reasoning | Trusted Tester, research papers    |
| **The AI Scientist**        | Oxford, UBC, DeepMind         | Fully automated scientific discovery, LLM autonomy         | Research paper, system for collaborators |
| **dzhng/deep-research, HKUDS/Auto-Deep-Research** | HKU, others           | Open-source, modular deep research agents                  | GitHub/institutional repos         |
| **LitSearch, ResearchArena, SciLitLLM, Agent Laboratory** | Multiple universities | Literature search, academic survey, multi-stage automation | Benchmarks, code often public      |

---

## 5. Emerging Startups & Notable New Entrants

| System/Startup              | Status/Availability                | Unique Features                                             |
|-----------------------------|------------------------------------|------------------------------------------------------------|
| **Grok DeepSearch (xAI)**   | Beta, API upcoming                 | Real-time, multi-source, cited reports, visual browser      |
| **AI2 Asta Platform**       | Beta, open-source                  | Agentic research assistants, benchmarking, toolkit          |
| **Zhipu AI AutoGLM**        | Commercial, research               | RL-based, self-refining, browser/code integration           |
| **Kompas AI**               | Commercial, paid                   | Evidence-backed research, in-text citations                 |
| **Mantle (YC)**             | Commercial, API                    | Agentic automation, multi-tool integration                  |
| **Landbase**                | Commercial, API                    | GTM research automation, agentic AI                         |
| **Periodic Labs**           | Stealth, $300M seed                | Autonomous labs, AI scientists, scientific discovery        |
| **FutureHouse**             | Nonprofit, research                | AI scientists for biology, open research                    |

---

## 6. Integration & Extensibility Highlights

- **Web Search:** All major systems support real-time web search (OpenAI, Azure, Google, Perplexity, open-source agents).
- **Internal/Private Data:** Model Context Protocol (MCP) is widely supported for connecting to private documents, file systems, and databases.
- **Custom Tools:** Plugin architectures and SDKs allow integration with custom APIs, code execution, and workflow automation.
- **Multi-Provider LLMs:** Many open-source systems support OpenAI, Anthropic, Gemini, Mistral, Ollama (local), and more.
- **Workflow Orchestration:** Advanced frameworks (LangChain, CrewAI, AutoGen, LangGraph) enable complex, multi-agent research pipelines.

---

## 7. Comparative Feature Table

| System/API/Framework        | Multi-Step Research | Clarifying Qs | Tool Calls (Web/File/DB) | Citation/Provenance | Local Hosting | API Access | Extensible/Custom Tools |
|-----------------------------|--------------------|---------------|--------------------------|---------------------|---------------|-----------|------------------------|
| OpenAI Deep Research API    | ✅                 | ✅            | ✅                       | ✅                  | ❌            | ✅        | ✅                     |
| Azure AI Foundry Deep Research | ✅              | ✅            | ✅                       | ✅                  | ❌            | ✅        | ✅                     |
| Google Gemini Deep Research | ✅                 | ✅            | ✅                       | ✅                  | ❌            | ✅        | ✅                     |
| Anthropic Claude API        | ✅                 | ✅            | ✅                       | ✅                  | ❌            | ✅        | ✅                     |
| Perplexity AI API           | ✅                 | ✅            | ✅                       | ✅                  | ❌            | ✅        | ✅                     |
| GPT Researcher (OSS)        | ✅                 | ✅            | ✅                       | ✅                  | ✅            | ✅        | ✅                     |
| DeepResearchAgent (OSS)     | ✅                 | ✅            | ✅                       | ✅                  | ✅            | ✅        | ✅                     |
| Langchain Open Deep Research| ✅                 | ✅            | ✅                       | ✅                  | ✅            | ✅        | ✅                     |
| ByteDance DeerFlow (OSS)    | ✅                 | ✅            | ✅                       | ✅                  | ✅            | ✅        | ✅                     |
| Suna (OSS)                  | ✅                 | ✅            | ✅                       | ✅                  | ✅            | ✅        | ✅                     |

---

## 8. Visual Summary: Deep Research API Ecosystem

> **Key Finding:**
> Whether you need a managed, enterprise-grade API or a fully local, open-source system, there are robust Deep Research solutions available for every use case—each supporting multi-step, tool-driven, citation-rich research automation.

---

## 🟢 **Conclusion**

The Deep Research API landscape in 2025 is vibrant and diverse, spanning:

- **Enterprise APIs** (OpenAI, Microsoft, Google, Anthropic, Perplexity) for scalable, managed research automation.
- **Open-source/local systems** (GPT Researcher, DeepResearchAgent, Langchain, DeerFlow, Suna) for privacy, customization, and extensibility.
- **Multi-agent frameworks** (LangChain, CrewAI, AutoGen) for building custom research agents and workflows.
- **Academic and emerging platforms** pushing the boundaries of autonomous, citation-backed research.

All these systems meet your definition: they accept prompts, clarify intent, orchestrate tool calls (web, file, database, code), and generate well-cited, provenance-rich research documents.
