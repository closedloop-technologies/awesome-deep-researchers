# Awesome Deep Researchers

Awesome Deep Researchers is a curated list of advanced AI agents and tools (as of 2025) that excel at deep research – autonomously gathering, analyzing, and synthesizing information from multiple sources to produce comprehensive, citation-backed insights. These agents go beyond simple Q&A, acting like diligent virtual researchers that plan multi-step inquiries, scour data sources, and compile findings into usable reports or outputs.

This list includes both free and paid solutions, with various interfaces (CLI, APIs, Web UIs) and configuration options, structured in the style of popular awesome-* repositories. It focuses on tools explicitly designed for in-depth research tasks, and excludes generic chatbots or search engines that lack multi-step autonomous research capabilities.

Table of Contents

Introduction

Quick Access Table

Deep Research Agent Profiles

ChatGPT (Deep Research mode)

Google Gemini – Deep Research

Perplexity AI

Kompas AI

Elicit by Ought

Consensus

Documind

ResearchRabbit

Semantic Scholar

Scite

Claude 2 (Anthropic)

Auto-GPT (Open Source)


Comparative Summary

Contributing


Introduction

Deep research AI agents are autonomous AI assistants specialized in complex information gathering and analysis. Unlike standard chatbots that answer questions with a single-shot response, deep research agents can break down complex queries into sub-tasks, perform iterative web searches or database lookups, read through numerous documents, and then synthesize the findings into a coherent output. In essence, they mimic the workflow of a skilled human researcher or analyst: formulating a research plan, collecting evidence, reasoning over the information, and presenting conclusions with references.

Why does this list matter? The past year has seen an explosion of AI research assistants, each with unique strengths. Some excel at web-scale research (browsing the internet for up-to-date facts), others specialize in academic literature or document analysis, and others serve as frameworks developers can program or extend. For researchers, students, analysts, and knowledge workers, choosing the right tool can dramatically reduce the time spent sifting through information overload. This list aims to highlight the top deep research agents of 2025, comparing their capabilities, access modes, citation support, and ideal use cases side by side.

What’s included: Autonomous or semi-autonomous AI tools that provide in-depth research assistance. This includes agents that can produce structured reports or answers with citations, perform multi-step reasoning (often via web browsing or database queries), and support features like planning, tool use (e.g. code execution or specialty plugins), or extended context length for analysis. Both open-source frameworks and commercial products are listed, as long as they enable “deep research” workflows via CLI, API, or web interfaces.

What’s excluded: General-purpose chatbots (without explicit research modes or tool use), basic search engines without AI synthesis, and simple Q&A assistants that do not perform multi-hop reasoning or provide source traceability. The focus is on tools designed for comprehensive exploration of a topic, not just brief answers. (For instance, standard Bing Chat or vanilla ChatGPT are not listed, but their specialized research modes or successors are.)

Quick Access Table

Here's a quick overview of all the deep research AI agents covered, with key attributes at a glance:

Name	Access	License	Domain/Focus	Citations	Link

ChatGPT (Deep Research)	[Web]	[Paid]	General Web (All domains)	✔️	OpenAI ChatGPT DR
Google Gemini (Research)	[Web]	[Paid]	General Web (All domains)	✔️	Gemini AI (Bard successor)
Perplexity AI	[Web, Mobile]	[Paid]	General Web Q&A	✔️	Perplexity.ai
Kompas AI	[Web]	[Paid]	General Web (Reports)	✔️	Kompas.ai
Elicit (Ought)	[Web]	[Paid]	Academic Literature	✔️	Elicit.org
Consensus	[Web]	[Paid]	Scientific Papers	✔️	Consensus.app
Documind	[Web]	[Paid]	PDF & Document Analysis	✘	Documind.chat
ResearchRabbit	[Web]	[Paid]	Academic Discovery	✘	ResearchRabbit.ai
Semantic Scholar	[Web, API]	[Paid]	Academic Search DB	✘	SemanticScholar.org
Scite	[Web, Browser Ext]	[Paid]	Citation Analysis	✔️	Scite.ai
Claude 2 (Anthropic)	[Web, API]	[Paid]	General (Large Context)	✘	Claude.ai
Auto-GPT (OSS)	[CLI, Config]	[OSS]	General Autonomous	✘	Auto-GPT GitHub


