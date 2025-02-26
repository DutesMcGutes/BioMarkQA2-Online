import streamlit as st
import os
from biomarkqa2.retrieval import retrieve_sections
from biomarkqa2.data_processing import load_papers
from biomarkqa2 import config

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
    st.image(LOGO_DARK, use_column_width=True)
else:
    st.image(LOGO_LIGHT, use_column_width=True)

st.markdown("</div>", unsafe_allow_html=True)

# --- SESSION STATE INITIALIZATION ---
if "api_key" not in st.session_state:
    st.session_state.api_key = config.OPENAI_API_KEY  # Default from config
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "selected_prompt" not in st.session_state:
    st.session_state.selected_prompt = list(config.PROMPT_TEMPLATES.keys())[0]

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
user_query = st.text_input("💬 Enter your question:", placeholder="What biomarkers are associated with breast cancer?")

# --- HANDLE CHAT SUBMISSION ---
if st.button("Send"):
    if not st.session_state.api_key:
        st.warning("⚠️ Please enter an OpenAI API key.")
    else:
        docs = load_papers(config.PAPER_DIRECTORY)
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
