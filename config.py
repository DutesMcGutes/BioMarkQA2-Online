import os

# Base directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Directory where papers are stored
PAPER_DIRECTORY = os.path.join(BASE_DIR, "../data/papers")

# Default Prompts for retrieval
PROMPT_TEMPLATES = {
    "General": "Extract key biomarkers and summarize their clinical significance.",
    "Clinical Focus": "Retrieve only clinically validated biomarkers and their approved medical applications.",
    "Mechanistic": "Describe the molecular mechanisms and pathways of each biomarker.",
}

# Default Model (Can be overridden in Streamlit UI)
DEFAULT_LLM_MODEL = "gpt-3.5-turbo"

# Default OpenAI API Key (Optional: can be set manually here, but best to enter in the UI)
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")

# CSV Download Path (Temporary Storage for Table Exports)
CSV_DOWNLOAD_PATH = os.path.join(BASE_DIR, "../data/exported_tables.csv")
