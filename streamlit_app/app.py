import streamlit as st
import os
import sys
import pandas as pd
import re
from biomarkqa2_model.retrieval import retrieve_sections
from biomarkqa2_model.data_processing import load_papers
from biomarkqa2_model import config

# Ensure the root directory is in Python's path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# --- STREAMLIT PAGE SETTINGS ---
st.set_page_config(page_title="BioMarkQA2 Chat", layout="wide")

# --- Define Paths for Logo Files ---
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))  # Moves up to root directory
LOGO_LIGHT = os.path.join(ROOT_DIR, "logo_light.png")  # Light mode logo
LOGO_DARK = os.path.join(ROOT_DIR, "logo_dark.png")  # Dark mode logo

# --- Sidebar Theme Selection ---
st.sidebar.header("🌓 Theme Selection")
theme_choice = st.sidebar.radio("Choose Theme:", ["Auto", "Light", "Dark"])

# --- Detect Dark/Light Mode & Display Logo ---
if theme_choice == "Auto":
    theme_detected = st.get_option("theme.base")  # Detect Streamlit's system theme
elif theme_choice == "Light":
    theme_detected = "light"
elif theme_choice == "Dark":
    theme_detected = "dark"

# Display logo in the center with dynamic sizing
st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)

if theme_detected == "dark":
    st.image(LOGO_DARK, use_container_width=True)
else:
    st.image(LOGO_LIGHT, use_container_width=True)

st.markdown("</div>", unsafe_allow_html=True)

# --- SESSION STATE INITIALIZATION ---
if "api_key" not in st.session_state:
    st.session_state.api_key = config.OPENAI_API_KEY  # Default from config
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "selected_prompt" not in st.session_state:
    st.session_state.selected_prompt = list(config.PROMPT_TEMPLATES.keys())[0]
if "table_df" not in st.session_state:
    st.session_state.table_df = None  # Store table data

st.sidebar.header("🔑 API Settings")

# LOCKED API KEY INPUTS (Users cannot edit)
st.sidebar.text_input(
    "OpenAI API Key (Locked):",
    value="●●●●●●●●●●●●●●",
    type="password",
    disabled=True  # Prevents user from modifying
)

st.sidebar.text_input(
    "Semantic Scholar API Key (Locked):",
    value="●●●●●●●●●●●●●●",
    type="password",
    disabled=True  # Prevents user from modifying
)

# --- PROMPT SELECTION ---
st.sidebar.header("📜 Select Prompt Template")
st.session_state.selected_prompt = st.sidebar.selectbox(
    "Choose a prompt:", list(config.PROMPT_TEMPLATES.keys())
)

# --- CHAT INPUT ---
user_query = st.text_input("💬 Enter your question:", placeholder="What biomarkers are associated with breast cancer?")

# --- HANDLE CHAT SUBMISSION ---
if st.button("Send"):
    if not st.session_state.api_key:
        st.warning("⚠️ Please enter an OpenAI API key.")
    else:
        docs = load_papers()  # Now automatically loads from GCS
        prompt_text = config.PROMPT_TEMPLATES[st.session_state.selected_prompt] + "\n\n" + user_query
        response = retrieve_sections(docs, prompt_text)

        # Store in chat history
        st.session_state.chat_history.append({"query": user_query, "response": response})

# --- DISPLAY CHAT HISTORY ---
st.subheader("📝 Chat History")
for entry in st.session_state.chat_history[::-1]:  # Reverse to show newest first
    st.markdown(f"**User:** {entry['query']}")
    st.markdown(f"**BioMarkQA2:**\n{entry['response']}")
    st.divider()

# --- TABLE GENERATION SECTION ---
st.sidebar.header("📊 Generate Biomarker Table")
table_query = st.sidebar.text_input("Enter a query for structured biomarkers:", placeholder="List biomarkers for lung cancer")

# --- Function to Extract Biomarker Data ---
def extract_biomarkers(response_text):
    """
    Parses structured biomarker details from the model's response.

    Args:
        response_text (str): The retrieved text response.

    Returns:
        list of dict: Parsed biomarker data for DataFrame conversion.
    """
    biomarker_list = []
    biomarker_entries = response_text.split("\n\n")  # Split by blank lines

    for entry in biomarker_entries:
        biomarker = {}
        biomarker["Biomarker Name"] = re.search(r"\*\*Biomarker Name:\*\*\s*(.*)", entry)
        biomarker["Associated Condition(s)"] = re.search(r"\*\*Associated Condition\(s\):\*\*\s*(.*)", entry)
        biomarker["Clinical Significance"] = re.search(r"\*\*Clinical Significance:\*\*\s*(.*)", entry)
        biomarker["Relevant Paper Reference"] = re.search(r"\*\*Relevant Paper Reference:\*\*\s*(.*)", entry)

        if biomarker["Biomarker Name"]:
            biomarker_list.append({key: val.group(1) if val else "N/A" for key, val in biomarker.items()})

    return biomarker_list

# --- TABLE GENERATION LOGIC ---
if st.sidebar.button("Generate Table"):
    if not st.session_state.api_key:
        st.sidebar.warning("⚠️ Please enter an OpenAI API key.")
    else:
        structured_query = config.PROMPT_TEMPLATES[st.session_state.selected_prompt] + "\n\n" + table_query
        table_response = retrieve_sections(load_papers(config.PAPER_DIRECTORY), structured_query)

        # Convert response into table format
        biomarker_data = extract_biomarkers(table_response)
        
        if biomarker_data:
            df = pd.DataFrame(biomarker_data)
            st.session_state.table_df = df
        else:
            st.session_state.table_df = None
            st.sidebar.error("❌ Failed to extract structured biomarker details.")

# --- DISPLAY TABLE & DOWNLOAD OPTION ---
if st.session_state.table_df is not None:
    st.sidebar.subheader("📋 Biomarker Table")
    st.sidebar.dataframe(st.session_state.table_df)

    # Save table to CSV
    csv_data = st.session_state.table_df.to_csv(index=False)
    st.sidebar.download_button(
        label="📥 Download Table as CSV",
        data=csv_data,
        file_name="biomarkers.csv",
        mime="text/csv"
    )