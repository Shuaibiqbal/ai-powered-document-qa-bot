import streamlit as st 
from dotenv import load_dotenv
import os 
import tempfile
from src.document_loader import load_and_chunk_pdf
from src.vector_store import build_vector_store, load_vector_store
from src.qa_chain import build_qa_chain

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
if "messages" not in st.session_state:
    st.session_state.messages = []
if uploaded_file:
    st.info(f"File uploaded: **{uploaded_file.name}**")
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(uploaded_file.read())
        tmp_path = tmp.name
    if st.button("Process PDF"):
        with st.spinner("Reading and indexing PDF..."):
            chunks = load_and_chunk_pdf(tmp_path)
            build_vector_store(chunks)
            st.session_state.messages = []
        st.success(f"PDF processed -- {len(chunks)} chunks indexed")
    st.subheader("Ask a Questions")
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])
    query = st.chat_input("type your question here...")

    if query:
        with st.chat_message("user"):
            st.write(query)
        st.session_state.messages.append({"role": "user", "content": query})
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                vector_store = load_vector_store()
                answer = build_qa_chain(vector_store).invoke(query)
            st.write(answer)
        st.session_state.messages.append({"role":"assistant", "content": answer})
else:
    st.warning("Please upload a PDF to get started.")

