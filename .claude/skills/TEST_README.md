# Testing Guide for Claude Skills

This directory contains comprehensive test suites for all Claude skills in the `awesome-deep-researchers` repository.

## Test Structure

Each skill has its own test directory:

```tree
.claude/skills/
├── exa-research/
│   ├── scripts/
│   │   └── exa_tools.py
│   └── tests/
│       ├── __init__.py
│       └── test_exa_tools.py
├── gpt-researcher/
│   ├── scripts/
│   │   └── run_research.py
│   └── tests/
│       ├── __init__.py
│       └── test_run_research.py
└── [... 8 more skills ...]
```

## Installation

Install test dependencies:

```bash
pip install -r test-requirements.txt
```

Or install pytest manually:

```bash
pip install pytest pytest-asyncio pytest-mock python-dotenv
```

## Running Tests

### Run all tests for all skills

```bash
# From the repository root
pytest .claude/skills/*/tests/ -v
```

### Run tests for a specific skill

```bash
# Example: Test only exa-research
pytest .claude/skills/exa-research/tests/ -v

# Example: Test only gpt-researcher
pytest .claude/skills/gpt-researcher/tests/ -v
```

### Run a specific test file

```bash
pytest .claude/skills/exa-research/tests/test_exa_tools.py -v
```

### Run tests with coverage

```bash
pip install pytest-cov
pytest .claude/skills/*/tests/ --cov=.claude/skills --cov-report=html
```

## Test Categories

### Unit Tests (Default)

These tests use mocking and don't require API keys:

```bash
pytest .claude/skills/*/tests/ -v
```

### Integration Tests (Require API Keys)

Integration tests are marked and skipped by default. To run them:

```bash
# Set required API keys first
export OPENAI_API_KEY="your-key"
export TAVILY_API_KEY="your-key"
# ... etc

# Run integration tests
pytest .claude/skills/*/tests/ -v -m integration
```

## Environment Variables

Tests use mocking by default and don't require real API keys. However, integration tests require:

### Exa Research

- `EXA_API_KEY`

### GPT Researcher

- `TAVILY_API_KEY`
- `OPENAI_API_KEY` (or other LLM key)

### Jina AI

- `JINA_API_KEY` (optional)

### LangChain Deep Research

- `OPENAI_API_KEY` or `ANTHROPIC_API_KEY`
- `TAVILY_API_KEY`

### OpenAI Deep Research

- `OPENAI_API_KEY`

### Perplexity Sonar

- `PERPLEXITY_API_KEY`

### Smolagents

- `HF_TOKEN` (for HuggingFace)
- `OPENAI_API_KEY` (for OpenAI models)
- `ANTHROPIC_API_KEY` (for Anthropic models)

### Stanford STORM

- `OPENAI_API_KEY` (or other LLM key)
- `BING_SEARCH_API_KEY` or `YDC_API_KEY`

### Tavily Search

- `TAVILY_API_KEY`

### xAI Grok

- `XAI_API_KEY`

## Test Features

### ✅ Mocking

All tests use mocking for external API calls, so they can run without API keys or network access.

### ✅ Async Support

Tests for async functions use `pytest-asyncio` for proper async testing.

### ✅ Error Handling

Each test suite includes tests for error scenarios (missing keys, API failures, etc.).

### ✅ Coverage

Tests cover:

- Basic functionality
- Custom parameters
- Error handling
- Edge cases
- Response processing

## Example Test Run

```bash
$ pytest .claude/skills/exa-research/tests/ -v

======================== test session starts =========================
platform linux -- Python 3.10.0, pytest-7.4.0
collected 15 items

test_exa_tools.py::TestSearch::test_search_with_text PASSED     [  6%]
test_exa_tools.py::TestSearch::test_search_with_highlights PASSED [ 13%]
test_exa_tools.py::TestSearch::test_search_multiple_results PASSED [ 20%]
test_exa_tools.py::TestResearch::test_research_basic PASSED      [ 26%]
test_exa_tools.py::TestResearch::test_research_with_pro_model PASSED [ 33%]
test_exa_tools.py::TestFindSimilar::test_find_similar_basic PASSED [ 40%]
test_exa_tools.py::TestGetExaClient::test_get_exa_client_with_key PASSED [ 46%]
test_exa_tools.py::TestGetExaClient::test_get_exa_client_without_key PASSED [ 53%]
test_exa_tools.py::TestErrorHandling::test_search_api_error PASSED [ 60%]
test_exa_tools.py::TestErrorHandling::test_research_api_error PASSED [ 66%]
...

======================= 15 passed in 0.42s ==========================
```

## Continuous Integration

To add these tests to CI/CD:

### GitHub Actions

```yaml
name: Test Skills

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: '3.10'
      - name: Install dependencies
        run: |
          pip install -r .claude/skills/test-requirements.txt
      - name: Run tests
        run: |
          pytest .claude/skills/*/tests/ -v
```

## Contributing

When adding new skills:

1. Create a `tests/` directory in your skill folder
2. Add `__init__.py` to make it a Python package
3. Create test files named `test_*.py`
4. Use mocking for external API calls
5. Include both success and error test cases
6. Mark integration tests with `@pytest.mark.integration`

## Troubleshooting

### Import Errors

If you get import errors, ensure the test file adds the parent directory to the path:

```python
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))
```

### Async Test Errors

For async tests, ensure you have `pytest-asyncio` installed and use the decorator:

```python
@pytest.mark.asyncio
async def test_async_function():
    await my_async_function()
```

### Mock Issues

If mocks aren't working, verify the patch path matches the import path in the tested module:

```python
# If the module does: from openai import OpenAI
with patch('module_name.OpenAI', return_value=mock_client):
    # test code
```

## License

These tests are part of the awesome-deep-researchers repository and follow the same license.
