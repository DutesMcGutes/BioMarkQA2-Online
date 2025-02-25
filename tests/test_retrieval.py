from biomarkqa2.retrieval import retrieve_sections
from biomarkqa2.data_processing import load_papers
import config

def test_retrieval():
    docs = load_papers(config.PAPER_DIRECTORY)
    query = "What biomarkers are associated with cardiovascular disease?"
    response = retrieve_sections(docs, query)
    
    assert response, "Retrieval failed."
    print("✅ Retrieval test passed.")

if __name__ == "__main__":
    test_retrieval()
