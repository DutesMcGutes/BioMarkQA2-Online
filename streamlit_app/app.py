import streamlit as st
import pandas as pd
import threading
import os
from PIL import Image
from biomarkqa2.retrieval import retrieve_sections
from biomarkqa2.data_processing import load_papers
from biomarkqa2 import config

# --- STREAMLIT PAGE SETTINGS ---
st.set_page_config(page_title="BioMarkQA2 Chat", layout="wide")

# --- Define Paths for Logo Files ---
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))  # Moves up to root directory
LOGO_LIGHT = os.path.join(ROOT_DIR, "logo_light.png")
LOGO_DARK = os.path.join(ROOT_DIR, "logo_dark.png")

# --- Load PNG Images Safely ---
def load_image(file_path):
    """Loads a PNG image if it exists."""
    if os.path.exists(file_path):
        return Image.open(file_path)
    return None

light_logo = load_image(LOGO_LIGHT)
dark_logo = load_image(LOGO_DARK)

# --- Detect Dark/Light Mode & Display Logo ---
if "theme" not in st.session_state:
    st.session_state.theme = "light"  # Default theme

st.sidebar.header("🌓 Theme Selection")
theme_choice = st.sidebar.radio("Choose Theme:", ["Auto", "Light", "Dark"])

if theme_choice == "Auto":
    st.session_state.theme = "auto"
elif theme_choice == "Light":
    st.session_state.theme = "light"
elif theme_choice == "Dark":
    st.session_state.theme = "dark"

# Display logo in center
st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)

if st.session_state.theme == "dark" and dark_logo:
    st.image(dark_logo, use_column_width=True)
elif st.session_state.theme == "light" and light_logo:
    st.image(light_logo, use_column_width=True)
elif light_logo:  # Default to light mode logo if auto-detection fails
    st.image(light_logo, use_column_width=True)

st.markdown("</div>", unsafe_allow_html=True)

# --- SESSION STATE INITIALIZATION ---
if "api_key" not in st.session_state:
    st.session_state.api_key = config.OPENAI_API_KEY  # Default from config
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "selected_prompt" not in st.session_state:
    st.session_state.selected_prompt = list(config.PROMPT_TEMPLATES.keys())[0]
if "table_df" not in st.session_state:
    st.session_state.table_df = None

# --- CACHE DOCUMENT LOADING ---
@st.cache_data
def load_cached_papers():
    return load_papers(config.PAPER_DIRECTORY)

if "docs" not in st.session_state:
    st.session_state.docs = load_cached_papers()

docs = st.session_state.docs  # Reuse loaded docs

# --- OPENAI API KEY INPUT ---
st.sidebar.header("🔑 API Settings")
st.session_state.api_key = st.sidebar.text_input(
    "Enter your OpenAI API Key:", value=st.session_state.api_key, type="password"
)

# --- PROMPT SELECTION ---
st.sidebar.header("📜 Select Prompt Template")
st.session_state.selected_prompt = st.sidebar.selectbox(
    "Choose a prompt:", list(config.PROMPT_TEMPLATES.keys())
)

# --- CHAT INPUT ---
user_query = st.text_input("Enter your question:", placeholder="What biomarkers are associated with breast cancer?")

# --- HANDLE CHAT SUBMISSION ---
if st.button("Send"):
    if not st.session_state.api_key:
        st.warning("⚠️ Please enter an OpenAI API key.")
    else:
        # Retrieve answer with structured prompt
        prompt_text = config.PROMPT_TEMPLATES[st.session_state.selected_prompt] + "\n\n" + user_query
        response = retrieve_sections(docs, prompt_text)

        # Store in chat history
        st.session_state.chat_history.append({"query": user_query, "response": response})

# --- Custom CSS for Larger Bolded Chat Names ---
st.markdown("""
    <style>
        .chat-name {
            font-size: 18px !important;  /* Increase font size */
            font-weight: bold !important; /* Make it bold */
            color: #333; /* Adjust color for readability */
        }
    </style>
""", unsafe_allow_html=True)

# --- DISPLAY CHAT HISTORY WITH STYLING ---
st.subheader("💬 Chat History")
for entry in st.session_state.chat_history[::-1]:  # Reverse to show newest first
    with st.chat_message("user"):
        st.markdown(f"<span class='chat-name'>User:</span> <br> {entry['query']}", unsafe_allow_html=True)  # Styled User Name

    with st.chat_message("assistant"):
        st.markdown(f"<span class='chat-name'>BioMarkQA2:</span> <br> {entry['response']}", unsafe_allow_html=True)  # Styled Assistant Name


# --- TABLE GENERATION SECTION ---
st.sidebar.header("📊 Generate Table")
table_query = st.sidebar.text_input("Enter biomarker table request:", placeholder="List biomarkers for lung cancer")

def generate_table_async():
    """
    Runs the biomarker table generation in the background using threading.
    """
    structured_query = (
        "Generate a structured table of biomarkers with rows for Name, Condition, and Clinical Use.\n\n"
        + table_query
    )
    table_response = retrieve_sections(docs, structured_query)

    try:
        df = pd.DataFrame(
            [row.split(",") for row in table_response.split("\n") if row],
            columns=["Biomarker", "Condition", "Clinical Use"]
        )
        st.session_state.table_df = df

        # Save to CSV
        df.to_csv(config.CSV_DOWNLOAD_PATH, index=False)
    except:
        st.session_state.table_df = None

if st.sidebar.button("Generate Table"):
    if not st.session_state.api_key:
        st.sidebar.warning("⚠️ Please enter an OpenAI API key.")
    else:
        thread = threading.Thread(target=generate_table_async)
        thread.start()

# --- DISPLAY GENERATED TABLE ---
if st.session_state.table_df is not None:
    st.sidebar.subheader("📋 Biomarker Table")
    st.sidebar.dataframe(st.session_state.table_df)
    st.sidebar.download_button("📥 Download Table", config.CSV_DOWNLOAD_PATH, file_name="biomarkers.csv", mime="text/csv")
