from django.shortcuts import render, redirect
from ..forms import AgentRequestForm
from ..models import AgentResponse
import asyncio
import together
import requests
from typing import List, Dict, Any

# Blockchain agent to interact with the Flask blockchain API
class BlockchainAgent:
    def __init__(self, base_url: str) -> None:
        self.base_url = base_url

    def fetch_block(self, index: int) -> Dict[str, Any]:
        response = requests.get(f"{self.base_url}/get_gen_chain_block/{index}")
        print(f"[DEBUG] Fetched block at index {index}: {response.json()}")
        return response.json()

    def search_entries(self, term: str) -> List[Dict[str, Any]]:
        response = requests.get(f"{self.base_url}/search_entries", params={'search_term': term})
        print(f"[DEBUG] Search results for term '{term}': {response.json()}")
        return response.json()

# Agent to perform analysis using the Together API
class AnalysisAgent:
    def __init__(self, api_key: str) -> None:
        self.client = together.Together(api_key=api_key)

    async def summarize_data(self, data: Dict[str, Any]) -> str:
        prompt = f"Summarize the following data: {data}"
        response = await self.client.chat.completions.create(
            model="meta-llama/Meta-Llama-3-8B-Instruct-Lite",
            messages=[{"role": "user", "content": prompt}]
        )
        print(f"[DEBUG] Summary of data: {response.choices[0].message.content}")
        return response.choices[0].message.content

# Agent to aggregate multiple responses into a single coherent output
class AggregationAgent:
    def __init__(self, api_key: str, aggregator_model: str) -> None:
        self.client = together.Together(api_key=api_key)
        self.aggregator_model = aggregator_model

    async def aggregate_responses(self, responses: List[str]) -> str:
        system_prompt = "You have been provided with a set of responses from various open-source models. Your task is to synthesize these responses into a single, high-quality response."
        final_prompt = system_prompt + "\n" + "\n".join([f"{i+1}. {response}" for i, response in enumerate(responses)])
        
        response = await self.client.chat.completions.create(
            model=self.aggregator_model,
            messages=[
                {"role": "system", "content": final_prompt},
                {"role": "user", "content": "Aggregate the information into a coherent summary."}
            ]
        )
        print(f"[DEBUG] Aggregated response: {response.choices[0].message.content}")
        return response.choices[0].message.content

async def run_agents(request_data: Dict[str, Any]) -> str:
    block_index = request_data['block_index']
    search_term = request_data['search_term']
    api_key = request_data['api_key']

    blockchain_agent = BlockchainAgent(base_url="http://127.0.0.1:8000")
    analysis_agent = AnalysisAgent(api_key=api_key)
    aggregation_agent = AggregationAgent(api_key=api_key, aggregator_model="mistralai/Mixtral-8x22B-Instruct-v0.1")

    # Fetch data from blockchain
    block_data = blockchain_agent.fetch_block(block_index)
    search_results = blockchain_agent.search_entries(search_term)

    # Analyze data
    summary_block_data = await analysis_agent.summarize_data(block_data)
    summary_search_results = await analysis_agent.summarize_data(search_results)

    # Aggregate responses
    final_summary = await aggregation_agent.aggregate_responses([summary_block_data, summary_search_results])

    return final_summary

def agent_request_view(request):
    if request.method == 'POST':
        form = AgentRequestForm(request.POST)
        if form.is_valid():
            # Run the agents asynchronously
            final_summary = asyncio.run(run_agents(form.cleaned_data))

            # Save the result in the database
            agent_response = form.save(commit=False)
            agent_response.final_summary = final_summary
            agent_response.save()

            return redirect('agent_result', pk=agent_response.pk)
    else:
        form = AgentRequestForm()

    return render(request, 'scientist/agent_request.html', {'form': form})

def agent_result_view(request, pk):
    agent_response = AgentResponse.objects.get(pk=pk)
    return render(request, 'scientist/agent_result.html', {'agent_response': agent_response})
