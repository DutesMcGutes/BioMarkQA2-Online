import os
import requests
import concurrent.futures
from paperqa import Docs
import streamlit as st
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

    # Use Streamlit session state or fallback to the default key
    api_key = st.session_state.get("semantic_api_key", config.SEMANTIC_SCHOLAR_API_KEY)

    headers = {"x-api-key": api_key}
    params = {"query": query, "fields": "title,authors,year,url,abstract"}

    try:
        response = requests.get(API_URL, headers=headers, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"Failed to fetch data: {response.status_code}"}
    except requests.RequestException as e:
        return {"error": f"Semantic Scholar request failed: {e}"}


def retrieve_sections(docs, query_text):
    """
    Queries the document database and retrieves structured biomarker information.

    Args:
        docs (Docs): PaperQA Docs instance.
        query_text (str): The user query related to biomarkers.

    Returns:
        str: Retrieved text relevant to the query.
    """
    
    # Run PaperQA and Semantic Scholar in parallel
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_paperqa = executor.submit(docs.query, query_text)
        future_semantic = executor.submit(query_semantic_scholar, query_text)

        paperqa_response = future_paperqa.result()
        semantic_results = future_semantic.result()

    # Process PaperQA Response
    if paperqa_response and paperqa_response.answer.strip():
        return format_response(paperqa_response.answer)

    # Process Semantic Scholar Results
    if "data" in semantic_results and semantic_results["data"]:
        result_text = "**Additional Semantic Scholar Results:**\n\n"
        for paper in semantic_results["data"][:3]:  # Limit results to 3
            authors = ', '.join([a['name'] for a in paper['authors']]) if paper['authors'] else "Unknown Authors"
            result_text += f"- **{paper['title']}** ({paper['year']}) by {authors}\n"
            result_text += f"  [Read More]({paper['url']})\n\n"
        return result_text

    return "No relevant biomarkers found."


def format_response(text):
    """
    Formats the retrieved response for better readability.

    Args:
        text (str): The retrieved text response.

    Returns:
        str: Formatted response.
    """
    return text
