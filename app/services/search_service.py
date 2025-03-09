import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Google Custom Search API setup
CSE_ID = os.getenv('CSE_ID')  # Custom Search Engine ID
SEARCH_API_KEY = os.getenv('SEARCH_API_KEY')  # Google Custom Search API key

def perform_web_search(query: str):
    """
    Perform a web search using Google Custom Search API and return relevant search results.
    """
    url = f'https://www.googleapis.com/customsearch/v1?q={query}&key={SEARCH_API_KEY}&cx={CSE_ID}'
    response = requests.get(url)
    search_results = response.json()

    if 'items' in search_results:
        search_items = [
            {
                'title': item['title'],
                'snippet': item['snippet'],
                'link': item['link']
            }
            for item in search_results['items']
        ]
        return search_items
    else:
        return []
