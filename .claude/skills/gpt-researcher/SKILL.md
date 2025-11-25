---
name: gpt-researcher
description: Run the GPT Researcher autonomous agent to generate comprehensive deep research reports. Requires LLM and Search API keys (e.g., OPENAI_API_KEY, TAVILY_API_KEY).
---

# GPT Researcher Skill

This skill allows you to utilize the GPT Researcher Python package as an autonomous research agent.

## Setup

1. **Dependencies:** Requires `gpt-researcher` and its dependencies.

    ```bash
    pip install gpt-researcher python-dotenv
    ```

2. **Configuration:** GPT Researcher needs API keys for an LLM (e.g., OpenAI) and a Search Provider (Tavily is recommended).

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
```

### Parameters

* `--query` (Required): The topic to research.
* `--report-type` (Optional): Default `research_report`. Options include: `research_report`, `resource_report`, `outline_report`, `deep_research_report`.

### Example

```bash
python3 scripts/run_research.py --query "The future of renewable energy sources" --report-type deep_research_report
```

## Output

The script outputs the final report in Markdown format to stdout. The research process (which can take several minutes) is logged to stderr.
