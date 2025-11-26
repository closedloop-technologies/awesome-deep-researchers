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
