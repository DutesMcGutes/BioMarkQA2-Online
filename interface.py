from biomarkqa2.data_processing import load_papers
from biomarkqa2.retrieval import retrieve_sections
from biomarkqa2.generation import generate_answer
from biomarkqa2 import config

def query_papers(query_text):
    """
    Handles the end-to-end process: loading papers, querying, and generating answers.

    Args:
        query_text (str): The biomarker-related query.

    Returns:
        str: Final response to the query.
    """
    print("[INFO] Loading papers...")
    docs = load_papers(config.PAPER_DIRECTORY)
    
    print("[INFO] Retrieving relevant sections...")
    response = retrieve_sections(docs, query_text)
    
    print("[INFO] Generating answer...")
    return generate_answer(response)

if __name__ == "__main__":
    query = input("Enter your biomarker query: ")
    print(query_papers(query))
