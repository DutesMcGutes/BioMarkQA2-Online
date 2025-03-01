import os
import requests
import asyncio
import concurrent.futures
from paperqa import Docs
from biomarkqa2_model import config

def query_semantic_scholar(query):
    """
    Queries the Semantic Scholar API for relevant biomarker papers.

    Args:
        query (str): The user query related to biomarkers.

    Returns:
        dict: JSON response from Semantic Scholar.
    """
    API_URL = "https://api.semanticscholar.org/graph/v1/paper/search"
    headers = {"x-api-key": config.SEMANTIC_SCHOLAR_API_KEY}
    params = {"query": query, "fields": "title,authors,year,url,abstract"}

    response = requests.get(API_URL, headers=headers, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"Failed to fetch data: {response.status_code}"}

def retrieve_sections(docs, query_text):
    """
    Queries the document database and retrieves structured biomarker information.

    Args:
        docs (Docs): PaperQA Docs instance.
        query_text (str): The user query related to biomarkers.

    Returns:
        str: Retrieved text relevant to the query.
    """
    def query_paperqa():
        return docs.query(query_text)

    def query_semantic():
        return query_semantic_scholar(query_text)

    # Run PaperQA and Semantic Scholar in parallel
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_paperqa = executor.submit(query_paperqa)
        future_semantic = executor.submit(query_semantic)

        paperqa_response = future_paperqa.result()
        semantic_results = future_semantic.result()

    # Process responses
    if paperqa_response and paperqa_response.answer.strip():
        return paperqa_response.answer

    if "data" in semantic_results and semantic_results["data"]:
        result_text = "**Additional Semantic Scholar Results:**\n\n"
        for paper in semantic_results["data"][:3]:  # Limit results to 3
            result_text += f"- **{paper['title']}** ({paper['year']}) by {', '.join([a['name'] for a in paper['authors']])}\n"
            result_text += f"  [Read More]({paper['url']})\n\n"
        return result_text

    return "No relevant biomarkers found."
