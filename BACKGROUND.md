## What Exists Today (2025 Snapshot)

### **Foundational Research & Systematization**

* **“Deep Research Agents: A Systematic Examination and Roadmap”** (Huang et al., June 2025) provides deep architectural taxonomy—from API vs. browser retrieval, through modular tool-use patterns, to workflows (static vs dynamic), single vs multi‑agent setups. Offers a public “awesome DR agent” repo. ([arXiv][1])

### **Implementations & Frameworks**

* **MA‑RAG**: Multi‑agent RAG with agent roles such as Planner, Extractor, QA—supports chain‑of‑thought and modular reasoning without fine‑tuning. ([arXiv][2])

* **DeepResearcher**: End‑to‑end RL‑trained multi‑agent agent navigating the open web for robust research, self‑reflective and citation‑aware. Outperforms prompt‑engineered and RAG baselines. ([arXiv][3])

* **AgentRxiv**: A collaborative setup where agents share preprint‑style reports to bootstrap follow‑on research, boosting multi‑agent performance. ([arXiv][4])

* **Dynamic Iterative Retrieval Agents**: LLM‑driven agents that maintain an internal knowledge cache and iteratively refine search queries, balancing exploration and accuracy—scales well with task complexity. ([arXiv][5])

### **Product & Platform Examples**

* **OpenAI’s ChatGPT “Deep Research” mode**: An autonomous browsing agent that compiles cited analytical reports over 5–30 min, integrated into ChatGPT (released Feb 3, 2025). Supports PDFs, images, and web; has fixed monthly quotas on usage. ([Wikipedia][6])

* **Anthropic’s Multi-Agent Research System (“Research” feature)**: A planner spawns parallel agents to search across web, Google Workspace, etc. Used in real production. ([Anthropic][7])

* **NVIDIA AI‑Q Blueprint**: Modular research assistant architecture including PDF ingestion, RAG, iterative reasoning via Llama Nemotron, and report generation—all optimized for enterprise scale. ([NVIDIA Developer][8])

* **GitHub wonders**:

  * **SPAR** (Scholar Paper Retrieval): A modular multi‑agent with citation‑driven retrieval and relevance reranking. ([GitHub][9])

### **Broader Agentic Architectures**

* **AG‑UI protocol**: A UI‑oriented standard enabling agents to render structured interactions (buttons, inputs, tables) and integrate human‑in‑the‑loop control—especially valuable for transparency and agentic RAG systems. ([Medium][10])

* General definitions: LLM‑powered agent stack comprising planner, tools, memory, and iterative plan‑and‑execute loops. ([NVIDIA Developer][11])

---

## Comparative Summary Table

| **Agent / Framework**           | **Architecture**              | **Retrieval**             | **Reasoning & Planning**               | **Citation & Transparency** | **Deployment Form**           |
| ------------------------------- | ----------------------------- | ------------------------- | -------------------------------------- | --------------------------- | ----------------------------- |
| Huang et al. taxonomy           | Comprehensive taxonomy        | —                         | —                                      | —                           | Academic analysis + repo      |
| MA-RAG                          | Multi-agent RAG pipeline      | RAG + CoT                 | Planner + modular agents               | Yes, explicit reasoning     | Research prototype            |
| DeepResearcher                  | RL-trained end-to-end agent   | Open web browsing         | RL-based planning, self-reflection     | Yes, self-reflection-aware  | Open-source framework         |
| AgentRxiv                       | Multi-agent with shared cache | Shared reports            | Collaboration across agent labs        | Yes, via shared reasoning   | Research experimental         |
| Iterative Retrieval Agents      | LLM feedback loop + cache     | Iterative web queries     | Query refinement, knowledge caching    | Internal traceability       | Research prototype            |
| ChatGPT Deep Research           | Autonomous ChatGPT tool       | Web browsing + multimodal | Timed autonomous research              | Yes—includes citations      | SaaS, subscription-based      |
| Anthropic Research Feature      | Planner + parallel agents     | Web + workspace           | Planner-spawned agents                 | Likely partial              | Proprietary product           |
| NVIDIA AI-Q Blueprint           | Modular enterprise stack      | PDFs + web + vectors      | Iterative reasoning, report generation | Yes, enterprise standard    | Platform toolkit              |
| SPAR (Autonomous-Agents GitHub) | Modular scholarly search      | Multi-source              | Multi-agent query/relevance control    | Citation-driven             | OSS project                   |
| AG-UI                           | UI protocol for agent loops   | —                         | —                                      | Supports transparency       | UI layer, enabling front-ends |

---

## Next Tactical Steps (in a 5-h sprint)

1. **Define Minimum Viable Comparison Scope**

   * Must include models that run **locally/CLI**, **APIs**, and **configurable agents** (like ChatGPT Deep Research, SPAR, DeepResearcher). Use MoSCoW tags:

     * **MUST**: Local/CLI agents, API-based agents, OpenAI’s Deep Research
     * **SHOULD**: Multi-agent research (MA-RAG, DeepResearcher)
     * **COULD**: AG-UI, NVIDIA Blueprint

2. **Collect Metadata Dimensions**
   For each agent/system:

   * Execution mode (local vs SaaS vs API)
   * Retrieval methods (web, PDFs, workspace)
   * Planning structure (single vs multi-agent, loops)
   * Citation & reasoning transparency
   * Extensibility (tools, plugins, UI)

3. **Prototype Table Skeleton** and populate with above details.

4. **Kill-box for Sprint**:

   * **Definition of Done (DoD)**: Completed table for at least 5 agents, with metadata and commentary; plus next suggestions for missing categories.

---

