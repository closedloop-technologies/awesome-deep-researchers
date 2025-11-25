
This collection provides Claude Code Skills for several key commercial APIs and open-source frameworks from the "Awesome Deep Researchers" list. These skills are designed using the standard script-based format, which involves a `SKILL.md` file for instructions and accompanying Python scripts for execution.

### How to Use These Skills

To install a skill in Claude Code:

1. Create a directory for the skill in your project (`.claude/skills/<skill-name>`) or globally (`~/.claude/skills/<skill-name>`).
2. Save the `SKILL.md` file in that directory.
3. Create a `scripts/` subdirectory and save the Python files there.
4. Ensure you have the necessary Python dependencies installed (e.g., `pip install openai python-dotenv`).

-----

## Commercial APIs & Search Infrastructure

### 1\. Perplexity Sonar (`perplexity-sonar`)

A skill for real-time, citation-backed answers using the Perplexity Sonar API.

#### `SKILL.md`

````yaml
---
name: perplexity-sonar
description: Use Perplexity Sonar API for real-time, citation-backed answers. Ideal for up-to-date information and quick synthesis. Requires PERPLEXITY_API_KEY.
---

# Perplexity Sonar Skill

This skill utilizes the Perplexity Sonar API to provide synthesized answers backed by real-time web sources. It uses the OpenAI Python library for compatibility.

## Setup

1.  **Dependencies:**
    ```bash
    pip install openai python-dotenv
    ```

2.  **API Key Configuration:** The skill requires the `PERPLEXITY_API_KEY`. Ensure it is set in a `.env` file in the project root.

    ```bash
    # If the script fails due to a missing key, run the following:
    echo "It seems the Perplexity API key is not set up."
    read -p "Enter your Perplexity API key: " PPLX_KEY
    echo "PERPLEXITY_API_KEY=$PPLX_KEY" >> .env
    # Ensure .env is ignored by git
    if [ -f .gitignore ] && ! grep -q ".env" .gitignore; then echo ".env" >> .gitignore; fi
    echo "API key saved to .env."
    ```

## Usage

Use the `scripts/ask.py` script to query the Sonar API.

### Command

```bash
python3 scripts/ask.py --prompt "<your_research_question>" [--model <model_name>]
````

### Parameters

* `--prompt` (Required): The research question.
* `--model` (Optional): Defaults to `sonar-medium-online`. Use `sonar-large-online` for comprehensive analysis.

### Example

```bash
python3 scripts/ask.py --prompt "What are the latest developments in the EV market in Q4 2025?" --model sonar-large-online
```

## Output

The script outputs the synthesized answer directly to stdout, with citations integrated by the Perplexity model.

````

#### `scripts/ask.py`

```python
import os
import argparse
import sys
from dotenv import load_dotenv

try:
    # Perplexity API is compatible with the OpenAI client structure
    from openai import OpenAI
except ImportError:
    print("Error: openai library not found. Please run 'pip install openai'", file=sys.stderr)
    sys.exit(1)

# Load environment variables
load_dotenv()

def ask_perplexity(prompt, model="sonar-medium-online"):
    """Sends a prompt to the Perplexity Sonar API."""
    api_key = os.environ.get("PERPLEXITY_API_KEY")
    if not api_key:
        print("Error: PERPLEXITY_API_KEY environment variable not set.", file=sys.stderr)
        sys.exit(1)

    client = OpenAI(api_key=api_key, base_url="https://api.perplexity.ai")

    try:
        messages = [
            {
                "role": "system",
                "content": (
                    "You are an expert researcher. Respond to the user's query using the most recent and relevant information available on the web."
                    "Provide a comprehensive, accurate, and neutral response. Cite your sources clearly."
                ),
            },
            {
                "role": "user",
                "content": prompt,
            },
        ]

        response = client.chat.completions.create(
            model=model,
            messages=messages,
        )

        # Extract and output the synthesized answer
        answer = response.choices[0].message.content
        print(answer)

    except Exception as e:
        print(f"Error during Perplexity API call: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Perplexity Sonar Tool for Claude Skills")
    parser.add_argument("--prompt", required=True, help="The research question or prompt.")
    parser.add_argument("--model", default="sonar-medium-online",
                        choices=["sonar-small-online", "sonar-medium-online", "sonar-large-online"],
                        help="The Perplexity Sonar model to use.")

    args = parser.parse_args()
    ask_perplexity(args.prompt, args.model)
