## 🧠 Expanded Guide: End-to-End Agentic Training Systems for Deep Research

> **Key Takeaway:**
> A new generation of Deep Research systems now supports not just inference, but full end-to-end agentic training—including fine-tuning, reinforcement learning, and custom tool integration. These platforms are enabled by leading AI labs, open-source communities, academic consortia, and commercial startups. They employ rigorous evaluation frameworks, support a wide range of LLMs, and enable flexible, extensible tool calls.

---

### What Is End-to-End Agentic Training?

End-to-end agentic training refers to the ability to **train, fine-tune, and evaluate research agents**—not just use them for inference. This includes:

- **Customizing agentic behaviors** (planning, tool use, citation, reasoning)
- **Integrating new tools** (web search, code, databases, etc.)
- **Evaluating outputs** with robust, multi-dimensional benchmarks
- **Supporting open, reproducible training pipelines**

The **DR Tulu** system from Allen AI is a leading example, providing open-source code, data, models, and evaluation for agentic research agent training.

---

## 🏆 Systems with End-to-End Agentic Training Capabilities

| System/Platform         | Who Enables Fine-Tuning         | Evaluation Methods/Benchmarks                | LLMs Used                        | Tool Calls Enabled                                 |
|-------------------------|---------------------------------|----------------------------------------------|-----------------------------------|----------------------------------------------------|
| **DR Tulu (Allen AI)**  | Allen AI, open-source community | HealthBench, Deep Research Bench, custom RL rubrics, citation verification | Qwen3-8B, LLaMA, vLLM, extensible | Web search, web browse, paper search, code, MCP    |
| **OpenAI Deep Research**| Developers, orgs (API/SDK)      | Loss/accuracy, Auto-Evals, Deep Research Bench, LLM-as-judge | GPT-4.1, GPT-4o, o3/o4, GPT-5     | Web, file, code, custom APIs                       |
| **Azure AI Foundry**    | Developers, enterprise teams    | Loss/accuracy, Auto-Evals, Deep Research Bench | GPT-4.1, o3/o4, Phi-4, Mistral    | Bing, web, file, code, custom tools                |
| **Google Gemini**       | Developers, enterprise (Vertex AI) | Built-in evals, Deep Research Bench, LLM-as-judge | Gemini 2.5 Pro, others            | Google Search, Gmail, Drive, code, multimodal      |
| **Anthropic Claude**    | Enterprise clients, partners    | Internal, LLM-as-judge, custom metrics       | Claude Sonnet 4, 3.5, others      | Web, file, code, browser, custom                   |
| **LangChain Open Deep Research** | Developers, researchers | Deep Research Bench, RACE, LLM-as-judge, LangSmith | OpenAI, Anthropic, Gemini, local  | Web, file, code, custom tools                      |
| **AgentGym-RL**         | Open-source, research community | WebArena, Deep Search, Games, SciWorld       | Model-agnostic (vllm)             | Web nav, search, file edit, command exec           |
| **SWE-Bench/RepoForge** | Agentica, open-source           | SWE-Bench Verified, RepoForge Harness, SPICE | Qwen3-32B, 8B+                    | Bash, search, file edit, finish/submit             |
| **WebAgent-R1**         | Open-source, research community | WebArena-Lite, binary outcome rewards        | Qwen-2.5-3B, Llama-3.1-8B         | Web navigation, form fill, info extraction         |
| **MLGym**               | Open-source, research community | MLGym-Bench, SWE-Bench, ScienceAgentBench    | Model-agnostic                    | Bash, file edit, shell, custom tools               |
| **Cognition Labs (Devin)** | Cognition Labs, enterprise   | Task completion, code correctness, workflow adherence | Proprietary, code-optimized       | GitHub, Slack, CI/CD, web, custom APIs             |
| **AWS Bedrock AgentCore** | AWS, partners, enterprise     | Task success, latency, cost, observability   | Amazon Nova, external             | Web, data, workflow, AWS services                  |

---

## 🏗️ System Profiles (DR Tulu Template)

### 1. **DR Tulu (Allen AI)**