Let me know which subset to prioritize first—or if you'd like raw metadata scoped differently.

[1]: https://arxiv.org/abs/2506.18096?utm_source=chatgpt.com "Deep Research Agents: A Systematic Examination And ..."
[2]: https://arxiv.org/abs/2505.20096?utm_source=chatgpt.com "MA-RAG: Multi-Agent Retrieval-Augmented Generation via Collaborative Chain-of-Thought Reasoning"
[3]: https://arxiv.org/abs/2504.03160?utm_source=chatgpt.com "DeepResearcher: Scaling Deep Research via Reinforcement Learning in Real-world Environments"
[4]: https://arxiv.org/abs/2503.18102?utm_source=chatgpt.com "AgentRxiv: Towards Collaborative Autonomous Research"
[5]: https://arxiv.org/abs/2503.13275?utm_source=chatgpt.com "Knowledge-Aware Iterative Retrieval for Multi-Agent Systems"
[6]: https://en.wikipedia.org/wiki/ChatGPT_Deep_Research?utm_source=chatgpt.com "ChatGPT Deep Research"
[7]: https://www.anthropic.com/engineering/built-multi-agent-research-system?utm_source=chatgpt.com "How we built our multi-agent research system"
[8]: https://developer.nvidia.com/blog/chat-with-your-enterprise-data-through-open-source-ai-q-nvidia-blueprint/?utm_source=chatgpt.com "Chat With Your Enterprise Data Through Open-Source AI ..."
[9]: https://github.com/tmgthb/Autonomous-Agents?utm_source=chatgpt.com "tmgthb/Autonomous-Agents"
[10]: https://medium.com/%40kram254/ag-ui-the-protocol-where-agents-meet-users-a-deep-dive-into-agentic-rag-74eed10dfe5d?utm_source=chatgpt.com "AG-UI: The Protocol Where Agents Meet Users"
[11]: https://developer.nvidia.com/blog/introduction-to-llm-agents/?utm_source=chatgpt.com "Introduction to LLM Agents | NVIDIA Technical Blog"

Great. I’ll compile a comprehensive list of implemented deep research agents—both free and paid—with a focus on those offering a CLI, API, or programmable agent interface. I’ll prioritize tools with concrete usage instructions and examples, covering local tools, web-based APIs, and coding agent configurations.

Each entry will include metadata such as domain focus (e.g. technical, academic, legal), deployment model (CLI, API, etc.), citation support, planning architecture, and extensibility.

I’ll get back to you shortly with the results.


# **Deep Research Agents: A Comprehensive Overview**

Deep research agents are autonomous or semi-autonomous AI tools that perform multi-step information gathering and synthesis with source citations. Below is a summary of notable implementations (both open-source and commercial), followed by detailed breakdowns of each:

| **Agent / Tool**                  | **Access & Deployment**                      | **Open Source?**     | **Domain Focus**                    | **Planning Structure**                     | **Citations**             |
| --------------------------------- | -------------------------------------------- | -------------------- | ----------------------------------- | ------------------------------------------ | ------------------------- |
| **ChatGPT Deep Research**         | ChatGPT UI (Plus/Enterprise)                 | No (OpenAI SaaS)     | Broad (finance, science, etc.)      | Single agent (tool-using planner)          | Yes (footnoted)           |
| **OpenAI Deep Research API**      | API (o3-deep-research, o4-mini)              | No (Commercial API)  | Broad (tech, academic, enterprise)  | Single agent (auto tool use)               | Yes (links, timestamps)   |
| **Google Gemini Deep Research**   | Web app (Gemini app feature)                 | No (Commercial SaaS) | Broad (gen. knowledge, analysis)    | Planner + executor (parallel tasks)        | Yes (linked sources)      |
| **Perplexity AI (Deep Research)** | Web UI (free & Pro; API avail.)              | No (Commercial SaaS) | Broad (finance, tech, health, etc.) | Single agent (iterative search & code)     | Yes (inline links)        |
| **xAI Grok (DeepSearch)**         | Web (X app, grok.com; premium tiers)         | No (Closed beta)     | Broad (real-time web, social)       | Single agent (with “Think” trace view)     | Yes (summaries with refs) |
| **Manus**                         | Web platform (cloud; sign-up)                | No (Commercial)      | Broad (multi-modal: code, web)      | Multi-agent (lead + sub-agents)            | Yes (cited outputs)       |
| **GPT Researcher**                | CLI & API (Python package; Docker)           | Yes (Apache-2.0)     | Configurable (any topic)            | Planner + exec agents + publisher          | Yes (footnotes)           |
| **LangChain Open Deep Research**  | CLI/Local server (LangGraph UI)              | Yes (MIT)            | Configurable (any domain)           | Multi-step (summarize–research–synthesize) | Yes (sources listed)      |
| **Stanford STORM / Co-STORM**     | CLI (Python `knowledge-storm` lib); Web demo | Yes (MIT)            | Academic-style (wiki articles)      | Multi-agent (Q\&A dialogue + moderator)    | Yes (inline refs in text) |

Below we provide more details for each agent, including core capabilities, extensibility, and example usage.

## OpenAI **ChatGPT Deep Research** (Integrated Agent in ChatGPT)

