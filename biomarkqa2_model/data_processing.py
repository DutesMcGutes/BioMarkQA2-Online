import requests
from paperqa import Docs
from biomarkqa2_model import config

def load_papers():
    """
    Dynamically loads PDFs from Google Cloud Storage into PaperQA.
    """
    doc_collection = Docs()

    # List of known PDFs in GCS (If listing is needed, we can automate it)
    paper_filenames = [
        "10.1002@mabi.201800407.pdf",
        "10.1021@acsnano.0c08430.pdf",
        "10.1177_1535370216647123.pdf"
    ]

    # Download and add PDFs to PaperQA dynamically
    for filename in paper_filenames:
        file_url = f"{config.GCS_BUCKET_URL}{filename}"
        response = requests.get(file_url)

        if response.status_code == 200:
            # Save temp file and load into PaperQA
            temp_path = f"/tmp/{filename}"
            with open(temp_path, "wb") as f:
                f.write(response.content)
            doc_collection.add(temp_path)
        else:
            print(f"⚠️ Failed to fetch {filename} from GCS")

    return doc_collection