````

### 2\. xAI Grok (`xai-grok`)

A skill leveraging Grok's Agent Tools API for real-time web and X (Twitter) search and synthesis.

#### `SKILL.md`

````yaml
---
name: xai-grok
description: Use xAI Grok API with Agent Tools for real-time web and X (Twitter) search and synthesis. Requires XAI_API_KEY.
---

# xAI Grok Research Skill

This skill utilizes the xAI Grok API and its Agent Tools for autonomous research, including real-time web and X platform search.

## Setup

1.  **Dependencies:** Requires the `xai-sdk`.
    ```bash
    pip install xai-sdk python-dotenv
    ```

2.  **API Key Configuration:** The skill requires the `XAI_API_KEY`.

    ```bash
    # If the script fails due to a missing key, run the following:
    echo "It seems the xAI API key is not set up."
    read -p "Enter your xAI API key: " GROK_KEY
    echo "XAI_API_KEY=$GROK_KEY" >> .env
    if [ -f .gitignore ] && ! grep -q ".env" .gitignore; then echo ".env" >> .gitignore; fi
    echo "API key saved to .env."
    ```

## Usage

Use the `scripts/grok_research.py` script. Grok will autonomously use the enabled tools.

### Command

```bash
python3 scripts/grok_research.py --query "<query>" [--model <model_name>] [--web-search] [--x-search]
````

### Parameters

* `--query` (Required): The research query.
* `--model` (Optional): Defaults to `grok-4.1-fast-reasoning` (optimized for tools).
* `--web-search` (Optional): Enable web search tool.
* `--x-search` (Optional): Enable X (Twitter) search tool.

### Example

```bash
python3 scripts/grok_research.py --query "What is the current public sentiment and news coverage on the latest AI regulations?" --web-search --x-search
```

## Output

The script streams the agent's thought process (to stderr) for visibility and outputs the final synthesized answer (to stdout) with citations.

````

#### `scripts/grok_research.py`

```python
import argparse
import json
import os
import sys
from dotenv import load_dotenv

try:
    from xai_sdk import Client
    from xai_sdk.chat import user
    # Import server-side tools
    from xai_sdk.tools import web_search, x_search
except ImportError:
    print("Error: xai-sdk not found. Please install it using 'pip install xai-sdk'", file=sys.stderr)
    sys.exit(1)

# Load environment variables
load_dotenv()

def grok_research(query, model="grok-4.1-fast-reasoning", enable_web_search=False, enable_x_search=False):
    api_key = os.getenv("XAI_API_KEY")
    if not api_key:
        print("Error: XAI_API_KEY environment variable not set.", file=sys.stderr)
        sys.exit(1)

    client = Client(api_key=api_key)

    tools = []
    if enable_web_search:
        tools.append(web_search())
    if enable_x_search:
        tools.append(x_search())

    if not tools:
        print("Note: No tools enabled. Grok will rely on internal knowledge.", file=sys.stderr)

    try:
        chat = client.chat.create(
            model=model,
            tools=tools,
        )
        chat.append(user(query))

        # Stream the response to see the agent's process
        print("--- Grok Agent Process (stderr) ---", file=sys.stderr)
        response = None
        for chunk in chat.stream():
            # Print tool calls and thought process to stderr for visibility
            if chunk.tool_calls:
                for call in chunk.tool_calls:
                    print(f"[Tool Call] {call.type}: {call.arguments}", file=sys.stderr)
            if chunk.is_thinking and chunk.content:
                 print(f"[Thinking] {chunk.content}", file=sys.stderr)
            response = chunk

        print("\n--- Final Answer (stdout) ---", file=sys.stderr)

        # Output the final answer to stdout
        if response and response.content:
            print(response.content)
            if response.citations:
                print("\n--- Citations ---")
                for c in response.citations:
                    print(f"- {c.title}: {c.url}")
        else:
            print("No final response received.")

    except Exception as e:
        print(f"Error calling xAI API: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Perform research using the xAI Grok API with agentic tools.")
    parser.add_argument("--query", required=True, help="The research query.")
    parser.add_argument("--model", default="grok-4.1-fast-reasoning", help="The Grok model to use (e.g., grok-4.1-fast-reasoning, grok-4).")
    parser.add_argument("--web-search", action="store_true", help="Enable web search tool.")
    parser.add_argument("--x-search", action="store_true", help="Enable X (Twitter) search tool.")

    args = parser.parse_args()
    grok_research(args.query, args.model, args.web_search, args.x_search)