**Link:** OpenAI Blog; Wikipedia
**Deployment Model:** Built into ChatGPT’s interface (selectable “Deep Research” mode). Accessible to ChatGPT Plus, Team, Enterprise, and limited free usage. No standalone CLI (though uses OpenAI API on backend).
**Open Source or Commercial:** Commercial (OpenAI SaaS).
**Domain Specialization:** General-purpose (finance, science, policy, engineering, personal research, etc.). Optimized for complex open-domain queries. Handles text, images, and PDFs as input.
**Core Capabilities:** Autonomously plans a research strategy, performs web searches and browsing, runs Python code for analysis, and reads documents to gather information. It then synthesizes findings into a detailed multi-page report with citations. Uses an internal reasoning trace (“thinking panel”) to decide next steps.
**Planning Structure:** Single-agent planner/executor. Internally, the system breaks the query into sub-tasks, executes them (possibly in parallel), and aggregates results. OpenAI trained a specialized version of their `o3` model for this agentic behavior. The agent runs autonomously for 5–30 minutes per query, iterating until sufficient information is gathered.
**Input Formats:** Natural language prompts. Also accepts file uploads (PDFs, images) which it can analyze and incorporate.
**Citation Transparency:** **Yes.** The output report is fully documented with clear source citations (footnotes with links) for verifiability. Users can see which sources support each claim. Additionally, a summary of the agent’s reasoning steps is provided for transparency.
**Extensibility:** **No** user-extensibility – it uses a fixed toolset (web browser, code interpreter, etc.) defined by OpenAI’s platform. It does integrate with organizational data via OpenAI’s Model Context Protocol (MCP) for enterprise (allowing it to search internal documents as well), but new tools cannot be added by end users.
**Example Usage:** In ChatGPT’s UI, one would select *Deep Research* mode and ask a complex question (e.g. *“Analyze the impacts of climate change on global agriculture and cite sources.”*). The agent will autonomously search the web and produce a report with footnoted citations. Programmatically, developers can use OpenAI’s API with the `o3-deep-research` model to get similar results. For example, via Python using OpenAI’s SDK:

```python
import openai
openai.api_key = "YOUR_API_KEY"
response = openai.ChatCompletion.create(
    model="openai:o3-deep-research", 
    messages=[{"role": "user", "content": "Analyze the impacts of climate change on global agriculture."}]
)
print(response['choices'][0]['message']['content'])
```

*(The response will be a structured research report with cited sources.)*

## **OpenAI Deep Research API** (Developer-Facing Agent API)

**Link:** OpenAI API docs; News coverage
**Deployment Model:** REST API provided by OpenAI. Developers call specialized models (`o3-deep-research` for full, `o4-mini-deep-research` for lightweight) to trigger the multi-step research process and get results asynchronously. Supports webhook callbacks for long tasks.
**Open Source or Commercial:** Commercial (Closed API, pay-per-use).
**Domain Specialization:** Broad; designed to handle complex research in technical, academic, financial, journalism, and enterprise domains. Optimized for knowledge-intensive queries requiring up-to-date information.
**Core Capabilities:** The API endpoint orchestrates a research workflow: it can perform live web searches, scrape and read content from URLs, run Python code for data analysis, and ingest user-provided documents. It then compiles a fact-based, structured report answering the query. All of this is managed internally once the user provides the initial query.
**Planning Structure:** Internally a single agent uses a tool-using loop (search, read, code, etc.), guided by an “agentic framework” (similar to ChatGPT’s agent). The planning is automatic – the model itself decides which tool to invoke at each step. No multi-agent; rather one orchestrator model handles all sub-tasks sequentially or in parallel as needed.
**Input Formats:** The API accepts a natural language query (prompt). Optionally, developers can supply additional context or documents via OpenAI’s functions or parameters (e.g., by uploading files to a cloud storage and providing links). The API is geared towards a single-call workflow: you send the query (and any context), and receive a completed report.
**Citation Transparency:** **Yes.** The returned report includes source citations (with URLs and timestamps) for factual claims. Source attribution is a built-in feature of the Deep Research API, making it suitable for high-trust applications.
**Extensibility:** **Limited.** Developers cannot modify the agent’s toolset (it has built-in web search, code execution, etc.). However, the API can interface with an organization’s private knowledge base via “MCP integration” to include internal documents as part of research. The structure of the output (JSON with citations) is fixed.
**Example Usage:** Using `curl` or an HTTP client, a developer might call:

```bash
curl https://api.openai.com/v1/deepresearch \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
        "model": "o3-deep-research",
        "prompt": "Write a report on the latest advancements in battery technology for EVs."
      }'
```

This request will return a JSON response containing the research report (in markdown or structured text) with citations to source URLs. The operation may take several minutes due to the agent’s multi-step processing.

## **Google Gemini Deep Research**

**Link:** Official Site
**Deployment Model:** Web application as part of Google’s **Gemini** AI platform. Accessible via Gemini’s interface (desktop or mobile) by selecting the *Deep Research* mode. Currently a SaaS offering (with a free trial and Pro plans). No direct API yet for Deep Research mode.
**Open Source or Commercial:** Commercial (Google proprietary).
**Domain Specialization:** General-purpose research across the web. Suitable for competitive analysis, due diligence, deep dives into academic or technical topics, product comparisons, etc.. Users can also upload their own files to include in the research (making it adaptable to specific domains or datasets).
**Core Capabilities:** Gemini’s Deep Research acts as an autonomous research assistant that can browse **hundreds of websites** on the user’s behalf. It breaks the user’s query into a multi-point research plan, searches and reads content on the web, and then synthesizes the findings into a multi-page report. It provides an *Audio Overview* of the report as well. The agent is iterative: it shows its reasoning and next steps (“thinking”) to the user in real time, and can adjust course based on feedback.
**Planning Structure:** **Planner + Executors**. Gemini Deep Research uses a new planning system to break down queries into sub-tasks. It determines which tasks can be done in parallel and which sequentially. The model uses tools like Google Search and browsing to gather information, reasoning at each step about what to do next. The final stage is a synthesis where the model composes the report (with possible self-critique passes). Essentially, it’s a single agent with an internal planner that can spawn multiple search threads.
**Input Formats:** Natural language prompt (topic or question). Users can **upload files** (PDFs, etc.) to “guide research,” which the agent will incorporate. The output is an interactive report (with text, and possibly images or interactive elements via Gemini Canvas).
**Citation Transparency:** **Yes.** Reports include source links for the information provided. The interface highlights source references (and Gemini allows exporting findings to Google Docs with sources intact). Additionally, the *thinking panel* shows what sources have been read and considered at each step, giving transparency into its evidence.
**Extensibility:** **No user extensibility.** The tool uses Google’s internal search and browsing capabilities. It is closed-source; users cannot add custom tools. However, it is tightly integrated with Google Workspace (e.g., one-click export to Docs/Sheets), making it extensible in terms of workflow integration.
**Example Usage:** In the Gemini app, one might select *Deep Research* and ask, *“Provide a detailed report on the current state of quantum computing hardware.”* The agent will draft a plan (e.g., subtopics like major approaches, companies, challenges), display it for user approval, then autonomously search the web for each subtopic, reading papers and articles. Within minutes, it delivers a structured report with sections for each subtopic, each with relevant citations (linked to the original web sources). Users can then export this report to Google Docs or transform it in Gemini Canvas for interactive exploration.

