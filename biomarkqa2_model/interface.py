from biomarkqa2_model.data_processing import load_papers
from biomarkqa2_model.retrieval import retrieve_sections
from biomarkqa2_model import config

def query_papers(query_text):
    """
    Queries the stored academic papers for relevant biomarker information.

    Args:
        query_text (str): The user query related to biomarkers.

    Returns:
        str: Formatted response with biomarker details.
    """
    docs = load_papers(config.PAPER_DIRECTORY)
    return retrieve_sections(docs, query_text)
