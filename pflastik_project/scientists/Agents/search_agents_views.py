from django.shortcuts import render, redirect, get_object_or_404
from ..forms import SearchForm
from ..models import SearchQuery, SearchResult
import os
import requests
from bs4 import BeautifulSoup
from googlesearch import search
from together import Together
from typing import List, Dict, Optional
from django.urls import reverse

# test it export TOGETHER_API_KEY="56ebf1cf19d9c7a2ee45c091ac4c4109d5fb53cb58700c93b57d3a3e36f77a88"

# Constants for token limits . increase it if you find the model can't understnad from this chunk . 
MAX_TOKENS = 8192 
CHUNK_SIZE = 3000  

def initialize_client(api_key: str) -> Together:
    print("Initializing Together AI client...")
    return Together(api_key=api_key)

def perform_search(query: str, num_results: int = 10) -> List[str]:
    print(f"Performing Google search for query: {query}")
    return search(query, num_results=num_results)

def fetch_and_parse(url: str) -> Optional[str]:
    try:
        print(f"Fetching content from URL: {url}")
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        text_content = ' '.join([p.get_text() for p in soup.find_all('p')])
        return text_content
    except Exception as e:
        print(f"Error fetching/parsing {url}: {e}")
        return None

def chunk_content(content: str, chunk_size: int = CHUNK_SIZE) -> List[str]:
    # Split the content into chunks
    return [content[i:i + chunk_size] for i in range(0, len(content), chunk_size)]

def analyze_content_with_agents(client: Together, contents: List[str]) -> List[Dict[str, str]]:
    descriptions = []
    
    for content in contents:
        chunks = chunk_content(content)
        for chunk in chunks:
            print("Analyzing chunk with specialized agents...")
            # Agent 1: Summarize the content
            summary_prompt = "You are a plant scientist specializing in plant diseases. Summarize the following content: "
            try:
                summary = client.chat.completions.create(
                    model="meta-llama/Meta-Llama-3-8B-Instruct-Lite",
                    messages=[{"role": "user", "content": f"{summary_prompt} {chunk}"}]
                ).choices[0].message.content
                print("Summary generated.")
            except Exception as e:
                print(f"Error generating summary: {e}")
                summary = "Error generating summary."

            # Agent 2: Extract the main topics
            topics_prompt = "Identify the key topics related to plant science, especially plant diseases, in the following content: "
            try:
                topics = client.chat.completions.create(
                    model="meta-llama/Meta-Llama-3-8B-Instruct-Lite",
                    messages=[{"role": "user", "content": f"{topics_prompt} {summary}"}]
                ).choices[0].message.content
                print("Key topics identified.")
            except Exception as e:
                print(f"Error identifying topics: {e}")
                topics = "Error identifying topics."

            # Agent 3: Assess the relevance to plant science
            relevance_prompt = "As an expert in plant science, assess how relevant the following content is to the study of plant diseases: "
            try:
                relevance = client.chat.completions.create(
                    model="meta-llama/Meta-Llama-3-8B-Instruct-Lite",
                    messages=[{"role": "user", "content": f"{relevance_prompt} {topics}"}]
                ).choices[0].message.content
                print("Relevance assessment completed.")
            except Exception as e:
                print(f"Error assessing relevance: {e}")
                relevance = "Error assessing relevance."

            descriptions.append({
                "summary": summary,
                "topics": topics,
                "relevance": relevance
            })

    return descriptions


def search_view(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            query_text = form.cleaned_data['query']
            search_query = SearchQuery.objects.create(query=query_text)

            # Initialize the Together client
            api_key = os.environ.get('TOGETHER_API_KEY')
            if not api_key:
                print("Error: TOGETHER_API_KEY not found in environment variables.")
                return redirect(reverse('search_agents')) # Redirect to the search form if API key is missing

            client = initialize_client(api_key)

            # Perform Google search
            search_results = perform_search(query_text)

            # Fetch and parse content
            parsed_contents = []
            for url in search_results:
                content = fetch_and_parse(url)
                if content:
                    parsed_contents.append(content)

            # Analyze content with specialized agents
            if parsed_contents:
                analysis_results = analyze_content_with_agents(client, parsed_contents)

                # Save results to the database
                for result in analysis_results:
                    SearchResult.objects.create(
                        query=search_query,
                        summary=result['summary'],
                        topics=result['topics'],
                        relevance=result['relevance']
                    )

            return redirect('search_results', query_id=search_query.id)
    else:
        form = SearchForm()

    return render(request, 'search_agents.html', {'form': form})

def results_view(request, query_id):
    query = get_object_or_404(SearchQuery, id=query_id)
    results = query.results.all()
    return render(request, 'search_results.html', {'query': query, 'results': results})