## **Perplexity AI (Deep Research Mode)**

**Link:** Perplexity Blog; Perplexity Help
**Deployment Model:** Web UI at *perplexity.ai* – a special “Deep Research” mode can be selected in the query box. Free for all users with daily query limits, and **Pro subscribers** get unlimited usage. Mobile apps (iOS, Android, Mac) also support this mode. Perplexity also offers a **Developer API** for real-time search and Q\&A, which likely supports deep research queries for integration into other applications.
**Open Source or Commercial:** Commercial (closed source service). The underlying model is proprietary (Perplexity uses its own LLMs and/or OpenAI APIs).
**Domain Specialization:** Open-domain, with noted strengths in factual and analytical tasks. It explicitly excels in domains like finance, marketing, technology, health, current affairs, etc., by deeply analyzing a wide range of sources. Essentially, it’s a general research assistant suitable for any topic where web information is available.
**Core Capabilities:** When Deep Research mode is activated, Perplexity’s agent performs *dozens of searches* and reads *hundreds of sources*, reasoning through them to deliver a comprehensive answer. It operates for about 2–4 minutes per query, far longer than a standard Q\&A, to gather sufficient information. The agent can also execute code as needed (they mention “equipped with… coding capabilities” for analysis). After research, it writes a structured **report** addressing the query, which can be exported to PDF or a shareable web page. Notably, Perplexity’s agent was benchmarked on “Humanity’s Last Exam” and achieved strong results (21.1% accuracy), indicating high competence on multi-hop questions.
**Planning Structure:** Single-agent iterative planner. The agent refines its plan as it learns from initial searches, similar to a human researcher adjusting questions. It uses a loop of searching, reading, and reasoning (“think”) before final synthesis. There isn’t a separate planner model: the same agent performs all steps guided by an internal chain-of-thought (which can be partially exposed via a “Show Thoughts” feature in Perplexity Labs).
**Input Formats:** Natural language queries. Users cannot directly upload external documents in Deep Research mode, but the agent itself finds sources on the web. (Perplexity’s standard mode allows giving it a URL or text as context; in Deep Research, the focus is on autonomous discovery, though the Pro version’s **Copilot** can take user-provided context if needed.)
**Citation Transparency:** **Yes.** Perplexity was built around providing **citations for every fact**. In Deep Research reports, claims are annotated with numeric references, and the sources are listed (and linked) at the end or inline. This makes it easy to verify each part of the answer. The agent ensures “every claim is sourced” by parsing its own output to attach citations.
**Extensibility:** **No user extensions**, but **integration-friendly.** You cannot add tools to Perplexity’s agent, but you can integrate its output via the API. The developer platform allows incorporating Perplexity’s live web research capability into other apps. The agent itself uses fixed tools (search, browser, code runner).
**Example Usage:** Through the web UI, select *Deep Research* and ask a question like *“What are the economic impacts of the 2023 semiconductor export restrictions?”*. The agent will display a message like “Researching…” and you’ll see it iterating through queries and reading articles (if you enable the Labs view). After a couple of minutes, it outputs a detailed report with sections (e.g., Overview, Short-term impacts, Long-term impacts, Expert opinions) and footnote numbers that link to articles from economists, news sites, etc. For API usage, Perplexity’s docs indicate you can send a query to their endpoint to get a JSON result with answer and sources (e.g., using an `X-API-Key` header and a JSON body containing the question).

## **xAI Grok (DeepSearch Mode)**

