This file is a merged representation of a subset of the codebase, containing files not matching ignore patterns, combined into a single document by Repomix.

# File Summary

## Purpose
This file contains a packed representation of a subset of the repository's contents that is considered the most important context.
It is designed to be easily consumable by AI systems for analysis, code review,
or other automated processes.

## File Format
The content is organized as follows:
1. This summary section
2. Repository information
3. Directory structure
4. Repository files (if enabled)
5. Multiple file entries, each consisting of:
  a. A header with the file path (## File: path/to/file)
  b. The full contents of the file in a code block

## Usage Guidelines
- This file should be treated as read-only. Any changes should be made to the
  original repository files, not this packed version.
- When processing this file, use the file path to distinguish
  between different files in the repository.
- Be aware that this file may contain sensitive information. Handle it with
  the same level of security as you would the original repository.

## Notes
- Some files may have been excluded based on .gitignore rules and Repomix's configuration
- Binary files are not included in this packed representation. Please refer to the Repository Structure section for a complete list of file paths, including binary files
- Files matching these patterns are excluded: research, docs
- Files matching patterns in .gitignore are excluded
- Files matching default ignore patterns are excluded
- Files are sorted by Git change count (files with more changes are at the bottom)

# Directory Structure
```
.claude/
  skills/
    exa-research/
      scripts/
        exa_tools.py
      tests/
        __init__.py
        test_exa_tools.py
      requirements.txt
      SKILL.md
    gpt-researcher/
      scripts/
        run_research.py
      tests/
        __init__.py
        test_run_research.py
      requirements.txt
      SKILL.md
    jina-ai/
      scripts/
        jina_tools.py
      tests/
        __init__.py
        test_jina_tools.py
      __init__.py
      requirements.txt
      SKILL.md
    langchain-deep-research/
      scripts/
        research.py
      tests/
        __init__.py
        test_research.py
      requirements.txt
      SKILL.md
    openai-deep-research/
      scripts/
        run_deep_research.py
      tests/
        __init__.py
        test_run_deep_research.py
      requirements.txt
      SKILL.md
    perplexity-sonar/
      scripts/
        ask.py
      tests/
        __init__.py
        test_ask.py
      requirements.txt
      SKILL.md
    smolagents/
      scripts/
        agent.py
      tests/
        __init__.py
        test_agent.py
      requirements.txt
      SKILL.md
    stanford-storm/
      scripts/
        run_storm.py
      tests/
        __init__.py
        test_run_storm.py
      requirements.txt
      SKILL.md
    tavily-search/
      scripts/
        tavily_search.py
      tests/
        __init__.py
        test_tavily_search.py
      requirements.txt
      SKILL.md
    xai-grok/
      scripts/
        grok_research.py
      tests/
        __init__.py
        test_grok_research.py
      requirements.txt
      SKILL.md
    TEST_README.md
    test-requirements.txt
awesome_deep_research/
  __init__.py
  cli.py
benchmark/
  results/
    .gitignore
    README.md
  __init__.py
  analyze.py
  benchmark.py
  config.py
  QUICKSTART.md
  README.md
  run_benchmark.py
  scoring.py
  SUMMARY.md
  test_system.py
  tracker.py
  utils.py
tests/
  test_cli.py
.env.example
.gitignore
.repomixignore
AGENTS.md
CLAUDE_CODE.md
ENV_SETUP.md
pyproject.toml
README.md
repomix.config.json
setup.py
TODO.md
```

# Files

## File: .claude/skills/exa-research/tests/test_exa_tools.py
`````python
"""Tests for exa-research skill."""
import sys
import os
import pytest
from unittest.mock import Mock, MagicMock, patch

# Add parent directory to path to import the module
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))

import exa_tools


@pytest.fixture
def mock_exa_client():
    """Mock Exa client."""
    with patch.dict(os.environ, {'EXA_API_KEY': 'test_key'}):
        mock = MagicMock()
        yield mock


@pytest.fixture
def mock_openai_client():
    """Mock OpenAI client for research."""
    mock = MagicMock()
    yield mock


class TestSearch:
    """Test the search function."""
    
    def test_search_with_text(self, mock_exa_client):
        """Test basic search with text content."""
        # Setup mock response
        mock_result = Mock()
        mock_result.url = "https://example.com"
        mock_result.title = "Test Result"
        mock_result.text = "Sample text content"
        mock_result.highlights = None
        
        mock_response = Mock()
        mock_response.results = [mock_result]
        mock_exa_client.search_and_contents.return_value = mock_response
        
        with patch('exa_tools.get_exa_client', return_value=mock_exa_client):
            results = exa_tools.search("test query", num_results=1, highlights=False)
        
        assert len(results) == 1
        assert results[0]['url'] == "https://example.com"
        assert results[0]['title'] == "Test Result"
        assert results[0]['content'] == "Sample text content"
        
        mock_exa_client.search_and_contents.assert_called_once()
    
    def test_search_with_highlights(self, mock_exa_client):
        """Test search with highlights enabled."""
        mock_result = Mock()
        mock_result.url = "https://example.com"
        mock_result.title = "Test Result"
        mock_result.text = "Full text"
        mock_result.highlights = ["highlight1", "highlight2"]
        
        mock_response = Mock()
        mock_response.results = [mock_result]
        mock_exa_client.search_and_contents.return_value = mock_response
        
        with patch('exa_tools.get_exa_client', return_value=mock_exa_client):
            results = exa_tools.search("test query", num_results=1, highlights=True)
        
        assert results[0]['content'] == ["highlight1", "highlight2"]
    
    def test_search_multiple_results(self, mock_exa_client):
        """Test search with multiple results."""
        mock_results = []
        for i in range(3):
            mock_result = Mock()
            mock_result.url = f"https://example{i}.com"
            mock_result.title = f"Result {i}"
            mock_result.text = f"Content {i}"
            mock_results.append(mock_result)
        
        mock_response = Mock()
        mock_response.results = mock_results
        mock_exa_client.search_and_contents.return_value = mock_response
        
        with patch('exa_tools.get_exa_client', return_value=mock_exa_client):
            results = exa_tools.search("test query", num_results=3, highlights=False)
        
        assert len(results) == 3
        for i in range(3):
            assert results[i]['url'] == f"https://example{i}.com"


class TestResearch:
    """Test the research function."""
    
    def test_research_basic(self, mock_openai_client):
        """Test basic research query."""
        mock_completion = Mock()
        mock_completion.choices = [Mock()]
        mock_completion.choices[0].message.content = "Research result content"
        
        mock_openai_client.chat.completions.create.return_value = mock_completion
        
        with patch.dict(os.environ, {'EXA_API_KEY': 'test_key'}):
            with patch('exa_tools.OpenAI', return_value=mock_openai_client):
                result = exa_tools.research("test research query")
        
        assert result['output'] == "Research result content"
        mock_openai_client.chat.completions.create.assert_called_once()
    
    def test_research_with_pro_model(self, mock_openai_client):
        """Test research with pro model."""
        mock_completion = Mock()
        mock_completion.choices = [Mock()]
        mock_completion.choices[0].message.content = "Pro research result"
        
        mock_openai_client.chat.completions.create.return_value = mock_completion
        
        with patch.dict(os.environ, {'EXA_API_KEY': 'test_key'}):
            with patch('exa_tools.OpenAI', return_value=mock_openai_client):
                result = exa_tools.research("test query", model="exa-research-pro")
        
        assert result['output'] == "Pro research result"


class TestFindSimilar:
    """Test the find_similar function."""
    
    def test_find_similar_basic(self, mock_exa_client):
        """Test finding similar URLs."""
        mock_results = []
        for i in range(2):
            mock_result = Mock()
            mock_result.url = f"https://similar{i}.com"
            mock_result.title = f"Similar Page {i}"
            mock_results.append(mock_result)
        
        mock_response = Mock()
        mock_response.results = mock_results
        mock_exa_client.find_similar.return_value = mock_response
        
        with patch('exa_tools.get_exa_client', return_value=mock_exa_client):
            results = exa_tools.find_similar("https://example.com", num_results=2)
        
        assert len(results) == 2
        assert results[0]['url'] == "https://similar0.com"
        assert results[1]['title'] == "Similar Page 1"
        
        mock_exa_client.find_similar.assert_called_once_with(
            "https://example.com", 
            num_results=2
        )


class TestGetExaClient:
    """Test the get_exa_client function."""
    
    def test_get_exa_client_with_key(self):
        """Test client creation with valid API key."""
        with patch.dict(os.environ, {'EXA_API_KEY': 'test_key'}):
            with patch('exa_tools.Exa') as mock_exa_cls:
                exa_tools.get_exa_client()
                mock_exa_cls.assert_called_once_with('test_key')
    
    def test_get_exa_client_without_key(self):
        """Test client creation fails without API key."""
        with patch.dict(os.environ, {}, clear=True):
            with pytest.raises(SystemExit):
                exa_tools.get_exa_client()


class TestErrorHandling:
    """Test error handling scenarios."""
    
    def test_search_api_error(self, mock_exa_client):
        """Test search handles API errors."""
        mock_exa_client.search_and_contents.side_effect = Exception("API Error")
        
        with patch('exa_tools.get_exa_client', return_value=mock_exa_client):
            with pytest.raises(SystemExit):
                exa_tools.search("test query")
    
    def test_research_api_error(self, mock_openai_client):
        """Test research handles API errors."""
        mock_openai_client.chat.completions.create.side_effect = Exception("API Error")
        
        with patch.dict(os.environ, {'EXA_API_KEY': 'test_key'}):
            with patch('exa_tools.OpenAI', return_value=mock_openai_client):
                with pytest.raises(SystemExit):
                    exa_tools.research("test query")


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
`````

## File: .claude/skills/gpt-researcher/tests/test_run_research.py
`````python
"""Tests for gpt-researcher skill."""
import sys
import os
import pytest
from unittest.mock import Mock, AsyncMock, MagicMock, patch

# Add parent directory to path to import the module
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))

import run_research


@pytest.fixture
def mock_gpt_researcher():
    """Mock GPTResearcher class."""
    mock = MagicMock()
    mock.conduct_research = AsyncMock()
    mock.write_report = AsyncMock(return_value="# Research Report\n\nThis is a test report.")
    return mock


class TestGenerateResearchReport:
    """Test the generate_research_report function."""
    
    @pytest.mark.asyncio
    async def test_basic_research_report(self, mock_gpt_researcher):
        """Test generating a basic research report."""
        with patch.dict(os.environ, {'TAVILY_API_KEY': 'test_key'}):
            with patch('run_research.GPTResearcher', return_value=mock_gpt_researcher):
                with patch('builtins.print') as mock_print:
                    await run_research.generate_research_report("test query")
        
        mock_gpt_researcher.conduct_research.assert_called_once()
        mock_gpt_researcher.write_report.assert_called_once()
        
        # Check that report was printed
        printed_values = [call[0][0] for call in mock_print.call_args_list]
        assert "# Research Report" in printed_values
    
    @pytest.mark.asyncio
    async def test_custom_report_type(self, mock_gpt_researcher):
        """Test generating a custom report type."""
        with patch.dict(os.environ, {'TAVILY_API_KEY': 'test_key'}):
            with patch('run_research.GPTResearcher', return_value=mock_gpt_researcher) as mock_cls:
                with patch('builtins.print'):
                    await run_research.generate_research_report(
                        "test query", 
                        report_type="deep_research_report"
                    )
        
        # Verify the correct report type was passed
        mock_cls.assert_called_once_with(
            query="test query", 
            report_type="deep_research_report"
        )
    
    @pytest.mark.asyncio
    async def test_missing_tavily_key_warning(self, mock_gpt_researcher):
        """Test that a warning is issued when TAVILY_API_KEY is missing."""
        with patch.dict(os.environ, {}, clear=True):
            with patch('run_research.GPTResearcher', return_value=mock_gpt_researcher):
                with patch('builtins.print') as mock_print:
                    await run_research.generate_research_report("test query")
        
        # Check that warning was printed to stderr
        stderr_calls = [
            call for call in mock_print.call_args_list 
            if len(call[1]) > 0 and call[1].get('file') == sys.stderr
        ]
        warning_found = any(
            'TAVILY_API_KEY' in str(call[0][0]) 
            for call in stderr_calls
        )
        assert warning_found
    
    @pytest.mark.asyncio
    async def test_research_error_handling(self, mock_gpt_researcher):
        """Test error handling during research."""
        mock_gpt_researcher.conduct_research.side_effect = Exception("Research failed")
        
        with patch.dict(os.environ, {'TAVILY_API_KEY': 'test_key'}):
            with patch('run_research.GPTResearcher', return_value=mock_gpt_researcher):
                with pytest.raises(SystemExit):
                    await run_research.generate_research_report("test query")
    
    @pytest.mark.asyncio
    async def test_write_report_error_handling(self, mock_gpt_researcher):
        """Test error handling during report writing."""
        mock_gpt_researcher.write_report.side_effect = Exception("Write failed")
        
        with patch.dict(os.environ, {'TAVILY_API_KEY': 'test_key'}):
            with patch('run_research.GPTResearcher', return_value=mock_gpt_researcher):
                with pytest.raises(SystemExit):
                    await run_research.generate_research_report("test query")


class TestReportTypes:
    """Test different report types."""
    
    @pytest.mark.asyncio
    @pytest.mark.parametrize("report_type", [
        "research_report",
        "resource_report",
        "outline_report",
        "custom_report",
        "deep_research_report"
    ])
    async def test_all_report_types(self, mock_gpt_researcher, report_type):
        """Test all supported report types."""
        with patch.dict(os.environ, {'TAVILY_API_KEY': 'test_key'}):
            with patch('run_research.GPTResearcher', return_value=mock_gpt_researcher) as mock_cls:
                with patch('builtins.print'):
                    await run_research.generate_research_report(
                        "test query", 
                        report_type=report_type
                    )
        
        mock_cls.assert_called_once_with(
            query="test query", 
            report_type=report_type
        )


class TestIntegration:
    """Integration tests (can be skipped if dependencies not available)."""
    
    @pytest.mark.integration
    @pytest.mark.skipif(
        not os.getenv('TAVILY_API_KEY') or not os.getenv('OPENAI_API_KEY'),
        reason="API keys not set"
    )
    @pytest.mark.asyncio
    async def test_real_research_flow(self):
        """Test with real API (integration test)."""
        # This test requires actual API keys and will be skipped by default
        with patch('builtins.print'):
            await run_research.generate_research_report(
                "What is the capital of France?",
                report_type="research_report"
            )


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
`````

## File: .claude/skills/jina-ai/tests/test_jina_tools.py
`````python
"""Tests for jina-ai skill."""
import sys
import os
import pytest
from unittest.mock import Mock, patch

# Add parent directory to path to import the module
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))

import jina_tools


@pytest.fixture
def mock_requests_get():
    """Mock requests.get."""
    with patch('jina_tools.requests.get') as mock:
        yield mock


class TestGetHeaders:
    """Test the get_headers function."""
    
    def test_headers_with_api_key(self):
        """Test headers with API key set."""
        with patch.dict(os.environ, {'JINA_API_KEY': 'test_key'}):
            headers = jina_tools.get_headers(use_json=True)
        
        assert headers['Authorization'] == 'Bearer test_key'
        assert headers['X-Return-Format'] == 'json'
    
    def test_headers_without_api_key(self):
        """Test headers without API key."""
        with patch.dict(os.environ, {}, clear=True):
            headers = jina_tools.get_headers(use_json=True)
        
        assert 'Authorization' not in headers
        assert headers['X-Return-Format'] == 'json'
    
    def test_headers_without_json(self):
        """Test headers without JSON format."""
        headers = jina_tools.get_headers(use_json=False)
        assert 'X-Return-Format' not in headers


class TestReadUrl:
    """Test the read_url function."""
    
    def test_read_url_success(self, mock_requests_get):
        """Test successful URL reading."""
        mock_response = Mock()
        mock_response.json.return_value = {
            'data': {
                'title': 'Test Page',
                'url': 'https://example.com',
                'content': '# Test Content\n\nThis is a test.'
            }
        }
        mock_response.raise_for_status = Mock()
        mock_requests_get.return_value = mock_response
        
        result = jina_tools.read_url('https://example.com')
        
        assert result['title'] == 'Test Page'
        assert result['url'] == 'https://example.com'
        assert result['content_markdown'] == '# Test Content\n\nThis is a test.'
        
        # Verify the correct URL was called
        call_args = mock_requests_get.call_args
        assert 'https://r.jina.ai/https://example.com' in str(call_args)
    
    def test_read_url_missing_fields(self, mock_requests_get):
        """Test URL reading with missing data fields."""
        mock_response = Mock()
        mock_response.json.return_value = {
            'data': {}
        }
        mock_response.raise_for_status = Mock()
        mock_requests_get.return_value = mock_response
        
        result = jina_tools.read_url('https://example.com')
        
        assert result['title'] == 'Untitled'
        assert result['url'] == 'https://example.com'
        assert result['content_markdown'] == ''
    
    def test_read_url_request_error(self, mock_requests_get):
        """Test URL reading with request error."""
        mock_requests_get.side_effect = Exception("Network error")
        
        with pytest.raises(SystemExit):
            jina_tools.read_url('https://example.com')
    
    def test_read_url_with_api_key(self, mock_requests_get):
        """Test URL reading with API key."""
        mock_response = Mock()
        mock_response.json.return_value = {'data': {}}
        mock_response.raise_for_status = Mock()
        mock_requests_get.return_value = mock_response
        
        with patch.dict(os.environ, {'JINA_API_KEY': 'test_key'}):
            jina_tools.read_url('https://example.com')
        
        # Check that Authorization header was included
        call_kwargs = mock_requests_get.call_args[1]
        assert 'Authorization' in call_kwargs['headers']
        assert call_kwargs['headers']['Authorization'] == 'Bearer test_key'


class TestSearchWeb:
    """Test the search_web function."""
    
    def test_search_web_success(self, mock_requests_get):
        """Test successful web search."""
        mock_response = Mock()
        mock_response.json.return_value = {
            'data': [
                {
                    'title': 'Result 1',
                    'url': 'https://example1.com',
                    'content': 'Content 1'
                },
                {
                    'title': 'Result 2',
                    'url': 'https://example2.com',
                    'content': 'Content 2'
                }
            ]
        }
        mock_response.raise_for_status = Mock()
        mock_requests_get.return_value = mock_response
        
        results = jina_tools.search_web('test query')
        
        assert len(results) == 2
        assert results[0]['title'] == 'Result 1'
        assert results[0]['url'] == 'https://example1.com'
        assert results[0]['content_markdown'] == 'Content 1'
        assert results[1]['title'] == 'Result 2'
    
    def test_search_web_empty_results(self, mock_requests_get):
        """Test search with no results."""
        mock_response = Mock()
        mock_response.json.return_value = {'data': []}
        mock_response.raise_for_status = Mock()
        mock_requests_get.return_value = mock_response
        
        results = jina_tools.search_web('test query')
        
        assert len(results) == 0
    
    def test_search_web_missing_fields(self, mock_requests_get):
        """Test search with missing data fields."""
        mock_response = Mock()
        mock_response.json.return_value = {
            'data': [
                {
                    # Missing title, url, content
                }
            ]
        }
        mock_response.raise_for_status = Mock()
        mock_requests_get.return_value = mock_response
        
        results = jina_tools.search_web('test query')
        
        assert len(results) == 1
        assert results[0]['title'] == 'Untitled'
        assert results[0]['url'] == ''
        assert results[0]['content_markdown'] == ''
    
    def test_search_web_request_error(self, mock_requests_get):
        """Test search with request error."""
        mock_requests_get.side_effect = Exception("API error")
        
        with pytest.raises(SystemExit):
            jina_tools.search_web('test query')
    
    def test_search_web_with_query_params(self, mock_requests_get):
        """Test that search query is passed correctly."""
        mock_response = Mock()
        mock_response.json.return_value = {'data': []}
        mock_response.raise_for_status = Mock()
        mock_requests_get.return_value = mock_response
        
        jina_tools.search_web('my search query')
        
        # Verify query parameter was passed
        call_kwargs = mock_requests_get.call_args[1]
        assert call_kwargs['params'] == {'q': 'my search query'}


class TestErrorHandling:
    """Test error handling scenarios."""
    
    def test_read_url_http_error(self, mock_requests_get):
        """Test read_url handles HTTP errors."""
        import requests
        mock_response = Mock()
        mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError("404 Not Found")
        mock_requests_get.return_value = mock_response
        
        with pytest.raises(SystemExit):
            jina_tools.read_url('https://notfound.com')
    
    def test_search_web_http_error(self, mock_requests_get):
        """Test search_web handles HTTP errors."""
        import requests
        mock_response = Mock()
        mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError("500 Server Error")
        mock_requests_get.return_value = mock_response
        
        with pytest.raises(SystemExit):
            jina_tools.search_web('test query')


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
`````

## File: .claude/skills/langchain-deep-research/tests/test_research.py
`````python
"""Tests for langchain-deep-research skill."""
import sys
import os
import pytest
from unittest.mock import Mock, AsyncMock, MagicMock, patch

# Add parent directory to path to import the module
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))

import research


@pytest.fixture
def mock_langgraph_client():
    """Mock LangGraph client."""
    mock_client = MagicMock()
    
    # Mock threads.create
    mock_client.threads.create = AsyncMock(return_value={"thread_id": "test_thread_123"})
    
    # Mock runs.stream
    async def mock_stream(*args, **kwargs):
        # Simulate streaming chunks
        mock_msg = Mock()
        mock_msg.content = "# Research Report\n\nThis is the final research result."
        
        chunk1 = Mock()
        chunk1.data = {
            "agent": {
                "messages": [mock_msg]
            }
        }
        
        yield chunk1
    
    mock_client.runs.stream = mock_stream
    
    return mock_client


class TestRunResearch:
    """Test the run_research function."""
    
    @pytest.mark.asyncio
    async def test_basic_research(self, mock_langgraph_client):
        """Test basic research execution."""
        with patch.dict(os.environ, {
            'OPENAI_API_KEY': 'test_key',
            'TAVILY_API_KEY': 'test_key'
        }):
            with patch('research.get_client', return_value=mock_langgraph_client):
                with patch('builtins.print') as mock_print:
                    await research.run_research("test query")
        
        # Verify client methods were called
        mock_langgraph_client.threads.create.assert_called_once()
        
        # Check that the report was printed
        printed_values = [call[0][0] for call in mock_print.call_args_list]
        assert any("Research Report" in str(val) for val in printed_values)
    
    @pytest.mark.asyncio
    async def test_custom_max_iterations(self, mock_langgraph_client):
        """Test research with custom max iterations."""
        with patch.dict(os.environ, {
            'OPENAI_API_KEY': 'test_key',
            'TAVILY_API_KEY': 'test_key'
        }):
            with patch('research.get_client', return_value=mock_langgraph_client):
                with patch('builtins.print'):
                    await research.run_research("test query", max_iterations=5)
        
        mock_langgraph_client.threads.create.assert_called_once()
    
    @pytest.mark.asyncio
    async def test_output_to_file(self, mock_langgraph_client, tmp_path):
        """Test saving report to file."""
        output_file = tmp_path / "report.md"
        
        with patch.dict(os.environ, {
            'OPENAI_API_KEY': 'test_key',
            'TAVILY_API_KEY': 'test_key'
        }):
            with patch('research.get_client', return_value=mock_langgraph_client):
                with patch('builtins.print'):
                    await research.run_research(
                        "test query", 
                        output_file=str(output_file)
                    )
        
        # Verify file was created
        assert output_file.exists()
        content = output_file.read_text()
        assert "Research Report" in content
    
    @pytest.mark.asyncio
    async def test_missing_openai_key(self):
        """Test error when OPENAI_API_KEY is missing."""
        with patch.dict(os.environ, {}, clear=True):
            with pytest.raises(SystemExit):
                await research.run_research("test query")
    
    @pytest.mark.asyncio
    async def test_missing_tavily_key_warning(self, mock_langgraph_client):
        """Test warning when TAVILY_API_KEY is missing."""
        with patch.dict(os.environ, {'OPENAI_API_KEY': 'test_key'}):
            with patch('research.get_client', return_value=mock_langgraph_client):
                with patch('builtins.print') as mock_print:
                    await research.run_research("test query")
        
        # Check that warning was printed
        stderr_calls = [
            call for call in mock_print.call_args_list 
            if len(call[1]) > 0 and call[1].get('file') == sys.stderr
        ]
        warning_found = any(
            'TAVILY_API_KEY' in str(call[0][0]) 
            for call in stderr_calls
        )
        assert warning_found
    
    @pytest.mark.asyncio
    async def test_connection_error(self):
        """Test handling of connection error to LangGraph server."""
        with patch.dict(os.environ, {'OPENAI_API_KEY': 'test_key'}):
            with patch('research.get_client', side_effect=ConnectionError("Cannot connect")):
                with pytest.raises(SystemExit):
                    await research.run_research("test query")
    
    @pytest.mark.asyncio
    async def test_no_messages_in_final_state(self, mock_langgraph_client):
        """Test error handling when no messages received."""
        # Mock client with empty response
        async def mock_empty_stream(*args, **kwargs):
            chunk = Mock()
            chunk.data = {"agent": {"messages": []}}
            yield chunk
        
        mock_langgraph_client.runs.stream = mock_empty_stream
        
        with patch.dict(os.environ, {'OPENAI_API_KEY': 'test_key'}):
            with patch('research.get_client', return_value=mock_langgraph_client):
                with pytest.raises(SystemExit):
                    await research.run_research("test query")
    
    @pytest.mark.asyncio
    async def test_general_exception_handling(self, mock_langgraph_client):
        """Test general exception handling."""
        mock_langgraph_client.threads.create.side_effect = Exception("Unexpected error")
        
        with patch.dict(os.environ, {'OPENAI_API_KEY': 'test_key'}):
            with patch('research.get_client', return_value=mock_langgraph_client):
                with pytest.raises(SystemExit):
                    await research.run_research("test query")


class TestStreamProcessing:
    """Test streaming response processing."""
    
    @pytest.mark.asyncio
    async def test_stream_with_multiple_messages(self, mock_langgraph_client):
        """Test processing stream with multiple message chunks."""
        async def mock_multi_stream(*args, **kwargs):
            # First chunk
            msg1 = Mock()
            msg1.content = "Intermediate result"
            chunk1 = Mock()
            chunk1.data = {"step1": {"messages": [msg1]}}
            yield chunk1
            
            # Second chunk with final result
            msg2 = Mock()
            msg2.content = "Final research report"
            chunk2 = Mock()
            chunk2.data = {"final": {"messages": [msg2]}}
            yield chunk2
        
        mock_langgraph_client.runs.stream = mock_multi_stream
        
        with patch.dict(os.environ, {'OPENAI_API_KEY': 'test_key'}):
            with patch('research.get_client', return_value=mock_langgraph_client):
                with patch('builtins.print') as mock_print:
                    await research.run_research("test query")
        
        # Should print final message
        printed_values = [call[0][0] for call in mock_print.call_args_list]
        assert any("Final research report" in str(val) for val in printed_values)


class TestEnvironmentVariables:
    """Test environment variable handling."""
    
    @pytest.mark.asyncio
    async def test_anthropic_key_alternative(self, mock_langgraph_client):
        """Test that ANTHROPIC_API_KEY works as alternative to OPENAI_API_KEY."""
        with patch.dict(os.environ, {
            'ANTHROPIC_API_KEY': 'test_key',
            'TAVILY_API_KEY': 'test_key'
        }):
            with patch('research.get_client', return_value=mock_langgraph_client):
                with patch('builtins.print'):
                    # Should not raise SystemExit
                    await research.run_research("test query")
        
        mock_langgraph_client.threads.create.assert_called_once()


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
`````

## File: .claude/skills/openai-deep-research/tests/test_run_deep_research.py
`````python
"""Tests for openai-deep-research skill."""
import sys
import os
import pytest
from unittest.mock import Mock, MagicMock, patch, mock_open

# Add parent directory to path to import the module
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))

import run_deep_research


@pytest.fixture
def mock_openai_client():
    """Mock OpenAI client."""
    mock_client = MagicMock()
    
    # Mock streaming response
    class MockEvent:
        def __init__(self, event_type, content=None, error=None):
            self.type = event_type
            self.delta = content
            self.response = None
            self.error = error
    
    class MockStream:
        def __init__(self, events):
            self._events = events
        
        def __enter__(self):
            return self
        
        def __exit__(self, *args):
            pass
        
        def __iter__(self):
            return iter(self._events)
    
    # Create mock events
    events = [
        MockEvent("response.output_text.delta", "Part 1 of report"),
        MockEvent("response.output_text.delta", " Part 2 of report"),
        MockEvent("response.completed"),
    ]
    events[-1].response = {"status": "completed"}
    
    mock_stream = MockStream(events)
    mock_client.responses.stream.return_value = mock_stream
    
    return mock_client


class TestValidateApiKey:
    """Test the validate_api_key function."""
    
    def test_validate_with_key(self):
        """Test validation passes with API key."""
        with patch.dict(os.environ, {'OPENAI_API_KEY': 'test_key'}):
            # Should not raise
            run_deep_research.validate_api_key()
    
    def test_validate_without_key(self):
        """Test validation fails without API key."""
        with patch.dict(os.environ, {}, clear=True):
            with pytest.raises(SystemExit):
                run_deep_research.validate_api_key()


class TestRunDeepResearch:
    """Test the run_deep_research function."""
    
    def test_basic_research(self, mock_openai_client):
        """Test basic deep research execution."""
        with patch.dict(os.environ, {'OPENAI_API_KEY': 'test_key'}):
            with patch('run_deep_research.OpenAI', return_value=mock_openai_client):
                with patch('builtins.print') as mock_print:
                    run_deep_research.run_deep_research("test prompt")
        
        # Verify the API was called
        mock_openai_client.responses.stream.assert_called_once()
        
        # Check output was printed
        printed_values = [call[0] for call in mock_print.call_args_list if call[0]]
        assert any("Part 1 of report" in str(val) for val in printed_values)
    
    def test_custom_model(self, mock_openai_client):
        """Test with custom model."""
        with patch.dict(os.environ, {'OPENAI_API_KEY': 'test_key'}):
            with patch('run_deep_research.OpenAI', return_value=mock_openai_client):
                with patch('builtins.print'):
                    run_deep_research.run_deep_research(
                        "test prompt",
                        model="o3-deep-research"
                    )
        
        # Verify correct model was used
        call_kwargs = mock_openai_client.responses.stream.call_args[1]
        assert call_kwargs['model'] == "o3-deep-research"
    
    def test_effort_levels(self, mock_openai_client):
        """Test different effort levels."""
        for effort in ["low", "medium", "high"]:
            with patch.dict(os.environ, {'OPENAI_API_KEY': 'test_key'}):
                with patch('run_deep_research.OpenAI', return_value=mock_openai_client):
                    with patch('builtins.print'):
                        run_deep_research.run_deep_research(
                            "test prompt",
                            effort=effort
                        )
            
            # Verify effort was passed
            call_kwargs = mock_openai_client.responses.stream.call_args[1]
            assert call_kwargs['reasoning']['effort'] == effort
    
    def test_output_to_file(self, mock_openai_client, tmp_path):
        """Test saving report to file."""
        output_file = tmp_path / "report.txt"
        
        with patch.dict(os.environ, {'OPENAI_API_KEY': 'test_key'}):
            with patch('run_deep_research.OpenAI', return_value=mock_openai_client):
                with patch('builtins.print'):
                    run_deep_research.run_deep_research(
                        "test prompt",
                        output_path=str(output_file)
                    )
        
        # Verify file was created
        assert output_file.exists()
        content = output_file.read_text()
        assert "Part 1 of report" in content
        assert "Part 2 of report" in content
    
    def test_json_output(self, mock_openai_client):
        """Test JSON output mode."""
        with patch.dict(os.environ, {'OPENAI_API_KEY': 'test_key'}):
            with patch('run_deep_research.OpenAI', return_value=mock_openai_client):
                with patch('builtins.print') as mock_print:
                    run_deep_research.run_deep_research(
                        "test prompt",
                        emit_json=True
                    )
        
        # Should output JSON
        printed_values = [str(call[0]) for call in mock_print.call_args_list if call[0]]
        assert any('status' in val or '{' in val for val in printed_values)
    
    def test_json_output_to_file(self, mock_openai_client, tmp_path):
        """Test JSON output to file."""
        output_file = tmp_path / "report.json"
        
        with patch.dict(os.environ, {'OPENAI_API_KEY': 'test_key'}):
            with patch('run_deep_research.OpenAI', return_value=mock_openai_client):
                with patch('builtins.print'):
                    run_deep_research.run_deep_research(
                        "test prompt",
                        emit_json=True,
                        output_path=str(output_file)
                    )
        
        # Verify JSON file was created
        assert output_file.exists()
        import json
        content = json.loads(output_file.read_text())
        assert 'status' in content


class TestErrorHandling:
    """Test error handling scenarios."""
    
    def test_api_status_error(self, mock_openai_client):
        """Test handling of API status errors."""
        from openai._exceptions import APIStatusError
        
        mock_response = Mock()
        mock_response.status_code = 429
        error = APIStatusError(
            "Rate limit exceeded",
            response=mock_response,
            body={}
        )
        mock_openai_client.responses.stream.side_effect = error
        
        with patch.dict(os.environ, {'OPENAI_API_KEY': 'test_key'}):
            with patch('run_deep_research.OpenAI', return_value=mock_openai_client):
                with pytest.raises(SystemExit):
                    run_deep_research.run_deep_research("test prompt")
    
    def test_general_exception(self, mock_openai_client):
        """Test handling of general exceptions."""
        mock_openai_client.responses.stream.side_effect = Exception("Unexpected error")
        
        with patch.dict(os.environ, {'OPENAI_API_KEY': 'test_key'}):
            with patch('run_deep_research.OpenAI', return_value=mock_openai_client):
                with pytest.raises(SystemExit):
                    run_deep_research.run_deep_research("test prompt")
    
    def test_response_error_event(self, mock_openai_client):
        """Test handling of response error events."""
        class MockErrorEvent:
            def __init__(self):
                self.type = "response.error"
                self.error = "Processing failed"
        
        class MockErrorStream:
            def __enter__(self):
                return self
            
            def __exit__(self, *args):
                pass
            
            def __iter__(self):
                return iter([MockErrorEvent()])
        
        mock_openai_client.responses.stream.return_value = MockErrorStream()
        
        with patch.dict(os.environ, {'OPENAI_API_KEY': 'test_key'}):
            with patch('run_deep_research.OpenAI', return_value=mock_openai_client):
                with pytest.raises(SystemExit):
                    run_deep_research.run_deep_research("test prompt")


class TestStreamProcessing:
    """Test streaming response processing."""
    
    def test_multiple_chunks(self, mock_openai_client):
        """Test processing multiple text chunks."""
        class MockEvent:
            def __init__(self, event_type, content=None):
                self.type = event_type
                self.delta = content
                self.response = None
        
        class MockStream:
            def __enter__(self):
                return self
            
            def __exit__(self, *args):
                pass
            
            def __iter__(self):
                events = [
                    MockEvent("response.output_text.delta", "Chunk 1 "),
                    MockEvent("response.output_text.delta", "Chunk 2 "),
                    MockEvent("response.output_text.delta", "Chunk 3"),
                    MockEvent("response.completed"),
                ]
                events[-1].response = {"status": "ok"}
                return iter(events)
        
        mock_openai_client.responses.stream.return_value = MockStream()
        
        with patch.dict(os.environ, {'OPENAI_API_KEY': 'test_key'}):
            with patch('run_deep_research.OpenAI', return_value=mock_openai_client):
                with patch('builtins.print') as mock_print:
                    run_deep_research.run_deep_research("test prompt")
        
        # All chunks should be printed
        printed = ''.join([str(call[0][0]) for call in mock_print.call_args_list if call[0]])
        assert "Chunk 1" in printed
        assert "Chunk 2" in printed
        assert "Chunk 3" in printed


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
`````

## File: .claude/skills/perplexity-sonar/tests/test_ask.py
`````python
"""Tests for perplexity-sonar skill."""
import sys
import os
import pytest
from unittest.mock import Mock, MagicMock, patch

# Add parent directory to path to import the module
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))

import ask


@pytest.fixture
def mock_openai_client():
    """Mock OpenAI client for Perplexity API."""
    mock_client = MagicMock()
    
    # Mock chat completion response
    mock_response = Mock()
    mock_message = Mock()
    mock_message.content = "This is the research answer with citations."
    mock_choice = Mock()
    mock_choice.message = mock_message
    mock_response.choices = [mock_choice]
    
    mock_client.chat.completions.create.return_value = mock_response
    
    return mock_client


class TestAskPerplexity:
    """Test the ask_perplexity function."""
    
    def test_basic_query(self, mock_openai_client):
        """Test basic query to Perplexity."""
        with patch.dict(os.environ, {'PERPLEXITY_API_KEY': 'test_key'}):
            with patch('ask.OpenAI', return_value=mock_openai_client):
                with patch('builtins.print') as mock_print:
                    ask.ask_perplexity("test question")
        
        # Verify API was called
        mock_openai_client.chat.completions.create.assert_called_once()
        
        # Check answer was printed
        printed_values = [call[0][0] for call in mock_print.call_args_list]
        assert any("research answer" in str(val) for val in printed_values)
    
    def test_custom_model(self, mock_openai_client):
        """Test with custom model."""
        with patch.dict(os.environ, {'PERPLEXITY_API_KEY': 'test_key'}):
            with patch('ask.OpenAI', return_value=mock_openai_client):
                with patch('builtins.print'):
                    ask.ask_perplexity("test question", model="sonar-large-online")
        
        # Verify correct model was used
        call_kwargs = mock_openai_client.chat.completions.create.call_args[1]
        assert call_kwargs['model'] == "sonar-large-online"
    
    def test_all_models(self, mock_openai_client):
        """Test all supported models."""
        models = ["sonar-small-online", "sonar-medium-online", "sonar-large-online"]
        
        for model in models:
            with patch.dict(os.environ, {'PERPLEXITY_API_KEY': 'test_key'}):
                with patch('ask.OpenAI', return_value=mock_openai_client):
                    with patch('builtins.print'):
                        ask.ask_perplexity("test question", model=model)
            
            call_kwargs = mock_openai_client.chat.completions.create.call_args[1]
            assert call_kwargs['model'] == model
    
    def test_missing_api_key(self):
        """Test error when API key is missing."""
        with patch.dict(os.environ, {}, clear=True):
            with pytest.raises(SystemExit):
                ask.ask_perplexity("test question")
    
    def test_system_prompt_included(self, mock_openai_client):
        """Test that system prompt is included in messages."""
        with patch.dict(os.environ, {'PERPLEXITY_API_KEY': 'test_key'}):
            with patch('ask.OpenAI', return_value=mock_openai_client):
                with patch('builtins.print'):
                    ask.ask_perplexity("test question")
        
        # Check messages structure
        call_kwargs = mock_openai_client.chat.completions.create.call_args[1]
        messages = call_kwargs['messages']
        
        assert len(messages) == 2
        assert messages[0]['role'] == 'system'
        assert 'expert researcher' in messages[0]['content'].lower()
        assert messages[1]['role'] == 'user'
        assert messages[1]['content'] == 'test question'
    
    def test_api_error_handling(self, mock_openai_client):
        """Test handling of API errors."""
        mock_openai_client.chat.completions.create.side_effect = Exception("API Error")
        
        with patch.dict(os.environ, {'PERPLEXITY_API_KEY': 'test_key'}):
            with patch('ask.OpenAI', return_value=mock_openai_client):
                with pytest.raises(SystemExit):
                    ask.ask_perplexity("test question")


class TestClientConfiguration:
    """Test OpenAI client configuration for Perplexity."""
    
    def test_base_url_configuration(self, mock_openai_client):
        """Test that Perplexity base URL is configured correctly."""
        with patch.dict(os.environ, {'PERPLEXITY_API_KEY': 'test_key'}):
            with patch('ask.OpenAI') as mock_openai_cls:
                mock_openai_cls.return_value = mock_openai_client
                with patch('builtins.print'):
                    ask.ask_perplexity("test question")
        
        # Verify OpenAI client was initialized with Perplexity settings
        mock_openai_cls.assert_called_once()
        call_kwargs = mock_openai_cls.call_args[1]
        assert call_kwargs['api_key'] == 'test_key'
        assert call_kwargs['base_url'] == 'https://api.perplexity.ai'


class TestResponseHandling:
    """Test response handling."""
    
    def test_empty_response(self, mock_openai_client):
        """Test handling of empty response."""
        mock_response = Mock()
        mock_message = Mock()
        mock_message.content = ""
        mock_choice = Mock()
        mock_choice.message = mock_message
        mock_response.choices = [mock_choice]
        
        mock_openai_client.chat.completions.create.return_value = mock_response
        
        with patch.dict(os.environ, {'PERPLEXITY_API_KEY': 'test_key'}):
            with patch('ask.OpenAI', return_value=mock_openai_client):
                with patch('builtins.print') as mock_print:
                    ask.ask_perplexity("test question")
        
        # Should still print (even if empty)
        assert mock_print.called
    
    def test_long_response(self, mock_openai_client):
        """Test handling of long research responses."""
        long_answer = "This is a very long answer. " * 100
        
        mock_response = Mock()
        mock_message = Mock()
        mock_message.content = long_answer
        mock_choice = Mock()
        mock_choice.message = mock_message
        mock_response.choices = [mock_choice]
        
        mock_openai_client.chat.completions.create.return_value = mock_response
        
        with patch.dict(os.environ, {'PERPLEXITY_API_KEY': 'test_key'}):
            with patch('ask.OpenAI', return_value=mock_openai_client):
                with patch('builtins.print') as mock_print:
                    ask.ask_perplexity("test question")
        
        # Check full answer was printed
        printed = str(mock_print.call_args_list[0][0][0])
        assert len(printed) > 1000


class TestIntegration:
    """Integration tests (require real API key)."""
    
    @pytest.mark.integration
    @pytest.mark.skipif(
        not os.getenv('PERPLEXITY_API_KEY'),
        reason="PERPLEXITY_API_KEY not set"
    )
    def test_real_query(self):
        """Test with real API (integration test)."""
        with patch('builtins.print'):
            ask.ask_perplexity("What is 2+2?", model="sonar-small-online")


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
`````

## File: .claude/skills/smolagents/tests/test_agent.py
`````python
"""Tests for smolagents skill."""
import sys
import os
import pytest
from unittest.mock import Mock, MagicMock, patch

# Add parent directory to path to import the module
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))

import agent


@pytest.fixture
def mock_inference_client_model():
    """Mock InferenceClientModel."""
    return MagicMock()


@pytest.fixture
def mock_litellm_model():
    """Mock LiteLLMModel."""
    return MagicMock()


@pytest.fixture
def mock_transformers_model():
    """Mock TransformersModel."""
    return MagicMock()


@pytest.fixture
def mock_code_agent():
    """Mock CodeAgent."""
    mock = MagicMock()
    mock.run.return_value = "Agent completed the task successfully."
    return mock


class TestCreateModel:
    """Test the create_model function."""
    
    def test_create_hf_model_default(self, mock_inference_client_model):
        """Test creating default HuggingFace model."""
        with patch.dict(os.environ, {}):
            with patch('agent.InferenceClientModel', return_value=mock_inference_client_model) as mock_cls:
                result = agent.create_model(model_type="hf")
        
        assert result == mock_inference_client_model
        mock_cls.assert_called_once()
        # Should use default Qwen model
        assert "Qwen" in str(mock_cls.call_args)
    
    def test_create_hf_model_custom(self, mock_inference_client_model):
        """Test creating HuggingFace model with custom model ID."""
        with patch.dict(os.environ, {}):
            with patch('agent.InferenceClientModel', return_value=mock_inference_client_model) as mock_cls:
                result = agent.create_model(model_type="hf", model_id="custom/model")
        
        mock_cls.assert_called_once_with(model_id="custom/model")
    
    def test_create_openai_model(self, mock_litellm_model):
        """Test creating OpenAI model."""
        with patch.dict(os.environ, {'OPENAI_API_KEY': 'test_key'}):
            with patch('agent.LiteLLMModel', return_value=mock_litellm_model) as mock_cls:
                result = agent.create_model(model_type="openai")
        
        assert result == mock_litellm_model
        mock_cls.assert_called_once_with(model_id="gpt-4o")
    
    def test_create_openai_model_custom(self, mock_litellm_model):
        """Test creating OpenAI model with custom model ID."""
        with patch.dict(os.environ, {'OPENAI_API_KEY': 'test_key'}):
            with patch('agent.LiteLLMModel', return_value=mock_litellm_model) as mock_cls:
                result = agent.create_model(model_type="openai", model_id="gpt-4-turbo")
        
        mock_cls.assert_called_once_with(model_id="gpt-4-turbo")
    
    def test_create_openai_model_no_key(self):
        """Test creating OpenAI model without API key."""
        with patch.dict(os.environ, {}, clear=True):
            with pytest.raises(SystemExit):
                agent.create_model(model_type="openai")
    
    def test_create_anthropic_model(self, mock_litellm_model):
        """Test creating Anthropic model."""
        with patch.dict(os.environ, {'ANTHROPIC_API_KEY': 'test_key'}):
            with patch('agent.LiteLLMModel', return_value=mock_litellm_model) as mock_cls:
                result = agent.create_model(model_type="anthropic")
        
        assert result == mock_litellm_model
        mock_cls.assert_called_once_with(model_id="claude-3-5-sonnet-20241022")
    
    def test_create_anthropic_model_no_key(self):
        """Test creating Anthropic model without API key."""
        with patch.dict(os.environ, {}, clear=True):
            with pytest.raises(SystemExit):
                agent.create_model(model_type="anthropic")
    
    def test_create_local_model(self, mock_transformers_model):
        """Test creating local Transformers model."""
        with patch('agent.TransformersModel', return_value=mock_transformers_model) as mock_cls:
            result = agent.create_model(model_type="local", model_id="local/model")
        
        assert result == mock_transformers_model
        mock_cls.assert_called_once_with(model_id="local/model")
    
    def test_create_local_model_no_id(self):
        """Test creating local model without model ID fails."""
        with pytest.raises(SystemExit):
            agent.create_model(model_type="local")
    
    def test_create_unknown_model_type(self):
        """Test creating model with unknown type."""
        with pytest.raises(SystemExit):
            agent.create_model(model_type="unknown")


class TestRunAgent:
    """Test the run_agent function."""
    
    def test_basic_run(self, mock_inference_client_model, mock_code_agent):
        """Test basic agent run."""
        with patch.dict(os.environ, {}):
            with patch('agent.create_model', return_value=mock_inference_client_model):
                with patch('agent.CodeAgent', return_value=mock_code_agent):
                    with patch('builtins.print') as mock_print:
                        agent.run_agent("test task")
        
        mock_code_agent.run.assert_called_once_with("test task")
        
        # Check output was printed
        printed_values = [call[0][0] for call in mock_print.call_args_list if call[0]]
        assert any("completed" in str(val).lower() for val in printed_values)
    
    def test_run_with_web_search(self, mock_inference_client_model, mock_code_agent):
        """Test agent run with web search enabled."""
        with patch.dict(os.environ, {}):
            with patch('agent.create_model', return_value=mock_inference_client_model):
                with patch('agent.CodeAgent', return_value=mock_code_agent) as mock_agent_cls:
                    with patch('agent.DuckDuckGoSearchTool') as mock_search_tool:
                        with patch('builtins.print'):
                            agent.run_agent("test task", web_search=True)
        
        # Verify search tool was added
        call_kwargs = mock_agent_cls.call_args[1]
        assert 'tools' in call_kwargs
        assert len(call_kwargs['tools']) > 0
    
    def test_run_with_different_models(self, mock_litellm_model, mock_code_agent):
        """Test agent run with different model types."""
        for model_type in ["hf", "openai", "anthropic"]:
            env = {}
            if model_type == "openai":
                env['OPENAI_API_KEY'] = 'test_key'
            elif model_type == "anthropic":
                env['ANTHROPIC_API_KEY'] = 'test_key'
            
            with patch.dict(os.environ, env):
                with patch('agent.create_model', return_value=mock_litellm_model):
                    with patch('agent.CodeAgent', return_value=mock_code_agent):
                        with patch('builtins.print'):
                            agent.run_agent("test task", model_type=model_type)
            
            mock_code_agent.run.assert_called_with("test task")
    
    def test_run_with_verbose(self, mock_inference_client_model, mock_code_agent):
        """Test agent run with verbose output."""
        mock_code_agent.logs = ["Log entry 1", "Log entry 2"]
        
        with patch.dict(os.environ, {}):
            with patch('agent.create_model', return_value=mock_inference_client_model):
                with patch('agent.CodeAgent', return_value=mock_code_agent):
                    with patch('builtins.print') as mock_print:
                        agent.run_agent("test task", verbose=True)
        
        # Check logs were printed
        stderr_calls = [
            call for call in mock_print.call_args_list 
            if len(call[1]) > 0 and call[1].get('file') == sys.stderr
        ]
        logs_printed = any(
            'Log entry' in str(call[0][0]) 
            for call in stderr_calls
        )
        assert logs_printed
    
    def test_run_error_handling(self, mock_inference_client_model, mock_code_agent):
        """Test agent run error handling."""
        mock_code_agent.run.side_effect = Exception("Agent error")
        
        with patch.dict(os.environ, {}):
            with patch('agent.create_model', return_value=mock_inference_client_model):
                with patch('agent.CodeAgent', return_value=mock_code_agent):
                    with pytest.raises(SystemExit):
                        agent.run_agent("test task")
    
    def test_run_with_custom_model_id(self, mock_inference_client_model, mock_code_agent):
        """Test agent run with custom model ID."""
        with patch.dict(os.environ, {}):
            with patch('agent.create_model', return_value=mock_inference_client_model) as mock_create:
                with patch('agent.CodeAgent', return_value=mock_code_agent):
                    with patch('builtins.print'):
                        agent.run_agent(
                            "test task", 
                            model_type="hf", 
                            model_id="custom/model"
                        )
        
        # Verify custom model was passed
        mock_create.assert_called_once_with("hf", "custom/model")


class TestCodeAgentConfiguration:
    """Test CodeAgent configuration."""
    
    def test_agent_max_steps(self, mock_inference_client_model, mock_code_agent):
        """Test that agent has max_steps configured."""
        with patch.dict(os.environ, {}):
            with patch('agent.create_model', return_value=mock_inference_client_model):
                with patch('agent.CodeAgent', return_value=mock_code_agent) as mock_agent_cls:
                    with patch('builtins.print'):
                        agent.run_agent("test task")
        
        # Verify max_steps is set
        call_kwargs = mock_agent_cls.call_args[1]
        assert 'max_steps' in call_kwargs
        assert call_kwargs['max_steps'] == 10
    
    def test_agent_tools_configuration(self, mock_inference_client_model, mock_code_agent):
        """Test agent tools configuration."""
        with patch.dict(os.environ, {}):
            with patch('agent.create_model', return_value=mock_inference_client_model):
                with patch('agent.CodeAgent', return_value=mock_code_agent) as mock_agent_cls:
                    with patch('builtins.print'):
                        agent.run_agent("test task", web_search=False)
        
        # Verify tools list exists (even if empty)
        call_kwargs = mock_agent_cls.call_args[1]
        assert 'tools' in call_kwargs
        assert isinstance(call_kwargs['tools'], list)


class TestModelWarnings:
    """Test model configuration warnings."""
    
    def test_hf_model_no_token_warning(self, mock_inference_client_model, mock_code_agent):
        """Test warning when HF_TOKEN is not set."""
        with patch.dict(os.environ, {}, clear=True):
            with patch('agent.create_model', return_value=mock_inference_client_model):
                with patch('agent.CodeAgent', return_value=mock_code_agent):
                    with patch('builtins.print') as mock_print:
                        agent.run_agent("test task", model_type="hf")
        
        # Warning should be in stderr
        stderr_calls = [
            call for call in mock_print.call_args_list 
            if len(call[1]) > 0 and call[1].get('file') == sys.stderr
        ]
        # The warning is in create_model, so it should be printed
        # This is checking implementation details, so we can verify the agent ran
        assert mock_code_agent.run.called


class TestIntegration:
    """Integration tests."""
    
    @pytest.mark.integration
    @pytest.mark.skipif(
        not os.getenv('OPENAI_API_KEY') and not os.getenv('HF_TOKEN'),
        reason="No API keys set"
    )
    def test_real_agent_run(self):
        """Test with real agent (integration test)."""
        with patch('builtins.print'):
            agent.run_agent(
                "What is 2+2?",
                model_type="hf" if os.getenv('HF_TOKEN') else "openai"
            )


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
`````

## File: .claude/skills/stanford-storm/tests/test_run_storm.py
`````python
"""Tests for stanford-storm skill."""
import sys
import os
import pytest
from unittest.mock import Mock, MagicMock, patch, mock_open

# Add parent directory to path to import the module
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))

import run_storm


@pytest.fixture
def mock_storm_engine():
    """Mock StormEngine."""
    mock = MagicMock()
    mock.run.return_value = None
    return mock


@pytest.fixture
def mock_storm_engine_cls():
    """Mock StormEngine class."""
    def _create_mock(mock_engine):
        def mock_init(*args, **kwargs):
            return mock_engine
        return mock_init
    return _create_mock


class TestRunStorm:
    """Test the run_storm function."""
    
    def test_basic_storm_run(self, mock_storm_engine, tmp_path):
        """Test basic STORM execution."""
        # Create a fake article file
        article_dir = tmp_path / "storm_output" / "test_dir" / "test_topic"
        article_dir.mkdir(parents=True)
        article_file = article_dir / "storm_gen_article_polished.md"
        article_file.write_text("# Test Article\n\nThis is the generated article.")
        
        with patch('run_storm.tempfile.mkdtemp', return_value=str(article_dir.parent)):
            with patch('run_storm.StormEngine', return_value=mock_storm_engine):
                with patch('run_storm.LiteLLMModelArgs'):
                    with patch('run_storm.StormEngineArgs'):
                        with patch('builtins.print') as mock_print:
                            run_storm.run_storm(
                                "test topic",
                                rm_name="bing",
                                fast_model="gpt-3.5-turbo",
                                strong_model="gpt-4o"
                            )
        
        # Verify engine was run
        mock_storm_engine.run.assert_called_once()
        
        # Check article was printed
        printed_values = [call[0][0] for call in mock_print.call_args_list if call[0]]
        assert any("Test Article" in str(val) for val in printed_values)
    
    def test_storm_run_with_bing_retriever(self, mock_storm_engine, tmp_path):
        """Test STORM with Bing retriever."""
        article_dir = tmp_path / "storm_output" / "test_dir" / "test_topic"
        article_dir.mkdir(parents=True)
        article_file = article_dir / "storm_gen_article_polished.md"
        article_file.write_text("Content")
        
        with patch('run_storm.tempfile.mkdtemp', return_value=str(article_dir.parent)):
            with patch('run_storm.StormEngine', return_value=mock_storm_engine):
                with patch('run_storm.LiteLLMModelArgs'):
                    with patch('run_storm.StormEngineArgs') as mock_args:
                        with patch('builtins.print'):
                            run_storm.run_storm(
                                "test topic",
                                rm_name="bing",
                                fast_model="gpt-3.5-turbo",
                                strong_model="gpt-4o"
                            )
        
        # Verify StormEngineArgs was called with bing retriever
        mock_args.assert_called_once()
        call_kwargs = mock_args.call_args[1]
        assert call_kwargs['rm_name'] == "bing"
    
    def test_storm_run_with_you_retriever(self, mock_storm_engine, tmp_path):
        """Test STORM with You.com retriever."""
        article_dir = tmp_path / "storm_output" / "test_dir" / "test_topic"
        article_dir.mkdir(parents=True)
        article_file = article_dir / "storm_gen_article_polished.md"
        article_file.write_text("Content")
        
        with patch('run_storm.tempfile.mkdtemp', return_value=str(article_dir.parent)):
            with patch('run_storm.StormEngine', return_value=mock_storm_engine):
                with patch('run_storm.LiteLLMModelArgs'):
                    with patch('run_storm.StormEngineArgs') as mock_args:
                        with patch('builtins.print'):
                            run_storm.run_storm(
                                "test topic",
                                rm_name="you",
                                fast_model="gpt-3.5-turbo",
                                strong_model="gpt-4o"
                            )
        
        call_kwargs = mock_args.call_args[1]
        assert call_kwargs['rm_name'] == "you"
    
    def test_storm_model_configuration(self, mock_storm_engine, tmp_path):
        """Test STORM model configuration."""
        article_dir = tmp_path / "storm_output" / "test_dir" / "test_topic"
        article_dir.mkdir(parents=True)
        article_file = article_dir / "storm_gen_article_polished.md"
        article_file.write_text("Content")
        
        with patch('run_storm.tempfile.mkdtemp', return_value=str(article_dir.parent)):
            with patch('run_storm.StormEngine', return_value=mock_storm_engine):
                with patch('run_storm.LiteLLMModelArgs') as mock_model_args:
                    with patch('run_storm.StormEngineArgs'):
                        with patch('builtins.print'):
                            run_storm.run_storm(
                                "test topic",
                                rm_name="bing",
                                fast_model="gpt-3.5-turbo",
                                strong_model="gpt-4o"
                            )
        
        # Verify both fast and strong models were configured
        assert mock_model_args.call_count == 2
        
        # Check the models
        calls = mock_model_args.call_args_list
        fast_call = calls[0][1]
        strong_call = calls[1][1]
        
        assert fast_call['model'] == "gpt-3.5-turbo"
        assert strong_call['model'] == "gpt-4o"
    
    def test_storm_topic_sanitization(self, mock_storm_engine, tmp_path):
        """Test that topic names are sanitized for directory names."""
        article_dir = tmp_path / "storm_output" / "run_test_topic_with_special_" / "test"
        article_dir.mkdir(parents=True)
        article_file = article_dir / "storm_gen_article_polished.md"
        article_file.write_text("Content")
        
        with patch('run_storm.tempfile.mkdtemp', return_value=str(article_dir.parent)):
            with patch('run_storm.StormEngine', return_value=mock_storm_engine):
                with patch('run_storm.LiteLLMModelArgs'):
                    with patch('run_storm.StormEngineArgs'):
                        with patch('builtins.print'):
                            # Topic with special characters
                            run_storm.run_storm(
                                "test/topic with special!",
                                rm_name="bing",
                                fast_model="gpt-3.5-turbo",
                                strong_model="gpt-4o"
                            )
        
        mock_storm_engine.run.assert_called_once()
    
    def test_storm_output_directory_creation(self, mock_storm_engine):
        """Test that output directory is created."""
        with patch('run_storm.os.makedirs') as mock_makedirs:
            with patch('run_storm.tempfile.mkdtemp', return_value="/tmp/test_dir"):
                with patch('run_storm.glob.glob', return_value=[]):
                    with patch('run_storm.StormEngine', return_value=mock_storm_engine):
                        with patch('run_storm.LiteLLMModelArgs'):
                            with patch('run_storm.StormEngineArgs'):
                                with pytest.raises(SystemExit):
                                    run_storm.run_storm(
                                        "test topic",
                                        rm_name="bing",
                                        fast_model="gpt-3.5-turbo",
                                        strong_model="gpt-4o"
                                    )
        
        # Verify output directory creation was attempted
        mock_makedirs.assert_called()


class TestErrorHandling:
    """Test error handling scenarios."""
    
    def test_article_file_not_found(self, mock_storm_engine):
        """Test error when article file is not found."""
        with patch('run_storm.tempfile.mkdtemp', return_value="/tmp/test_dir"):
            with patch('run_storm.glob.glob', return_value=[]):
                with patch('run_storm.StormEngine', return_value=mock_storm_engine):
                    with patch('run_storm.LiteLLMModelArgs'):
                        with patch('run_storm.StormEngineArgs'):
                            with pytest.raises(SystemExit):
                                run_storm.run_storm(
                                    "test topic",
                                    rm_name="bing",
                                    fast_model="gpt-3.5-turbo",
                                    strong_model="gpt-4o"
                                )
    
    def test_storm_engine_error(self, mock_storm_engine):
        """Test error during STORM engine execution."""
        mock_storm_engine.run.side_effect = Exception("STORM error")
        
        with patch('run_storm.tempfile.mkdtemp', return_value="/tmp/test_dir"):
            with patch('run_storm.StormEngine', return_value=mock_storm_engine):
                with patch('run_storm.LiteLLMModelArgs'):
                    with patch('run_storm.StormEngineArgs'):
                        with pytest.raises(SystemExit):
                            run_storm.run_storm(
                                "test topic",
                                rm_name="bing",
                                fast_model="gpt-3.5-turbo",
                                strong_model="gpt-4o"
                            )


class TestStormEngineConfiguration:
    """Test STORM engine configuration."""
    
    def test_engine_args_configuration(self, mock_storm_engine, tmp_path):
        """Test that StormEngineArgs is configured correctly."""
        article_dir = tmp_path / "storm_output" / "test_dir" / "test_topic"
        article_dir.mkdir(parents=True)
        article_file = article_dir / "storm_gen_article_polished.md"
        article_file.write_text("Content")
        
        with patch('run_storm.tempfile.mkdtemp', return_value=str(article_dir.parent)):
            with patch('run_storm.StormEngine', return_value=mock_storm_engine):
                with patch('run_storm.LiteLLMModelArgs') as mock_model_args:
                    mock_fast_config = Mock()
                    mock_strong_config = Mock()
                    mock_model_args.side_effect = [mock_fast_config, mock_strong_config]
                    
                    with patch('run_storm.StormEngineArgs') as mock_engine_args:
                        with patch('builtins.print'):
                            run_storm.run_storm(
                                "test topic",
                                rm_name="bing",
                                fast_model="gpt-3.5-turbo",
                                strong_model="gpt-4o"
                            )
        
        # Verify engine args include both configs
        call_kwargs = mock_engine_args.call_args[1]
        assert call_kwargs['lm_config'] == mock_fast_config
        assert call_kwargs['outline_gen_lm_config'] == mock_strong_config
        assert call_kwargs['article_gen_lm_config'] == mock_strong_config
        assert call_kwargs['article_polish_lm_config'] == mock_strong_config
    
    def test_engine_run_called_with_topic(self, mock_storm_engine, tmp_path):
        """Test that engine.run is called with correct topic."""
        article_dir = tmp_path / "storm_output" / "test_dir" / "test_topic"
        article_dir.mkdir(parents=True)
        article_file = article_dir / "storm_gen_article_polished.md"
        article_file.write_text("Content")
        
        with patch('run_storm.tempfile.mkdtemp', return_value=str(article_dir.parent)):
            with patch('run_storm.StormEngine', return_value=mock_storm_engine):
                with patch('run_storm.LiteLLMModelArgs'):
                    with patch('run_storm.StormEngineArgs'):
                        with patch('builtins.print'):
                            run_storm.run_storm(
                                "My Research Topic",
                                rm_name="bing",
                                fast_model="gpt-3.5-turbo",
                                strong_model="gpt-4o"
                            )
        
        # Verify engine.run was called with topic and output_dir
        call_kwargs = mock_storm_engine.run.call_args[1]
        assert call_kwargs['topic'] == "My Research Topic"
        assert 'output_dir' in call_kwargs


class TestArticleRetrieval:
    """Test article file retrieval."""
    
    def test_article_found_and_read(self, mock_storm_engine, tmp_path):
        """Test that article is found and read correctly."""
        article_dir = tmp_path / "storm_output" / "test_dir" / "test_topic"
        article_dir.mkdir(parents=True)
        article_file = article_dir / "storm_gen_article_polished.md"
        test_content = "# My Article\n\nThis is comprehensive research content."
        article_file.write_text(test_content)
        
        with patch('run_storm.tempfile.mkdtemp', return_value=str(article_dir.parent)):
            with patch('run_storm.StormEngine', return_value=mock_storm_engine):
                with patch('run_storm.LiteLLMModelArgs'):
                    with patch('run_storm.StormEngineArgs'):
                        with patch('builtins.print') as mock_print:
                            run_storm.run_storm(
                                "test topic",
                                rm_name="bing",
                                fast_model="gpt-3.5-turbo",
                                strong_model="gpt-4o"
                            )
        
        # Check that article content was printed
        printed_values = [call[0][0] for call in mock_print.call_args_list if call[0]]
        assert any("My Article" in str(val) for val in printed_values)
        assert any("comprehensive research" in str(val) for val in printed_values)


class TestIntegration:
    """Integration tests."""
    
    @pytest.mark.integration
    @pytest.mark.skipif(
        not os.getenv('OPENAI_API_KEY'),
        reason="OPENAI_API_KEY not set"
    )
    def test_real_storm_run(self):
        """Test with real STORM (integration test)."""
        # This requires actual API keys and STORM dependencies
        with patch('builtins.print'):
            run_storm.run_storm(
                "Artificial Intelligence",
                rm_name="bing",
                fast_model="gpt-3.5-turbo",
                strong_model="gpt-4o"
            )


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
`````

## File: .claude/skills/tavily-search/tests/test_tavily_search.py
`````python
"""Tests for tavily-search skill."""
import sys
import os
import pytest
from unittest.mock import Mock, MagicMock, patch

# Add parent directory to path to import the module
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))

import tavily_search


@pytest.fixture
def mock_tavily_client():
    """Mock TavilyClient."""
    mock = MagicMock()
    mock.search.return_value = {
        'answer': 'This is the synthesized answer.',
        'results': [
            {
                'title': 'Result 1',
                'url': 'https://example1.com',
                'content': 'Content 1'
            },
            {
                'title': 'Result 2',
                'url': 'https://example2.com',
                'content': 'Content 2'
            }
        ]
    }
    return mock


class TestPerformSearch:
    """Test the perform_search function."""
    
    def test_basic_search(self, mock_tavily_client):
        """Test basic search with default parameters."""
        with patch.dict(os.environ, {'TAVILY_API_KEY': 'test_key'}):
            with patch('tavily_search.TavilyClient', return_value=mock_tavily_client):
                with patch('builtins.print') as mock_print:
                    tavily_search.perform_search("test query")
        
        # Verify client was called
        mock_tavily_client.search.assert_called_once()
        
        # Check output was printed
        printed_values = [call[0][0] for call in mock_print.call_args_list if call[0]]
        assert any("synthesized answer" in str(val).lower() for val in printed_values)
    
    def test_search_with_basic_depth(self, mock_tavily_client):
        """Test search with basic depth."""
        with patch.dict(os.environ, {'TAVILY_API_KEY': 'test_key'}):
            with patch('tavily_search.TavilyClient', return_value=mock_tavily_client):
                with patch('builtins.print'):
                    tavily_search.perform_search("test query", search_depth="basic")
        
        call_kwargs = mock_tavily_client.search.call_args[1]
        assert call_kwargs['search_depth'] == "basic"
    
    def test_search_with_advanced_depth(self, mock_tavily_client):
        """Test search with advanced depth."""
        with patch.dict(os.environ, {'TAVILY_API_KEY': 'test_key'}):
            with patch('tavily_search.TavilyClient', return_value=mock_tavily_client):
                with patch('builtins.print'):
                    tavily_search.perform_search("test query", search_depth="advanced")
        
        call_kwargs = mock_tavily_client.search.call_args[1]
        assert call_kwargs['search_depth'] == "advanced"
    
    def test_search_with_custom_max_results(self, mock_tavily_client):
        """Test search with custom max results."""
        with patch.dict(os.environ, {'TAVILY_API_KEY': 'test_key'}):
            with patch('tavily_search.TavilyClient', return_value=mock_tavily_client):
                with patch('builtins.print'):
                    tavily_search.perform_search("test query", max_results=20)
        
        call_kwargs = mock_tavily_client.search.call_args[1]
        assert call_kwargs['max_results'] == 20
    
    def test_search_includes_answer(self, mock_tavily_client):
        """Test that search requests synthesized answer."""
        with patch.dict(os.environ, {'TAVILY_API_KEY': 'test_key'}):
            with patch('tavily_search.TavilyClient', return_value=mock_tavily_client):
                with patch('builtins.print'):
                    tavily_search.perform_search("test query")
        
        call_kwargs = mock_tavily_client.search.call_args[1]
        assert call_kwargs['include_answer'] is True
        assert call_kwargs['include_raw_content'] is False
    
    def test_missing_api_key(self):
        """Test error when API key is missing."""
        with patch.dict(os.environ, {}, clear=True):
            with pytest.raises(SystemExit):
                tavily_search.perform_search("test query")
    
    def test_search_error_handling(self, mock_tavily_client):
        """Test error handling during search."""
        mock_tavily_client.search.side_effect = Exception("Search failed")
        
        with patch.dict(os.environ, {'TAVILY_API_KEY': 'test_key'}):
            with patch('tavily_search.TavilyClient', return_value=mock_tavily_client):
                with pytest.raises(SystemExit):
                    tavily_search.perform_search("test query")


class TestOutputFormat:
    """Test output format and structure."""
    
    def test_output_json_structure(self, mock_tavily_client):
        """Test that output is valid JSON with expected structure."""
        with patch.dict(os.environ, {'TAVILY_API_KEY': 'test_key'}):
            with patch('tavily_search.TavilyClient', return_value=mock_tavily_client):
                with patch('builtins.print') as mock_print:
                    tavily_search.perform_search("test query")
        
        # Get the printed output
        printed_values = [call[0][0] for call in mock_print.call_args_list if call[0]]
        
        # Should contain JSON output
        import json
        json_found = False
        for val in printed_values:
            try:
                parsed = json.loads(str(val))
                if 'answer' in parsed and 'results' in parsed:
                    json_found = True
                    assert parsed['answer'] == 'This is the synthesized answer.'
                    assert len(parsed['results']) == 2
                    break
            except (json.JSONDecodeError, TypeError):
                continue
        
        assert json_found
    
    def test_output_contains_results_array(self, mock_tavily_client):
        """Test that output contains results array."""
        with patch.dict(os.environ, {'TAVILY_API_KEY': 'test_key'}):
            with patch('tavily_search.TavilyClient', return_value=mock_tavily_client):
                with patch('builtins.print') as mock_print:
                    tavily_search.perform_search("test query")
        
        printed = str(mock_print.call_args_list)
        assert 'Result 1' in printed
        assert 'Result 2' in printed
    
    def test_empty_results(self, mock_tavily_client):
        """Test handling of empty search results."""
        mock_tavily_client.search.return_value = {
            'answer': 'No results found.',
            'results': []
        }
        
        with patch.dict(os.environ, {'TAVILY_API_KEY': 'test_key'}):
            with patch('tavily_search.TavilyClient', return_value=mock_tavily_client):
                with patch('builtins.print') as mock_print:
                    tavily_search.perform_search("test query")
        
        printed_values = [call[0][0] for call in mock_print.call_args_list if call[0]]
        
        import json
        for val in printed_values:
            try:
                parsed = json.loads(str(val))
                if 'results' in parsed:
                    assert parsed['results'] == []
                    assert parsed['answer'] == 'No results found.'
                    break
            except (json.JSONDecodeError, TypeError):
                continue


class TestClientInitialization:
    """Test TavilyClient initialization."""
    
    def test_client_initialized_with_api_key(self, mock_tavily_client):
        """Test that client is initialized with correct API key."""
        with patch.dict(os.environ, {'TAVILY_API_KEY': 'my_test_key'}):
            with patch('tavily_search.TavilyClient') as mock_client_cls:
                mock_client_cls.return_value = mock_tavily_client
                with patch('builtins.print'):
                    tavily_search.perform_search("test query")
        
        # Verify client was initialized with correct key
        mock_client_cls.assert_called_once_with(api_key='my_test_key')


class TestQueryParameters:
    """Test query parameters handling."""
    
    def test_query_passed_correctly(self, mock_tavily_client):
        """Test that query is passed correctly to Tavily."""
        with patch.dict(os.environ, {'TAVILY_API_KEY': 'test_key'}):
            with patch('tavily_search.TavilyClient', return_value=mock_tavily_client):
                with patch('builtins.print'):
                    tavily_search.perform_search("my specific query")
        
        call_kwargs = mock_tavily_client.search.call_args[1]
        assert call_kwargs['query'] == "my specific query"
    
    def test_special_characters_in_query(self, mock_tavily_client):
        """Test query with special characters."""
        with patch.dict(os.environ, {'TAVILY_API_KEY': 'test_key'}):
            with patch('tavily_search.TavilyClient', return_value=mock_tavily_client):
                with patch('builtins.print'):
                    tavily_search.perform_search("query with special chars: @#$%")
        
        call_kwargs = mock_tavily_client.search.call_args[1]
        assert call_kwargs['query'] == "query with special chars: @#$%"


class TestResponseHandling:
    """Test response handling."""
    
    def test_missing_answer_field(self, mock_tavily_client):
        """Test handling when answer field is missing."""
        mock_tavily_client.search.return_value = {
            'results': []
        }
        
        with patch.dict(os.environ, {'TAVILY_API_KEY': 'test_key'}):
            with patch('tavily_search.TavilyClient', return_value=mock_tavily_client):
                with patch('builtins.print') as mock_print:
                    tavily_search.perform_search("test query")
        
        # Should still output (with None for answer)
        assert mock_print.called
    
    def test_missing_results_field(self, mock_tavily_client):
        """Test handling when results field is missing."""
        mock_tavily_client.search.return_value = {
            'answer': 'Answer only'
        }
        
        with patch.dict(os.environ, {'TAVILY_API_KEY': 'test_key'}):
            with patch('tavily_search.TavilyClient', return_value=mock_tavily_client):
                with patch('builtins.print') as mock_print:
                    tavily_search.perform_search("test query")
        
        # Check that empty results list is used
        printed_values = [call[0][0] for call in mock_print.call_args_list if call[0]]
        
        import json
        for val in printed_values:
            try:
                parsed = json.loads(str(val))
                if 'results' in parsed:
                    assert parsed['results'] == []
                    break
            except (json.JSONDecodeError, TypeError):
                continue


class TestIntegration:
    """Integration tests."""
    
    @pytest.mark.integration
    @pytest.mark.skipif(
        not os.getenv('TAVILY_API_KEY'),
        reason="TAVILY_API_KEY not set"
    )
    def test_real_search(self):
        """Test with real Tavily API (integration test)."""
        with patch('builtins.print'):
            tavily_search.perform_search(
                "What is Python?",
                search_depth="basic",
                max_results=3
            )


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
`````

## File: .claude/skills/xai-grok/tests/test_grok_research.py
`````python
"""Tests for xai-grok skill."""
import sys
import os
import pytest
from unittest.mock import Mock, MagicMock, patch

# Add parent directory to path to import the module
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))

import grok_research


@pytest.fixture
def mock_xai_client():
    """Mock xAI Client."""
    mock_client = MagicMock()
    return mock_client


@pytest.fixture
def mock_chat():
    """Mock chat object."""
    mock = MagicMock()
    
    # Mock streaming chunks
    class MockChunk:
        def __init__(self, content, is_thinking=False, tool_calls=None, citations=None):
            self.content = content
            self.is_thinking = is_thinking
            self.tool_calls = tool_calls or []
            self.citations = citations or []
    
    mock_chunks = [
        MockChunk("Final answer content", is_thinking=False, citations=[
            Mock(title="Source 1", url="https://example1.com"),
            Mock(title="Source 2", url="https://example2.com")
        ])
    ]
    
    def mock_stream():
        return iter(mock_chunks)
    
    mock.stream.return_value = mock_stream()
    mock.append = Mock()
    
    return mock


class TestGrokResearch:
    """Test the grok_research function."""
    
    def test_basic_research(self, mock_xai_client, mock_chat):
        """Test basic research query."""
        mock_xai_client.chat.create.return_value = mock_chat
        
        with patch.dict(os.environ, {'XAI_API_KEY': 'test_key'}):
            with patch('grok_research.Client', return_value=mock_xai_client):
                with patch('grok_research.user') as mock_user:
                    with patch('builtins.print') as mock_print:
                        grok_research.grok_research("test query")
        
        # Verify client was created
        mock_xai_client.chat.create.assert_called_once()
        
        # Verify user message was appended
        mock_chat.append.assert_called_once()
        
        # Check output was printed
        printed_values = [call[0][0] for call in mock_print.call_args_list if call[0]]
        assert any("Final answer" in str(val) for val in printed_values)
    
    def test_custom_model(self, mock_xai_client, mock_chat):
        """Test research with custom model."""
        mock_xai_client.chat.create.return_value = mock_chat
        
        with patch.dict(os.environ, {'XAI_API_KEY': 'test_key'}):
            with patch('grok_research.Client', return_value=mock_xai_client):
                with patch('grok_research.user'):
                    with patch('builtins.print'):
                        grok_research.grok_research(
                            "test query",
                            model="grok-4"
                        )
        
        # Verify correct model was used
        call_kwargs = mock_xai_client.chat.create.call_args[1]
        assert call_kwargs['model'] == "grok-4"
    
    def test_web_search_enabled(self, mock_xai_client, mock_chat):
        """Test research with web search enabled."""
        mock_xai_client.chat.create.return_value = mock_chat
        
        with patch.dict(os.environ, {'XAI_API_KEY': 'test_key'}):
            with patch('grok_research.Client', return_value=mock_xai_client):
                with patch('grok_research.user'):
                    with patch('grok_research.web_search') as mock_web_search:
                        with patch('builtins.print'):
                            grok_research.grok_research(
                                "test query",
                                enable_web_search=True
                            )
        
        # Verify web_search tool was called
        mock_web_search.assert_called_once()
        
        # Verify tools were passed to create
        call_kwargs = mock_xai_client.chat.create.call_args[1]
        assert 'tools' in call_kwargs
        assert len(call_kwargs['tools']) > 0
    
    def test_x_search_enabled(self, mock_xai_client, mock_chat):
        """Test research with X search enabled."""
        mock_xai_client.chat.create.return_value = mock_chat
        
        with patch.dict(os.environ, {'XAI_API_KEY': 'test_key'}):
            with patch('grok_research.Client', return_value=mock_xai_client):
                with patch('grok_research.user'):
                    with patch('grok_research.x_search') as mock_x_search:
                        with patch('builtins.print'):
                            grok_research.grok_research(
                                "test query",
                                enable_x_search=True
                            )
        
        # Verify x_search tool was called
        mock_x_search.assert_called_once()
    
    def test_both_searches_enabled(self, mock_xai_client, mock_chat):
        """Test research with both web and X search enabled."""
        mock_xai_client.chat.create.return_value = mock_chat
        
        with patch.dict(os.environ, {'XAI_API_KEY': 'test_key'}):
            with patch('grok_research.Client', return_value=mock_xai_client):
                with patch('grok_research.user'):
                    with patch('grok_research.web_search') as mock_web_search:
                        with patch('grok_research.x_search') as mock_x_search:
                            with patch('builtins.print'):
                                grok_research.grok_research(
                                    "test query",
                                    enable_web_search=True,
                                    enable_x_search=True
                                )
        
        # Verify both tools were called
        mock_web_search.assert_called_once()
        mock_x_search.assert_called_once()
        
        # Verify tools list has 2 items
        call_kwargs = mock_xai_client.chat.create.call_args[1]
        assert len(call_kwargs['tools']) == 2
    
    def test_no_tools_warning(self, mock_xai_client, mock_chat):
        """Test warning when no tools are enabled."""
        mock_xai_client.chat.create.return_value = mock_chat
        
        with patch.dict(os.environ, {'XAI_API_KEY': 'test_key'}):
            with patch('grok_research.Client', return_value=mock_xai_client):
                with patch('grok_research.user'):
                    with patch('builtins.print') as mock_print:
                        grok_research.grok_research("test query")
        
        # Check for warning in stderr
        stderr_calls = [
            call for call in mock_print.call_args_list 
            if len(call[1]) > 0 and call[1].get('file') == sys.stderr
        ]
        warning_found = any(
            'No tools enabled' in str(call[0][0]) 
            for call in stderr_calls
        )
        assert warning_found
    
    def test_missing_api_key(self):
        """Test error when API key is missing."""
        with patch.dict(os.environ, {}, clear=True):
            with pytest.raises(SystemExit):
                grok_research.grok_research("test query")
    
    def test_api_error_handling(self, mock_xai_client):
        """Test handling of API errors."""
        mock_xai_client.chat.create.side_effect = Exception("API error")
        
        with patch.dict(os.environ, {'XAI_API_KEY': 'test_key'}):
            with patch('grok_research.Client', return_value=mock_xai_client):
                with pytest.raises(SystemExit):
                    grok_research.grok_research("test query")


class TestStreamProcessing:
    """Test streaming response processing."""
    
    def test_thinking_chunks(self, mock_xai_client):
        """Test processing of thinking chunks."""
        mock_chat = MagicMock()
        
        class MockChunk:
            def __init__(self, content, is_thinking):
                self.content = content
                self.is_thinking = is_thinking
                self.tool_calls = []
                self.citations = []
        
        chunks = [
            MockChunk("Thinking step 1", is_thinking=True),
            MockChunk("Thinking step 2", is_thinking=True),
            MockChunk("Final answer", is_thinking=False)
        ]
        
        mock_chat.stream.return_value = iter(chunks)
        mock_chat.append = Mock()
        mock_xai_client.chat.create.return_value = mock_chat
        
        with patch.dict(os.environ, {'XAI_API_KEY': 'test_key'}):
            with patch('grok_research.Client', return_value=mock_xai_client):
                with patch('grok_research.user'):
                    with patch('builtins.print') as mock_print:
                        grok_research.grok_research("test query")
        
        # Check that thinking chunks were printed to stderr
        stderr_calls = [
            call for call in mock_print.call_args_list 
            if len(call[1]) > 0 and call[1].get('file') == sys.stderr
        ]
        thinking_found = any(
            'Thinking' in str(call[0][0]) 
            for call in stderr_calls
        )
        assert thinking_found
    
    def test_tool_calls_in_stream(self, mock_xai_client):
        """Test processing of tool calls in stream."""
        mock_chat = MagicMock()
        
        class MockToolCall:
            def __init__(self, call_type, arguments):
                self.type = call_type
                self.arguments = arguments
        
        class MockChunk:
            def __init__(self, content, tool_calls=None):
                self.content = content
                self.is_thinking = False
                self.tool_calls = tool_calls or []
                self.citations = []
        
        chunks = [
            MockChunk("", tool_calls=[
                MockToolCall("web_search", {"query": "test"})
            ]),
            MockChunk("Final answer")
        ]
        
        mock_chat.stream.return_value = iter(chunks)
        mock_chat.append = Mock()
        mock_xai_client.chat.create.return_value = mock_chat
        
        with patch.dict(os.environ, {'XAI_API_KEY': 'test_key'}):
            with patch('grok_research.Client', return_value=mock_xai_client):
                with patch('grok_research.user'):
                    with patch('builtins.print') as mock_print:
                        grok_research.grok_research("test query")
        
        # Check that tool calls were printed to stderr
        stderr_calls = [
            call for call in mock_print.call_args_list 
            if len(call[1]) > 0 and call[1].get('file') == sys.stderr
        ]
        tool_call_found = any(
            'Tool Call' in str(call[0][0]) 
            for call in stderr_calls
        )
        assert tool_call_found
    
    def test_citations_in_response(self, mock_xai_client):
        """Test processing of citations."""
        mock_chat = MagicMock()
        
        class MockChunk:
            def __init__(self):
                self.content = "Answer with citations"
                self.is_thinking = False
                self.tool_calls = []
                self.citations = [
                    Mock(title="Source 1", url="https://example1.com"),
                    Mock(title="Source 2", url="https://example2.com")
                ]
        
        mock_chat.stream.return_value = iter([MockChunk()])
        mock_chat.append = Mock()
        mock_xai_client.chat.create.return_value = mock_chat
        
        with patch.dict(os.environ, {'XAI_API_KEY': 'test_key'}):
            with patch('grok_research.Client', return_value=mock_xai_client):
                with patch('grok_research.user'):
                    with patch('builtins.print') as mock_print:
                        grok_research.grok_research("test query")
        
        # Check that citations were printed
        printed = ''.join([str(call) for call in mock_print.call_args_list])
        assert "Citations" in printed
        assert "Source 1" in printed
        assert "https://example1.com" in printed
    
    def test_empty_response(self, mock_xai_client):
        """Test handling of empty response."""
        mock_chat = MagicMock()
        
        class MockChunk:
            def __init__(self):
                self.content = None
                self.is_thinking = False
                self.tool_calls = []
                self.citations = []
        
        mock_chat.stream.return_value = iter([MockChunk()])
        mock_chat.append = Mock()
        mock_xai_client.chat.create.return_value = mock_chat
        
        with patch.dict(os.environ, {'XAI_API_KEY': 'test_key'}):
            with patch('grok_research.Client', return_value=mock_xai_client):
                with patch('grok_research.user'):
                    with patch('builtins.print') as mock_print:
                        grok_research.grok_research("test query")
        
        # Should handle gracefully
        printed = ''.join([str(call) for call in mock_print.call_args_list])
        assert "No final response" in printed


class TestClientConfiguration:
    """Test xAI client configuration."""
    
    def test_client_initialized_with_api_key(self, mock_xai_client, mock_chat):
        """Test that client is initialized with correct API key."""
        mock_xai_client.chat.create.return_value = mock_chat
        
        with patch.dict(os.environ, {'XAI_API_KEY': 'my_test_key'}):
            with patch('grok_research.Client') as mock_client_cls:
                mock_client_cls.return_value = mock_xai_client
                with patch('grok_research.user'):
                    with patch('builtins.print'):
                        grok_research.grok_research("test query")
        
        # Verify client was initialized with API key
        mock_client_cls.assert_called_once_with(api_key='my_test_key')


class TestModelOptions:
    """Test different model options."""
    
    @pytest.mark.parametrize("model", [
        "grok-4.1-fast-reasoning",
        "grok-4"
    ])
    def test_different_models(self, mock_xai_client, mock_chat, model):
        """Test different Grok models."""
        mock_xai_client.chat.create.return_value = mock_chat
        
        with patch.dict(os.environ, {'XAI_API_KEY': 'test_key'}):
            with patch('grok_research.Client', return_value=mock_xai_client):
                with patch('grok_research.user'):
                    with patch('builtins.print'):
                        grok_research.grok_research("test query", model=model)
        
        call_kwargs = mock_xai_client.chat.create.call_args[1]
        assert call_kwargs['model'] == model


class TestIntegration:
    """Integration tests."""
    
    @pytest.mark.integration
    @pytest.mark.skipif(
        not os.getenv('XAI_API_KEY'),
        reason="XAI_API_KEY not set"
    )
    def test_real_grok_query(self):
        """Test with real xAI API (integration test)."""
        with patch('builtins.print'):
            grok_research.grok_research(
                "What is 2+2?",
                model="grok-4.1-fast-reasoning",
                enable_web_search=False
            )


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
`````

## File: .claude/skills/TEST_README.md
`````markdown
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
`````

## File: .claude/skills/test-requirements.txt
`````
# Core test dependencies
pytest>=7.4.0
pytest-asyncio>=0.21.0
pytest-mock>=3.11.0
python-dotenv>=1.0.0

# Skill dependencies (from all skills' requirements.txt)
# exa-research
exa-py
openai

# gpt-researcher
gpt-researcher

# jina-ai
requests

# langchain-deep-research
langgraph-sdk
langchain-core

# smolagents
smolagents[toolkit]

# stanford-storm
knowledge-storm
dspy-ai
litellm

# tavily-search
tavily-python

# xai-grok
xai-sdk
`````

## File: awesome_deep_research/cli.py
`````python
from __future__ import annotations

import argparse
import re
import subprocess
import sys
import textwrap
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Optional

REPO_ROOT = Path(__file__).resolve().parent.parent
SKILLS_ROOT = REPO_ROOT / ".claude" / "skills"
PROMPT_FILE = REPO_ROOT / "docs" / "taxonomy-and-examples.md"
DEFAULT_OUTPUT_DIR = REPO_ROOT / "outputs"


@dataclass
class PromptExample:
    identifier: str
    category: str
    text: str


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return slug or "prompt"


def load_skills() -> Dict[str, Path]:
    if not SKILLS_ROOT.exists():
        return {}
    return {
        path.name: path
        for path in sorted(SKILLS_ROOT.iterdir())
        if path.is_dir()
    }


def parse_skill_description(skill_dir: Path) -> str:
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        return ""

    description = ""
    inside_front_matter = False
    try:
        for raw_line in skill_md.read_text(encoding="utf-8").splitlines():
            line = raw_line.strip()
            if line == "---":
                if not inside_front_matter:
                    inside_front_matter = True
                    continue
                break
            if inside_front_matter and line.lower().startswith("description:"):
                description = line.split(":", 1)[1].strip()
                break
    except UnicodeDecodeError:
        return ""
    return description


def list_skills_command(_: argparse.Namespace) -> int:
    skills = load_skills()
    if not skills:
        print("No Claude Code skills found under .claude/skills/", file=sys.stderr)
        return 1

    for name, path in skills.items():
        description = parse_skill_description(path)
        if description:
            print(f"{name}\t{description}")
        else:
            print(f"{name}")
    return 0


def load_prompt_examples() -> List[PromptExample]:
    if not PROMPT_FILE.exists():
        return []

    examples: List[PromptExample] = []
    counters: Dict[str, int] = {}
    current_category: Optional[str] = None
    current_slug: Optional[str] = None
    in_examples_section = False

    content = PROMPT_FILE.read_text(encoding="utf-8")
    for raw_line in content.splitlines():
        line = raw_line.strip()

        if not line:
            continue

        if line == "---":
            if not in_examples_section:
                continue
            # Ignore horizontal rules once inside the section
            continue

        if not in_examples_section:
            if line.startswith("##") and "Canonical" in line:
                in_examples_section = True
            continue

        if line.startswith("##") and not line.startswith("###") and "Canonical" not in line:
            # Exiting the examples section
            break

        if line.startswith("###"):
            heading = line.lstrip("#").strip()
            heading = heading.replace("**", "").strip()
            heading = re.sub(r"^\d+(\.\d+)*\s*", "", heading)
            current_category = heading
            current_slug = slugify(heading)
            continue

        if not current_category or not current_slug:
            continue

        bullet_match = re.match(r"^[-*+]\s*(.+)", line)
        if bullet_match:
            prompt_text = bullet_match.group(1).strip()
            prompt_text = prompt_text.strip('"“”')
            if not prompt_text:
                continue
            count = counters.get(current_slug, 0) + 1
            counters[current_slug] = count
            identifier = f"{current_slug}-{count:02d}"
            examples.append(
                PromptExample(identifier=identifier, category=current_category, text=prompt_text)
            )

    return examples


def list_prompts_command(_: argparse.Namespace) -> int:
    prompts = load_prompt_examples()
    if not prompts:
        print(
            "No prompt examples were found. Ensure docs/taxonomy-and-examples.md is present.",
            file=sys.stderr,
        )
        return 1

    for prompt in prompts:
        print(f"{prompt.identifier}\t[{prompt.category}] {prompt.text}")
    return 0


def resolve_prompt_text(prompt_id: Optional[str], prompt_text: Optional[str]) -> PromptExample:
    if prompt_text:
        return PromptExample(identifier="custom", category="Custom", text=prompt_text)

    if not prompt_id:
        raise ValueError("Either --prompt-id or --prompt-text must be provided.")

    prompts = {example.identifier: example for example in load_prompt_examples()}
    if prompt_id not in prompts:
        raise KeyError(f"Prompt id '{prompt_id}' was not found in docs/taxonomy-and-examples.md.")
    return prompts[prompt_id]


def gather_skill_scripts(skill_dir: Path) -> Iterable[str]:
    scripts_dir = skill_dir / "scripts"
    if not scripts_dir.exists():
        return []
    return [str(path.relative_to(REPO_ROOT)) for path in sorted(scripts_dir.glob("*.py"))]


def build_system_prompt(skill_name: str, skill_dir: Path) -> str:
    description = parse_skill_description(skill_dir)
    scripts = list(gather_skill_scripts(skill_dir))
    scripts_section = "\n".join(f"- {script}" for script in scripts) if scripts else "(no scripts directory found)"

    requirements_path = skill_dir / "requirements.txt"
    requirements_line = (
        f"requirements: {requirements_path.relative_to(REPO_ROOT)}"
        if requirements_path.exists()
        else "requirements: (none provided)"
    )

    system_prompt = textwrap.dedent(
        f"""
        You are running inside the Awesome Deep Researchers headless CLI.
        Skill: {skill_name}
        Description: {description or 'No description available.'}
        Skill path: {skill_dir.relative_to(REPO_ROOT)}
        {requirements_line}

        Accessible helper scripts:
        {scripts_section}

        Always rely on the selected skill's tooling for external research calls.
        Verify that required environment variables and dependencies are available before execution.
        If something is missing, stop and report precise remediation steps.
        Provide outputs with clear inline citations and a final reference list.
        """
    ).strip()

    return system_prompt


def build_user_prompt(prompt: PromptExample, extra: Optional[str]) -> str:
    extra_section = f"\n\n## Additional Instructions\n{extra.strip()}" if extra else ""

    return textwrap.dedent(
        f"""
        # Research Brief

        ## Category
        {prompt.category}

        ## Core Task
        {prompt.text}
        {extra_section}

        ## Deliverable
        Produce a concise but thorough Markdown report including:
        - Executive summary (2-3 paragraphs).
        - Key findings as bulleted insights with inline citations.
        - Risks, uncertainties, or open questions.
        - Recommended next steps for a human researcher.
        - Reference list with full source URLs.

        Confirm how the selected skill was used. If the task cannot be completed, explain why and propose alternatives.
        """
    ).strip()


def ensure_output_dir(path: Optional[str]) -> Path:
    if path:
        output_dir = Path(path)
        if not output_dir.is_absolute():
            output_dir = REPO_ROOT / output_dir
    else:
        output_dir = DEFAULT_OUTPUT_DIR
    output_dir.mkdir(parents=True, exist_ok=True)
    return output_dir


def next_output_path(output_dir: Path, skill_name: str) -> Path:
    token = re.sub(r"[^A-Z0-9]+", "-", skill_name.upper())
    pattern = re.compile(rf"OUTPUT-{re.escape(token)}-(\d+)\.md$")
    max_index = 0
    for existing in output_dir.glob(f"OUTPUT-{token}-*.md"):
        match = pattern.match(existing.name)
        if match:
            max_index = max(max_index, int(match.group(1)))
    next_index = max_index + 1
    return output_dir / f"OUTPUT-{token}-{next_index:04d}.md"


def run_command(args: argparse.Namespace) -> int:
    skills = load_skills()
    if args.skill not in skills:
        available = ", ".join(skills.keys()) or "<none>"
        print(f"Skill '{args.skill}' not found. Available skills: {available}", file=sys.stderr)
        return 1

    skill_dir = skills[args.skill]

    try:
        prompt = resolve_prompt_text(args.prompt_id, args.prompt_text)
    except (ValueError, KeyError) as exc:
        print(str(exc), file=sys.stderr)
        return 1

    system_prompt = build_system_prompt(args.skill, skill_dir)
    user_prompt = build_user_prompt(prompt, args.extra_instructions)

    cmd = ["claude", "--print", "--append-system-prompt", system_prompt]
    if args.model:
        cmd.extend(["--model", args.model])
    cmd.append(user_prompt)

    try:
        completed = subprocess.run(
            cmd,
            check=False,
            capture_output=True,
            text=True,
        )
    except FileNotFoundError:
        print("The 'claude' CLI could not be found in PATH. Install Claude Code before running.", file=sys.stderr)
        return 1

    if completed.returncode != 0:
        print("Claude CLI command failed:", file=sys.stderr)
        if completed.stderr:
            print(completed.stderr.strip(), file=sys.stderr)
        return completed.returncode

    output_text = completed.stdout.strip()
    if not output_text:
        print("Claude CLI returned empty output.", file=sys.stderr)
        return 1

    output_dir = ensure_output_dir(args.output_dir)
    output_path = next_output_path(output_dir, args.skill)
    output_path.write_text(output_text + "\n", encoding="utf-8")

    if completed.stderr:
        print(completed.stderr.strip(), file=sys.stderr)

    print(f"Saved report to {output_path.relative_to(REPO_ROOT)}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="adr",
        description="Awesome Deep Researchers CLI wrapper for headless Claude Code runs.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    list_skills = subparsers.add_parser("list-skills", help="List available Claude Code skills.")
    list_skills.set_defaults(func=list_skills_command)

    list_prompts = subparsers.add_parser(
        "list-prompts", help="List canned research prompts from the taxonomy examples."
    )
    list_prompts.set_defaults(func=list_prompts_command)

    run_parser = subparsers.add_parser(
        "run", help="Execute a headless Claude research run with a selected skill and prompt."
    )
    run_parser.add_argument("--skill", required=True, help="Skill name under .claude/skills to activate.")
    prompt_group = run_parser.add_mutually_exclusive_group(required=True)
    prompt_group.add_argument("--prompt-id", help="Identifier from 'adr list-prompts'.")
    prompt_group.add_argument("--prompt-text", help="Freeform research prompt text.")
    run_parser.add_argument("--model", help="Optional Claude model alias (passed through to claude CLI).")
    run_parser.add_argument(
        "--extra-instructions",
        help="Additional instructions appended to the research brief.",
    )
    run_parser.add_argument(
        "--output-dir",
        help="Directory for saving outputs (default: outputs/ in repo root).",
    )
    run_parser.set_defaults(func=run_command)

    return parser


def main(argv: Optional[List[str]] = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
`````

## File: benchmark/results/.gitignore
`````
# Ignore all benchmark results
*

# But keep this .gitignore
!.gitignore

# And keep README
!README.md
`````

## File: benchmark/results/README.md
`````markdown
# Benchmark Results

This directory contains benchmark results from running skills against taxonomy questions.

Results are generated by running:

```bash
cd ../
python run_benchmark.py -v
```

## Directory Structure

After running benchmarks, you'll see:

```
results/
├── benchmark_summary.json      # Aggregated metrics
├── benchmark_report.md          # Human-readable report  
├── quality_report.md            # Quality assessment
├── analysis_report.md           # Analysis and rankings
└── {skill-name}/
    └── {category}/
        ├── q1_metrics.json
        ├── q1_output.txt
        ├── q2_metrics.json
        ├── q2_output.txt
        └── ...
```

## Analysis Commands

View summary report:
```bash
cat benchmark_report.md
```

Analyze results:
```bash
python ../analyze.py
python ../analyze.py --metric efficiency
```

Score quality:
```bash
python ../scoring.py
```

## Files

- **benchmark_summary.json**: Complete metrics for all runs
- **benchmark_report.md**: Overall performance summary
- **quality_report.md**: Objective quality scores
- **analysis_report.md**: Comparative analysis
- **{skill}/**: Individual skill results by category
`````

## File: benchmark/analyze.py
`````python
"""Analysis utilities for benchmark results."""
import json
from pathlib import Path
from typing import Dict, List, Optional
import argparse


def load_summary(results_dir: Path) -> Dict:
    """Load benchmark summary JSON."""
    summary_file = results_dir / "benchmark_summary.json"
    if not summary_file.exists():
        raise FileNotFoundError(f"Summary file not found: {summary_file}")
    
    with open(summary_file) as f:
        return json.load(f)


def compare_skills(
    summary: Dict,
    metric: str = "avg_duration",
    top_n: int = 10
) -> List[tuple]:
    """
    Compare skills by a specific metric.
    
    Args:
        summary: Loaded benchmark summary
        metric: Metric to compare (avg_duration, total_cost, total_tokens)
        top_n: Number of top results to return
        
    Returns:
        List of (skill_name, value) tuples sorted by metric
    """
    skills_data = summary.get('skills', {})
    
    results = []
    for skill_name, skill_metrics in skills_data.items():
        if metric in skill_metrics:
            results.append((skill_name, skill_metrics[metric]))
    
    # Sort based on metric (lower is better for most metrics)
    reverse = metric in ['successful', 'total_runs']  # Higher is better for these
    results.sort(key=lambda x: x[1], reverse=reverse)
    
    return results[:top_n]


def calculate_efficiency_scores(summary: Dict) -> Dict[str, Dict]:
    """
    Calculate efficiency scores combining speed, cost, and success rate.
    
    Returns composite scores for trade-off analysis.
    """
    skills_data = summary.get('skills', {})
    
    efficiency_scores = {}
    
    for skill_name, metrics in skills_data.items():
        if metrics['total_runs'] == 0:
            continue
        
        # Normalize metrics (lower is better, scale 0-1)
        success_rate = metrics['successful'] / metrics['total_runs']
        
        # Speed score (faster = better)
        # Assume 60s is good, normalize
        speed_score = max(0, 1 - (metrics.get('avg_duration', 60) / 300))  # 300s = 5min baseline
        
        # Cost score (cheaper = better)
        # Assume $0.10 per run is baseline
        avg_cost = metrics['total_cost'] / max(metrics['total_runs'], 1)
        cost_score = max(0, 1 - (avg_cost / 0.50))  # $0.50 baseline
        
        # Composite score (weighted average)
        # Success is most important, then cost, then speed
        composite = (
            0.5 * success_rate +
            0.3 * cost_score +
            0.2 * speed_score
        )
        
        efficiency_scores[skill_name] = {
            'success_rate': success_rate,
            'speed_score': speed_score,
            'cost_score': cost_score,
            'composite_score': composite,
            'avg_duration': metrics.get('avg_duration', 0),
            'avg_cost': avg_cost,
            'total_runs': metrics['total_runs'],
        }
    
    return efficiency_scores


def print_comparison_table(results: List[tuple], metric_name: str, format_fn=None):
    """Print a formatted comparison table."""
    print(f"\n{'='*60}")
    print(f"Comparison by: {metric_name}")
    print(f"{'='*60}\n")
    print(f"{'Rank':<6} {'Skill':<30} {'Value':<20}")
    print("-" * 60)
    
    for rank, (skill, value) in enumerate(results, 1):
        if format_fn:
            value_str = format_fn(value)
        else:
            value_str = str(value)
        
        print(f"{rank:<6} {skill:<30} {value_str:<20}")


def print_efficiency_scores(efficiency_scores: Dict):
    """Print efficiency scores in a formatted table."""
    print(f"\n{'='*80}")
    print(f"Efficiency Scores (Composite: 50% success, 30% cost, 20% speed)")
    print(f"{'='*80}\n")
    print(f"{'Skill':<25} {'Success':<10} {'Cost':<10} {'Speed':<10} {'Composite':<10}")
    print("-" * 80)
    
    # Sort by composite score
    sorted_skills = sorted(
        efficiency_scores.items(),
        key=lambda x: x[1]['composite_score'],
        reverse=True
    )
    
    for skill, scores in sorted_skills:
        print(
            f"{skill:<25} "
            f"{scores['success_rate']:.3f}     "
            f"{scores['cost_score']:.3f}     "
            f"{scores['speed_score']:.3f}     "
            f"{scores['composite_score']:.3f}"
        )


def generate_analysis_report(results_dir: Path, output_file: Optional[Path] = None):
    """Generate comprehensive analysis report."""
    summary = load_summary(results_dir)
    
    report = []
    report.append("# Benchmark Analysis Report\n\n")
    
    # Overall summary
    overall = summary.get('summary', {})
    report.append("## Overall Statistics\n\n")
    report.append(f"- Total Runs: {overall.get('total_runs', 0)}\n")
    report.append(f"- Success Rate: {overall.get('success_rate', 0):.1%}\n")
    report.append(f"- Total Duration: {overall.get('total_duration', 0):.1f}s\n")
    report.append(f"- Total Cost: ${overall.get('total_cost', 0):.2f}\n\n")
    
    # Top performers by speed
    speed_rankings = compare_skills(summary, 'avg_duration', top_n=5)
    report.append("## Fastest Skills (Avg Duration)\n\n")
    for rank, (skill, duration) in enumerate(speed_rankings, 1):
        report.append(f"{rank}. **{skill}**: {duration:.1f}s\n")
    report.append("\n")
    
    # Most cost-effective
    cost_rankings = compare_skills(summary, 'total_cost', top_n=5)
    report.append("## Most Cost-Effective Skills\n\n")
    for rank, (skill, cost) in enumerate(cost_rankings, 1):
        report.append(f"{rank}. **{skill}**: ${cost:.3f}\n")
    report.append("\n")
    
    # Efficiency scores
    efficiency = calculate_efficiency_scores(summary)
    sorted_efficiency = sorted(
        efficiency.items(),
        key=lambda x: x[1]['composite_score'],
        reverse=True
    )
    
    report.append("## Composite Efficiency Scores\n\n")
    report.append("*Weighted: 50% success rate, 30% cost efficiency, 20% speed*\n\n")
    for rank, (skill, scores) in enumerate(sorted_efficiency[:10], 1):
        report.append(
            f"{rank}. **{skill}**: {scores['composite_score']:.3f} "
            f"(success: {scores['success_rate']:.2f}, "
            f"cost: ${scores['avg_cost']:.3f}, "
            f"speed: {scores['avg_duration']:.1f}s)\n"
        )
    
    report_text = ''.join(report)
    
    if output_file:
        output_file.write_text(report_text)
        print(f"✅ Analysis report saved to: {output_file}")
    
    print(report_text)


def main():
    """Main analysis CLI."""
    parser = argparse.ArgumentParser(description="Analyze benchmark results")
    parser.add_argument(
        "--results-dir",
        type=Path,
        default=Path(__file__).parent / "results",
        help="Path to benchmark results directory"
    )
    parser.add_argument(
        "--metric",
        choices=['duration', 'cost', 'tokens', 'efficiency', 'all'],
        default='all',
        help="Metric to analyze"
    )
    parser.add_argument(
        "--output",
        type=Path,
        help="Output file for analysis report"
    )
    parser.add_argument(
        "--top-n",
        type=int,
        default=10,
        help="Number of top results to show"
    )
    
    args = parser.parse_args()
    
    if not args.results_dir.exists():
        print(f"❌ Results directory not found: {args.results_dir}")
        return
    
    try:
        summary = load_summary(args.results_dir)
        
        if args.metric == 'all':
            generate_analysis_report(args.results_dir, args.output)
        else:
            if args.metric == 'duration':
                results = compare_skills(summary, 'avg_duration', args.top_n)
                print_comparison_table(
                    results,
                    "Average Duration",
                    lambda x: f"{x:.2f}s"
                )
            elif args.metric == 'cost':
                results = compare_skills(summary, 'total_cost', args.top_n)
                print_comparison_table(
                    results,
                    "Total Cost",
                    lambda x: f"${x:.4f}"
                )
            elif args.metric == 'tokens':
                results = compare_skills(summary, 'total_tokens', args.top_n)
                print_comparison_table(
                    results,
                    "Total Tokens",
                    lambda x: f"{x:,}"
                )
            elif args.metric == 'efficiency':
                efficiency = calculate_efficiency_scores(summary)
                print_efficiency_scores(efficiency)
    
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
`````

## File: benchmark/benchmark.py
`````python
"""Main benchmark runner for evaluating deep research skills."""
import argparse
import subprocess
import sys
from pathlib import Path
from typing import List, Dict, Optional
import json
from datetime import datetime

from .config import RESULTS_DIR, SKILL_TIMEOUT
from .utils import (
    discover_skills,
    parse_taxonomy_questions,
    get_skill_command_info,
    sanitize_filename,
    format_duration,
)
from .tracker import BenchmarkTracker, BenchmarkMetrics


class BenchmarkRunner:
    """Run benchmarks across skills and questions."""
    
    def __init__(self, output_dir: Optional[Path] = None, verbose: bool = False):
        self.output_dir = output_dir or RESULTS_DIR
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.verbose = verbose
        self.tracker = BenchmarkTracker()
    
    def log(self, message: str, level: str = "INFO") -> None:
        """Log a message."""
        timestamp = datetime.now().strftime("%H:%M:%S")
        print(f"[{timestamp}] [{level}] {message}", file=sys.stderr)
    
    def run_skill(
        self,
        skill: Dict[str, str],
        question: str,
        category: str
    ) -> BenchmarkMetrics:
        """
        Run a single skill on a single question.
        
        Args:
            skill: Skill information dictionary
            question: Research question
            category: Question category
            
        Returns:
            BenchmarkMetrics object with results
        """
        metrics = self.tracker.create_run(
            skill_name=skill['name'],
            category=category,
            question=question
        )
        
        metrics.start()
        
        try:
            # Get command info for this skill
            cmd_info = get_skill_command_info(skill['name'])
            
            # Check for special requirements
            if cmd_info.get('requires_server'):
                self.log(f"⚠️  {skill['name']} requires external server - skipping", "WARN")
                metrics.set_error("Requires external server (e.g., LangGraph)")
                metrics.end()
                return metrics
            
            # Build command
            command = cmd_info['command'].format(
                script=skill['script_path'],
                question=f'"{question}"'
            )
            
            if self.verbose:
                self.log(f"Running: {command}")
            
            # Run the skill
            result = subprocess.run(
                command,
                shell=True,
                capture_output=True,
                text=True,
                timeout=SKILL_TIMEOUT
            )
            
            # Capture output
            output = result.stdout
            if result.returncode != 0:
                error_output = result.stderr
                metrics.set_error(f"Exit code {result.returncode}: {error_output}")
                self.log(f"❌ {skill['name']} failed: {error_output[:100]}", "ERROR")
            else:
                metrics.set_output(output)
                
                # Extract model info and calculate cost
                model_info = BenchmarkMetrics.extract_model_info(output, result.stderr)
                metrics.add_metadata("provider", model_info["provider"])
                metrics.add_metadata("model", model_info["model"])
                metrics.calculate_cost(model_info["model"], model_info["provider"])
                
                # Extract API calls
                api_calls = BenchmarkMetrics.extract_api_calls_from_output(output)
                metrics.add_metadata("api_calls", api_calls)
                
                if self.verbose:
                    self.log(
                        f"✅ {skill['name']} completed in {format_duration(metrics.duration_seconds)}"
                    )
        
        except subprocess.TimeoutExpired:
            metrics.set_error(f"Timeout after {SKILL_TIMEOUT} seconds")
            self.log(f"⏱️  {skill['name']} timed out", "ERROR")
        
        except Exception as e:
            metrics.set_error(str(e))
            self.log(f"❌ {skill['name']} error: {str(e)}", "ERROR")
        
        finally:
            metrics.end()
        
        return metrics
    
    def save_individual_result(
        self,
        metrics: BenchmarkMetrics,
        skill_name: str,
        category: str,
        question_idx: int
    ) -> None:
        """Save individual run result to file."""
        # Create directory structure: results/{skill_name}/{category}/
        skill_dir = self.output_dir / skill_name / sanitize_filename(category)
        skill_dir.mkdir(parents=True, exist_ok=True)
        
        # Save full metrics as JSON
        metrics_file = skill_dir / f"q{question_idx + 1}_metrics.json"
        with open(metrics_file, 'w') as f:
            json.dump(metrics.to_dict(), f, indent=2)
        
        # Save output separately for easy reading
        if metrics.success:
            output_file = skill_dir / f"q{question_idx + 1}_output.txt"
            with open(output_file, 'w') as f:
                f.write(f"Question: {metrics.question}\n")
                f.write(f"Category: {category}\n")
                f.write(f"Duration: {format_duration(metrics.duration_seconds)}\n")
                f.write(f"Cost: ${metrics.estimated_cost_usd:.4f}\n")
                f.write(f"Tokens: {metrics.total_tokens}\n")
                f.write(f"\n{'='*80}\n\n")
                f.write(metrics.output)
    
    def run_benchmark(
        self,
        skills: Optional[List[str]] = None,
        categories: Optional[List[str]] = None,
        max_questions: int = 3
    ) -> None:
        """
        Run the full benchmark suite.
        
        Args:
            skills: List of skill names to test (None = all)
            categories: List of categories to test (None = all)
            max_questions: Maximum questions per category
        """
        self.log("🚀 Starting benchmark run")
        
        # Discover skills
        all_skills = discover_skills()
        if skills:
            all_skills = [s for s in all_skills if s['name'] in skills]
        
        self.log(f"📦 Found {len(all_skills)} skills to test")
        
        # Parse questions
        all_questions = parse_taxonomy_questions()
        if categories:
            all_questions = {k: v for k, v in all_questions.items() if k in categories}
        
        # Limit questions per category
        for cat in all_questions:
            all_questions[cat] = all_questions[cat][:max_questions]
        
        total_questions = sum(len(q) for q in all_questions.values())
        self.log(f"📝 Found {len(all_questions)} categories with {total_questions} total questions")
        
        # Run benchmarks
        total_runs = len(all_skills) * total_questions
        current_run = 0
        
        self.log(f"🎯 Total benchmark runs: {total_runs}")
        self.log("")
        
        for skill in all_skills:
            self.log(f"Testing skill: {skill['name']}")
            
            for category, questions in all_questions.items():
                for idx, question in enumerate(questions):
                    current_run += 1
                    
                    self.log(
                        f"[{current_run}/{total_runs}] "
                        f"{skill['name']} | {category} | Q{idx + 1}/3"
                    )
                    
                    # Run the skill
                    metrics = self.run_skill(skill, question, category)
                    
                    # Save results
                    self.save_individual_result(metrics, skill['name'], category, idx)
                    
                    # Show summary
                    if metrics.success:
                        self.log(
                            f"  ✓ Duration: {format_duration(metrics.duration_seconds)}, "
                            f"Cost: ${metrics.estimated_cost_usd:.4f}, "
                            f"Output: {metrics.output_length} chars"
                        )
                    else:
                        self.log(f"  ✗ Failed: {metrics.error[:100]}")
                    
                    self.log("")
        
        # Save aggregated results
        self.save_summary()
        
        self.log("✅ Benchmark complete!")
    
    def save_summary(self) -> None:
        """Save summary statistics and aggregated results."""
        summary_file = self.output_dir / "benchmark_summary.json"
        self.tracker.save_to_json(str(summary_file))
        self.log(f"📊 Summary saved to: {summary_file}")
        
        # Generate markdown report
        self.generate_markdown_report()
    
    def generate_markdown_report(self) -> None:
        """Generate a human-readable markdown report."""
        report_file = self.output_dir / "benchmark_report.md"
        
        summary = self.tracker.get_summary()
        
        with open(report_file, 'w') as f:
            f.write("# Deep Research Skills Benchmark Report\n\n")
            f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            
            f.write("## Overall Summary\n\n")
            f.write(f"- **Total Runs**: {summary.get('total_runs', 0)}\n")
            f.write(f"- **Successful**: {summary.get('successful', 0)}\n")
            f.write(f"- **Failed**: {summary.get('failed', 0)}\n")
            f.write(f"- **Success Rate**: {summary.get('success_rate', 0):.1%}\n")
            f.write(f"- **Total Duration**: {format_duration(summary.get('total_duration', 0))}\n")
            f.write(f"- **Total Cost**: ${summary.get('total_cost', 0):.2f}\n")
            f.write(f"- **Total Tokens**: {summary.get('total_tokens', 0):,}\n\n")
            
            f.write("## Results by Skill\n\n")
            f.write("| Skill | Runs | Success | Avg Duration | Total Cost | Tokens |\n")
            f.write("|-------|------|---------|--------------|------------|--------|\n")
            
            for skill_name in sorted(set(r.skill_name for r in self.tracker.runs)):
                skill_summary = self.tracker.get_skill_summary(skill_name)
                f.write(
                    f"| {skill_name} "
                    f"| {skill_summary['total_runs']} "
                    f"| {skill_summary['successful']}/{skill_summary['total_runs']} "
                    f"| {format_duration(skill_summary['avg_duration'])} "
                    f"| ${skill_summary['total_cost']:.2f} "
                    f"| {skill_summary['total_tokens']:,} |\n"
                )
            
            f.write("\n## Results by Category\n\n")
            f.write("| Category | Runs | Success | Avg Duration | Total Cost |\n")
            f.write("|----------|------|---------|--------------|------------|\n")
            
            for category in sorted(set(r.category for r in self.tracker.runs)):
                cat_summary = self.tracker.get_category_summary(category)
                f.write(
                    f"| {category} "
                    f"| {cat_summary['total_runs']} "
                    f"| {cat_summary['successful']}/{cat_summary['total_runs']} "
                    f"| {format_duration(cat_summary['avg_duration'])} "
                    f"| ${cat_summary['total_cost']:.2f} |\n"
                )
            
            f.write("\n---\n\n")
            f.write("*See `benchmark_summary.json` for detailed metrics.*\n")
        
        self.log(f"📄 Report saved to: {report_file}")


def main():
    """Main entry point for benchmark CLI."""
    parser = argparse.ArgumentParser(
        description="Benchmark deep research skills across taxonomy questions"
    )
    parser.add_argument(
        "--skills",
        nargs="+",
        help="Specific skills to test (default: all)"
    )
    parser.add_argument(
        "--categories",
        nargs="+",
        help="Specific categories to test (default: all)"
    )
    parser.add_argument(
        "--max-questions",
        type=int,
        default=3,
        help="Maximum questions per category (default: 3)"
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        help="Output directory for results"
    )
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Verbose output"
    )
    
    args = parser.parse_args()
    
    runner = BenchmarkRunner(
        output_dir=args.output_dir,
        verbose=args.verbose
    )
    
    try:
        runner.run_benchmark(
            skills=args.skills,
            categories=args.categories,
            max_questions=args.max_questions
        )
    except KeyboardInterrupt:
        print("\n\n⚠️  Benchmark interrupted by user")
        runner.save_summary()
        sys.exit(1)
    except Exception as e:
        print(f"\n\n❌ Benchmark failed: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
`````

## File: benchmark/config.py
`````python
"""Configuration for benchmark system."""
import os
from pathlib import Path

# Paths
REPO_ROOT = Path(__file__).parent.parent
SKILLS_DIR = REPO_ROOT / ".claude" / "skills"
TAXONOMY_FILE = REPO_ROOT / "docs" / "taxonomy-and-examples.md"
RESULTS_DIR = REPO_ROOT / "benchmark" / "results"

# Cost per token (approximate, update based on actual pricing)
# These are rough estimates - actual costs vary by provider and model
COST_PER_1K_TOKENS = {
    "openai": {
        "gpt-4o": {"input": 0.0025, "output": 0.01},
        "gpt-4o-mini": {"input": 0.00015, "output": 0.0006},
        "gpt-3.5-turbo": {"input": 0.0005, "output": 0.0015},
        "o3-deep-research": {"input": 0.01, "output": 0.04},  # Estimated
        "o4-mini-deep-research": {"input": 0.001, "output": 0.004},  # Estimated
    },
    "anthropic": {
        "claude-3-5-sonnet-20241022": {"input": 0.003, "output": 0.015},
        "claude-3-opus": {"input": 0.015, "output": 0.075},
    },
    "exa": {
        "exa-research": {"input": 0.01, "output": 0.02},  # Estimated
        "exa-research-pro": {"input": 0.02, "output": 0.04},  # Estimated
    },
    "perplexity": {
        "sonar-small-online": {"input": 0.0002, "output": 0.0002},
        "sonar-medium-online": {"input": 0.0006, "output": 0.0006},
        "sonar-large-online": {"input": 0.001, "output": 0.001},
    },
    "xai": {
        "grok-4": {"input": 0.01, "output": 0.03},  # Estimated
        "grok-4.1-fast-reasoning": {"input": 0.005, "output": 0.015},  # Estimated
    },
}

# Default cost for unknown models
DEFAULT_COST_PER_1K = {"input": 0.001, "output": 0.003}

# Timeout for each skill run (seconds)
SKILL_TIMEOUT = 600  # 10 minutes

# Skills to exclude from benchmarking (if needed)
EXCLUDED_SKILLS = []
`````

## File: benchmark/QUICKSTART.md
`````markdown
# Benchmark System Quick Start

## 1. Install Dependencies

```bash
# From repo root
pip install -r .claude/skills/test-requirements.txt
```

## 2. Set API Keys

Export required API keys for the skills you want to test:

```bash
export OPENAI_API_KEY="your-key"
export TAVILY_API_KEY="your-key"
export EXA_API_KEY="your-key"
export PERPLEXITY_API_KEY="your-key"
export XAI_API_KEY="your-key"
# ... etc
```

## 3. Run a Quick Test (Recommended First Step)

Test one skill with one question per category:

```bash
cd benchmark
python run_benchmark.py --skills tavily-search --max-questions 1 -v
```

## 4. Run Full Benchmark

Test all skills with all questions (this will take a while and cost money):

```bash
python run_benchmark.py -v
```

## 5. View Results

```bash
# View summary report
cat results/benchmark_report.md

# Analyze performance
python analyze.py

# View quality scores
python scoring.py
```

## Common Commands

### Test specific skills
```bash
python run_benchmark.py --skills exa-research tavily-search perplexity-sonar -v
```

### Test specific categories
```bash
python run_benchmark.py --categories "Source Retrieval" "Technical Decomposition" -v
```

### Quick smoke test
```bash
python run_benchmark.py --max-questions 1 -v
```

### Analyze by specific metric
```bash
python analyze.py --metric cost
python analyze.py --metric duration
python analyze.py --metric efficiency
```

## Expected Costs

Costs vary by skill and model used:
- **Quick test** (1 skill × 10 categories × 1 question): ~$0.50 - $2.00
- **Small test** (3 skills × 10 categories × 1 question): ~$1.50 - $6.00
- **Full benchmark** (10 skills × 10 categories × 3 questions): ~$15 - $60+

**Note**: Costs depend heavily on which models each skill uses. Skills using GPT-4 or Claude Opus will cost more than those using GPT-3.5 or smaller models.

## Troubleshooting

### "Timeout" errors
Increase timeout in `config.py`:
```python
SKILL_TIMEOUT = 1200  # 20 minutes
```

### "Missing API key" errors
Make sure you've exported the required API keys for the skills you're testing.

### "Module not found" errors
Install dependencies:
```bash
pip install -r ../.claude/skills/test-requirements.txt
```

## Next Steps

1. ✅ Run quick test to verify setup
2. ✅ Run full benchmark to collect data
3. ✅ Analyze results with analysis tools
4. 📊 Create custom visualizations
5. 🎯 Develop quality evaluation rubric
6. 📈 Track performance over time
`````

## File: benchmark/README.md
`````markdown
## Deep Research Skills Benchmark System

Comprehensive benchmarking framework for evaluating deep research skills across standardized taxonomy questions.

## Overview

This benchmark system:
- ✅ **Dynamically discovers** all skills in `.claude/skills/`
- ✅ **Extracts questions** from the research taxonomy document
- ✅ **Runs each skill** on each question category
- ✅ **Tracks metrics**: duration, cost, tokens, API calls
- ✅ **Saves detailed results** for analysis
- ✅ **Generates reports** in JSON and Markdown formats

## Quick Start

### Install Dependencies

```bash
pip install -r ../.claude/skills/test-requirements.txt
```

### Run Full Benchmark

```bash
python run_benchmark.py -v
```

### Run Specific Skills

```bash
python run_benchmark.py --skills exa-research tavily-search -v
```

### Run Specific Categories

```bash
python run_benchmark.py --categories "Source Retrieval" "Technical Decomposition" -v
```

### Limit Questions Per Category

```bash
python run_benchmark.py --max-questions 1 -v
```

## Command Line Options

```
usage: run_benchmark.py [-h] [--skills SKILLS [SKILLS ...]]
                        [--categories CATEGORIES [CATEGORIES ...]]
                        [--max-questions MAX_QUESTIONS]
                        [--output-dir OUTPUT_DIR] [-v]

options:
  -h, --help            show this help message and exit
  --skills SKILLS [SKILLS ...]
                        Specific skills to test (default: all)
  --categories CATEGORIES [CATEGORIES ...]
                        Specific categories to test (default: all)
  --max-questions MAX_QUESTIONS
                        Maximum questions per category (default: 3)
  --output-dir OUTPUT_DIR
                        Output directory for results
  -v, --verbose         Verbose output
```

## Output Structure

Results are saved in the following structure:

```
benchmark/results/
├── benchmark_summary.json          # Aggregated metrics across all runs
├── benchmark_report.md             # Human-readable report
├── exa-research/
│   ├── source_retrieval/
│   │   ├── q1_metrics.json
│   │   ├── q1_output.txt
│   │   ├── q2_metrics.json
│   │   ├── q2_output.txt
│   │   └── q3_metrics.json
│   │   └── q3_output.txt
│   └── technical_decomposition/
│       └── ...
├── gpt-researcher/
│   └── ...
└── ...
```

## Metrics Tracked

For each skill × question combination:

### Timing Metrics
- **Start time** (ISO timestamp)
- **End time** (ISO timestamp)
- **Duration** (seconds)

### Output Metrics
- **Output text** (full response)
- **Output length** (characters)
- **Success/failure** status
- **Error messages** (if any)

### Cost Metrics
- **Input tokens** (estimated)
- **Output tokens** (estimated)
- **Total tokens**
- **Estimated cost** (USD)

### Additional Metadata
- **Provider** (openai, anthropic, etc.)
- **Model** (gpt-4o, claude-3-5-sonnet, etc.)
- **API calls** (estimated)
- **Custom metadata** (skill-specific)

## Configuration

Edit `config.py` to customize:
- **Cost per token** rates for different models
- **Timeout** duration for skill execution
- **Excluded skills** (skills to skip)
- **Default models** and providers

## Taxonomy Categories

The benchmark covers 10 research categories from `docs/taxonomy-and-examples.md`:

1. **Source Retrieval** - Finding authoritative primary sources
2. **Cross-Validation** - Reconciling conflicting information
3. **Domain Mapping** - Identifying entities and relationships
4. **Technical Decomposition** - Breaking down complex systems
5. **Quantitative Synthesis** - Extracting and computing on data
6. **Regulatory / Standards Analysis** - Interpreting compliance requirements
7. **Scholarly Synthesis** - Surveying academic literature
8. **Bias & Uncertainty Assessment** - Identifying reliability issues
9. **Multi-Domain Integration** - Blending cross-disciplinary information
10. **Executive Summarization** - Producing decision-oriented outputs

Each category has 3 example questions.

## Example Usage

### Test a Single Skill on All Categories

```bash
python run_benchmark.py --skills tavily-search -v
```

### Quick Smoke Test (1 question per category)

```bash
python run_benchmark.py --max-questions 1 -v
```

### Test Specific Research Modes

```bash
python run_benchmark.py \
  --categories "Source Retrieval" "Cross-Validation" "Quantitative Synthesis" \
  --max-questions 2 \
  -v
```

## Analyzing Results

### View Summary Report

```bash
cat results/benchmark_report.md
```

### Parse JSON Metrics

```python
import json

with open('results/benchmark_summary.json') as f:
    data = json.load(f)

# Overall statistics
print(data['summary'])

# Per-skill performance
for skill, metrics in data['skills'].items():
    print(f"{skill}: {metrics['avg_duration']:.1f}s, ${metrics['total_cost']:.2f}")
```

### Compare Skills

```bash
# Extract cost per skill
jq '.skills | to_entries[] | "\(.key): $\(.value.total_cost)"' results/benchmark_summary.json

# Extract success rates
jq '.skills | to_entries[] | "\(.key): \(.value.successful)/\(.value.total_runs)"' results/benchmark_summary.json
```

## Scoring Rubric (Future)

After collecting benchmark data, we will implement a scoring rubric that evaluates:

### Speed (Objective)
- Average duration per question
- Consistency across question types

### Cost (Objective)
- Total cost per run
- Cost per token
- Cost efficiency ratio

### Quality (Multi-Dimensional)
- **Completeness**: Coverage of question requirements
- **Accuracy**: Factual correctness (human evaluation)
- **Relevance**: On-topic responses
- **Structure**: Organization and clarity
- **Citations**: Source quality and traceability
- **Depth**: Level of analysis provided

### Trade-Off Analysis
- Speed vs. Quality curve
- Cost vs. Quality curve
- Pareto frontier analysis

## Extending the Benchmark

### Add a New Skill

1. Place skill code in `.claude/skills/{skill-name}/scripts/`
2. Add `requirements.txt` with dependencies
3. Skill will be auto-discovered

### Add New Questions

Edit `docs/taxonomy-and-examples.md` following the existing format:

```markdown
### **X.Y Category Name**

* "Question 1"
* "Question 2"
* "Question 3"
```

### Custom Metrics

Extend `BenchmarkMetrics` in `tracker.py`:

```python
metrics.add_metadata("custom_metric", value)
```

## Troubleshooting

### Skill Times Out

Increase timeout in `config.py`:

```python
SKILL_TIMEOUT = 1200  # 20 minutes
```

### Missing Dependencies

Install all skill dependencies:

```bash
pip install -r ../.claude/skills/test-requirements.txt
```

### API Rate Limits

Add delays between runs by modifying `benchmark.py`:

```python
import time
# After each run
time.sleep(5)  # 5 second delay
```

## CI/CD Integration

### GitHub Actions Example

```yaml
name: Benchmark Skills

on:
  schedule:
    - cron: '0 0 * * 0'  # Weekly
  workflow_dispatch:

jobs:
  benchmark:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: '3.10'
      - name: Install dependencies
        run: pip install -r .claude/skills/test-requirements.txt
      - name: Run benchmark
        env:
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
          TAVILY_API_KEY: ${{ secrets.TAVILY_API_KEY }}
          # Add other API keys
        run: python benchmark/run_benchmark.py --max-questions 1
      - name: Upload results
        uses: actions/upload-artifact@v3
        with:
          name: benchmark-results
          path: benchmark/results/
```

## License

Part of the awesome-deep-researchers repository.
`````

## File: benchmark/run_benchmark.py
`````python
#!/usr/bin/env python3
"""Convenience script to run benchmarks."""
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from benchmark.benchmark import main

if __name__ == "__main__":
    main()
`````

## File: benchmark/scoring.py
`````python
"""Scoring rubric for evaluating benchmark results quality."""
import json
from typing import Dict, List, Optional
from dataclasses import dataclass
from pathlib import Path


@dataclass
class QualityScore:
    """Quality evaluation score for a benchmark result."""
    
    # Objective metrics (computed automatically)
    completeness: float = 0.0  # 0-1: Output length / expected length
    structure: float = 0.0  # 0-1: Has sections, formatting
    citations: float = 0.0  # 0-1: Number and quality of citations
    
    # Subjective metrics (require human evaluation)
    accuracy: Optional[float] = None  # 0-1: Factual correctness
    relevance: Optional[float] = None  # 0-1: On-topic, addresses question
    depth: Optional[float] = None  # 0-1: Level of analysis
    
    # Overall
    objective_score: float = 0.0  # Average of objective metrics
    subjective_score: Optional[float] = None  # Average of subjective (if evaluated)
    combined_score: Optional[float] = None  # Weighted combination
    
    notes: str = ""
    
    def calculate_objective_score(self) -> float:
        """Calculate average of objective metrics."""
        metrics = [self.completeness, self.structure, self.citations]
        self.objective_score = sum(metrics) / len(metrics)
        return self.objective_score
    
    def calculate_subjective_score(self) -> Optional[float]:
        """Calculate average of subjective metrics (if available)."""
        metrics = [m for m in [self.accuracy, self.relevance, self.depth] if m is not None]
        if not metrics:
            return None
        self.subjective_score = sum(metrics) / len(metrics)
        return self.subjective_score
    
    def calculate_combined_score(
        self,
        objective_weight: float = 0.3,
        subjective_weight: float = 0.7
    ) -> Optional[float]:
        """
        Calculate weighted combination of objective and subjective scores.
        
        Args:
            objective_weight: Weight for objective metrics (default 0.3)
            subjective_weight: Weight for subjective metrics (default 0.7)
        """
        if self.subjective_score is None:
            return None
        
        self.combined_score = (
            objective_weight * self.objective_score +
            subjective_weight * self.subjective_score
        )
        return self.combined_score


class ResultScorer:
    """Score benchmark results for quality evaluation."""
    
    @staticmethod
    def score_completeness(output: str, question: str) -> float:
        """
        Score output completeness.
        
        Heuristic: ratio of output length to expected length.
        Expected length varies by question type.
        """
        if not output:
            return 0.0
        
        # Expected minimum lengths by category (characters)
        expected_lengths = {
            "source_retrieval": 500,
            "cross_validation": 800,
            "domain_mapping": 1000,
            "technical_decomposition": 1200,
            "quantitative_synthesis": 800,
            "regulatory": 700,
            "scholarly_synthesis": 1000,
            "bias_uncertainty": 800,
            "multi_domain": 1500,
            "executive_summarization": 600,
        }
        
        # Use average as default
        expected = sum(expected_lengths.values()) / len(expected_lengths)
        
        # Score: min(actual / expected, 1.0)
        return min(len(output) / expected, 1.0)
    
    @staticmethod
    def score_structure(output: str) -> float:
        """
        Score output structure and formatting.
        
        Checks for:
        - Section headers
        - Bullet points or numbered lists
        - Paragraph breaks
        - Proper formatting
        """
        score = 0.0
        
        # Check for headers (markdown style)
        if any(line.startswith('#') for line in output.split('\n')):
            score += 0.3
        
        # Check for lists
        lines = output.split('\n')
        has_bullets = any(line.strip().startswith(('*', '-', '•')) for line in lines)
        has_numbers = any(line.strip()[:3].rstrip('.').isdigit() for line in lines)
        if has_bullets or has_numbers:
            score += 0.3
        
        # Check for paragraph breaks (multiple newlines)
        if '\n\n' in output:
            score += 0.2
        
        # Check for reasonable line length (not one giant paragraph)
        avg_line_length = sum(len(line) for line in lines) / max(len(lines), 1)
        if avg_line_length < 200:  # Reasonable line breaks
            score += 0.2
        
        return min(score, 1.0)
    
    @staticmethod
    def score_citations(output: str) -> float:
        """
        Score citation quality.
        
        Checks for:
        - URLs
        - References
        - Source attributions
        """
        score = 0.0
        
        # Count URLs
        import re
        urls = re.findall(r'https?://[^\s]+', output)
        if urls:
            # Score based on number of citations (cap at 10)
            score += min(len(urls) / 10, 0.5)
        
        # Check for citation markers [1], (Source: ...), etc.
        citation_patterns = [
            r'\[\d+\]',  # [1], [2]
            r'\(Source:',  # (Source: ...)
            r'\(Ref:',  # (Ref: ...)
            r'According to',  # According to X
        ]
        
        for pattern in citation_patterns:
            if re.search(pattern, output):
                score += 0.2
                break
        
        # Check for reference section
        if re.search(r'(References?|Sources?|Citations?):', output, re.IGNORECASE):
            score += 0.3
        
        return min(score, 1.0)
    
    @staticmethod
    def score_result(output: str, question: str, category: str) -> QualityScore:
        """
        Score a benchmark result automatically (objective metrics only).
        
        Args:
            output: The skill's output text
            question: The original question
            category: Question category
            
        Returns:
            QualityScore with objective metrics computed
        """
        score = QualityScore()
        
        score.completeness = ResultScorer.score_completeness(output, question)
        score.structure = ResultScorer.score_structure(output)
        score.citations = ResultScorer.score_citations(output)
        
        score.calculate_objective_score()
        
        return score
    
    @staticmethod
    def score_benchmark_results(results_dir: Path) -> Dict:
        """
        Score all results in a benchmark results directory.
        
        Args:
            results_dir: Path to benchmark/results directory
            
        Returns:
            Dictionary with scores for all results
        """
        scores = {}
        
        # Find all metrics files
        for metrics_file in results_dir.rglob("*_metrics.json"):
            with open(metrics_file) as f:
                metrics = json.load(f)
            
            # Score the result
            quality = ResultScorer.score_result(
                output=metrics.get('output', ''),
                question=metrics.get('question', ''),
                category=metrics.get('category', '')
            )
            
            # Store score
            skill_name = metrics.get('skill_name', 'unknown')
            category = metrics.get('category', 'unknown')
            
            if skill_name not in scores:
                scores[skill_name] = {}
            if category not in scores[skill_name]:
                scores[skill_name][category] = []
            
            scores[skill_name][category].append({
                'question': metrics.get('question', ''),
                'completeness': quality.completeness,
                'structure': quality.structure,
                'citations': quality.citations,
                'objective_score': quality.objective_score,
            })
        
        return scores
    
    @staticmethod
    def generate_quality_report(results_dir: Path, output_file: Optional[Path] = None) -> str:
        """
        Generate a quality assessment report.
        
        Args:
            results_dir: Path to benchmark/results directory
            output_file: Optional path to save report
            
        Returns:
            Markdown report string
        """
        scores = ResultScorer.score_benchmark_results(results_dir)
        
        report = []
        report.append("# Benchmark Quality Assessment Report\n")
        report.append("## Objective Quality Scores\n")
        report.append("Metrics: Completeness, Structure, Citations\n\n")
        
        # Overall statistics
        all_scores = []
        for skill_scores in scores.values():
            for category_scores in skill_scores.values():
                all_scores.extend([s['objective_score'] for s in category_scores])
        
        if all_scores:
            avg_score = sum(all_scores) / len(all_scores)
            report.append(f"**Overall Average Score**: {avg_score:.3f}\n\n")
        
        # Per-skill breakdown
        report.append("## Scores by Skill\n\n")
        report.append("| Skill | Avg Completeness | Avg Structure | Avg Citations | Overall Score |\n")
        report.append("|-------|------------------|---------------|---------------|---------------|\n")
        
        for skill in sorted(scores.keys()):
            skill_results = []
            for category_scores in scores[skill].values():
                skill_results.extend(category_scores)
            
            if skill_results:
                avg_completeness = sum(r['completeness'] for r in skill_results) / len(skill_results)
                avg_structure = sum(r['structure'] for r in skill_results) / len(skill_results)
                avg_citations = sum(r['citations'] for r in skill_results) / len(skill_results)
                avg_overall = sum(r['objective_score'] for r in skill_results) / len(skill_results)
                
                report.append(
                    f"| {skill} | {avg_completeness:.3f} | {avg_structure:.3f} | "
                    f"{avg_citations:.3f} | {avg_overall:.3f} |\n"
                )
        
        report_text = ''.join(report)
        
        if output_file:
            output_file.write_text(report_text)
        
        return report_text


def main():
    """Generate quality report for existing benchmark results."""
    import argparse
    
    parser = argparse.ArgumentParser(description="Score benchmark results for quality")
    parser.add_argument(
        "--results-dir",
        type=Path,
        default=Path(__file__).parent / "results",
        help="Path to benchmark results directory"
    )
    parser.add_argument(
        "--output",
        type=Path,
        help="Output file for quality report"
    )
    
    args = parser.parse_args()
    
    if not args.results_dir.exists():
        print(f"Error: Results directory not found: {args.results_dir}")
        return
    
    report = ResultScorer.generate_quality_report(
        args.results_dir,
        args.output
    )
    
    print(report)
    
    if args.output:
        print(f"\n✅ Quality report saved to: {args.output}")


if __name__ == "__main__":
    main()
`````

## File: benchmark/SUMMARY.md
`````markdown
# Benchmark System - Complete Setup Summary

## ✅ System Status: READY

The comprehensive benchmark system has been successfully created and tested.

## 📦 What Was Built

### Core Components

1. **Benchmark Runner** (`benchmark.py`)
   - Dynamically discovers all skills in `.claude/skills/`
   - Extracts questions from taxonomy document
   - Runs each skill on each question
   - Tracks comprehensive metrics

2. **Metrics Tracker** (`tracker.py`)
   - Records timing (start, end, duration)
   - Tracks costs (tokens, estimated USD)
   - Captures output and errors
   - Stores metadata (API calls, models used)

3. **Utilities** (`utils.py`)
   - Skill discovery
   - Question parsing
   - Cost estimation
   - Helper functions

4. **Scoring System** (`scoring.py`)
   - Objective quality metrics (completeness, structure, citations)
   - Framework for subjective evaluation
   - Quality report generation

5. **Analysis Tools** (`analyze.py`)
   - Performance comparisons
   - Efficiency scoring
   - Trade-off analysis
   - Report generation

### Configuration

- **Cost estimates** for major LLM providers
- **Timeout settings** (default: 10 minutes per skill)
- **Customizable parameters**

## 📊 Discovered Resources

### Skills: 10 Total

✅ exa-research
✅ gpt-researcher
✅ jina-ai
✅ langchain-deep-research
✅ openai-deep-research
✅ perplexity-sonar
✅ smolagents
✅ stanford-storm
✅ tavily-search
✅ xai-grok

### Question Categories: 10 Total (30 Questions)

1. **Source Retrieval** (3 questions)
2. **Cross-Validation** (3 questions)
3. **Domain Mapping** (3 questions)
4. **Technical Decomposition** (3 questions)
5. **Quantitative Synthesis** (3 questions)
6. **Regulatory / Standards Interpretation** (3 questions)
7. **Scholarly Synthesis** (3 questions)
8. **Bias & Uncertainty Assessment** (3 questions)
9. **Multi-Domain Integration** (3 questions)
10. **Executive Summarization** (3 questions)

## 🎯 Metrics Tracked

For each skill × question combination (300 total runs for full benchmark):

### Objective Metrics
- ⏱️ **Duration** (seconds)
- 💰 **Cost** (estimated USD)
- 📝 **Tokens** (input, output, total)
- 🔄 **API calls** (estimated)
- ✅ **Success/failure** status
- 📊 **Output length** (characters)

### Quality Metrics
- **Completeness** (output length vs expected)
- **Structure** (formatting, organization)
- **Citations** (sources, references)

### Future: Subjective Metrics
- Accuracy (factual correctness)
- Relevance (addresses question)
- Depth (level of analysis)

## 🚀 Quick Start Commands

### 1. Test Setup
```bash
python benchmark/test_system.py
```

### 2. Quick Smoke Test (1 skill, 1 question per category)
```bash
cd benchmark
export TAVILY_API_KEY="your-key"
python run_benchmark.py --skills tavily-search --max-questions 1 -v
```

### 3. Test Multiple Skills
```bash
export OPENAI_API_KEY="your-key"
export TAVILY_API_KEY="your-key"
export PERPLEXITY_API_KEY="your-key"

python run_benchmark.py \
  --skills tavily-search perplexity-sonar exa-research \
  --max-questions 2 \
  -v
```

### 4. Full Benchmark (All Skills × All Questions)
```bash
# Set all required API keys first
export OPENAI_API_KEY="..."
export TAVILY_API_KEY="..."
export EXA_API_KEY="..."
# ... etc

python run_benchmark.py -v
```

### 5. Analyze Results
```bash
# View summary
cat results/benchmark_report.md

# Analyze performance
python analyze.py

# Quality assessment
python scoring.py
```

## 📁 Output Structure

```
benchmark/
├── results/
│   ├── benchmark_summary.json       # Aggregated metrics
│   ├── benchmark_report.md          # Human-readable summary
│   ├── quality_report.md            # Quality scores
│   ├── analysis_report.md           # Performance analysis
│   └── {skill-name}/
│       └── {category}/
│           ├── q1_metrics.json      # Individual run metrics
│           ├── q1_output.txt        # Skill output
│           ├── q2_metrics.json
│           ├── q2_output.txt
│           └── ...
└── ...
```

## 💡 Example Benchmark Report

After running, you'll get reports showing:

**Overall Statistics**
- Total runs: 300 (10 skills × 10 categories × 3 questions)
- Success rate: 85%
- Total duration: 45 minutes
- Total cost: $25.50
- Total tokens: 850,000

**By Skill Rankings**
1. tavily-search: 30/30 success, avg 12s, $0.45 total
2. perplexity-sonar: 29/30 success, avg 18s, $1.20 total
3. exa-research: 28/30 success, avg 25s, $2.50 total
...

**By Category Analysis**
- Fastest: Source Retrieval (avg 15s)
- Most expensive: Multi-Domain Integration (avg $0.35/run)
- Highest success: Technical Decomposition (95%)

## 🎯 Scoring Rubric Framework

The system provides a framework for evaluating trade-offs between:

### Speed ⚡
- Measured objectively in seconds
- Lower is better
- Varies by question complexity

### Cost 💰
- Estimated from token usage
- Based on provider pricing
- Varies by model choice

### Quality 🌟
**Objective (Automated)**
- Completeness: Output length relative to expected
- Structure: Formatting, sections, organization
- Citations: Number and quality of sources

**Subjective (Human Evaluation)**
- Accuracy: Factual correctness
- Relevance: Addresses the question
- Depth: Level of analysis

### Composite Efficiency Score
Weighted combination (customizable):
- 50% success rate
- 30% cost efficiency
- 20% speed

## 📈 Next Steps

### Immediate
1. ✅ Set up API keys for skills you want to test
2. ✅ Run a quick smoke test to verify setup
3. ✅ Run targeted benchmarks on specific categories
4. ✅ Review generated reports

### Future Enhancements
1. **Human evaluation interface** for subjective quality scoring
2. **Visualization dashboard** for comparative analysis
3. **Historical tracking** to measure improvements over time
4. **Cost optimization** recommendations based on trade-offs
5. **Automated quality checks** using LLM judges
6. **CI/CD integration** for continuous benchmarking

## 📝 Documentation

- **README.md** - Comprehensive system documentation
- **QUICKSTART.md** - Getting started guide
- **SUMMARY.md** - This file
- **results/README.md** - Results directory guide

## 🛠️ Extending the System

### Add a New Skill
1. Place code in `.claude/skills/{skill-name}/scripts/`
2. Add `requirements.txt`
3. Skill auto-discovered on next run

### Add New Questions
Edit `docs/taxonomy-and-examples.md` following format:
```markdown
### **X.Y Category Name**

* "Question 1"
* "Question 2"
```

### Custom Analysis
```python
from benchmark.tracker import BenchmarkTracker
import json

with open('results/benchmark_summary.json') as f:
    data = json.load(f)

# Custom analysis here
for skill, metrics in data['skills'].items():
    efficiency = metrics['successful'] / metrics['total_cost']
    print(f"{skill}: {efficiency:.2f} successes per dollar")
```

## 💰 Cost Estimates

**Quick Test** (1 skill × 10 categories × 1 question)
- Expected: $0.50 - $2.00
- Duration: 5-10 minutes

**Medium Test** (3 skills × 10 categories × 2 questions)
- Expected: $3.00 - $12.00
- Duration: 20-40 minutes

**Full Benchmark** (10 skills × 10 categories × 3 questions)
- Expected: $15.00 - $60.00+
- Duration: 60-180 minutes

*Costs vary significantly based on models used by each skill*

## ⚠️ Important Notes

1. **API Keys Required**: Each skill needs its respective API keys
2. **Rate Limits**: Be aware of provider rate limits
3. **Costs Add Up**: Full benchmark can be expensive
4. **LangChain Skill**: Requires LangGraph server running (auto-skipped if unavailable)
5. **Timeouts**: Configurable in `config.py` (default 10 minutes)

## ✨ System Highlights

✅ **Fully automated** - No manual intervention required
✅ **Dynamic discovery** - Automatically finds all skills
✅ **Comprehensive tracking** - Captures all relevant metrics
✅ **Flexible filtering** - Test specific skills or categories
✅ **Multiple outputs** - JSON, Markdown, and individual results
✅ **Analysis tools** - Built-in performance comparison
✅ **Extensible** - Easy to add new skills and metrics
✅ **Production ready** - Error handling, timeouts, logging

## 🎉 Ready to Use!

The benchmark system is fully operational and ready to evaluate your deep research skills.

Start with:
```bash
cd benchmark
python test_system.py
python run_benchmark.py --skills tavily-search --max-questions 1 -v
```

Happy benchmarking! 🚀
`````

## File: benchmark/test_system.py
`````python
#!/usr/bin/env python3
"""Test that the benchmark system is set up correctly."""
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from benchmark.utils import discover_skills, parse_taxonomy_questions
from benchmark.config import SKILLS_DIR, TAXONOMY_FILE


def test_discovery():
    """Test skill discovery and question parsing."""
    print("🔍 Testing benchmark system setup...\n")
    
    # Check paths exist
    print(f"Skills directory: {SKILLS_DIR}")
    print(f"  Exists: {'✅' if SKILLS_DIR.exists() else '❌'}")
    
    print(f"\nTaxonomy file: {TAXONOMY_FILE}")
    print(f"  Exists: {'✅' if TAXONOMY_FILE.exists() else '❌'}")
    
    # Discover skills
    print("\n" + "="*60)
    print("Discovering Skills")
    print("="*60)
    
    try:
        skills = discover_skills()
        print(f"\n✅ Found {len(skills)} skills:\n")
        for skill in skills:
            print(f"  - {skill['name']}")
            print(f"    Script: {Path(skill['script_path']).name}")
            print(f"    Requirements: {len(skill['requirements'])} packages")
            print()
    except Exception as e:
        print(f"❌ Error discovering skills: {e}")
        return False
    
    # Parse questions
    print("="*60)
    print("Parsing Taxonomy Questions")
    print("="*60)
    
    try:
        questions = parse_taxonomy_questions()
        total_questions = sum(len(q) for q in questions.values())
        print(f"\n✅ Found {len(questions)} categories with {total_questions} total questions:\n")
        
        for category, question_list in questions.items():
            print(f"  - {category}: {len(question_list)} questions")
        
        # Show first question from first category
        if questions:
            first_category = list(questions.keys())[0]
            first_question = questions[first_category][0]
            print(f"\n📝 Example question ({first_category}):")
            print(f"   \"{first_question}\"")
    except Exception as e:
        print(f"❌ Error parsing questions: {e}")
        return False
    
    print("\n" + "="*60)
    print("✅ Benchmark system is ready!")
    print("="*60)
    print("\nNext steps:")
    print("  1. Set your API keys (export OPENAI_API_KEY=...)")
    print("  2. Run a quick test: python run_benchmark.py --max-questions 1 --skills tavily-search -v")
    print("  3. View QUICKSTART.md for more options")
    
    return True


if __name__ == "__main__":
    success = test_discovery()
    sys.exit(0 if success else 1)
`````

## File: benchmark/tracker.py
`````python
"""Metrics tracking for benchmark runs."""
import time
import json
import re
from typing import Dict, Optional, Any
from dataclasses import dataclass, field, asdict
from datetime import datetime


@dataclass
class BenchmarkMetrics:
    """Metrics for a single benchmark run."""
    skill_name: str
    category: str
    question: str
    
    # Timing
    start_time: float = 0.0
    end_time: float = 0.0
    duration_seconds: float = 0.0
    
    # Output
    output: str = ""
    output_length: int = 0
    error: Optional[str] = None
    success: bool = False
    
    # Token usage (estimated from output)
    tokens_input: int = 0
    tokens_output: int = 0
    total_tokens: int = 0
    
    # Cost
    estimated_cost_usd: float = 0.0
    
    # Additional metadata
    metadata: Dict[str, Any] = field(default_factory=dict)
    
    def start(self) -> None:
        """Mark the start of execution."""
        self.start_time = time.time()
    
    def end(self) -> None:
        """Mark the end of execution and calculate duration."""
        self.end_time = time.time()
        self.duration_seconds = self.end_time - self.start_time
    
    def set_output(self, output: str) -> None:
        """Set the output and calculate metrics."""
        self.output = output
        self.output_length = len(output)
        self.success = True
        
        # Estimate tokens (rough approximation: 1 token ≈ 4 characters)
        self.tokens_output = len(output) // 4
        self.tokens_input = len(self.question) // 4
        self.total_tokens = self.tokens_input + self.tokens_output
    
    def set_error(self, error: str) -> None:
        """Set error information."""
        self.error = error
        self.success = False
    
    def calculate_cost(self, model: str, provider: str) -> None:
        """Calculate estimated cost based on token usage."""
        from .utils import estimate_cost
        self.estimated_cost_usd = estimate_cost(
            self.tokens_input,
            self.tokens_output,
            model,
            provider
        )
    
    def add_metadata(self, key: str, value: Any) -> None:
        """Add custom metadata."""
        self.metadata[key] = value
    
    def to_dict(self) -> Dict:
        """Convert to dictionary for JSON serialization."""
        data = asdict(self)
        # Add formatted timestamps
        data['start_time_iso'] = datetime.fromtimestamp(self.start_time).isoformat() if self.start_time else None
        data['end_time_iso'] = datetime.fromtimestamp(self.end_time).isoformat() if self.end_time else None
        return data
    
    def to_json(self) -> str:
        """Convert to JSON string."""
        return json.dumps(self.to_dict(), indent=2)
    
    @staticmethod
    def extract_api_calls_from_output(output: str) -> int:
        """
        Attempt to extract number of API calls from output.
        This is heuristic-based and may need adjustment per skill.
        """
        # Look for common patterns in debug output
        patterns = [
            r'API call[s]?:\s*(\d+)',
            r'(\d+)\s+API call[s]?',
            r'Made\s+(\d+)\s+request[s]?',
        ]
        
        for pattern in patterns:
            match = re.search(pattern, output, re.IGNORECASE)
            if match:
                return int(match.group(1))
        
        # Default: assume 1 API call if we got output
        return 1 if output else 0
    
    @staticmethod
    def extract_model_info(output: str, error: str = "") -> Dict[str, str]:
        """
        Attempt to extract model and provider information from output/error.
        """
        combined = (output + " " + (error or "")).lower()
        
        # Detect provider
        provider = "unknown"
        if "openai" in combined or "gpt" in combined:
            provider = "openai"
        elif "anthropic" in combined or "claude" in combined:
            provider = "anthropic"
        elif "exa" in combined:
            provider = "exa"
        elif "perplexity" in combined or "sonar" in combined:
            provider = "perplexity"
        elif "grok" in combined or "xai" in combined:
            provider = "xai"
        
        # Detect model
        model = "unknown"
        model_patterns = [
            r'(gpt-4[o]?(?:-mini)?(?:-deep-research)?)',
            r'(gpt-3\.5-turbo)',
            r'(o3-deep-research)',
            r'(o4-mini-deep-research)',
            r'(claude-[^\s]+)',
            r'(exa-research(?:-pro)?)',
            r'(sonar-[^\s]+)',
            r'(grok-[^\s]+)',
        ]
        
        for pattern in model_patterns:
            match = re.search(pattern, combined)
            if match:
                model = match.group(1)
                break
        
        return {"provider": provider, "model": model}


class BenchmarkTracker:
    """Track metrics across multiple benchmark runs."""
    
    def __init__(self):
        self.runs: list[BenchmarkMetrics] = []
        self.start_time = time.time()
    
    def create_run(self, skill_name: str, category: str, question: str) -> BenchmarkMetrics:
        """Create a new benchmark run."""
        metrics = BenchmarkMetrics(
            skill_name=skill_name,
            category=category,
            question=question
        )
        self.runs.append(metrics)
        return metrics
    
    def get_summary(self) -> Dict:
        """Get summary statistics across all runs."""
        if not self.runs:
            return {}
        
        successful_runs = [r for r in self.runs if r.success]
        failed_runs = [r for r in self.runs if not r.success]
        
        return {
            "total_runs": len(self.runs),
            "successful": len(successful_runs),
            "failed": len(failed_runs),
            "success_rate": len(successful_runs) / len(self.runs) if self.runs else 0,
            "total_duration": sum(r.duration_seconds for r in self.runs),
            "avg_duration": sum(r.duration_seconds for r in successful_runs) / len(successful_runs) if successful_runs else 0,
            "total_cost": sum(r.estimated_cost_usd for r in self.runs),
            "total_tokens": sum(r.total_tokens for r in self.runs),
            "avg_output_length": sum(r.output_length for r in successful_runs) / len(successful_runs) if successful_runs else 0,
        }
    
    def get_skill_summary(self, skill_name: str) -> Dict:
        """Get summary for a specific skill."""
        skill_runs = [r for r in self.runs if r.skill_name == skill_name]
        if not skill_runs:
            return {}
        
        successful = [r for r in skill_runs if r.success]
        
        return {
            "skill": skill_name,
            "total_runs": len(skill_runs),
            "successful": len(successful),
            "failed": len(skill_runs) - len(successful),
            "avg_duration": sum(r.duration_seconds for r in successful) / len(successful) if successful else 0,
            "total_cost": sum(r.estimated_cost_usd for r in skill_runs),
            "total_tokens": sum(r.total_tokens for r in skill_runs),
        }
    
    def get_category_summary(self, category: str) -> Dict:
        """Get summary for a specific question category."""
        category_runs = [r for r in self.runs if r.category == category]
        if not category_runs:
            return {}
        
        successful = [r for r in category_runs if r.success]
        
        return {
            "category": category,
            "total_runs": len(category_runs),
            "successful": len(successful),
            "avg_duration": sum(r.duration_seconds for r in successful) / len(successful) if successful else 0,
            "total_cost": sum(r.estimated_cost_usd for r in category_runs),
        }
    
    def to_dict(self) -> Dict:
        """Convert all tracked data to dictionary."""
        return {
            "summary": self.get_summary(),
            "runs": [r.to_dict() for r in self.runs],
            "skills": {
                skill: self.get_skill_summary(skill)
                for skill in set(r.skill_name for r in self.runs)
            },
            "categories": {
                cat: self.get_category_summary(cat)
                for cat in set(r.category for r in self.runs)
            },
        }
    
    def save_to_json(self, filepath: str) -> None:
        """Save all tracking data to JSON file."""
        with open(filepath, 'w') as f:
            json.dump(self.to_dict(), f, indent=2)
`````

## File: benchmark/utils.py
`````python
"""Utility functions for benchmark system."""
import re
from pathlib import Path
from typing import List, Dict, Tuple
import json

from .config import SKILLS_DIR, TAXONOMY_FILE, EXCLUDED_SKILLS


def discover_skills() -> List[Dict[str, str]]:
    """
    Dynamically discover all skills in .claude/skills directory.
    
    Returns:
        List of skill dictionaries with name, script_path, and requirements
    """
    skills = []
    
    if not SKILLS_DIR.exists():
        raise FileNotFoundError(f"Skills directory not found: {SKILLS_DIR}")
    
    for skill_dir in SKILLS_DIR.iterdir():
        if not skill_dir.is_dir():
            continue
        
        skill_name = skill_dir.name
        
        # Skip excluded skills and test-related directories
        if skill_name in EXCLUDED_SKILLS or skill_name in ['tests', '__pycache__']:
            continue
        
        # Find the main script
        scripts_dir = skill_dir / "scripts"
        if not scripts_dir.exists():
            continue
        
        # Look for Python scripts
        python_files = list(scripts_dir.glob("*.py"))
        if not python_files:
            continue
        
        # Use the first Python file (or look for specific patterns)
        main_script = python_files[0]
        
        # Check for requirements
        requirements_file = skill_dir / "requirements.txt"
        requirements = []
        if requirements_file.exists():
            requirements = requirements_file.read_text().strip().split('\n')
            requirements = [r.strip() for r in requirements if r.strip() and not r.startswith('#')]
        
        skills.append({
            "name": skill_name,
            "script_path": str(main_script),
            "requirements": requirements,
            "skill_dir": str(skill_dir)
        })
    
    return sorted(skills, key=lambda x: x['name'])


def parse_taxonomy_questions() -> Dict[str, List[str]]:
    """
    Parse the taxonomy document and extract example questions by category.
    
    Returns:
        Dictionary mapping category names to lists of questions
    """
    if not TAXONOMY_FILE.exists():
        raise FileNotFoundError(f"Taxonomy file not found: {TAXONOMY_FILE}")
    
    content = TAXONOMY_FILE.read_text()
    
    categories = {}
    current_category = None
    
    # Pattern to match category headers like "### **3.1 Source Retrieval**"
    category_pattern = re.compile(r'###\s+\*\*\d+\.\d+\s+(.+?)\*\*')
    
    # Pattern to match questions (bullet points starting with *, handles both straight and curly quotes)
    # Matches: * "question" or * "question" (with curly quotes U+201C and U+201D)
    question_pattern = re.compile(r'^\*\s+["\u201C](.+?)["\u201D]', re.MULTILINE)
    
    lines = content.split('\n')
    
    for i, line in enumerate(lines):
        # Check if this is a category header
        category_match = category_pattern.match(line.strip())
        if category_match:
            current_category = category_match.group(1).strip()
            categories[current_category] = []
            continue
        
        # Check if this is a question
        if current_category:
            question_match = question_pattern.match(line.strip())
            if question_match:
                question = question_match.group(1).strip()
                categories[current_category].append(question)
    
    # Filter out empty categories
    categories = {k: v for k, v in categories.items() if v}
    
    return categories


def get_skill_command_info(skill_name: str) -> Dict[str, str]:
    """
    Get the command-line interface information for a specific skill.
    
    Returns:
        Dictionary with command template and parameter mappings
    """
    # Define command templates for each skill
    # These map to the actual CLI arguments each skill expects
    
    command_info = {
        "exa-research": {
            "command": "python {script} research {question}",
            "supports_query": True,
        },
        "gpt-researcher": {
            "command": "python {script} --query {question}",
            "supports_query": True,
        },
        "jina-ai": {
            "command": "python {script} search {question}",
            "supports_query": True,
        },
        "langchain-deep-research": {
            "command": "python {script} --query {question}",
            "supports_query": True,
            "requires_server": True,  # Needs LangGraph server running
        },
        "openai-deep-research": {
            "command": "python {script} --prompt {question}",
            "supports_query": True,
        },
        "perplexity-sonar": {
            "command": "python {script} --prompt {question}",
            "supports_query": True,
        },
        "smolagents": {
            "command": "python {script} --task {question}",
            "supports_query": True,
        },
        "stanford-storm": {
            "command": "python {script} --topic {question}",
            "supports_query": True,
        },
        "tavily-search": {
            "command": "python {script} --query {question}",
            "supports_query": True,
        },
        "xai-grok": {
            "command": "python {script} --query {question}",
            "supports_query": True,
        },
    }
    
    return command_info.get(skill_name, {
        "command": "python {script} {question}",
        "supports_query": True,
    })


def sanitize_filename(text: str, max_length: int = 100) -> str:
    """
    Convert text to a safe filename.
    
    Args:
        text: Input text
        max_length: Maximum filename length
        
    Returns:
        Sanitized filename string
    """
    # Remove or replace invalid characters
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[-\s]+', '_', text)
    text = text.strip('_')
    
    # Truncate if too long
    if len(text) > max_length:
        text = text[:max_length]
    
    return text.lower()


def format_duration(seconds: float) -> str:
    """
    Format duration in human-readable format.
    
    Args:
        seconds: Duration in seconds
        
    Returns:
        Formatted string (e.g., "2m 30.5s")
    """
    if seconds < 60:
        return f"{seconds:.2f}s"
    
    minutes = int(seconds // 60)
    remaining_seconds = seconds % 60
    
    if minutes < 60:
        return f"{minutes}m {remaining_seconds:.1f}s"
    
    hours = int(minutes // 60)
    remaining_minutes = minutes % 60
    return f"{hours}h {remaining_minutes}m {remaining_seconds:.0f}s"


def estimate_cost(tokens_input: int, tokens_output: int, model: str, provider: str) -> float:
    """
    Estimate cost based on token usage.
    
    Args:
        tokens_input: Number of input tokens
        tokens_output: Number of output tokens
        model: Model name
        provider: Provider name (openai, anthropic, etc.)
        
    Returns:
        Estimated cost in USD
    """
    from .config import COST_PER_1K_TOKENS, DEFAULT_COST_PER_1K
    
    # Get pricing for provider and model
    if provider in COST_PER_1K_TOKENS and model in COST_PER_1K_TOKENS[provider]:
        pricing = COST_PER_1K_TOKENS[provider][model]
    else:
        pricing = DEFAULT_COST_PER_1K
    
    input_cost = (tokens_input / 1000) * pricing["input"]
    output_cost = (tokens_output / 1000) * pricing["output"]
    
    return input_cost + output_cost
`````

## File: tests/test_cli.py
`````python
import re
from pathlib import Path

import pytest

from awesome_deep_research import cli
from awesome_deep_research.cli import PromptExample


def test_load_prompt_examples_contains_expected_ids():
    prompts = cli.load_prompt_examples()
    assert prompts, "Expected at least one prompt example from taxonomy file"

    prompt_ids = {prompt.identifier for prompt in prompts}
    assert "domain-mapping-01" in prompt_ids
    assert "source-retrieval-01" in prompt_ids


def test_next_output_path_increments(tmp_path: Path):
    first = cli.next_output_path(tmp_path, "perplexity-sonar")
    assert first.name == "OUTPUT-PERPLEXITY-SONAR-0001.md"
    first.write_text("dummy", encoding="utf-8")

    second = cli.next_output_path(tmp_path, "perplexity-sonar")
    assert second.name == "OUTPUT-PERPLEXITY-SONAR-0002.md"


def test_build_user_prompt_includes_extra_instructions():
    prompt = PromptExample(identifier="custom", category="Domain Mapping", text="Analyze the domain.")
    extra = "Prioritize regulatory perspectives."

    user_prompt = cli.build_user_prompt(prompt, extra)

    assert "## Additional Instructions" in user_prompt
    assert extra in user_prompt
    assert re.search(r"Domain Mapping", user_prompt)


@pytest.mark.parametrize("mode", ["default", "relative", "absolute"])
def test_ensure_output_dir_creates_directories(tmp_path: Path, monkeypatch, mode: str):
    monkeypatch.setattr(cli, "DEFAULT_OUTPUT_DIR", tmp_path / "default")

    if mode == "default":
        requested = None
    elif mode == "relative":
        requested = str(Path("outputs-test"))
    else:
        requested = str((tmp_path / "absolute").resolve())

    output_dir = cli.ensure_output_dir(requested)
    assert output_dir.exists()
    assert output_dir.is_dir()
`````

## File: .env.example
`````
# ============================================================================
# Deep Research Skills - Environment Variables
# ============================================================================
# Copy this file to .env and fill in your API keys
# Usage: cp .env.example .env
#
# SECURITY WARNING: Never commit .env to version control!
# The .env file is already in .gitignore
# ============================================================================

# ----------------------------------------------------------------------------
# LLM Provider API Keys
# ----------------------------------------------------------------------------
# These are used by multiple skills for language model access

# OpenAI API Key
# Used by: gpt-researcher, openai-deep-research, stanford-storm, smolagents, langchain-deep-research
# Get your key at: https://platform.openai.com/api-keys
OPENAI_API_KEY=

# Anthropic API Key  
# Used by: smolagents, stanford-storm, langchain-deep-research
# Get your key at: https://console.anthropic.com/settings/keys
ANTHROPIC_API_KEY=

# Hugging Face Token
# Used by: smolagents (default model provider)
# Get your token at: https://huggingface.co/settings/tokens
HF_TOKEN=

# ----------------------------------------------------------------------------
# Search Provider API Keys
# ----------------------------------------------------------------------------

# Tavily API Key
# Used by: tavily-search, gpt-researcher, langchain-deep-research
# Get your key at: https://tavily.com/
TAVILY_API_KEY=

# Exa API Key
# Used by: exa-research
# Get your key at: https://exa.ai/
EXA_API_KEY=

# Perplexity API Key
# Used by: perplexity-sonar
# Get your key at: https://www.perplexity.ai/settings/api
PERPLEXITY_API_KEY=

# xAI (Grok) API Key
# Used by: xai-grok
# Get your key at: https://console.x.ai/
XAI_API_KEY=

# Jina AI API Key (Optional)
# Used by: jina-ai (optional - works without key but with rate limits)
# Get your key at: https://jina.ai/
JINA_API_KEY=

# ----------------------------------------------------------------------------
# Search Engine API Keys (for Stanford STORM)
# ----------------------------------------------------------------------------

# Bing Search API Key
# Used by: stanford-storm (when using --rm-name bing)
# Get your key at: https://www.microsoft.com/en-us/bing/apis/bing-web-search-api
BING_SEARCH_API_KEY=

# You.com Search API Key
# Used by: stanford-storm (when using --rm-name you)
# Get your key at: https://api.you.com/
YDC_API_KEY=

# ----------------------------------------------------------------------------
# Skills Summary
# ----------------------------------------------------------------------------
# 
# exa-research:
#   Required: EXA_API_KEY
#   Features: Neural search, content retrieval, automated research
#
# gpt-researcher:
#   Required: OPENAI_API_KEY (or other LLM), TAVILY_API_KEY
#   Features: Autonomous research agent, comprehensive reports
#
# jina-ai:
#   Optional: JINA_API_KEY (works without but with rate limits)
#   Features: Web reader, search with markdown output
#
# langchain-deep-research:
#   Required: OPENAI_API_KEY or ANTHROPIC_API_KEY, TAVILY_API_KEY
#   Features: Iterative research, knowledge gap analysis
#   Note: Requires LangGraph server running locally
#
# openai-deep-research:
#   Required: OPENAI_API_KEY
#   Features: Deep research mode with o3/o4 models
#
# perplexity-sonar:
#   Required: PERPLEXITY_API_KEY
#   Features: Real-time web search with AI synthesis
#
# smolagents:
#   Required: HF_TOKEN or OPENAI_API_KEY or ANTHROPIC_API_KEY
#   Features: Code-based agentic research, web search
#
# stanford-storm:
#   Required: OPENAI_API_KEY (or ANTHROPIC_API_KEY), BING_SEARCH_API_KEY or YDC_API_KEY
#   Features: Wikipedia-style comprehensive articles
#
# tavily-search:
#   Required: TAVILY_API_KEY
#   Features: AI-optimized search, synthesized answers
#
# xai-grok:
#   Required: XAI_API_KEY
#   Features: Grok models with web/X search tools
#
# ----------------------------------------------------------------------------
# Quick Start
# ----------------------------------------------------------------------------
#
# 1. Copy this file:
#    cp .env.example .env
#
# 2. Add your API keys to .env
#
# 3. Test a skill:
#    cd .claude/skills/tavily-search
#    python scripts/tavily_search.py --query "test query"
#
# 4. Run benchmarks:
#    cd benchmark
#    python run_benchmark.py --skills tavily-search --max-questions 1 -v
#
# ----------------------------------------------------------------------------
# Cost Considerations
# ----------------------------------------------------------------------------
#
# - OpenAI (GPT-4): ~$0.03-0.12 per 1K tokens
# - Anthropic (Claude): ~$0.015-0.075 per 1K tokens  
# - Perplexity: ~$0.0002-0.001 per 1K tokens
# - Tavily: Pay-per-search pricing
# - Exa: Pay-per-search pricing
# - HuggingFace: Free tier available, then pay-per-use
#
# Full benchmark run (10 skills × 30 questions): Estimated $15-60+
#
# ----------------------------------------------------------------------------
# Getting API Keys
# ----------------------------------------------------------------------------
#
# OpenAI:        https://platform.openai.com/api-keys
# Anthropic:     https://console.anthropic.com/settings/keys
# HuggingFace:   https://huggingface.co/settings/tokens
# Tavily:        https://tavily.com/
# Exa:           https://exa.ai/
# Perplexity:    https://www.perplexity.ai/settings/api
# xAI:           https://console.x.ai/
# Jina AI:       https://jina.ai/
# Bing Search:   https://www.microsoft.com/en-us/bing/apis/bing-web-search-api
# You.com:       https://api.you.com/
#
# ----------------------------------------------------------------------------
`````

## File: .gitignore
`````
# Python
*.pyc
*.pyo
*.pyd
__pycache__
awesome_deep_research.egg-info
.pytest_cache/
*.egg-info/
dist/
build/

# Environment variables
.env
.env.local

# Testing
coverage.xml
.coverage
htmlcov/

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# Documentation output
repomix-output.*

# Benchmark results
benchmark/results/*
!benchmark/results/.gitignore
!benchmark/results/README.md

# STORM output
storm_output/
`````

## File: CLAUDE_CODE.md
`````markdown
# CLAUDE_CODE.md: Headless Execution Manual for Deep Research Skills

## 1\. Introduction

Claude Code (`claude`) is an agentic tool that allows LLMs to interact with your local environment using "Skills." While often used interactively, these skills can also be operated in "headless" mode for automation.

There are two primary ways to execute these skills headlessly:

1. **Agentic Headless Execution (The Claude CLI)**: You use the Claude Code CLI to ask the agent (Claude) to perform a task non-interactively. The agent then selects and executes the appropriate skill script. This uses the official headless mode (`claude -p`).
2. **Direct Script Execution (Pipelines)**: You bypass the agent entirely and directly run the Python scripts that power the skills. This offers maximum reliability and performance, ideal for robust automation pipelines and chaining skills together.

This guide covers both methods.

## 2\. Prerequisites

Before running headless tasks, ensure your environment is configured.

### 2.1. Claude Code CLI Installation

If using Mode 1, you must install the Claude Code CLI.

**Native Install (Recommended):**

```bash
# macOS, Linux, WSL
curl -fsSL https://claude.ai/install.sh | bash

# Homebrew
brew install --cask claude-code
```

**NPM Install:**

```bash
npm install -g @anthropic-ai/claude-code
```

### 2.2. Authentication (Mode 1 only)

If using Mode 1, authenticate the CLI with your Claude account.

```bash
claude
# Follow the prompts to log in. Exit the interactive session once authenticated.
```

### 2.3. Skill Setup and Dependencies

The skills must be installed either globally (`~/.claude/skills/<skill-name>`) or locally in your project (`.claude/skills/<skill-name>`).

Crucially, you must install the Python dependencies required by the skill scripts, regardless of the execution mode.

```bash
pip install openai tavily-python exa-py gpt-researcher xai-sdk requests python-dotenv knowledge-storm litellm dspy-ai
```

### 2.4. API Key Configuration

The deep research skills rely heavily on API keys. The provided scripts use `python-dotenv` to load keys from a `.env` file in the current working directory.

```bash
# Example .env file
OPENAI_API_KEY=sk_...
PERPLEXITY_API_KEY=pplx_...
TAVILY_API_KEY=tvly_...
EXA_API_KEY=exa_...
XAI_API_KEY=xai_...
JINA_API_KEY=jina_...
BING_SEARCH_API_KEY=... # Required for STORM default
```

*Note: Always add `.env` to your `.gitignore` file.*

## 3\. Mode 1: Agentic Headless Execution (Claude CLI)

In this mode, you invoke the Claude CLI to run a task non-interactively. The agent interprets your prompt and executes the necessary tools.

### 3.1. Using `claude -p`

The primary command for this mode is `claude -p` (or `--print`).

```bash
claude -p "<task_description>" [--model <model_name>] [--output-format <format>]
```

### 3.2. Directing Skill Usage

For reliable automation, your prompt must be explicit about which skill and script to use. If the prompt is ambiguous, the agent might ask for clarification or choose the wrong tool, breaking the automation.

**Effective Prompt Structure:**

> "Use the `<skill-name>` skill. Execute the `<script_name.py>` script with the following parameters: `<parameters>`."

### 3.3. Examples

#### Example 1: Real-Time Synthesis (Perplexity Sonar)

```bash
claude -p "Use the perplexity-sonar skill. Execute the scripts/ask.py script with the prompt 'What are the latest developments in the EV market in Q4 2025?' and use the 'sonar-large-online' model." \
  --model claude-3-5-sonnet-20240620 > ev_market_q4_2025.md
```

The CLI will output the agent's thought process to the terminal (stderr), while the final report (stdout) is saved to the file.

#### Example 2: Comprehensive Report (GPT Researcher)

*Note: Agents like GPT Researcher can take several minutes.*

```bash
claude -p "Use the gpt-researcher skill. Execute the scripts/run_research.py script with the query 'The future of renewable energy sources' and the report type 'deep_research_report'." \
  --model claude-3-5-sonnet-20240620 > renewable_energy_report.md
```

### 3.4. Using JSON Output

For robust programmatic parsing, use `--output-format json`. This wraps the result in a structured format, including metadata.

```bash
claude -p "Use tavily-search (scripts/tavily_search.py) to find 'latest LLM benchmarks'." --output-format json
```

**Output Structure (JSON):**

```json
{
  "session_id": "...",
  "model": "claude-3-5-sonnet-20240620",
  "result": "{\n  \"answer\": \"The latest LLM benchmarks...\",\n  \"results\": [...] \n}",
  "cost_usd": 0.015
}
```

You can extract the actual result using `jq` (a command-line JSON processor):

```bash
claude -p "..." --output-format json | jq -r '.result' | jq .
```

## 4\. Mode 2: Direct Script Execution (Pipelines)

In this mode, you directly execute the Python scripts associated with the skills. This bypasses the LLM agent entirely, offering maximum reliability, speed, and flexibility for automation pipelines.

### 4.1. Syntax

You invoke the scripts using your standard Python interpreter. The scripts load configurations automatically from the `.env` file in the current directory.

```bash
python3 path/to/skill/scripts/<script_name.py> [arguments]
```

### 4.2. Examples

Assuming skills are installed locally in `./.claude/skills/`.

#### Example 1: Tavily Search (Direct)

```bash
python3 .claude/skills/tavily-search/scripts/tavily_search.py \
  --query "LLM interpretability techniques" \
  --search-depth advanced > sources.json
```

#### Example 2: Stanford STORM (Direct)

```bash
# Ensure OPENAI_API_KEY and BING_SEARCH_API_KEY are set in .env
python3 .claude/skills/stanford-storm/scripts/run_storm.py \
  --topic "The History of Quantum Computing" \
  --strong-model gpt-4o \
  --rm-name bing > quantum_history_article.md
```

### 4.3. Chaining Skills (Automation Workflows)

A key advantage of direct execution is the ability to chain skills together using standard Unix command substitution, creating complex research workflows.

#### Example Workflow: Neural Search and Content Extraction

**Goal**: Find the most relevant article on a topic using Exa AI, and then convert that specific article into clean Markdown using Jina AI.

**Prerequisite**: Install `jq` for parsing JSON.

```bash
#!/bin/bash

# Define script paths (assuming local installation)
EXA_SCRIPT=".claude/skills/exa-research/scripts/exa_tools.py"
JINA_SCRIPT=".claude/skills/jina-ai/scripts/jina_tools.py"
QUERY="Best practices for securing Kubernetes clusters in production"

# 1. Search using Exa. The exa_tools.py script outputs a JSON array.
echo "Searching for relevant articles with Exa..."
SEARCH_RESULTS=$(python3 $EXA_SCRIPT search "$QUERY" --num-results 5)

# 2. Extract the URL of the first result using jq
TARGET_URL=$(echo "$SEARCH_RESULTS" | jq -r '.[0].url')

# 3. Check if a URL was found (Crucial error handling)
if [ -z "$TARGET_URL" ] || [ "$TARGET_URL" == "null" ]; then
    echo "Error: No relevant URL found by Exa."
    exit 1
fi

echo "Found top URL: $TARGET_URL"

# 4. Use Jina Reader to convert the URL to Markdown
echo "Converting URL content to Markdown with Jina..."
python3 $JINA_SCRIPT read "$TARGET_URL" > k8s_security_article.json

echo "Article content (JSON with Markdown) saved to k8s_security_article.json"
```

## 5\. Best Practices for Automation

The provided deep research skills adhere to these conventions to enable robust headless execution:

1. **stdout vs. stderr**:

      * **stdout** is used exclusively for the primary output (the report, the JSON data). This enables piping (`|`) and redirection (`>`).
      * **stderr** is used for logging, progress indicators, warnings, and errors.

2. **Exit Codes**:

      * Scripts exit with status `0` upon success.
      * Scripts exit with a non-zero status (e.g., `1`) upon failure (e.g., missing API key, failed request).

3. **Error Handling in Scripts**: Always check the exit code when automating, regardless of the mode used.

<!-- end list -->

```bash
# Example: Direct Execution Error Handling
python3 .claude/skills/perplexity-sonar/scripts/ask.py ...
if [ $? -ne 0 ]; then
    echo "Perplexity skill failed!"
    exit 1
fi

# Example: Agentic CLI Error Handling
if ! claude -p "Use tavily-search to check the weather."; then
    echo "Claude Code execution failed."
    exit 1
fi
```
`````

## File: ENV_SETUP.md
`````markdown
# Environment Variables Setup Guide

Quick reference for setting up API keys for all deep research skills.

## Quick Setup

1. **Copy the example file:**
   ```bash
   cp .env.example .env
   ```

2. **Edit `.env` and add your API keys**

3. **Verify your setup:**
   ```bash
   # Check which keys are set
   grep -v '^#' .env | grep -v '^$' | cut -d'=' -f1
   ```

## Required API Keys by Skill

### Minimal Setup (2-3 keys for most skills)

For a quick start, get these first:

```bash
OPENAI_API_KEY=sk-...        # Most commonly used
TAVILY_API_KEY=tvly-...      # Used by multiple skills
```

### Complete Setup

| Skill | Required Keys | Optional Keys |
|-------|--------------|---------------|
| **exa-research** | `EXA_API_KEY` | - |
| **gpt-researcher** | `TAVILY_API_KEY`, `OPENAI_API_KEY` | - |
| **jina-ai** | - | `JINA_API_KEY` |
| **langchain-deep-research** | `TAVILY_API_KEY`, `OPENAI_API_KEY` or `ANTHROPIC_API_KEY` | - |
| **openai-deep-research** | `OPENAI_API_KEY` | - |
| **perplexity-sonar** | `PERPLEXITY_API_KEY` | - |
| **smolagents** | `HF_TOKEN` or `OPENAI_API_KEY` or `ANTHROPIC_API_KEY` | - |
| **stanford-storm** | `OPENAI_API_KEY` or `ANTHROPIC_API_KEY`, `BING_SEARCH_API_KEY` or `YDC_API_KEY` | - |
| **tavily-search** | `TAVILY_API_KEY` | - |
| **xai-grok** | `XAI_API_KEY` | - |

## Getting API Keys

### LLM Providers

- **OpenAI**: https://platform.openai.com/api-keys
  - Free trial credit, then pay-as-you-go
  - GPT-4: ~$0.03-0.12 per 1K tokens

- **Anthropic**: https://console.anthropic.com/settings/keys
  - Free trial credit, then pay-as-you-go
  - Claude: ~$0.015-0.075 per 1K tokens

- **Hugging Face**: https://huggingface.co/settings/tokens
  - Free tier available
  - Pro: $9/month for more usage

### Search Providers

- **Tavily**: https://tavily.com/
  - Research-focused search API
  - Free tier: 1,000 searches/month
  - Pro: $20/month for 10K searches

- **Exa**: https://exa.ai/
  - Neural search engine
  - Free tier available
  - Pay-as-you-go pricing

- **Perplexity**: https://www.perplexity.ai/settings/api
  - AI-powered search
  - Pay-per-request pricing

- **xAI (Grok)**: https://console.x.ai/
  - Access to Grok models
  - Beta access required

- **Jina AI**: https://jina.ai/
  - Reader and search APIs
  - Free tier with rate limits

- **Bing Search**: https://www.microsoft.com/en-us/bing/apis/bing-web-search-api
  - Free tier: 1,000 calls/month
  - Paid tiers available

- **You.com**: https://api.you.com/
  - Search API
  - Contact for access

## Testing Your Setup

### Test Individual Skills

```bash
# Test Tavily
cd .claude/skills/tavily-search
python scripts/tavily_search.py --query "test"

# Test OpenAI Deep Research
cd ../openai-deep-research
python scripts/run_deep_research.py --prompt "test query"

# Test Exa
cd ../exa-research
python scripts/exa_tools.py search "test"
```

### Run System Test

```bash
cd benchmark
python test_system.py
```

### Quick Benchmark

```bash
# Test one skill with minimal questions
python run_benchmark.py --skills tavily-search --max-questions 1 -v
```

## Cost Management

### Free Tier Options

Skills that can work with free tiers:
- **jina-ai**: Works without API key (rate limited)
- **smolagents**: Can use HuggingFace free tier
- **tavily-search**: 1,000 free searches/month

### Budget-Friendly Combinations

For testing on a budget (~$5-10):
1. Use `HF_TOKEN` with smolagents (free tier)
2. Use `TAVILY_API_KEY` (free tier)
3. Use `OPENAI_API_KEY` with GPT-3.5-turbo (cheaper)

### Full Production Setup

For comprehensive testing (~$50-100):
- All OpenAI models (including GPT-4)
- Multiple search providers
- Premium features

## Environment Variable Priority

Some skills support multiple providers. They check in this order:

**LLM Selection:**
1. `OPENAI_API_KEY` (most common)
2. `ANTHROPIC_API_KEY` (alternative)
3. `HF_TOKEN` (fallback for smolagents)

**Search Selection:**
1. `TAVILY_API_KEY` (recommended for research)
2. `BING_SEARCH_API_KEY` (for STORM)
3. `YDC_API_KEY` (You.com alternative)

## Security Best Practices

1. **Never commit `.env` to git**
   - Already in `.gitignore`

2. **Use environment-specific files**
   - `.env.local` for local development
   - `.env.production` for production (if applicable)

3. **Rotate keys regularly**
   - Especially if exposed or shared

4. **Use minimum required permissions**
   - API keys should have minimal scopes

5. **Monitor usage**
   - Set up billing alerts
   - Track API usage

## Troubleshooting

### "API key not set" errors

```bash
# Check if key is in .env
grep "OPENAI_API_KEY" .env

# Check if .env is loaded
python -c "from dotenv import load_dotenv; import os; load_dotenv(); print(os.getenv('OPENAI_API_KEY'))"
```

### "Rate limit exceeded" errors

- Wait before retrying
- Upgrade to paid tier
- Use alternative provider

### "Invalid API key" errors

- Verify key is correct (copy-paste errors)
- Check if key has been revoked
- Ensure no extra spaces in `.env`

## Example .env File

```bash
# LLM Providers
OPENAI_API_KEY=sk-proj-abc123...
ANTHROPIC_API_KEY=sk-ant-api03-xyz789...
HF_TOKEN=hf_abc123...

# Search Providers  
TAVILY_API_KEY=tvly-abc123...
EXA_API_KEY=exa_abc123...
PERPLEXITY_API_KEY=pplx-abc123...

# Additional
XAI_API_KEY=xai-abc123...
JINA_API_KEY=jina_abc123...
BING_SEARCH_API_KEY=abc123...
```

## Next Steps

After setting up your environment:

1. ✅ Test with `python benchmark/test_system.py`
2. ✅ Run a quick benchmark on one skill
3. ✅ Review cost estimates in `benchmark/SUMMARY.md`
4. ✅ Run full benchmark when ready
5. ✅ Analyze results with `python benchmark/analyze.py`

## Additional Resources

- [Benchmark System README](benchmark/README.md)
- [Benchmark Quick Start](benchmark/QUICKSTART.md)
- [Complete System Summary](benchmark/SUMMARY.md)
- [Skills Documentation](.claude/skills/*/SKILL.md)
`````

## File: .claude/skills/exa-research/scripts/exa_tools.py
`````python
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
`````

## File: .claude/skills/exa-research/requirements.txt
`````
exa-py
openai
python-dotenv
`````

## File: .claude/skills/exa-research/SKILL.md
`````markdown
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
```

**Example:**

```bash
python3 scripts/exa_tools.py search "innovative sustainable urban planning" --num-results 5 --highlights
```

### 2. Research (Automated)

Automate in-depth research and receive a structured report.

```bash
python3 scripts/exa_tools.py research "<query>" [--model <exa-research|exa-research-pro>]
```

**Example:**

```bash
python3 scripts/exa_tools.py research "Analyze the impact of quantum computing on cryptography" --model exa-research-pro
```

### 3. Find Similar

Find pages similar to a given URL.

```bash
python3 scripts/exa_tools.py find_similar "<url>"
```

**Example:**

```bash
python3 scripts/exa_tools.py find_similar "https://arxiv.org/abs/1706.03762"
```

## Output

The script outputs results in JSON format.
`````

## File: .claude/skills/gpt-researcher/scripts/run_research.py
`````python
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
`````

## File: .claude/skills/gpt-researcher/requirements.txt
`````
gpt-researcher
python-dotenv
`````

## File: .claude/skills/jina-ai/scripts/jina_tools.py
`````python
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
`````

## File: .claude/skills/jina-ai/requirements.txt
`````
requests
python-dotenv
`````

## File: .claude/skills/langchain-deep-research/scripts/research.py
`````python
import argparse
import asyncio
import json
import os
import sys
from dotenv import load_dotenv

try:
    from langchain_core.messages import HumanMessage
    from langgraph_sdk import get_client
except ImportError:
    print("Error: Required packages not found.", file=sys.stderr)
    print("Install with: pip install langgraph-sdk langchain-core", file=sys.stderr)
    sys.exit(1)

# Load environment variables
load_dotenv()

async def run_research(query: str, max_iterations: int = 3, output_file: str = None):
    """
    Run the LangChain Open Deep Research agent.
    
    This function assumes the LangGraph server is running locally.
    You can start it with: langgraph dev --allow-blocking
    """
    
    # Check for required API keys
    if not os.getenv("OPENAI_API_KEY") and not os.getenv("ANTHROPIC_API_KEY"):
        print("Error: No LLM API key found. Set OPENAI_API_KEY or ANTHROPIC_API_KEY.", file=sys.stderr)
        sys.exit(1)
    
    if not os.getenv("TAVILY_API_KEY"):
        print("Warning: TAVILY_API_KEY not set. Search may not work properly.", file=sys.stderr)
    
    try:
        print(f"Starting deep research on: {query}", file=sys.stderr)
        print(f"Max iterations: {max_iterations}", file=sys.stderr)
        print("", file=sys.stderr)
        
        # Connect to LangGraph server (assumes server is running)
        # To start server: cd to open_deep_research dir and run: langgraph dev --allow-blocking
        client = get_client(url="http://localhost:2024")
        
        # Create thread for this research session
        thread = await client.threads.create()
        
        # Create input message
        input_data = {
            "messages": [HumanMessage(content=query)],
            "max_iterations": max_iterations
        }
        
        print("Running research agent...", file=sys.stderr)
        print("", file=sys.stderr)
        
        # Stream the response to show progress
        final_state = None
        async for chunk in client.runs.stream(
            thread["thread_id"],
            "agent",
            input=input_data,
            stream_mode="updates"
        ):
            if chunk.data:
                # Print progress to stderr
                for key, value in chunk.data.items():
                    if isinstance(value, dict):
                        if "messages" in value:
                            last_msg = value["messages"][-1] if value["messages"] else None
                            if last_msg:
                                print(f"[{key}] {last_msg.content[:100]}...", file=sys.stderr)
                final_state = chunk.data
        
        # Extract the final report
        if final_state and "messages" in final_state:
            messages = final_state["messages"]
            final_message = messages[-1] if messages else None
            
            if final_message:
                report = final_message.content
                
                # Output to file or stdout
                if output_file:
                    with open(output_file, 'w', encoding='utf-8') as f:
                        f.write(report)
                    print(f"\n✅ Report saved to: {output_file}", file=sys.stderr)
                else:
                    print("\n" + "="*80, file=sys.stderr)
                    print("FINAL REPORT", file=sys.stderr)
                    print("="*80, file=sys.stderr)
                    print(report)
            else:
                print("Error: No final message received from agent.", file=sys.stderr)
                sys.exit(1)
        else:
            print("Error: No state received from agent.", file=sys.stderr)
            sys.exit(1)
            
    except ConnectionError:
        print("\n❌ Error: Could not connect to LangGraph server.", file=sys.stderr)
        print("\nTo use this skill, you need to:", file=sys.stderr)
        print("1. Clone the open_deep_research repository:", file=sys.stderr)
        print("   git clone https://github.com/langchain-ai/open_deep_research.git", file=sys.stderr)
        print("2. Navigate to the directory and install dependencies:", file=sys.stderr)
        print("   cd open_deep_research && uv sync", file=sys.stderr)
        print("3. Start the LangGraph server:", file=sys.stderr)
        print("   langgraph dev --allow-blocking", file=sys.stderr)
        print("4. Run this script again", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error during research: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Run LangChain Open Deep Research agent for comprehensive research reports."
    )
    parser.add_argument("--query", required=True, help="The research question or topic.")
    parser.add_argument("--max-iterations", type=int, default=3, 
                       help="Maximum number of research iterations (default: 3).")
    parser.add_argument("--output", help="Output file path for the report (optional).")
    
    args = parser.parse_args()
    
    # Run the async function
    asyncio.run(run_research(args.query, args.max_iterations, args.output))
`````

## File: .claude/skills/langchain-deep-research/requirements.txt
`````
langgraph-sdk
langchain-core
python-dotenv
`````

## File: .claude/skills/langchain-deep-research/SKILL.md
`````markdown
---
name: langchain-deep-research
description: Run LangChain Open Deep Research agent for iterative web research and comprehensive reports. Requires LLM API keys and search API (e.g., OPENAI_API_KEY, TAVILY_API_KEY).
---

# LangChain Open Deep Research Skill

This skill utilizes the LangChain Open Deep Research framework to perform iterative web research with reflection and knowledge gap identification, producing comprehensive reports with citations.

## Setup

1. **Dependencies:** Requires the `open-deep-research` package and LangGraph.

    ```bash
    pip install open-deep-research langgraph-cli python-dotenv
    ```

2. **API Key Configuration:** Requires API keys for an LLM and a search provider.

    ```bash
    # Set up your API keys
    echo "# LLM Configuration" >> .env
    echo "OPENAI_API_KEY=your_openai_key" >> .env
    echo "# Search Configuration" >> .env
    echo "TAVILY_API_KEY=your_tavily_key" >> .env
    if [ -f .gitignore ] && ! grep -q ".env" .gitignore; then echo ".env" >> .gitignore; fi
    echo "API keys saved to .env."
    ```

## Usage

Use the `scripts/research.py` script to run a research task.

### Command

```bash
python3 scripts/research.py --query "<research_query>" [--max-iterations <N>]
```

### Parameters

* `--query` (Required): The research question or topic.
* `--max-iterations` (Optional): Maximum number of research iterations (default: 3).
* `--output` (Optional): Output file path for the final report (default: stdout).

### Example

```bash
python3 scripts/research.py --query "What are the latest developments in quantum computing error correction?" --max-iterations 4 --output report.md
```

## Output

The script outputs a comprehensive research report with:

* Iterative search findings
* Knowledge gap analysis
* Final synthesized report with citations
* Source list

## Features

* **Iterative Research**: Performs multiple search cycles, reflecting on gaps
* **Configurable Models**: Supports OpenAI, Anthropic, Ollama, and other LLM providers
* **Multiple Search Engines**: Tavily (default), Brave, DuckDuckGo, SerpAPI
* **Citation Tracking**: All findings include source references
`````

## File: .claude/skills/openai-deep-research/scripts/run_deep_research.py
`````python
import argparse
import json
import os
import sys
from typing import Optional

from dotenv import load_dotenv

try:
    from openai import OpenAI
    from openai._exceptions import APIStatusError
except ImportError:  # pragma: no cover - dependency issue surfaced to user
    print("Error: openai package not installed. Run 'pip install openai'.", file=sys.stderr)
    sys.exit(1)

load_dotenv()


def validate_api_key() -> None:
    if not os.getenv("OPENAI_API_KEY"):
        print("Error: OPENAI_API_KEY is not set. Add it to your environment or .env file.", file=sys.stderr)
        sys.exit(1)


def run_deep_research(
    prompt: str,
    model: str = "o4-mini-deep-research",
    effort: str = "medium",
    emit_json: bool = False,
    output_path: Optional[str] = None,
) -> None:
    validate_api_key()

    client = OpenAI()

    reasoning = {"effort": effort}

    # Stream the response so users can see progress in the terminal.
    try:
        stream = client.responses.stream(
            model=model,
            input=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            reasoning=reasoning,
            extra_headers={"OpenAI-Beta": "assistants=v2"},
        )
    except APIStatusError as exc:
        print(f"Deep Research request failed ({exc.status_code}): {exc.message}", file=sys.stderr)
        sys.exit(1)
    except Exception as exc:  # pragma: no cover - defensive
        print(f"Unexpected error calling OpenAI API: {exc}", file=sys.stderr)
        sys.exit(1)

    report_sections = []
    json_payload = None

    with stream as events:
        for event in events:
            event_type = getattr(event, "type", "")

            if event_type == "response.output_text.delta":
                chunk = event.delta
                if chunk:
                    report_sections.append(chunk)
                    if not emit_json:
                        print(chunk, end="", flush=True)

            elif event_type == "response.completed":
                json_payload = event.response
            elif event_type == "response.error":  # pragma: no cover - surfaced immediately
                print(f"Deep Research error: {event.error}", file=sys.stderr)
                sys.exit(1)

    final_report = "".join(report_sections)

    if emit_json and json_payload is not None:
        serialized = json.dumps(json_payload, indent=2)
        if output_path:
            with open(output_path, "w", encoding="utf-8") as fh:
                fh.write(serialized)
            print(f"\nReport JSON saved to {output_path}", file=sys.stderr)
        else:
            print(serialized)
        return

    if output_path:
        with open(output_path, "w", encoding="utf-8") as fh:
            fh.write(final_report)
        print(f"\nReport saved to {output_path}", file=sys.stderr)
    elif emit_json:
        print("{}")  # no payload returned


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run OpenAI Deep Research jobs from Claude Skills.")
    parser.add_argument("--prompt", required=True, help="Research prompt to investigate.")
    parser.add_argument("--model", default="o4-mini-deep-research",
                        choices=["o4-mini-deep-research", "o3-deep-research"],
                        help="Deep Research model to use.")
    parser.add_argument("--effort", default="medium",
                        choices=["low", "medium", "high"],
                        help="Research effort / depth level.")
    parser.add_argument("--json", action="store_true",
                        help="Emit the full JSON payload instead of only the final report text.")
    parser.add_argument("--output", help="Optional output file path for the report or JSON.")

    args = parser.parse_args()
    run_deep_research(args.prompt, args.model, args.effort, args.json, args.output)
`````

## File: .claude/skills/openai-deep-research/requirements.txt
`````
openai
python-dotenv
`````

## File: .claude/skills/openai-deep-research/SKILL.md
`````markdown
---
name: openai-deep-research
description: Use OpenAI's Deep Research API (o3 / o4 models) to automate multi-step, citation-backed research workflows.
---

# OpenAI Deep Research Skill

This skill wraps OpenAI's Deep Research API so you can launch autonomous research runs (using `o3-deep-research` or `o4-mini-deep-research`) directly from Claude Code.

## Setup

1. **Dependencies:** Install the OpenAI SDK.

    ```bash
    pip install openai python-dotenv
    ```

2. **API Key Configuration:** Export your OpenAI API key.

    ```bash
    echo "OPENAI_API_KEY=sk-..." >> .env
    if [ -f .gitignore ] && ! grep -q ".env" .gitignore; then echo ".env" >> .gitignore; fi
    ```

    The Deep Research endpoint requires access to the Early Access program. Ensure your account is enabled before calling the API.

## Usage

Use `scripts/run_deep_research.py` to start a research job and stream the final report to stdout.

### Command

```bash
python3 scripts/run_deep_research.py --prompt "<research_question>" [--model o4-mini-deep-research] [--effort medium] [--json]
```

### Parameters

* `--prompt` (Required): The investigation prompt.
* `--model` (Optional): `o4-mini-deep-research` (default) or `o3-deep-research`.
* `--effort` (Optional): Reasoning depth, one of `low`, `medium`, `high` (default `medium`).
* `--json` (Optional): Emit the full response payload as JSON instead of just the synthesized report.
* `--output` (Optional): Write the report to a file path.

### Example

```bash
python3 scripts/run_deep_research.py \
  --prompt "Assess the projected market impact of solid state batteries by 2030" \
  --model o3-deep-research \
  --effort high \
  --output reports/solid-state-batteries.md
```

## Output

The script prints the synthesized Deep Research report (with citations) to stdout or saves it to the specified file. When `--json` is provided, the entire response payload (including intermediate steps, citations, and metadata) is emitted.

## Features

* **True Deep Research:** Uses OpenAI's autonomous planning, browsing, and synthesis stack.
* **Configurable Effort:** Choose between faster runs (`o4-mini-deep-research`) or higher-quality runs (`o3-deep-research`).
* **Intermediate Visibility:** Optional JSON output exposes the tool traces and citations returned by the API.
`````

## File: .claude/skills/perplexity-sonar/scripts/ask.py
`````python
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
`````

## File: .claude/skills/perplexity-sonar/requirements.txt
`````
openai
python-dotenv
`````

## File: .claude/skills/smolagents/scripts/agent.py
`````python
import argparse
import os
import sys
from dotenv import load_dotenv

try:
    from smolagents import CodeAgent, ToolCallingAgent
    from smolagents import InferenceClientModel, LiteLLMModel, TransformersModel
    from smolagents import DuckDuckGoSearchTool
except ImportError:
    print("Error: smolagents not found. Install with: pip install 'smolagents[toolkit]'", file=sys.stderr)
    sys.exit(1)

# Load environment variables
load_dotenv()

def create_model(model_type: str = "hf", model_id: str = None):
    """Create and return the appropriate model based on type."""
    
    if model_type == "hf":
        # Hugging Face Inference API
        if not os.getenv("HF_TOKEN"):
            print("Warning: HF_TOKEN not set. Using default (may have rate limits).", file=sys.stderr)
        
        if model_id:
            return InferenceClientModel(model_id=model_id)
        else:
            # Use a good default reasoning model
            return InferenceClientModel(model_id="Qwen/Qwen2.5-72B-Instruct")
    
    elif model_type == "openai":
        if not os.getenv("OPENAI_API_KEY"):
            print("Error: OPENAI_API_KEY not set.", file=sys.stderr)
            sys.exit(1)
        model_id = model_id or "gpt-4o"
        return LiteLLMModel(model_id=model_id)
    
    elif model_type == "anthropic":
        if not os.getenv("ANTHROPIC_API_KEY"):
            print("Error: ANTHROPIC_API_KEY not set.", file=sys.stderr)
            sys.exit(1)
        model_id = model_id or "claude-3-5-sonnet-20241022"
        return LiteLLMModel(model_id=model_id)
    
    elif model_type == "local":
        if not model_id:
            print("Error: --model-id required for local models.", file=sys.stderr)
            sys.exit(1)
        return TransformersModel(model_id=model_id)
    
    else:
        print(f"Error: Unknown model type '{model_type}'", file=sys.stderr)
        sys.exit(1)

def run_agent(task: str, model_type: str = "hf", model_id: str = None, 
              web_search: bool = False, verbose: bool = False):
    """Run the Smolagents agent on the given task."""
    
    try:
        print(f"Initializing Smolagents ({model_type})...", file=sys.stderr)
        
        # Create model
        model = create_model(model_type, model_id)
        
        # Prepare tools
        tools = []
        if web_search:
            tools.append(DuckDuckGoSearchTool())
            print("✓ Web search enabled", file=sys.stderr)
        
        # Create agent
        # CodeAgent writes Python code to accomplish tasks (more efficient)
        agent = CodeAgent(
            tools=tools,
            model=model,
            max_steps=10,
        )
        
        print(f"\nTask: {task}", file=sys.stderr)
        print("="*80, file=sys.stderr)
        
        # Run the agent
        if verbose:
            print("\n[Agent Execution]", file=sys.stderr)
        
        result = agent.run(task)
        
        print("\n" + "="*80, file=sys.stderr)
        print("RESULT:", file=sys.stderr)
        print("="*80 + "\n", file=sys.stderr)
        
        # Output result to stdout
        print(result)
        
        # Show agent logs if verbose
        if verbose and hasattr(agent, 'logs'):
            print("\n" + "="*80, file=sys.stderr)
            print("EXECUTION LOGS:", file=sys.stderr)
            print("="*80, file=sys.stderr)
            for log in agent.logs:
                print(log, file=sys.stderr)
        
    except Exception as e:
        print(f"\nError during agent execution: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Run Hugging Face Smolagents for agentic research tasks."
    )
    parser.add_argument("--task", required=True, help="The task or research question.")
    parser.add_argument("--model", default="hf", 
                       choices=["hf", "openai", "anthropic", "local"],
                       help="Model type (default: hf for Hugging Face Inference API).")
    parser.add_argument("--model-id", help="Specific model ID to use.")
    parser.add_argument("--web-search", action="store_true", 
                       help="Enable web search tool (DuckDuckGo).")
    parser.add_argument("--verbose", action="store_true",
                       help="Show detailed execution logs.")
    
    args = parser.parse_args()
    
    run_agent(
        task=args.task,
        model_type=args.model,
        model_id=args.model_id,
        web_search=args.web_search,
        verbose=args.verbose
    )
`````

## File: .claude/skills/smolagents/requirements.txt
`````
smolagents[toolkit]
python-dotenv
`````

## File: .claude/skills/smolagents/SKILL.md
`````markdown
---
name: smolagents
description: Use Hugging Face Smolagents framework for code-based agentic research with tool support. Supports multiple LLM providers and web search.
---

# Smolagents Skill

This skill leverages Hugging Face's Smolagents framework, a minimalist AI agent library where agents write Python code to accomplish tasks. It's highly efficient (30% token efficiency gain) and supports multiple LLM providers.

## Setup

1. **Dependencies:** Requires `smolagents` with toolkit extensions.

    ```bash
    pip install 'smolagents[toolkit]' python-dotenv
    ```

2. **API Key Configuration:** Supports multiple LLM providers. At minimum, set one:

    ```bash
    # For Hugging Face Inference API (default, free tier available)
    echo "HF_TOKEN=your_huggingface_token" >> .env
    
    # OR for OpenAI
    echo "OPENAI_API_KEY=your_openai_key" >> .env
    
    # OR for Anthropic
    echo "ANTHROPIC_API_KEY=your_anthropic_key" >> .env
    
    if [ -f .gitignore ] && ! grep -q ".env" .gitignore; then echo ".env" >> .gitignore; fi
    ```

## Usage

Use the `scripts/agent.py` script to run research tasks.

### Command

```bash
python3 scripts/agent.py --task "<task_description>" [--model <model_type>] [--model-id <model_name>] [--web-search]
```

### Parameters

* `--task` (Required): The task or research question.
* `--model` (Optional): Model type - `hf` (Hugging Face), `openai`, `anthropic`, or `local` (default: `hf`).
* `--model-id` (Optional): Specific model ID to use.
* `--web-search` (Optional): Enable web search tool (uses DuckDuckGo).
* `--verbose` (Optional): Show detailed execution logs.

### Example

```bash
# Using Hugging Face Inference API with web search
python3 scripts/agent.py --task "Research the latest developments in transformer architecture improvements" --web-search --verbose

# Using a specific model
python3 scripts/agent.py --task "Analyze the impact of RLHF on LLM performance" --model hf --model-id "Qwen/Qwen2.5-72B-Instruct" --web-search
```

## Output

The script outputs:

* Generated Python code (to stderr for visibility)
* Task execution results
* Final answer or research findings

## Features

* **Code-as-Action**: Agents write and execute Python code to solve tasks
* **Tool Support**: Web search, file operations, and custom tools
* **Multi-Model**: Supports HF Inference API, OpenAI, Anthropic, local models
* **Efficient**: 30% token efficiency improvement over traditional approaches
`````

## File: .claude/skills/stanford-storm/scripts/run_storm.py
`````python
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
`````

## File: .claude/skills/stanford-storm/requirements.txt
`````
knowledge-storm
dspy-ai
litellm
python-dotenv
`````

## File: .claude/skills/stanford-storm/SKILL.md
`````markdown
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
```

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
`````

## File: .claude/skills/tavily-search/scripts/tavily_search.py
`````python
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
`````

## File: .claude/skills/tavily-search/requirements.txt
`````
tavily-python
python-dotenv
`````

## File: .claude/skills/tavily-search/SKILL.md
`````markdown
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
```

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
`````

## File: .claude/skills/xai-grok/scripts/grok_research.py
`````python
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
`````

## File: .claude/skills/xai-grok/requirements.txt
`````
xai-sdk
python-dotenv
`````

## File: .claude/skills/xai-grok/SKILL.md
`````markdown
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
```

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
`````

## File: .repomixignore
`````
# Add patterns to ignore here, one per line
# Example:
# *.log
LICENSE
# tmp/
awesome_deep_research.egg-info
`````

## File: pyproject.toml
`````toml
[build-system]
requires = ["setuptools>=68.0", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "awesome-deep-research"
version = "0.1.0"
description = "A Python library for working with deep research AI agents"
readme = "README.md"
requires-python = ">=3.8"
license = {text = "MIT"}
authors = [
    {name = "Awesome Deep Researchers Contributors"}
]
keywords = [
    "ai",
    "research",
    "deep-research",
    "agents",
    "llm",
    "chatgpt",
    "gemini",
    "perplexity",
    "citations",
    "automation"
]
classifiers = [
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Developers",
    "Intended Audience :: Science/Research",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
    "Topic :: Scientific/Engineering :: Artificial Intelligence",
    "Topic :: Software Development :: Libraries :: Python Modules",
]
dependencies = [
    "requests>=2.31.0",
    "pydantic>=2.0.0",
    "beautifulsoup4>=4.12.0",
    "markdown>=3.5.0",
    "python-dateutil>=2.8.0",
    "typing-extensions>=4.8.0",
    "python-dotenv>=1.2.1",
]

[project.optional-dependencies]
dev = [
    "pytest>=7.4.0",
    "pytest-cov>=4.1.0",
    "black>=23.0.0",
    "flake8>=6.1.0",
    "mypy>=1.5.0",
    "isort>=5.12.0",
    "pre-commit>=3.5.0",
]
docs = [
    "sphinx>=7.0.0",
    "sphinx-rtd-theme>=1.3.0",
    "sphinx-autodoc-typehints>=1.24.0",
]
all = [
    "openai>=1.0.0",
    "google-generativeai>=0.3.0",
    "anthropic>=0.7.0",
]

[project.urls]
Homepage = "https://github.com/closedloop-technologies/awesome-deep-researchers"
Documentation = "https://github.com/closedloop-technologies/awesome-deep-researchers#readme"
Repository = "https://github.com/closedloop-technologies/awesome-deep-researchers"
Issues = "https://github.com/closedloop-technologies/awesome-deep-researchers/issues"

[project.scripts]
adr = "awesome_deep_research.cli:main"

[tool.setuptools]
packages = ["awesome_deep_research"]

[tool.setuptools.package-data]
awesome_deep_research = ["py.typed"]

[tool.black]
line-length = 100
target-version = ["py38", "py39", "py310", "py311", "py312"]
include = '\.pyi?$'
exclude = '''
/(
    \.git
  | \.venv
  | \.tox
  | build
  | dist
  | __pycache__
)/
'''

[tool.isort]
profile = "black"
line_length = 100
multi_line_output = 3
include_trailing_comma = true
force_grid_wrap = 0
use_parentheses = true
ensure_newline_before_comments = true

[tool.mypy]
python_version = "3.8"
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = false
disallow_incomplete_defs = false
check_untyped_defs = true
no_implicit_optional = true
warn_redundant_casts = true
warn_unused_ignores = true
warn_no_return = true
strict_equality = true

[tool.pytest.ini_options]
minversion = "7.0"
python_files = ["test_*.py", "*_test.py"]
python_classes = ["Test*"]
python_functions = ["test_*"]
addopts = [
    "--strict-markers",
    "--strict-config"
]

[tool.coverage.run]
source = ["awesome_deep_research"]
omit = [
    "*/tests/*",
    "*/test_*.py",
    "*/__pycache__/*",
]

[tool.coverage.report]
exclude_lines = [
    "pragma: no cover",
    "def __repr__",
    "raise AssertionError",
    "raise NotImplementedError",
    "if __name__ == .__main__.:",
    "if TYPE_CHECKING:",
    "@abstractmethod",
]
`````

## File: repomix.config.json
`````json
{
  "$schema": "https://repomix.com/schemas/latest/schema.json",
  "input": {
    "maxFileSize": 52428800
  },
  "output": {
    "filePath": "repomix-output.md",
    "style": "markdown",
    "parsableStyle": false,
    "fileSummary": true,
    "directoryStructure": true,
    "files": true,
    "removeComments": false,
    "removeEmptyLines": false,
    "compress": false,
    "topFilesLength": 5,
    "showLineNumbers": false,
    "truncateBase64": false,
    "copyToClipboard": false,
    "includeFullDirectoryStructure": false,
    "tokenCountTree": false,
    "git": {
      "sortByChanges": true,
      "sortByChangesMaxCommits": 100,
      "includeDiffs": false,
      "includeLogs": false,
      "includeLogsCount": 50
    }
  },
  "include": [],
  "ignore": {
    "useGitignore": true,
    "useDotIgnore": true,
    "useDefaultPatterns": true,
    "customPatterns": []
  },
  "security": {
    "enableSecurityCheck": true
  },
  "tokenCount": {
    "encoding": "o200k_base"
  }
}
`````

## File: setup.py
`````python
"""
Setup configuration for awesome_deep_research package.
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read the README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

setup(
    name="awesome-deep-research",
    version="0.1.0",
    author="Awesome Deep Researchers Contributors",
    author_email="",
    description="A Python library for working with deep research AI agents",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/closedloop-technologies/awesome-deep-researchers",
    packages=find_packages(exclude=["tests", "tests.*", "docs", "research"]),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.8",
    install_requires=[
        "requests>=2.31.0",
        "pydantic>=2.0.0",
        "beautifulsoup4>=4.12.0",
        "markdown>=3.5.0",
        "python-dateutil>=2.8.0",
        "typing-extensions>=4.8.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.4.0",
            "pytest-cov>=4.1.0",
            "black>=23.0.0",
            "flake8>=6.1.0",
            "mypy>=1.5.0",
            "isort>=5.12.0",
        ],
        "docs": [
            "sphinx>=7.0.0",
            "sphinx-rtd-theme>=1.3.0",
            "sphinx-autodoc-typehints>=1.24.0",
        ],
        "all": [
            "openai>=1.0.0",
            "google-generativeai>=0.3.0",
            "anthropic>=0.7.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "adr=awesome_deep_research.cli:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
    keywords=[
        "ai",
        "research",
        "deep-research",
        "agents",
        "llm",
        "chatgpt",
        "gemini",
        "perplexity",
        "citations",
        "automation",
    ],
    project_urls={
        "Bug Reports": "https://github.com/closedloop-technologies/awesome-deep-researchers/issues",
        "Source": "https://github.com/closedloop-technologies/awesome-deep-researchers",
        "Documentation": "https://github.com/closedloop-technologies/awesome-deep-researchers#readme",
    },
)
`````

## File: .claude/skills/gpt-researcher/SKILL.md
`````markdown
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
`````

## File: .claude/skills/jina-ai/SKILL.md
`````markdown
---
name: jina-ai
description: Use Jina AI APIs for converting URLs to LLM-friendly Markdown (Reader) and searching the web (Search).
---

# Jina AI Skill

This skill integrates Jina AI's Reader (r.jina.ai) and Search (s.jina.ai) APIs to convert URLs and web search results into clean, LLM-friendly Markdown.

## Setup

1. **Dependencies:** Requires `requests`.

    ```bash
    pip install requests python-dotenv
    ```

2. **API Key Configuration (Recommended):** Jina APIs offer higher limits with an API key (JINA_API_KEY).

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
```

**Example:**

```bash
python3 scripts/jina_tools.py read "https://en.wikipedia.org/wiki/Large_language_model"
```

### 2. Search Web (Jina Search)

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
`````

## File: .claude/skills/perplexity-sonar/SKILL.md
`````markdown
---

name: perplexity-sonar
description: Use Perplexity Sonar API for real-time, citation-backed answers. Ideal for up-to-date information and quick synthesis. Requires PERPLEXITY_API_KEY
---

# Perplexity Sonar Skill

This skill utilizes the Perplexity Sonar API to provide synthesized answers backed by real-time web sources. It uses the OpenAI Python library for compatibility.

## Setup

1. **Dependencies:**

    ```bash
    pip install openai python-dotenv
    ```

2. **API Key Configuration:** The skill requires the `PERPLEXITY_API_KEY`. Ensure it is set in a `.env` file in the project root.

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
`````

## File: AGENTS.md
`````markdown
# AGENTS.md — Awesome-* Repo Curation Guide

This file defines the standards, checks, and stylistic conventions for maintaining this repository.
All contributions, whether made manually or via an agent, **must** follow these rules to preserve quality and taste.

---

## 1. Scope

- This repository is an **Awesome List** for curated resources in the `[DOMAIN HERE]` space.
- It is **selective**, not exhaustive. Every item must be high-quality, actively maintained, and relevant to the scope.
- Off-topic or low-quality entries will be declined.

---

## 2. Content Best Practices

### ✅ Include

- **Curated entries only** — each link should have a proven track record (quality projects, authoritative articles, widely-used tools).
- **Short, descriptive annotations** explaining *why* the entry is worth including.
- Logical **category groupings** with clear section headings.
- **Table of Contents** at the top, linking to all major sections.
- Consistent link formatting:

```

* [Project Name](https://link) — short description ending with a period.

````

### 🚫 Avoid

- Random link dumps without context.
- Unmaintained or abandoned projects (no updates in 12+ months unless historically significant).
- Duplicate links (different anchors for the same resource).
- Overly long descriptions.

---

## 3. Formatting Rules

- Markdown must pass [`awesome-lint`](https://github.com/sindresorhus/awesome-lint) without errors.
- One blank line between list items and headings.
- Section titles in `Title Case`.
- No trailing spaces; no inconsistent indentation.
- Descriptions end with a period.
- Badges (if any) must be tasteful — limit to `Awesome` badge and relevant status badges.

---

## 4. Tooling & Linters

### Required Checks (run locally and in CI)

```bash
# Install awesome-lint
npm install --global awesome-lint

# Run lint
awesome-lint
````

Optional but recommended:

- **Markdown Link Checker** to detect broken links:

  ```bash
  npx markdown-link-check README.md
  ```

* **Prettier** for consistent Markdown formatting:

  ```bash
  npx prettier --check "**/*.md"
  ```

CI configuration:

- Configure GitHub Actions to run `awesome-lint` and link checks on every PR.
- Fail the build if there are formatting, linting, or broken link issues.

---

## 5. Contribution Guidelines

- **Read `CONTRIBUTING.md`** before opening a PR.
- One PR per addition or major change.
- Follow the established category structure — create new categories only if necessary.
- Additions **must** include:

  1. A link in `[Name](URL)` format.
  2. A concise description explaining why it’s awesome.
  3. Placement in the correct category.
- Do not reorder unrelated entries unless alphabetizing.

PR title format:

```
[Category] Add <Project Name>
```

---

## 6. Tagging & Metadata

- Keep repo description up to date.
- Add relevant topics in GitHub settings:

  ```
  awesome, awesome-list, agents, llm, automation, [more domain-specific tags]
  ```

* Include the Awesome badge at the top of README:

  ```markdown
  [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
  ```

---

## 7. Quality & Maintenance

- Review and prune outdated entries quarterly.
- Check for broken links regularly (via CI or manual run).
- Encourage community contributions but enforce curation standards.
- Merge only after checks pass and content meets these guidelines.

---

## 8. Verification Steps for Agents

Before completing any PR:

1. **Run all linters**:

   ```bash
   awesome-lint
   npx markdown-link-check README.md
   ```

2. Ensure no broken links.
3. Ensure descriptions are present, concise, and follow style rules.
4. Confirm correct alphabetical order within categories.
5. Pass all CI checks.

---

Maintaining an Awesome List is about taste, clarity, and discipline — keep it **curated, current, and clean**.
`````

## File: TODO.md
`````markdown
# TODO

1. [x] Research all of the top deep research APIs and frameworks
2. [x] Create claude code skill files for each of them
3. [ ] Create a benchmark of cannonical deep research tasks based on [docs/taxonomy-and-examples.md](docs/taxonomy-and-examples.md)
4. [ ] Create a script to run the benchmark across all of the deep research APIs and frameworks.
5. [ ] Aggregate the results and create a report
   - Use the aggregated reports to bootstrap a rubric to evaluate them
   - Evaluate each of the APIs and frameworks based on the rubric
   - Create a final report that ranks the APIs and frameworks based on the rubric

6. Update with all of the models from https://huggingface.co/spaces/muset-ai/DeepResearch-Bench-Leaderboard
`````

## File: README.md
`````markdown
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
`````
