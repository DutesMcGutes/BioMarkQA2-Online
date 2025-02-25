from paperqa import Docs

# Define a structured prompt template
PROMPT_TEMPLATE = """
You are a biomedical literature expert. Your task is to extract relevant information from scientific papers. 
Focus on biomarkers, their roles, associated conditions, and clinical significance.
Use the following structured format:

- **Biomarker Name:** 
- **Associated Condition(s):** 
- **Clinical Significance:** 
- **Relevant Paper Reference:** 

Now, answer this query: {query_text}
"""

def retrieve_sections(docs, query_text):
    """
    Queries the document database with a structured prompt.

    Args:
        docs (Docs): PaperQA Docs instance.
        query_text (str): The user query related to biomarkers.

    Returns:
        str: Retrieved text relevant to the query.
    """
    formatted_query = PROMPT_TEMPLATE.format(query_text=query_text)
    response = docs.query(formatted_query)  # Uses PaperQA's `query` method
    
    if response:
        return response.answer
    else:
        return "No relevant sections found."