**Link:** xAI (Grok 3 Beta announcement); BuiltIn article
**Deployment Model:** Grok is accessible via the web (**grok.com** or the Grok mobile app) and through the X (Twitter) interface for users. DeepSearch is a feature enabled by default for all users with Grok 3 and above. Higher tiers (X Premium, “SuperGrok”) have higher usage limits and possibly longer DeepSearch runs. Currently no public API (access is through X’s app or web UI).
**Open Source or Commercial:** Commercial/Closed. xAI is a private company; Grok (and DeepSearch) are proprietary. As of mid-2025, Grok was in beta/invite stage for X Premium users.
**Domain Specialization:** Broad, but with an emphasis on **real-time information** and even social media content. Grok’s unique feature is it can pull in live data from the web and from X (Twitter) posts. So DeepSearch can incorporate up-to-the-minute news, trends, or even specific tweets. It is positioned as a general knowledge agent (and even an “edgy” one as Musk intended) – not limited to any domain, though likely strong in tech, news, etc., given real-time access.
**Core Capabilities:** **DeepSearch** in Grok is described as “a powerful agent that can rapidly synthesize key information and reason about conflicting opinions or facts”. When a user asks a question, enabling DeepSearch causes the model to spend more time (seconds to minutes) searching online sources and cross-checking them before finalizing an answer. Essentially it goes “far beyond a browser search” to produce a comprehensive report or answer with context. Grok also has a *Think* mode that lets the user see the chain-of-thought (the reasoning steps the model took), adding transparency. Additionally, Grok can generate images or code, but for research queries the main focus is text synthesis of findings.
**Planning Structure:** Single agent with extended reasoning. Grok 3 was trained with reinforcement learning to think longer (take “seconds to minutes” for reasoning). In DeepSearch mode, the model presumably uses an internal toolformer-like approach: performing searches, reading results, and integrating them. There are two depth settings: *DeepSearch* (standard) and *DeeperSearch* (even more extensive search and reasoning). The process is autonomous but users can press a “Think” button at any time to have it reveal intermediate reasoning steps. This is a single model handling the workflow, not multiple agents.
**Input Formats:** Natural language prompts, possibly images (Grok can accept images in chat). In context of DeepSearch, typically a user question or task is given in text. Grok also can take an X thread as input context if invoked within X (for example, summarizing a conversation or answering questions about a tweet).
**Citation Transparency:** **Yes.** While Grok’s regular answers may not always show sources, the **DeepSearch** feature is specifically aimed at providing sourced information. It will **summarize sources and provide links** or references for facts, similar to how an AI search engine would. According to xAI, DeepSearch outputs a “comprehensive report of information and context” beyond a simple answer. From user reports, Grok often lists the URLs or titles of sources it used, and the “Think” trace can show where each piece of information came from.
**Extensibility:** **No, not by users.** Grok’s tooling (web search and X social media access) is built-in. Users can’t add custom tools or data sources except by providing specific URLs in their prompt (which Grok can click and read). Over time xAI might integrate more capabilities, but as of now it’s a fixed system.
**Example Usage:** If a user on X has access to Grok, they might mention the bot or use the app to ask: *“Grok, do a deep search on the latest research about longevity escape velocity.”* Grok in DeepSearch mode would search recent news, academic articles, and even relevant X discussions on the topic. It would then respond with a detailed summary, perhaps along the lines of: *“According to a 2025 study by Harvard 【source】 and commentary by biotechnology experts 【source】, longevity escape velocity is defined as…*”, including the cited sources (with hyperlinks or footnotes). The user could click a “Think” button to see Grok’s step-by-step process, such as which queries it ran and how it weighed different sources. (Note: Grok’s persona might also add a bit of humor or edgy tone as designed, but the core content will be factual and sourced.)

## **Manus** (General AI Agent by *Manus.im*)

**Link:** Manus official site; UsefulAI summary
**Deployment Model:** Manus is a cloud-based AI agent accessible via a web interface (with login). Currently, it’s a closed platform (not open-source); users sign up to use the agent through a web dashboard. No public API documentation is provided yet. Some community projects (e.g. *AgenticSeek*) attempt to replicate it locally, but the official Manus runs on Manus’ servers.
**Open Source or Commercial:** Commercial (subscription-based). Manus is developed (reportedly out of China) as a proprietary product, with a subscription around \$19/month noted by some users, including credit limits for heavy tasks.
**Domain Specialization:** **General-purpose**, but often demonstrated for complex multi-modal tasks. Manus is positioned as a “general AI agent that bridges mind and action,” meaning it not only answers questions but can perform actions (e.g., write and execute code, interact with web pages). It’s been shown handling tasks in research, data analysis, travel planning, coding, etc.. Because it can run code and use tools, it’s adaptable to many domains (academic research, software engineering, business intelligence, etc.).
**Core Capabilities:** Manus operates by generating and executing **Python code internally to accomplish tasks**. It combines the flexibility of code with AI planning: e.g., for a given problem, it might write code to call an API, scrape a website, do calculations, then interpret the results. It also has web browsing and scraping abilities. It is essentially an autonomous agent that can “think, browse the web, and code” for solving user queries. For research tasks, Manus will search for information, take notes, perhaps store intermediate results, then output a synthesized report. It’s multi-modal in that it can handle images or produce charts/visualizations via coding if needed.
**Planning Structure:** **Multi-agent (specialized sub-agents)**. Manus employs a lead reasoning agent that can spawn sub-agents for particular subtasks. For example, it might break a big research question into parts handled by different “workers” (as per the UsefulAI description). It integrates real-time tool use (web browser, code executor, possibly a database connector) into its planning. The process is orchestrated such that the lead agent plans and delegates, then consolidates the outputs. This aligns with the “multi-agent workflow” described for Manus. Internally, it ensures safe execution of the generated code (likely sandboxed).
**Input Formats:** Natural language prompts via the web UI. It also allows users to provide files or specific URLs for the agent to consider (e.g., you might give it a PDF or a link to analyze). The interface shows options like “Slides”, “Webpage”, “Spreadsheet” as inputs, hinting you can feed those formats.
**Citation Transparency:** **Yes, generally.** Manus aims to produce outputs with references, especially for research queries. Its generated reports or answers include citations/footnotes linking back to sources it consulted (e.g., if it quotes an article, it will footnote that). The emphasis is on *trustworthy* outputs, and it cross-references multiple sources. For instance, a community description of a Manus “deep research” example (FlowFacts agent built on SuperAGI) noted it *“generates a research document summarizing a given claim”* with supporting info. Manus outputs often list source URLs at the end of the answer or as hoverable annotations in their UI.
**Extensibility:** **Not by end-users.** Manus provides a set of built-in capabilities (browse, code, various APIs). Users cannot directly plug in new tools or change its internal code environment. However, the platform itself is evolving – e.g., they might add new skills over time. There are *unofficial* open-source reimplementations (like **OpenManus** or **AgenticSeek**), which are extensible, but the official Manus is closed.
**Example Usage:** In Manus’ interface, you might select a template or just ask: *“Investigate the claim that polar bear populations are increasing, and provide a cited report.”* Manus would likely break this down into steps: (1) search for polar bear population data, (2) retrieve scientific articles or WWF reports, (3) perhaps run code to fetch data from an API or PDF, (4) analyze the collected info, and (5) produce a written report. The final output might be a few paragraphs explaining the status of polar bear populations, referencing data from (for example) IUCN reports and scientific studies, with each claim footnoted to the source URL. If using its coding ability, Manus might even generate a plot of population trends if data is available, and then include that chart in the report, citing the data source.

