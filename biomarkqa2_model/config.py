import os

# Base directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Directory where papers are stored
PAPER_DIRECTORY = os.path.join(BASE_DIR, "../data/papers")

# Default OpenAI API Key (Can be set in UI)
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")

# Load Semantic Scholar API Key from environment variable
SEMANTIC_SCHOLAR_API_KEY = os.getenv("SEMANTIC_SCHOLAR_API_KEY", "")

# Default Prompts for Retrieval
PROMPT_TEMPLATES = {
    "General": """You are an expert biomedical AI tasked with retrieving a complete and structured list of biomarkers from scientific literature.

Please extract and organize all relevant biomarkers using the following format:

- **Biomarker Name:**  
- **Associated Condition(s):**  
- **Clinical Significance:**  
- **Relevant Paper Reference:**  

Ensure that:
- All available biomarkers are retrieved, with no truncation or missing entries.
- Responses are structured exactly as requested.
- Paper references are formatted as (First author et al., Year).

Begin extraction now:
""",
    "Clinical Focus": """You are assisting medical professionals in finding clinical biomarker information. 
Your task is to extract biomarkers, their associated conditions, and their clinical relevance from literature. 
Ensure that results follow this format:

- **Biomarker Name:**  
- **Associated Condition(s):**  
- **Clinical Use:**  
- **Relevant Paper Reference:**  

Begin extraction now:
""",
    "Mechanistic": """You are retrieving mechanistic details of biomarkers from scientific literature. 
Focus on molecular mechanisms and relevance in disease pathways. Use this format:

- **Biomarker Name:**  
- **Associated Condition(s):**  
- **Mechanism of Action:**  
- **Relevant Paper Reference:**  

Begin extraction now:
"""
}

# CSV Download Path (Temporary Storage for Table Exports)
CSV_DOWNLOAD_PATH = os.path.join(BASE_DIR, "../data/exported_tables.csv")
