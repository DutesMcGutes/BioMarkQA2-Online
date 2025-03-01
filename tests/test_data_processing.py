import os
from biomarkqa2_model.data_processing import load_papers
import config

def test_load_papers():
    docs = load_papers(config.PAPER_DIRECTORY)
    assert docs is not None, "Failed to load documents"
    print("✅ Paper loading test passed.")

if __name__ == "__main__":
    test_load_papers()