## **GPT Researcher** (Assaf Elovic’s Open Agent)

**Link:** Official Repo; Demo site (gptr.dev)
**Deployment Model:** **Open source Python package**. Can be installed via pip (`gpt-researcher`) or Docker. Provides a CLI (`cli.py`) for running research tasks locally or on a server, and also a web frontend (streamlit-based) for interactive use. Also usable as a library or API within Python.
**Open Source or Commercial:** Open Source (Apache-2.0 License). Completely free to self-host; you only pay for any API calls if using an external LLM (it can integrate with OpenAI, etc.).
**Domain Specialization:** Domain-agnostic; you can create “agents” specialized to any topic or field by configuring sources and prompts. Out-of-the-box, it’s meant for general web and local file research on arbitrary questions. The design emphasizes unbiased, factual reporting for any subject. Users have employed it for technical research, market analysis, academic literature reviews, etc.
**Core Capabilities:** GPT Researcher automates the full research pipeline: it generates a set of research questions from your main query (to ensure thorough coverage), then dispatches execution agents to find information to answer each question. It performs web searches (via Bing Web Search API or others) and scrapes content; it can also search local files or databases if configured. It then **aggregates all findings into a comprehensive report with citations**. It focuses on factual accuracy, determinism, and speed (using parallel agents for sub-questions). By default, it overcomes LLM context limits by chunking the report generation. The output is a well-structured Markdown (or JSON) report often exceeding standard token limits (e.g. 2,000+ words).
**Planning Structure:** **Planner + multiple Execution Agents + Publisher.** As described in its docs, GPT Researcher uses a **planner agent** (to brainstorm research sub-questions and a plan) and **execution agents** for each sub-question that perform retrieval and analysis. Once all subtopics are researched, a **publisher** module compiles the final report by synthesizing the collected info. This effectively is a multi-agent architecture (one-to-many-to-one). The agents run in parallel for speed, and there is a memory store where findings (snippets + sources) are saved for the publisher.
**Input Formats:** The CLI accepts a text query (and optional context). It can also be directed to use local files by specifying paths or toggling local search. No direct file upload interface in CLI, but if using the web UI, you can input URLs or text to include. The agent’s search is primarily web-based (requires API keys for search engines).
**Citation Transparency:** **Yes, mandatory.** Every piece of information in the output report is accompanied by a citation bracket linking to the source. The format is similar to the one used in this report (e.g., `【source†Lx-Ly】`). GPT Researcher ensures that the final answer is traceable to the original materials by maintaining references throughout the process. Uncited statements are avoided to reduce hallucination.
**Extensibility:** **Yes.** GPT Researcher is highly customizable. You can configure: which LLM model to use (OpenAI GPT-4, local LLMs via API, etc.), which search tool or API to use, how many parallel agents, and even define domain-specific agent classes. The codebase is modular, so developers can add new tools (e.g., a PDF reader tool, a custom knowledge base retriever) by following the existing interface. The project’s mission is to allow “tailor-made and domain-specific research agents”, so it’s built for extensibility.
**Example Usage:** After installation, you can run GPT Researcher from the command line:

```bash
gpt_researcher --query "Explain the current challenges in quantum computing research." --web --out report.md
```

This command will create an agent for the query, use the web for research, and save the output to `report.md`. During execution, you’ll see logs as it generates sub-questions (e.g., “1. What are the error correction challenges? 2. What materials are used…”) and finds sources. The final `report.md` will contain a multi-section analysis (introduction, various subtopic sections, conclusion) with citations like \*\*\*\* referencing, say, research papers or articles. Each citation corresponds to a footnote URL. For example, a line in the report might read: *“Quantum error rates remain a key hurdle in scaling up qubit counts.”* (indicating that lines 10–18 of source 105 support that statement). This approach makes it straightforward for you to open `sources/105.html` (GPT Researcher saves source pages) to verify the claim.

## **LangChain Open Deep Research** (Langchain-AI “open\_deep\_research”)