````

### 3\. Exa Research (`exa-research`)

A skill for neural search, content retrieval, and automated research using the Exa AI API.

#### `SKILL.md`

````yaml
---
name: exa-research
description: Use Exa AI for neural search, content retrieval, and automated deep research. Requires EXA_API_KEY.
---

# Exa Research Skill

This skill leverages the Exa AI API for neural search, finding similar content, and autonomous research via their Research endpoint.

## Setup

1.  **Dependencies:** Requires `exa-py` and `openai` (for research endpoint compatibility).
    ```bash
    pip install exa-py openai python-dotenv
    ```

2.  **API Key Configuration:** Requires `EXA_API_KEY`.

    ```bash
    # If the script fails due to a missing key, run the following:
    echo "It seems the Exa API key is not set up."
    read -p "Enter your Exa API key: " EXA_KEY
    echo "EXA_API_KEY=$EXA_KEY" >> .env
    if [ -f .gitignore ] && ! grep -q ".env" .gitignore; then echo ".env" >> .gitignore; fi
    echo "API key saved to .env."
    ```

## Usage

The script `scripts/exa_tools.py` supports multiple operations.

### 1. Search and Contents

Perform a neural search and retrieve content or highlights.

```bash
python3 scripts/exa_tools.py search "<query>" [--num-results <N>] [--highlights]
````

**Example:**

```bash
python3 scripts/exa_tools.py search "innovative sustainable urban planning" --num-results 5 --highlights
```

### 2\. Research (Automated)

Automate in-depth research and receive a structured report.

```bash
python3 scripts/exa_tools.py research "<query>" [--model <exa-research|exa-research-pro>]
```

**Example:**

```bash
python3 scripts/exa_tools.py research "Analyze the impact of quantum computing on cryptography" --model exa-research-pro
```

### 3\. Find Similar

Find pages similar to a given URL.

```bash
python3 scripts/exa_tools.py find_similar "<url>"
```

**Example:**

```bash
python3 scripts/exa_tools.py find_similar "[https://arxiv.org/abs/1706.03762](https://arxiv.org/abs/1706.03762)"
```

## Output

The script outputs results in JSON format.

````

#### `scripts/exa_tools.py`

```python
import argparse
import json
import os
import sys
from dotenv import load_dotenv

try:
    from exa_py import Exa
    # Exa's research endpoint uses OpenAI SDK compatibility
    from openai import OpenAI
except ImportError:
    print("Error: exa-py or openai not found. 'pip install exa-py openai'", file=sys.stderr)
    sys.exit(1)

# Load environment variables
load_dotenv()

EXA_API_KEY = os.getenv("EXA_API_KEY")

def get_exa_client():
    if not EXA_API_KEY:
        print("Error: EXA_API_KEY not found.", file=sys.stderr)
        sys.exit(1)
    return Exa(EXA_API_KEY)

def search(query, num_results=5, highlights=False):
    exa = get_exa_client()
    try:
        # Configure content options
        contents_options = {"highlights": True} if highlights else {"text": True}
        response = exa.search_and_contents(
            query,
            num_results=num_results,
            type="neural", # Default to neural search
            **contents_options
        )

        results = []
        for result in response.results:
            results.append({
                "url": result.url,
                "title": result.title,
                # Return highlights or text based on the flag
                "content": result.highlights if highlights else result.text,
            })
        return results
    except Exception as e:
        print(f"Error during Exa search: {e}", file=sys.stderr)
        sys.exit(1)