Access: Indicates available interfaces – e.g. [Web] UI, [Mobile] apps, [CLI] command-line usage, [API] for developers, etc.

License: [OSS] for open-source, [Paid] for proprietary (may have free tiers or trials).

Domain/Focus: Primary domain or use-case focus (e.g. general web research, academic papers, documents, etc.).

Citations: ✔️ if the agent provides source citations or references in its outputs; ✘ if not (or not applicable).


(Next, see detailed profiles for each agent/tool with features, examples, and more.)

Deep Research Agent Profiles

ChatGPT (Deep Research mode)

Link: ChatGPT Deep Research – OpenAI
Description: ChatGPT Deep Research is OpenAI’s advanced research agent mode built on an upcoming “GPT-o3” model optimized for web browsing and analysis. In this mode, ChatGPT moves beyond being a simple chatbot – it autonomously performs multi-step web research on your query for up to 30 minutes, then returns a structured report with in-depth findings and citations. The agent will search the internet, read through many sources, and synthesize information, much like a human analyst compiling a briefing. Every answer is documented with reference links to allow verification. This makes ChatGPT’s outputs far more traceable and reliable for serious research tasks.

Access mode: Available through the ChatGPT web interface for subscribers – simply select the “Deep Research” tool and enter your query. (As of 2025, Deep Research is offered to ChatGPT Plus users with monthly limits, and higher-tier “Pro” users for expanded usage. Free users have a very limited number of runs.) There is currently no standalone CLI or API for this agent; it runs on OpenAI’s servers. Usage is straightforward: you pose a broad or complex question, optionally attach relevant files (PDFs, data sheets, images) for context, and the agent will begin researching. During its run, a sidebar shows the plan and sources being consulted in real time, giving transparency into its process.

Example use-case: “Provide a comprehensive analysis of the current state of battery technology for electric vehicles.” – ChatGPT Deep Research will break this down into subtopics (market trends, chemistry breakthroughs, manufacturers, safety issues, etc.), search the web for each, analyze technical reports or news articles, and produce a report perhaps titled “Battery Tech for EVs – 2025 Analysis” with sections, bullet points, charts or tables if relevant, and footnote-style citations linking to sources.

Planning & architecture: This agent uses an autonomous planner with tools. It was trained via reinforcement learning on tasks requiring browsing and even code (it can execute Python for data analysis during research). When given a prompt, it plans a multi-step strategy, searches for information, adapts based on what it finds, and may pivot to new searches as needed. The underlying model is specialized for long-context reasoning and can integrate text from many webpages, PDFs, or even images (via OCR) into its analysis. Notably, ChatGPT Deep Research achieved state-of-the-art performance on difficult reasoning benchmarks (e.g. ~26.6% on the “Humanity’s Last Exam” test vs 3.3% by the older GPT-4 model), demonstrating its ability to handle extremely complex questions with multi-hop reasoning.

Input formats: Supports natural language queries (the more detailed, the better). You can also attach supplementary files like PDFs, spreadsheets, or images to the chat which the agent will incorporate into its research. This is useful for asking questions about specific documents or data you provide (e.g., “Analyze the attached market report and compare its projections to current trends”). It does not require writing prompts for each subtask; you just give one high-level task and it self-directs from there.

Citation support & transparency: Strong. Every report includes inline citations (usually numbered or linked references) for facts and quotes, so you can click through to the original sources. The agent also provides a summary of its reasoning steps (either in a sidebar or a brief “here’s how I approached this” section), increasing trust. However, OpenAI cautions that users should still critically evaluate outputs, as the model can occasionally misattribute info or “hallucinate” a citation. The interface allows you to follow up with questions or corrections in the same conversation, which the model will use to adjust any inaccuracies.

Extensibility: Being a closed service, ChatGPT’s Deep Research mode does not allow swapping out the underlying model or adding custom tools/plugins (beyond what OpenAI provides). It uses the built-in browser and code execution tools by default. On the plus side, it can handle images and PDFs natively and produce visualizations in answers (e.g., it might create a table or chart if relevant). Developers cannot directly integrate this mode into their own apps yet (no API access as of 2025). It’s primarily aimed at end-users via ChatGPT’s interface.