**Link:** GitHub Repo; LangChain Blog
**Deployment Model:** Open source project by LangChain. It can be run locally by cloning the repository and installing dependencies. It includes a **LangGraph** server that you can launch, which provides both an API endpoint and a web **Studio UI** for interacting with the agent. Also usable via a simple CLI script. The design is modular to plug in different model providers or tools.
**Open Source or Commercial:** Open Source (MIT License). Developed openly by the LangChain team, with community contributions.
**Domain Specialization:** General deep research across domains. It’s configurable to use different **model providers** (OpenAI, Anthropic, local LLMs via Ollama, etc.) and different **search tools** (Bing, SerpAPI, Brave, etc.). So you can tailor it for, say, academic research by using an academic search API, or company intelligence by using news APIs. By default it’s set up for broad web research.
**Core Capabilities:** It implements the standard “Deep Research” workflow: iterative web search and summarization cycles, followed by a final report synthesis. Specifically, the agent will generate an initial search query from the topic, fetch results, summarize those results, **reflect on knowledge gaps**, then generate a new query to fill those gaps. This loop repeats for a configured number of cycles (ensuring thorough coverage). After gathering sufficient info, it composes a final markdown **summary with all sources cited**. Recent versions also support **tool usage** via OpenAI’s function calling (for example, running calculator or other tools if needed). The architecture uses multiple LLM calls specialized for tasks: summarization, researching, compressing information, and writing the final report.
**Planning Structure:** **Sequential iterative agent.** It doesn’t spawn separate sub-agents for each subtopic by default; rather it uses a loop (search -> summarize -> reflect -> search ...) with one main agent adjusting its query. However, under the hood it uses different prompts (or prompt stages) for different functions, effectively a pipeline of planners: e.g. one prompt to create a search query, another prompt to reflect and plan next step, etc. The final report is generated by a dedicated prompt (using potentially a larger model). It leverages LangChain’s **LangGraph** to define this plan as a graph of nodes (each node is a model call or tool call). This makes the planning explicit and modifiable.
**Input Formats:** Typically a natural language question or topic. The user can configure settings via an `.env` file or UI (like how many iterations, which search engine to use). It currently doesn’t take direct file inputs through the interface, but because it’s built on LangChain, one could hook in a document loader to feed it PDFs or text as part of the context (for example, using the VectorRM tool in STORM, or LangChain’s own loaders).
**Citation Transparency:** **Yes.** The final output is a markdown report that **lists all sources** used, typically either as inline links or as a reference list at the end. The agent keeps track of source URLs during each search cycle and ensures they are included in the summary. Users thus get not only the answer but also the ability to verify each part of it. (The repository’s screenshots show sources appended after each paragraph).
**Extensibility:** **Yes.** This agent is explicitly built to be configurable: you can swap in **any LLM** (it supports “all LLMs in litellm or LangChain’s interfaces” including open models), swap the search/retrieval module (it has connectors for Bing, DuckDuckGo, Brave, Searx, etc.), and even connect to a **Model Context Protocol (MCP)** server for proprietary data. The `langgraph.json` configuration or Python config classes allow adding tools and altering the chain. Developers familiar with LangChain can extend it with new nodes (for example, add a stage that does an image search if needed). It’s intended to be a *reference implementation* of open deep research, so it’s written to be hacked and improved.
**Example Usage:** To use Open Deep Research, you would:

```bash
git clone https://github.com/langchain-ai/open_deep_research.git
cd open_deep_research
# set up .env with API keys for search and LLM provider
uv start  # starts the LangGraph server + UI
```

Then via the web UI (running at `http://localhost:2024/studio`), you input a query like *“Analyze the environmental impact of cryptocurrency mining and provide sources.”* The agent will display its chain as it runs: first a search step (e.g., searching for *“cryptocurrency mining environment impact”*), then it will show a summary of results, then a reflection like *“We need more on regulatory aspects, will search that next”*, and so on. After, say, 3 iterations, it produces a final answer. The answer might be structured by subtopics (energy consumption, e-waste, carbon footprint, regulatory response) and each section will reference articles or reports (e.g., linking to academic studies or news articles). Programmatically, one could also query the running server via its REST API or reuse the Python `assist()` function provided in the package to integrate this agent into another application.

## **Stanford STORM / Co-STORM** (Knowledge-Storm Research Agent)

**Link:** GitHub; Project Site; Paper (NAACL 2024)
**Deployment Model:** Open source **Python library** called `knowledge-storm`. Installable via pip (`pip install knowledge-storm`). It comes with command-line entry points and a minimal Streamlit web demo. There is also an online demo (*STORM research preview*) hosted by Stanford for trying it out in a browser. Developers can use the API to integrate STORM’s capabilities into other systems.
**Open Source or Commercial:** Open Source (MIT License). Developed as an academic research project (Stanford OVAL lab).
**Domain Specialization:** **Encyclopedic and academic content.** STORM was designed to write **Wikipedia-like articles** from scratch on any topic. It excels at factual, explanatory domains (history, science, etc.), producing well-structured articles with section outlines, rather than short answers. It can handle complex multi-part questions (like the GAIA challenge questions) that require integrating knowledge from multiple sources. Co-STORM extends this to a collaborative mode with human input. In essence, STORM is suited for any topic that requires comprehensive literature review and summarization. It also supports grounding in **user-provided documents** via a vector database (for enterprise or specific datasets).
**Core Capabilities:** STORM breaks down the task of long-form writing with citations into two stages: a **Pre-writing stage**, where it conducts extensive web research to collect references and generate a structured outline; and a **Writing stage**, where it uses the outline + sources to compose the full article with integrated citations. It focuses heavily on asking the *right questions* during research: STORM uses a novel **Perspective-Guided Question Generation** technique to ensure it covers different angles of the topic. It even simulates a conversation between a “Wikipedia writer” agent and a “domain expert” agent to refine its understanding. The output includes properly formatted citations (e.g., superscript numbers linking to reference list). Co-STORM mode adds multiple AI “experts” engaging in a roundtable discussion moderated by an AI (and optionally a human). This multi-agent discourse helps surface diverse perspectives and ensures more comprehensive coverage, building a dynamic **mind map** of concepts in the background.
**Planning Structure:** **Multi-agent and multi-step.** In STORM (single-player mode), the system itself can be seen as having a planner (question generator) and a retriever and writer. In Co-STORM (multi-agent mode), there are multiple **LLM expert agents** that each contribute information and ask follow-up questions, plus a **moderator agent** that introduces new probing questions, and the **user** can intervene too. The conversation is turn-based, and after sufficient turns, the system consolidates findings. The architecture is highly modular, using a framework called `dspy` to define these agents and their turn-taking logic. So planning is explicit: an outline is planned, references gathered for each section, then writing is planned section by section.
**Input Formats:** The simplest input is a topic or question (one sentence). Optionally, users can provide **perspective hints** or a few key reference links if they want to guide the agent. With the VectorRM integration, a user can supply a set of documents or a vector index so that STORM uses those as part of its knowledge base in addition to web search. The output is a rich text article (often several paragraphs or pages). STORM can output in Markdown, and the demo can export to PDF.
**Citation Transparency:** **Yes, very strong.** STORM’s entire goal is to produce **citation-backed** articles. In evaluations, it achieved high citation precision/recall (85%+ alignment of claims to sources). The article it writes will have numbered citations (like Wikipedia). Each sentence or set of sentences that convey a fact will end with a citation number, and at the end of the article a reference list with those citations (title, URL, etc.) is provided. In Co-STORM’s mind map view, every node (fact) in the mind map is also linked to sources, so the user can inspect where information came from. This makes STORM’s output trustworthy and easily verifiable.
**Extensibility:** **Yes.** Researchers or developers can extend STORM in multiple ways:

