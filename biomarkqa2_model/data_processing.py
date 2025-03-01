import os
import streamlit as st
from paperqa import Docs

@st.cache_data  # Ensures papers are only loaded once per session
def load_papers(directory):
    """
    Loads academic papers into the PaperQA Docs object and caches them.

    Args:
        directory (str): Path to the directory containing papers.

    Returns:
        Docs: A PaperQA Docs object containing loaded papers.
    """
    docs = Docs()
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if file_path.endswith(".pdf"):  # Ensure only PDFs are loaded
            try:
                docs.add(file_path)
            except Exception as e:
                print(f"⚠️ Error loading {filename}: {str(e)}")
    
    print(f"📄 Total Papers Loaded: {len(docs.docs)}")
    return docs