License/Cost: Proprietary. Included with ChatGPT Plus (paid subscription $200/mo) for higher-volume professional use. No self-hosted or open version is available.

Google Gemini – Deep Research

Link: Integrated in Google’s Gemini AI (successor to Bard)
Description: Google’s Deep Research is the answer to OpenAI’s agent, built into Google’s Gemini AI assistant (the next-gen system following Bard). It leverages Google’s core strength – search – combined with a powerful LLM. When activated, it formulates a multi-step research plan for your query and executes it by iteratively querying the web, similar to how a skilled researcher uses Google Search. The outcome is a detailed, well-structured analysis with cited sources, presented as a report. For example, ask Gemini “Explain the impact of climate change on global agriculture yields” and it will search for data across climate studies, agricultural reports, news, etc., then synthesize a report with sections (climate effects, regional impacts, adaptation strategies, etc.) and include references.

Access mode: Through Google’s interface (e.g. the Bard/Gemini web app or possibly integrated in Google Search in the future). As of late 2024, Deep Research was available via the Gemini Advanced subscription (~$20/month). It rolled out broadly (150+ countries, 45+ languages), making it widely accessible relative to OpenAI’s initial limited release. The workflow involves the AI showing you a proposed research plan after you enter your question. For instance, it might outline: “1. Search for X, 2. Summarize finding Y, 3. Compare perspectives on Z.” You have the option to review or tweak this outline, then hit “Start Research”. This interactive step gives users more control or insight into the process (a distinguishing usability feature). Once approved, the agent proceeds autonomously and then returns the final report in the chat. You can continue the conversation, refining or drilling down further on aspects of the answer, just like with ChatGPT.

Capabilities and domain: Being backed by Google Search means this agent has excellent coverage of up-to-date, broad web information. It excels at finding the latest statistics, news, or niche web content that others might miss. The LLM (Gemini) then summarizes and analyzes those findings. Depth-wise, Google’s agent is very good at gathering facts from many sources (“breadth through depth”). Some reports suggest it may not be quite as nuanced in complex reasoning as OpenAI’s model in certain cases, but it is continually improving. The output style tends to be factual and concise, often listing key findings or stats from each source, whereas ChatGPT might inject a bit more analytical narrative. Both are thorough, but users note Google’s results lean into ensuring no stone is unturned (covering many facets with evidence).

Example use-case: Market research and trend analysis. If a small business owner asks, “Give me a detailed market analysis for eco-friendly packaging in 2025,” the Google agent might search recent industry reports, competitor websites, news articles on consumer preferences, etc. It then produces a shareable report with sections like market size, growth rate, key players, consumer sentiment (each backed by sources). The user sees the plan (e.g. “we will gather market size from source A, trends from source B…”) and after execution, gets a ready-to-use overview. The report is formatted with headings, bullet points, and a list of references at the end.

Planning & transparency: Plan visibility is a key feature. Gemini’s interface shows a draft outline or a step-by-step plan before and during execution. This not only adds a layer of user trust (you know what it’s going to do) but also allows intervention (you might add “make sure to include data after 2023” or remove a section if it’s not relevant). The agent then uses the approved plan to guide its autonomous search. Technically, the agent uses Google’s internal tools – likely the Search API, possibly Google’s Knowledge Graph for certain queries, and Gemini’s reasoning for synthesizing. It can iterate: search, read results, then search again with refined terms as needed. The model can also utilize up-to-the-minute information (for instance, if you ask about “this week’s development in X”, it can get that). One advantage is that if a result requires navigating a website (e.g., clicking through pages or logging info), Google’s agent might have better compatibility given it’s within their ecosystem (though specifics on tool usage aren’t public).

Output & citations: The final answer is formatted as a polished report. Expect an introduction, structured sections, and a conclusion or summary of recommendations if applicable. Citations are usually inlined or listed per section. Google ensures sources are clearly listed (often with the title of the article and link) for each major fact. You can think of it as an enhanced Google result where instead of just snippets from each source, it writes a cohesive narrative and still tells you which source contributed which piece of information. This makes it ready to share or present with minimal editing.