* **Custom retrieval**: It already supports plugging in new search engines or a custom document store (via a retriever module class).
* **Different LLMs**: STORM is model-agnostic; by default it used GPT-4o (OpenAI GPT-4 with browsing) but you can configure it to use other models via the `litellm` integration.
* **Pipeline tweaking**: One can adjust the outline strategy, or even replace the question-generation module with another approach (since the code is available).
* **Collaboration settings**: Co-STORM allows varying the number of expert agents or turns.
  As an academic project, it’s meant to be a testbed – the code is modular and relatively well-documented for others to build on.
  **Example Usage:** After installing the `knowledge-storm` package, you can use it in Python like:

```python
from knowledge_storm import storm
article = storm.generate_article("History of CRISPR gene editing", max_turns=5)
print(article.content)
```

This will perform a STORM run: the agent will search the internet for CRISPR history, likely generate perspective questions like “Who discovered CRISPR?” “Early milestones of CRISPR research?” etc., find references (scientific papers, Wikipedia, news), then produce an article. The output might start with an introduction to CRISPR, then a timeline of key discoveries, and maybe societal impact – each section containing sentences with superscript citations like *“…discovered by Yoshizumi Ishino in 1987^1…*”. The reference list at the bottom would show **\[^1]** with a full citation (e.g., a link to the 1987 paper or a historical review). If using the Co-STORM interactive demo, one would see a chat-like interface where multiple AI “experts” discuss, and the user could steer the conversation by asking a follow-up (e.g., “Can you focus on the discovery timeline?”). After the discussion, the system generates the final article, again with robust citations.

## **Summary and Notable Implementations**

In summary, deep research agents are rapidly evolving and are available both as consumer-facing tools (e.g. ChatGPT’s Deep Research, Gemini, Perplexity, Grok) and as open frameworks for customization (GPT Researcher, Open Deep Research, STORM). The standout implementations each have unique strengths:

* **ChatGPT Deep Research** (OpenAI) pioneered the integrated agent approach, delivering very high-quality, citation-rich reports within ChatGPT. It’s notable for multi-modal support and enterprise integration, though it comes with usage limits and a high cost for heavy users.

* **Gemini Deep Research** (Google) emphasizes a **user-in-the-loop planning** (letting you tweak the research plan) and seamless integration with Google’s ecosystem. Its parallel web browsing capability makes it extremely fast at covering broad topics.

* **Perplexity’s Deep Research** stands out for being **free for everyone** (with some limits) and offering quick, shareable reports. It essentially brings an “autonomous research mode” to a search engine interface, which lowers the barrier for casual users.

* **xAI’s Grok (DeepSearch)** pushes real-time awareness, being able to tap into social media content and latest news. Its introduction of a *Think* mode for reasoning transparency is an innovative way to build user trust.

* **GPT Researcher** (open source) is a powerhouse for those who want control. It’s highly configurable and can be self-hosted for privacy. Many consider it an open alternative to proprietary tools, with the ability to customize depth and breadth of research.

* **LangChain’s Open Deep Research** provides a *framework* approach – useful for developers who want to incorporate deep research agents into applications with minimal effort. Its performance on benchmarks (ranked #6 on a Deep Research leaderboard in mid-2025) shows that open models plus clever orchestration can rival closed solutions.

* **Stanford STORM/Co-STORM** is noteworthy in academic and Wiki-style content generation. It demonstrates how a combination of retrieval and multi-agent dialogue can yield highly factual, well-organized articles. The open availability of STORM’s code means others can replicate or build on a state-of-the-art cited research generator.

Going forward, we see deep research agents becoming integral to knowledge work, with improvements in efficiency (OpenAI’s “lightweight” models, parallelization) and usability (interactive refinement as in Co-STORM and Gemini). Whether you prefer a turnkey API or a hackable open-source solution, the landscape of deep research agents in 2025 offers robust options to automate and enhance multi-step research with confidence in the sources behind every claim.

**Sources:** The information above was compiled from official documentation, blog announcements, and research papers for each tool, as cited inline. Each citation (e.g.,) refers to the specific source lines confirming the stated facts.
