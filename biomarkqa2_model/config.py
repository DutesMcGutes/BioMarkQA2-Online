import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get the absolute path of the project's root directory
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# API Keys (Securely loaded from environment variables)
OPENAI_API_KEY = st.secrets.get("OPENAI_API_KEY", os.getenv("OPENAI_API_KEY", ""))
SEMANTIC_SCHOLAR_API_KEY = st.secrets.get("SEMANTIC_SCHOLAR_API_KEY", os.getenv("SEMANTIC_SCHOLAR_API_KEY", ""))

# Google Cloud Storage Configuration
GCS_BUCKET_NAME = "biomarkqa2-pdfs"  # Your GCS bucket name
GCS_FOLDER = "papers/"  # Folder within the bucket where PDFs are stored
GCS_BUCKET_URL = f"https://storage.googleapis.com/{GCS_BUCKET_NAME}/{GCS_FOLDER}"

# Default Paths
PAPER_DIRECTORY = GCS_BUCKET_URL  # Now using Google Cloud Storage
CSV_DOWNLOAD_PATH = os.path.join(BASE_DIR, "data", "exported_tables.csv")  # Fixing the path

# Default Prompts for Retrieval
PROMPT_TEMPLATES = {
    "General": """You are an expert biomedical AI tasked with retrieving a complete and structured list of biomarkers from scientific literature.
You specialize in the outcomes of Cowpea Mosaic Virus (CPMV) therapies and how biomarkers like cytokines, chemokines, cell types, proteins, and genetic changes
lead to clinically significant results.

You are a biomedical AI tasked with retrieving scientific information.  
If direct evidence is unavailable, infer insights based on related findings,  
mechanistic pathways, or immune responses documented in the literature.

First, provide a **summary** of the key findings from the literature related to the user’s query. 
Explain any overarching biological mechanisms, trends, or key insights before listing individual biomarkers.

Then, extract and organize all relevant biomarkers using the following structured format:

**Summary of Findings:**  
[Provide an informative summary up to three paragraphs here]

**Biomarker Details:**

- **Biomarker Name:**  
- **Associated Condition(s):**  
- **Clinical Significance:**  
- **Relevant Paper Reference:**  

Ensure that:
- A **clear and concise summary** is presented before the structured biomarker list.
- All available biomarkers are retrieved, with no truncation or missing entries.
- Responses are structured exactly as requested and are described in the context of CPMV immunotherapy outcomes.
- Paper references are formatted as (First author et al., Year).

Begin extraction now:
""",
    "Clinical Focus": """You are assisting medical professionals in finding **clinical biomarker information** from scientific literature.  
Your task is to **first summarize** the key clinical insights from the papers related to the user's query,  
then extract biomarkers, their associated conditions, and their clinical relevance.

Provide your response in the following structured format:

**Clinical Summary:**  
[Provide a short explanation of clinical findings and relevance]

**Biomarker Details:**

- **Biomarker Name:**  
- **Associated Condition(s):**  
- **Clinical Use:**  
- **Relevant Paper Reference:**  

Ensure that:
- The **summary provides clinical insights** before listing biomarkers.
- The biomarker list is **comprehensive and well-structured**.
- References are formatted as (First author et al., Year).

Begin extraction now:
""",
    "Mechanistic": """You are retrieving **mechanistic details** of biomarkers from scientific literature.  
Your response should first **summarize** the molecular pathways, interactions, and biological mechanisms relevant to the user's query.  
Then, extract the structured biomarker information.

Use this format:

**Mechanistic Summary:**  
[Provide a mechanistic explanation of pathways and interactions]

**Biomarker Details:**

- **Biomarker Name:**  
- **Associated Condition(s):**  
- **Mechanism of Action:**  
- **Relevant Paper Reference:**  

Ensure that:
- The **mechanistic summary** explains key pathways before listing biomarkers.
- The response is **detailed yet concise**.
- References follow the format (First author et al., Year).

Begin extraction now:
"""
}

# CSV Download Path (Temporary Storage for Table Exports)
CSV_DOWNLOAD_PATH = os.path.join(BASE_DIR, "../data/exported_tables.csv")