Extensibility: The Gemini Deep Research agent is closed-source and tied to Google’s platform. There is no direct plugin or custom tool integration by end users. It benefits from Google’s ecosystem (could integrate with Google Docs or Drive for exporting the report, or use Google’s translation to operate in many languages seamlessly). For developers, Google Cloud did announce a Conversational Agents Console for building custom agents, but that’s more for enterprise (customer service bots) and not the same as the web research agent. So, as a user, you can’t swap the search backend or the model – you use what Google provides. But given Google’s continuous updates, it’s likely to improve automatically (e.g., upgrading from Gemini v1 to v2 in the background, adding more real-time data sources like Google News, Scholar, etc. over time).

License/Cost: Proprietary. As mentioned, it’s offered via a subscription (Gemini’s premium tier). The cost (~$20/month for individuals) is notably lower than OpenAI’s professional tier, making it relatively accessible. Google may also offer it free for a limited number of uses in certain regions or as promotions, but generally it’s part of the paid package. It requires a Google account to use, and usage is subject to Google’s privacy and data policies (important for enterprise users to consider).

Perplexity AI

Link: Perplexity.ai (Deep Research mode)
Description: Perplexity AI is a popular AI answer engine known for its concise answers with sources, and it introduced a Deep Research mode to tackle more complex queries. Perplexity’s Deep Research turns a simple question into an autonomous investigation: the system performs dozens of searches and reads hundreds of webpages to produce a thorough answer. It effectively does hours of research in a couple of minutes, then gives you a mini-report or long-form answer instead of a quick paragraph. The result is usually an organized response (sometimes with an intro and subsections or bullet points) that addresses the question from multiple angles. All factual claims are footnoted with citations to the web sources it used. This mode is like having an AI research analyst comb through the internet for you, distinct from the normal Perplexity single-turn Q&A.

Access mode: Perplexity is available via its web interface (no login required for basic use) and also through mobile apps (iOS, Android). Using Deep Research is as simple as choosing the “Deep” mode from a dropdown next to the query bar and entering your question. There’s no special installation; everything runs in the cloud. Notably, Perplexity has made Deep Research free for all users (with limits) – non-subscribers can do a certain number of deep queries per day free, while Pro subscribers get unlimited use. This low barrier to entry means students or independent researchers can leverage it without upfront cost. There isn’t an official API for Deep Research exposed to users yet (Perplexity is a closed source service), though they have a “share as link” feature that outputs the answer as a web page.

Workflow: The user experience is very straightforward: just ask a question as you normally would (“What are the long-term effects of sedentary lifestyle according to research?”). Perplexity’s agent then iteratively searches the web. Under the hood, it likely uses a combination of a language model to decide what to search and how to read results, and possibly some coding tool (they mention coding capabilities – possibly to run small analyses or parse data if needed). You don’t see each step in real-time (unlike ChatGPT or Google, which show intermediate steps), but the process usually takes 2–4 minutes before the answer is ready. The answer will pop up as a nicely formatted response, often starting with an overview. Perplexity emphasizes clarity and brevity: it tries to answer the question directly and then provide details, rather than writing a huge essay. It may use headings or bold text to separate parts of the answer if multiple facets are covered.

After you get the answer, you can click on the citation numbers to see the sources. Each citation opens the web source (news article, Wikipedia, scientific paper, etc.) that the info came from. You can also follow up with another question in the same session. While Perplexity does allow follow-up questions (contextual conversation), note that the follow-up might not incorporate the entire deep research context unless you explicitly reference it. Essentially, it doesn’t carry forward a long memory of the full report (unlike ChatGPT’s persistent thread), but you can copy parts of the answer or refer to them in your next question if needed.

Example use-cases: Perplexity Deep Research shines for broad knowledge questions and preliminary research:

Journalism: e.g. “Give me an in-depth rundown of the recent EU regulations on AI and their implications.” The agent will gather info from news sites, official EU documents, expert analyses, etc., and produce a summary with references for each claim (like quoting a line from a EU directive with a link).

Academic assignments: e.g. “Detailed summary of theories on the fall of the Indus Valley Civilization.” It will pull from archaeology journals, history websites, perhaps Wikipedia, to compile a multi-source answer (with each theory attributed to a source).

General curiosity: e.g. “How 