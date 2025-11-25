Based on your request, I have identified that **"yes.com"** is primarily an open-banking and identity framework. It is highly likely you are referring to **You.com**, which recently launched a high-profile "Deep Research" product called **ARI (Advanced Research & Insights)**.

Below is the **Appendix Report** detailing You.com’s agent, along with three other significant Deep Research APIs (Jina AI, Exa, and Zilliz) that were not covered in the primary dossier.

***

# Appendix: Emerging & Specialized Deep Research APIs

This appendix covers **You.com**, **Jina AI**, **Exa**, and **Zilliz**. These providers represent the "Specialized Layer" of the market—focusing either on high-cost/high-fidelity enterprise reports (You.com) or search-centric infrastructure (Jina/Exa).

### 1. You.com: ARI & Advanced Agent API

**Status:** Commercial (SaaS & API)
**The "Consultant-in-a-Box" Model**

While OpenAI and Perplexity focus on consumer-grade research, You.com has positioned its **ARI (Advanced Research & Insights)** agent as a B2B enterprise tool. It is distinct in its pricing model: rather than charging by the token, it charges by the **Call**, reflecting its nature as a complete workflow automation tool rather than just a model.

* **Architecture:** ARI uses a "chain-of-thought" process that can simultaneously analyze up to **400+ sources** (web pages, PDFs, and internal documents). It does not just summarize; it executes a recursive research strategy to produce a "professional-grade" report complete with data visualizations, interactive charts, and a table of contents.
* **API Product:** **"Advanced Agent API"**
  * **Cost:** **$15.00 per call** (Beta pricing).[1]
  * **Economics:** This is the most expensive per-unit API on the market. A single API call triggers the full agentic loop (planning, reading hundreds of pages, synthesis). It is designed for high-value workflows (e.g., "Generate a 30-page competitive landscape report") where a $15 cost is cheaper than 5 hours of human analyst time.
  * **Differentiation:** Unlike standard LLMs that hallucinate citations, ARI is built on You.com’s proprietary search index, claiming higher precision-recall on factual queries than GPT-4o.

### 2. Jina AI: DeepSearch

**Status:** Commercial API
**The "Middleware" Agent**

Jina AI is best known for its "Reader" API (converting URLs to LLM-friendly Markdown). Their **DeepSearch** endpoint extends this by wrapping the "Search-Read-Reason" loop into a single OpenAI-compatible endpoint.

* **Architecture:** Jina DeepSearch functions as a "Middleware Agent." You send a query to `deepsearch.jina.ai` (swapping out `api.openai.com`), and it autonomously performs iterative searches and content reading before streaming the answer back.[2]
* **Pricing:**
  * **Model:** Token-based, but calculated on the *total process* (input + internal reasoning + output).
  * **Rate:** **$2.00 / 1M Input** and **$8.00 / 1M Output** (aligned with Perplexity Sonar).
  * **Search Costs:** Unlike Perplexity, Jina often bundles the "work" into the token count or offers specific package tiers (e.g., 11 Billion token packages for production).[2]
* **Use Case:** Best for developers who already have an OpenAI-compatible chat interface and want to "upgrade" it to perform deep research without rewriting code.[2]

### 3. Exa AI (formerly Metaphor): Deep Search

**Status:** Commercial API
**The "Search-Native" Agent**

Exa is fundamentally a search engine optimized for LLMs (embedding-based search) rather than humans. Their **Deep Search** mode is an enhancement of their retrieval pipeline.

* **Architecture:** Exa Deep Search uses "Smart Query Expansion." When given a complex prompt, it doesn't just search once. It automatically generates multiple distinct query variations, retrieves content using its "Neural Search" (understanding meaning, not just keywords), and synthesizes a richer context.
* **Pricing:**
  * **Cost:** **$5.00 per 1,000 requests** for the "Research" tier.
  * **Economics:** This is highly competitive for applications that need to ingest massive amounts of context. Unlike agents that charge for "reasoning tokens," Exa charges for the *retrieval task*, making costs more predictable for high-volume data gathering.
* **Differentiation:** Exa returns "clean content" (HTML processed into text) specifically optimized for RAG, avoiding the noise of standard Google Search APIs.

### 4. Zilliz: DeepSearcher

**Status:** Open Source (Python)
**The "Private Data" Specialist**

While most deep research agents focus on the public web, **Zilliz DeepSearcher** is an open-source framework designed to apply deep research patterns to **private vector databases** (like Milvus).

* **Architecture:** It combines an LLM (OpenAI, DeepSeek, etc.) with a Vector DB to perform "Agentic RAG." Instead of a simple semantic search, it creates a plan, queries the internal database multiple times, and reflects on the retrieved private data.
* **Repository:** `zilliztech/deep-searcher`
* **Use Case:** "Sovereign Deep Research." If a bank needs to perform deep research on 10 million internal PDF contracts, they would use Zilliz DeepSearcher connected to a local Milvus instance, ensuring no data leaves their VPC (except for the LLM inference calls).

### Summary Comparison Table (Appendix)

| Agent / API | Type | Pricing Model | Best For |
| :--- | :--- | :--- | :--- |
| **You.com ARI** | Commercial SaaS/API | **$15.00 / Call** | Enterprise reports; replacing human analysts. |
| **Jina DeepSearch** | Commercial API | **~$8.00 / 1M Output** | Drop-in replacement for OpenAI Chat Completions. |
| **Exa Deep Search** | Search API | **$5.00 / 1k Searches** | High-volume RAG; retrieving context for other agents. |
| **Zilliz DeepSearcher**| Open Source Code | **Free (Self-Hosted)** | Deep research over *private* internal datasets. |
