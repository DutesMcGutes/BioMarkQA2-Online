import os
from paperqa import Docs

def load_papers(directory):
    """
    Loads papers from the given directory into the PaperQA Docs object.
    
    Args:
        directory (str): Path to the folder containing PDF and text files.

    Returns:
        Docs: A PaperQA Docs instance containing all loaded documents.
    """
    docs = Docs()
    for filename in os.listdir(directory):
        if filename.endswith('.pdf') or filename.endswith('.txt'):
            docs.add(os.path.join(directory, filename))
    return docs