- **Who Enables Training:** Allen Institute for AI (AI2), open-source contributors
- **LLMs Used:** Qwen3-8B (open), extensible to other strong base models
- **Tool Calls:** Web search, web browse, paper search (via Model Context Protocol), code execution, custom tools
- **Evaluation:**
  - Long-form: HealthBench, Deep Research Bench, ScholarQA-CSv2
  - Short-form: SimpleQA, 2Wiki, WebWalkerQA
  - Rubric-based RL, citation verification, open evaluation suite
- **Training Methodology:**
  - Prompt curation from diverse sources
  - Supervised fine-tuning (teacher-generated traces)
  - RL with evolving rubrics (instance-specific, reward for citation quality)
- **Extensibility:** Plug in new tools via MCP without retraining
- **Reproducibility:** Full open-source stack (data, code, models, eval scripts)

---

### 2. **OpenAI Deep Research API**

- **Who Enables Training:** Developers, organizations (API/SDK)
- **LLMs Used:** GPT-4.1, GPT-4o, o3/o4, GPT-5
- **Tool Calls:** Web search, file/document retrieval (MCP), code execution, custom APIs
- **Evaluation:**
  - Loss/accuracy, Auto-Evals, Deep Research Bench, LLM-as-a-judge
- **Training Methodology:**
  - Supervised fine-tuning, DPO, RLHF, RFT
- **Extensibility:** Custom tool integration, multi-agent workflows

---

### 3. **Azure AI Foundry Deep Research**

- **Who Enables Training:** Developers, enterprise teams (Azure portal, SDK)
- **LLMs Used:** GPT-4.1, o3/o4, Phi-4, Mistral
- **Tool Calls:** Bing Search, web APIs, file/document search (MCP), code execution, custom tools
- **Evaluation:**
  - Built-in metrics, Auto-Evals, Deep Research Bench
- **Training Methodology:**
  - Supervised, DPO, RLHF, continuous/iterative refinement

---

### 4. **Google Gemini Deep Research**

- **Who Enables Training:** Developers, enterprise (Vertex AI)
- **LLMs Used:** Gemini 2.5 Pro, others
- **Tool Calls:** Google Search, Gmail, Drive, code execution, multimodal (audio, vision)
- **Evaluation:**
  - Built-in tools, Deep Research Bench, LLM-as-judge
- **Training Methodology:**
  - Supervised, parameter-efficient fine-tuning (LoRA, adapters)

---

### 5. **Anthropic Claude**

- **Who Enables Training:** Enterprise clients, partners
- **LLMs Used:** Claude Sonnet 4, 3.5, others
- **Tool Calls:** Web search, file/document retrieval, code execution, browser-based actions
- **Evaluation:**
  - Internal benchmarks, LLM-as-judge, custom metrics
- **Training Methodology:**
  - Supervised, instruction tuning, RL

---

### 6. **LangChain Open Deep Research**

- **Who Enables Training:** Developers, researchers (external fine-tuning)
- **LLMs Used:** OpenAI, Anthropic, Gemini, DeepSeek, Hugging Face, local (Ollama, LM Studio)
- **Tool Calls:** Web search (Tavily, Serper, OpenAI), file/document search (MCP), website crawling, code execution, custom tools
- **Evaluation:**
  - Deep Research Bench, RACE, LLM-as-judge, LangSmith datasets
- **Training Methodology:**
  - External fine-tuning, plug-and-play agentic workflows

---

### 7. **AgentGym-RL, SWE-Bench, WebAgent-R1, MLGym (Open Source)**

- **Who Enables Training:** Open-source community, research labs
- **LLMs Used:** Model-agnostic (Qwen, Llama, DeepSeek, custom)
- **Tool Calls:**
  - AgentGym-RL: Web navigation, search, file edit, command exec
  - SWE-Bench: Bash, search, file edit, code submit
  - WebAgent-R1: Web navigation, form fill, info extraction
  - MLGym: Bash, file edit, shell, custom tools
- **Evaluation:**
  - WebArena, SWE-Bench Verified, RepoForge Harness, MLGym-Bench, ScienceAgentBench, pass@1, cost/performance, visual replay
- **Training Methodology:**
  - RL (PPO, GRPO, RLOO), SFT, DPO, multi-agent, behavior cloning

---

### 8. **Cognition Labs (Devin)**

