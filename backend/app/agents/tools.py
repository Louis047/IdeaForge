from crewai.tools import BaseTool
import json
from duckduckgo_search import DDGS
from pydantic import Field

class WebSearchTool(BaseTool):
    name: str = "Web Search Tool"
    description: str = "Search the web for current market trends, competitors, and industry reports."
    
    def _run(self, query: str) -> str:
        """Execute the web search."""
        try:
            with DDGS() as ddgs:
                results = list(ddgs.text(query, max_results=5))
                if not results:
                    return f"No results found for '{query}'."
                return json.dumps(results, indent=2)
        except Exception as e:
            return f"Error executing search: {str(e)}"

class AcademicSearchTool(BaseTool):
    name: str = "Academic Search Tool"
    description: str = "Search Semantic Scholar for academic papers, patents, and scientific research."
    
    def _run(self, query: str) -> str:
        """
        Mock for Semantic Scholar integration.
        In a full implementation, you'd use the Semantic Scholar API here.
        """
        import time
        time.sleep(1) # simulate network request
        
        # We return a mock response that the LLM can parse
        mock_results = [
            {
                "title": f"Recent advances in {query}",
                "url": "https://api.semanticscholar.org/123",
                "authors": ["Author A", "Author B"],
                "year": 2023,
                "abstract": f"This paper explores novel approaches in {query}. We found significant potential for commercialization."
            },
            {
                "title": f"Current challenges and opportunities in {query}",
                "url": "https://api.semanticscholar.org/456",
                "authors": ["Author C"],
                "year": 2024,
                "abstract": f"A comprehensive review of the current bottlenecks applying machine learning to {query}."
            }
        ]
        
        return json.dumps(mock_results, indent=2)
