from paperqa import Docs  # Correct import based on PaperQA's available methods

def retrieve_sections(docs, query_text):
    """
    Queries the document database to retrieve relevant text sections.

    Args:
        docs (Docs): PaperQA Docs instance.
        query_text (str): The user query related to biomarkers.

    Returns:
        str: Retrieved text relevant to the query.
    """
    response = docs.query(query_text)  # PaperQA uses the `query` method on `Docs`
    
    if response:
        return response.answer
    else:
        return "No relevant sections found."