- **Who Enables Training:** Cognition Labs, enterprise clients
- **LLMs Used:** Proprietary, code-optimized
- **Tool Calls:** GitHub, Slack, CI/CD, web, custom APIs
- **Evaluation:**
  - Task completion, code correctness, workflow adherence, analytics
- **Training Methodology:**
  - Supervised, RLHF, real-world workflow data

---

### 9. **AWS Bedrock AgentCore**

- **Who Enables Training:** AWS, partners, enterprise
- **LLMs Used:** Amazon Nova, external models
- **Tool Calls:** Web browsing, data access, workflow automation, AWS services
- **Evaluation:**
  - Task success, latency, cost, observability
- **Training Methodology:**
  - Custom agent development, fine-tuning, memory, observability

---

## 📊 Comparative Table

| System/Framework      | Fine-Tuning Enabled By                | LLMs Used (Examples)         | Evaluation Benchmarks/Frameworks         | Tool Calls Supported (Examples)           |
|----------------------|---------------------------------------|------------------------------|------------------------------------------|-------------------------------------------|
| DR Tulu              | Allen AI, open-source                 | Qwen3-8B, LLaMA, vLLM        | HealthBench, Deep Research Bench, RL rubrics | Web search, file/doc search, code, MCP    |
| OpenAI Deep Research | Developers, orgs                      | GPT-4.1, o3/o4, GPT-5        | Loss, Auto-Evals, Deep Research Bench    | Web, file, code, custom APIs              |
| Azure AI Foundry     | Developers, enterprise                | GPT-4.1, o3/o4, Phi-4, Mistral | Loss, Auto-Evals, Deep Research Bench    | Bing, web, file, code, custom tools       |
| Google Gemini        | Developers, enterprise                | Gemini 2.5 Pro, others       | Built-in, Deep Research Bench            | Google Search, Gmail, Drive, code, multimodal |
| Anthropic Claude     | Enterprise clients, partners          | Claude Sonnet 4, 3.5, others | Internal, LLM-as-judge, custom metrics   | Web, file, code, browser, custom          |
| LangChain Open Deep Research | Developers, researchers        | OpenAI, Anthropic, Gemini, local | Deep Research Bench, RACE, LLM-as-judge | Web, file, code, custom tools             |
| AgentGym-RL, SWE-Bench, WebAgent-R1, MLGym | Open-source, research | Qwen, Llama, DeepSeek, custom | WebArena, SWE-Bench, MLGym-Bench         | Web, code, shell, file, custom            |
| Cognition Labs (Devin) | Cognition Labs, enterprise          | Proprietary, code-optimized  | Task completion, code correctness        | GitHub, Slack, CI/CD, web, custom APIs    |
| AWS Bedrock AgentCore | AWS, partners, enterprise            | Amazon Nova, external        | Task success, latency, cost              | Web, data, workflow, AWS services         |

---

## 🧩 Key Trends & Takeaways

> **Key Finding:**
> The frontier of deep research agents is defined by open, extensible training pipelines, robust evaluation (including real-world and rubric-based metrics), and flexible tool integration. Both open-source and commercial systems are converging on best practices for agentic training, with a strong emphasis on reproducibility, transparency, and real-world utility.

- **Who Enables Training:**
  - Open-source: Research labs, academic consortia, developer communities
  - Commercial: Platform providers, enterprise clients, domain experts

- **Evaluation Methods:**
  - Standardized benchmarks (Deep Research Bench, HealthBench, SWE-Bench, WebArena, MLGym-Bench)
  - Rubric-based RL, LLM-as-a-judge, pass@k, cost/performance, citation verification, human review

- **LLMs Used:**
  - Open-source (Qwen, LLaMA, DeepSeek, vLLM, custom)
  - Commercial (GPT-4, Claude, Gemini, Amazon Nova, proprietary)

- **Tool Calls Enabled:**
  - Web search, file/document/database search, code execution, workflow automation, custom APIs, multimodal (audio, vision), shell commands

---

## 🟢 **Conclusion**

The landscape of Deep Research APIs and locally hosted systems now includes a robust set of platforms supporting **end-to-end agentic training**. These systems empower users to fine-tune, evaluate, and extend research agents for complex, multi-step, tool-driven tasks—backed by transparent evaluation and open, reproducible methodologies.
