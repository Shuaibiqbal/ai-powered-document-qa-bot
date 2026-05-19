import streamlit as st 
from dotenv import load_dotenv
import os 

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

st.set_page_config(
    page_title="AI-Powered Document A&A Bot",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI-Powered Document Q&A Bot")
st.markdown("Upload a PDF and ask any question about it.")

if not api_key:
    st.error("❌ OpenAI API key not found. Please add it to your .env file.")
    st.stop()
else:
    st.success("✅ API key loaded successfully.")

st.subheader("Upload Your PDF")
uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file:
    st.info(f"File uploaded: **{uploaded_file.name}**")
else:
    st.warning("Please upload a PDF to get started.")