def research(query, model="exa-research"):
    # Research uses OpenAI compatible endpoint hosted by Exa
    if not EXA_API_KEY:
        print("Error: EXA_API_KEY not found.", file=sys.stderr)
        sys.exit(1)

    # Initialize OpenAI client pointing to Exa's base URL
    client = OpenAI(
        base_url="https://api.exa.ai",
        api_key=EXA_API_KEY
    )

    try:
        # Using Chat Completions API for Exa research models
        print(f"Starting Exa Research task (Model: {model})...", file=sys.stderr)
        completion = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": query}]
        )
        # Note: Citations are typically embedded in the content for this endpoint format.
        return {"output": completion.choices[0].message.content}

    except Exception as e:
        print(f"Error during Exa research: {e}", file=sys.stderr)
        sys.exit(1)


def find_similar(url, num_results=5):
    exa = get_exa_client()
    try:
        response = exa.find_similar(url, num_results=num_results)
        results = []
        for result in response.results:
            results.append({
                "url": result.url,
                "title": result.title,
            })
        return results
    except Exception as e:
        print(f"Error during Exa find_similar: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Use Exa AI for search and research.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Search parser
    search_parser = subparsers.add_parser("search", help="Perform a neural search and retrieve content.")
    search_parser.add_argument("query")
    search_parser.add_argument("--num-results", type=int, default=5)
    search_parser.add_argument("--highlights", action="store_true", help="Return highlights instead of full text.")

    # Research parser
    research_parser = subparsers.add_parser("research", help="Automate in-depth web research.")
    research_parser.add_argument("query")
    research_parser.add_argument("--model", default="exa-research", choices=["exa-research", "exa-research-pro"])

    # Find Similar parser
    similar_parser = subparsers.add_parser("find_similar", help="Find pages similar to a given URL.")
    similar_parser.add_argument("url")
    similar_parser.add_argument("--num-results", type=int, default=5)

    args = parser.parse_args()

    result = None
    if args.command == "search":
        result = search(args.query, args.num_results, args.highlights)
    elif args.command == "research":
        result = research(args.query, args.model)
    elif args.command == "find_similar":
        result = find_similar(args.url, args.num_results)

    if result:
        print(json.dumps(result, indent=2))
````

### 4\. Tavily Search (`tavily-search`)

A skill to use the Tavily Search API, optimized for RAG applications.

#### `SKILL.md`

````yaml
---
name: tavily-search
description: Use Tavily Search API for optimized, real-time web search results for RAG. Requires TAVILY_API_KEY.
---

# Tavily Search Skill

This skill utilizes the Tavily Search API, providing clean, real-time web search results optimized for LLMs and RAG pipelines.

## Setup

1.  **Dependencies:** Requires `tavily-python`.
    ```bash
    pip install tavily-python python-dotenv
    ```

2.  **API Key Configuration:** Requires `TAVILY_API_KEY`.

    ```bash
    # If the script fails due to a missing key, run the following:
    echo "It seems the Tavily API key is not set up."
    read -p "Enter your Tavily API key: " TAVILY_KEY
    echo "TAVILY_API_KEY=$TAVILY_KEY" >> .env
    if [ -f .gitignore ] && ! grep -q ".env" .gitignore; then echo ".env" >> .gitignore; fi
    echo "API key saved to .env."
    ```

## Usage

Use the `scripts/tavily_search.py` script.

### Command

```bash
python3 scripts/tavily_search.py --query "<query>" [--max-results <N>] [--search-depth <basic|advanced>]
````

### Parameters

* `--query` (Required): The search query.
* `--search-depth` (Optional): Default `basic`. Use `advanced` for intensive research (higher quality, slower).
* `--max-results` (Optional): Default 10.

### Example

```bash
python3 scripts/tavily_search.py --query "autonomous research agents comparison" --search-depth advanced
```

## Output

The script outputs JSON containing a synthesized `answer` (if requested by the script) and a list of `results` (URL, title, content snippets).

````

#### `scripts/tavily_search.py`

```python
import os
import argparse
import json
import sys
from dotenv import load_dotenv

try:
    from tavily import TavilyClient
except ImportError:
    print("Error: tavily-python not found. 'pip install tavily-python'", file=sys.stderr)
    sys.exit(1)

# Load environment variables
load_dotenv()

def perform_search(query, search_depth="basic", max_results=10):
    """Performs a search using the Tavily API."""
    api_key = os.environ.get("TAVILY_API_KEY")
    if not api_key:
        print("Error: TAVILY_API_KEY environment variable not set.", file=sys.stderr)
        exit(1)

    try:
        tavily = TavilyClient(api_key=api_key)
        response = tavily.search(
            query=query,
            search_depth=search_depth,
            max_results=max_results,
            include_answer=True, # Request synthesized answer alongside results
            include_raw_content=False,
        )

        # Structure the output for LLM consumption
        output = {
            "answer": response.get("answer"),
            "results": response.get("results", [])
        }

        # Output the results as JSON
        print(json.dumps(output, indent=2))

    except Exception as e:
        print(f"Error during Tavily search: {e}", file=sys.stderr)
        exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Tavily Research Tool")
    parser.add_argument("--query", required=True, help="The search query.")
    parser.add_argument("--search-depth", default="basic", choices=["basic", "advanced"])
    parser.add_argument("--max-results", type=int, default=10)

    args = parser.parse_args()
    perform_search(args.query, args.search_depth, args.max_results)
````

### 5\. Jina AI (`jina-ai`)

A skill integrating Jina Reader (URL to Markdown) and Jina Search (Web Search to Markdown).

#### `SKILL.md`

````yaml
---
name: jina-ai
description: Use Jina AI APIs for converting URLs to LLM-friendly Markdown (Reader) and searching the web (Search).
---

# Jina AI Skill

This skill integrates Jina AI's Reader (r.jina.ai) and Search (s.jina.ai) APIs to convert URLs and web search results into clean, LLM-friendly Markdown.

## Setup

1.  **Dependencies:** Requires `requests`.
    ```bash
    pip install requests python-dotenv
    ```

2.  **API Key Configuration (Recommended):** Jina APIs offer higher limits with an API key (JINA_API_KEY).

    ```bash
    read -p "Enter your Jina API key (optional, press Enter to skip): " JINA_KEY
    if [ ! -z "$JINA_KEY" ]; then
        echo "JINA_API_KEY=$JINA_KEY" >> .env
        if [ -f .gitignore ] && ! grep -q ".env" .gitignore; then echo ".env" >> .gitignore; fi
        echo "API key saved to .env."
    fi
    ```

## Usage

The script `scripts/jina_tools.py` supports `read` and `search` operations.

### 1. Read URL (Jina Reader)

Convert a URL into clean Markdown.

```bash
python3 scripts/jina_tools.py read "<url>"
````

**Example:**

```bash
python3 scripts/jina_tools.py read "[https://en.wikipedia.org/wiki/Large_language_model](https://en.wikipedia.org/wiki/Large_language_model)"
```

### 2\. Search Web (Jina Search)

Search the web and return the top results converted to Markdown.

```bash
python3 scripts/jina_tools.py search "<query>"
```

**Example:**

```bash
python3 scripts/jina_tools.py search "What is Jina AI?"
```

## Output

The script outputs results in JSON format, containing title, URL, and `content_markdown`.

````

#### `scripts/jina_tools.py`

```python
import argparse
import json
import os
import sys
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

JINA_API_KEY = os.getenv("JINA_API_KEY")

def get_headers(use_json=True):
    headers = {}
    if JINA_API_KEY:
        headers["Authorization"] = f"Bearer {JINA_API_KEY}"
    if use_json:
        # Request structured JSON output
        headers["X-Return-Format"] = "json"
    return headers

def read_url(url):
    # Jina Reader API structure: prefix the target URL
    target_url = f"https://r.jina.ai/{url}"
    headers = get_headers(use_json=True)

    try:
        response = requests.get(target_url, headers=headers)
        response.raise_for_status()

        data = response.json().get('data', {})
        return {
            "title": data.get("title", "Untitled"),
            "url": data.get("url", url),
            "content_markdown": data.get("content", "")
        }

    except requests.exceptions.RequestException as e:
        print(f"Error during Jina Reader request: {e}", file=sys.stderr)
        sys.exit(1)

def search_web(query):
    # Jina Search API endpoint
    target_url = "https://s.jina.ai/search"
    params = {"q": query}
    headers = get_headers(use_json=True)

    try:
        response = requests.get(target_url, headers=headers, params=params)
        response.raise_for_status()

        results = []
        data = response.json().get('data', [])

        for item in data:
            results.append({
                "title": item.get("title", "Untitled"),
                "url": item.get("url", ""),
                "content_markdown": item.get("content", "")
            })

        return results

    except requests.exceptions.RequestException as e:
        print(f"Error during Jina Search request: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Use Jina AI tools (Reader and Search).")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Read parser
    read_parser = subparsers.add_parser("read", help="Convert a URL to Markdown.")
    read_parser.add_argument("url", help="The URL to read.")

    # Search parser
    search_parser = subparsers.add_parser("search", help="Search the web and return Markdown results.")
    search_parser.add_argument("query", help="The search query.")

    args = parser.parse_args()

    result = None
    if args.command == "read":
        result = read_url(args.url)
    elif args.command == "search":
        result = search_web(args.query)

    if result:
        print(json.dumps(result, indent=2))
````

## Open Source Frameworks

### 6\. GPT Researcher (`gpt-researcher`)

A skill to run the GPT Researcher autonomous agent.

#### `SKILL.md`

````yaml
---
name: gpt-researcher
description: Run the GPT Researcher autonomous agent to generate comprehensive deep research reports. Requires LLM and Search API keys (e.g., OPENAI_API_KEY, TAVILY_API_KEY).
---

# GPT Researcher Skill

This skill allows you to utilize the GPT Researcher Python package as an autonomous research agent.

## Setup

1.  **Dependencies:** Requires `gpt-researcher` and its dependencies.
    ```bash
    pip install gpt-researcher python-dotenv
    ```

2.  **Configuration:** GPT Researcher needs API keys for an LLM (e.g., OpenAI) and a Search Provider (Tavily is recommended).

    ```bash
    # Prompt user for keys if not set (assuming OpenAI and Tavily)
    if [ -z "$OPENAI_API_KEY" ] || [ -z "$TAVILY_API_KEY" ]; then
        echo "GPT Researcher requires API keys."
        read -p "Enter your OpenAI API key: " OAI_KEY
        read -p "Enter your Tavily API key: " TAVILY_KEY
        echo "OPENAI_API_KEY=$OAI_KEY" >> .env
        echo "TAVILY_API_KEY=$TAVILY_KEY" >> .env
        if [ -f .gitignore ] && ! grep -q ".env" .gitignore; then echo ".env" >> .gitignore; fi
        echo "API keys saved to .env."
    fi
    ```

## Usage

Use the `scripts/run_research.py` script to initiate a research task.

### Command

```bash
python3 scripts/run_research.py --query "<query>" [--report-type <type>]
````

### Parameters

* `--query` (Required): The topic to research.
* `--report-type` (Optional): Default `research_report`. Options include: `research_report`, `resource_report`, `outline_report`, `deep_research_report`.

### Example

```bash
python3 scripts/run_research.py --query "The future of renewable energy sources" --report-type deep_research_report
```

## Output

The script outputs the final report in Markdown format to stdout. The research process (which can take several minutes) is logged to stderr.

````

#### `scripts/run_research.py`

```python
import asyncio
import os
import argparse
import sys
from dotenv import load_dotenv

try:
    from gpt_researcher import GPTResearcher
except ImportError:
    print("Error: gpt-researcher not found. 'pip install gpt-researcher'", file=sys.stderr)
    sys.exit(1)

# Load environment variables
load_dotenv()

async def generate_research_report(query, report_type="research_report"):
    """Generates a research report using GPT Researcher."""

    # Basic check for required keys (GPT-R uses these by default)
    if not os.getenv("TAVILY_API_KEY"):
         print("Warning: TAVILY_API_KEY not set. GPT Researcher may fail without a search provider.", file=sys.stderr)

    # Note: LLM keys (like OPENAI_API_KEY) are also required depending on the LLM configured.

    try:
        print(f"Initializing GPT Researcher for query: {query} (Type: {report_type})...", file=sys.stderr)
        # Initialize the researcher
        # Configuration for LLM is typically handled via environment variables
        researcher = GPTResearcher(query=query, report_type=report_type)

        print("Conducting research (this may take a few minutes)...", file=sys.stderr)
        await researcher.conduct_research()

        print("Writing report...", file=sys.stderr)
        report = await researcher.write_report()

        # Output the final report to stdout
        print(report)

    except Exception as e:
        print(f"Error running GPT Researcher: {e}", file=sys.stderr)
        print("Please ensure all required dependencies and API keys (LLM and Search) are configured.", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run GPT Researcher.")
    parser.add_argument("--query", required=True, help="The research topic.")
    parser.add_argument("--report-type", default="research_report",
                        choices=["research_report", "resource_report", "outline_report", "custom_report", "deep_research_report"],
                        help="The type of report to generate.")

    args = parser.parse_args()
    # Run the async function
    asyncio.run(generate_research_report(args.query, args.report_type))
````

### 7\. Stanford STORM (`stanford-storm`)

A skill to run the Stanford STORM framework for generating Wikipedia-style articles.

#### `SKILL.md`

````yaml
---
name: stanford-storm
description: Run Stanford STORM (knowledge-storm) to generate comprehensive, Wikipedia-style articles with citations. Requires LLM and Search API keys (Bing or You.com).
---

# Stanford STORM Skill

This skill allows you to use Stanford STORM, an LLM-powered system for generating detailed, Wikipedia-style articles. It uses `litellm` for flexible LLM configuration.

## Setup

1.  **Dependencies:** Requires `knowledge-storm` and `litellm`.
    ```bash
    pip install knowledge-storm dspy-ai litellm python-dotenv
    ```

2.  **Configuration:** STORM needs API keys for the LLM (e.g., OPENAI_API_KEY, ANTHROPIC_API_KEY) and a Search Provider (BING_SEARCH_API_KEY or YDC_API_KEY). LiteLLM reads these standard environment variable names.

    ```bash
    # Ensure keys are set. Example for OpenAI and Bing:
    if [ -z "$OPENAI_API_KEY" ] || [ -z "$BING_SEARCH_API_KEY" ]; then
        echo "STORM requires API keys."
        echo "Ensure your LLM key (e.g., OPENAI_API_KEY) and Search key (BING_SEARCH_API_KEY or YDC_API_KEY) are set in .env."
        # Add interactive setup here if desired, ensuring the correct variable names are used.
    fi
    ```

## Usage

Use the `scripts/run_storm.py` script to generate an article.

### Command

```bash
python3 scripts/run_storm.py --topic "<topic>" [--rm-name <bing|you>] [--fast-model <model>] [--strong-model <model>]
````

### Parameters

* `--topic` (Required): The subject to research.
* `--rm-name` (Optional): Retriever module (default `bing`). Ensure the corresponding API key is set.
* `--fast-model` (Optional): LLM for simulation/questions (e.g., `gpt-3.5-turbo`).
* `--strong-model` (Optional): LLM for outline/writing (e.g., `gpt-4o`, `claude-3-5-sonnet-20240620`).

### Example

```bash
python3 scripts/run_storm.py --topic "The History of Quantum Computing" --strong-model gpt-4o --rm-name bing
```

## Output

The script outputs the final article in Markdown format to stdout. Intermediate files (outline, raw research) are saved in the `storm_output/` directory (logged to stderr). The process can take several minutes.

````

#### `scripts/run_storm.py`

```python
import os
import argparse
import sys
import tempfile
import glob
from dotenv import load_dotenv

try:
    # Import STORM components, using LiteLLM for flexible configuration
    from knowledge_storm.storm_wiki.engine import StormEngine, StormEngineArgs
    from knowledge_storm.lm import LiteLLMModelArgs
except ImportError:
    print("Error: 'knowledge-storm' or dependencies not found. 'pip install knowledge-storm litellm dspy-ai'", file=sys.stderr)
    sys.exit(1)

load_dotenv()

def run_storm(topic: str, rm_name: str, fast_model: str, strong_model: str):
    # Define the output directory
    output_base_dir = "./storm_output"
    os.makedirs(output_base_dir, exist_ok=True)

    # Create a unique subdirectory for this run
    sanitized_topic = "".join(c if c.isalnum() else "_" for c in topic[:30])
    run_dir = tempfile.mkdtemp(prefix=f"run_{sanitized_topic}_", dir=output_base_dir)

    try:
        print(f"Starting STORM run for topic: '{topic}'", file=sys.stderr)
        print(f"Models: Fast={fast_model}, Strong={strong_model}. Retriever: {rm_name}", file=sys.stderr)
        print(f"Output directory: {run_dir}", file=sys.stderr)

        # 1. Configure Language Models using LiteLLM
        # LiteLLM automatically detects API keys from standard env vars (e.g., OPENAI_API_KEY).

        fast_lm_config = LiteLLMModelArgs(
            model=fast_model,
            temperature=0.7,
            max_tokens=1000
        )

        strong_lm_config = LiteLLMModelArgs(
            model=strong_model,
            temperature=0.7,
            max_tokens=4000
        )

        # 2. Initialize the STORM engine
        # We pass the fast config as the default, and override specific components.
        engine_args = StormEngineArgs(
            lm_config=fast_lm_config,
            rm_name=rm_name,
            # Override specific components to use the strong model
            outline_gen_lm_config=strong_lm_config,
            article_gen_lm_config=strong_lm_config,
            article_polish_lm_config=strong_lm_config
        )

        engine = StormEngine(engine_args)

        # 3. Run the engine (Research, Outline, Write, Polish)
        engine.run(
            topic=topic,
            output_dir=run_dir
        )

        # 4. Extract the results
        # The final polished article is typically saved in a subdirectory named after the topic.

        # STORM organizes output within the output_dir
        article_files = glob.glob(os.path.join(run_dir, "*", "storm_gen_article_polished.md"))

        if article_files:
            article_path = article_files[0]
            with open(article_path, 'r', encoding='utf-8') as f:
                content = f.read()

            print("STORM run completed successfully.", file=sys.stderr)
            # Output the final article to stdout
            print(content)
        else:
            print(f"Error: Final article file not found. Check logs in {run_dir}.", file=sys.stderr)
            sys.exit(1)

    except Exception as e:
        print(f"Error running Stanford STORM: {e}.", file=sys.stderr)
        print(f"Ensure API keys for the LLM ({strong_model}) and Search ({rm_name}) are correctly set.", file=sys.stderr)
        print(f"Intermediate files at: {run_dir}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run Stanford STORM.")
    parser.add_argument("--topic", required=True, help="The subject to research.")
    parser.add_argument("--rm-name", default="bing", choices=["bing", "you"], help="Retriever module (ensure API key BING_SEARCH_API_KEY or YDC_API_KEY is set).")
    # Default models (can be overridden by user)
    parser.add_argument("--fast-model", default="gpt-3.5-turbo", help="LLM for faster tasks (LiteLLM compatible name).")
    parser.add_argument("--strong-model", default="gpt-4o", help="LLM for complex tasks (LiteLLM compatible name).")

    args = parser.parse_args()
    run_storm(args.topic, args.rm_name, args.fast_model, args.strong_model)
````
