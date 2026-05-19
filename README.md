# 🤖 AI-Powered Document Q&A Bot

> Upload any PDF and get instant, accurate, AI-powered answers — grounded in your document, not hallucinations.

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat&logo=python&logoColor=white)](https://python.org)
[![LangChain](https://img.shields.io/badge/LangChain-0.1+-1C3C3C?style=flat&logo=chainlink&logoColor=white)](https://langchain.com)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.x-FF4B4B?style=flat&logo=streamlit&logoColor=white)](https://streamlit.io)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--3.5-412991?style=flat&logo=openai&logoColor=white)](https://openai.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## 📌 What

**AI-Powered Document Q&A Bot** is a Streamlit web application that transforms any PDF into an interactive knowledge base. Users upload a document, ask natural language questions, and receive precise answers — complete with the source page numbers that support each response.

This project implements a full **RAG (Retrieval-Augmented Generation)** pipeline: the document is read, chunked, embedded into a vector store, and retrieved semantically at query time before being synthesized by GPT.

---

## 💡 Why

Every company — from startups to enterprises — is drowning in documentation: contracts, research papers, policy manuals, technical specs. Reading through hundreds of pages to find one answer is inefficient and error-prone.

RAG is the architecture powering 90% of modern enterprise AI products. Instead of fine-tuning a model on proprietary data (expensive, slow), you **ground the LLM on your own documents at query time** — making it accurate, auditable, and updatable without retraining.

This project demonstrates:
- The most in-demand LangChain skill in AI engineering job listings
- Production-quality document intelligence architecture
- A deployable, end-to-end AI application built from scratch

---

## ⚙️ How It Works

```
PDF Upload → Chunking → Embedding → Vector Store → Semantic Search → GPT Answer
```

1. **Load** — The PDF is parsed using `PyPDFLoader`, extracting raw text page by page
2. **Chunk** — Text is split into 500-token overlapping segments via `RecursiveCharacterTextSplitter`
3. **Embed** — Each chunk is converted into a vector using `OpenAIEmbeddings`
4. **Store** — Vectors are indexed in a **FAISS** vector store for fast similarity search
5. **Retrieve** — On each query, the top-k most semantically relevant chunks are fetched
6. **Answer** — GPT-3.5-turbo synthesizes a grounded answer from retrieved chunks
7. **Cite** — Source page numbers are displayed alongside the answer in the Streamlit UI

---

## 🛠️ Tech Stack

| Tool | Version | Purpose |
|------|---------|---------|
| Python | 3.10+ | Core language |
| LangChain | 0.1+ | RAG orchestration & chain management |
| OpenAI GPT-3.5-turbo | Latest | LLM for answer generation |
| FAISS | Latest | Vector similarity search |
| OpenAI Embeddings | text-embedding-ada-002 | Text vectorization |
| PyPDF2 / pdfplumber | Latest | PDF parsing |
| Streamlit | 1.x | Web UI |
| python-dotenv | Latest | Environment variable management |

---

## 📁 Folder Structure

```
ai-powered-document-qa-bot/
├── app.py                    # Streamlit UI entry point
├── requirements.txt          # Project dependencies
├── .env.example              # OPENAI_API_KEY=your_key_here
├── README.md
├── src/
│   ├── document_loader.py    # PDF loading + chunking logic
│   ├── vector_store.py       # FAISS embedding + save/load
│   └── qa_chain.py           # RetrievalQA chain setup
├── data/
│   └── sample.pdf            # Sample test document
└── tests/
    └── test_qa_chain.py      # Unit tests for QA chain
```

---

## 📦 Requirements

```txt
langchain==0.1.20
langchain-community==0.0.38
langchain-openai==0.1.6
openai==1.30.1
faiss-cpu==1.8.0
streamlit==1.35.0
pypdf2==3.0.1
pdfplumber==0.11.0
python-dotenv==1.0.1
tiktoken==0.7.0
```

> Install all dependencies at once:
> ```bash
> pip install -r requirements.txt
> ```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or higher
- An [OpenAI API key](https://platform.openai.com/api-keys)

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/Shuaibiqbal/ai-powered-document-qa-bot
cd ai-powered-document-qa-bot

# 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set up environment variables
cp .env.example .env
# Open .env and add your OpenAI API key:
# OPENAI_API_KEY=sk-...

# 5. Run the app
streamlit run app.py
```

The app will open at `http://localhost:8501`

---

## 🧪 Running Tests

```bash
pytest tests/test_qa_chain.py -v
```

---

## 📸 Screenshot

> *Add your Streamlit Cloud screenshot here*

---

## 🌐 Live Demo

> *Add your Streamlit Cloud deployment link here*

---

## 🔑 Key Concepts Demonstrated

- **RAG Architecture** — Retrieval-Augmented Generation end-to-end
- **Vector Databases** — FAISS indexing and similarity search
- **Text Embeddings** — Semantic representation of document chunks
- **LangChain Chains** — `RetrievalQA` chain composition
- **PDF Ingestion** — Real-world document parsing and preprocessing
- **Streamlit UI** — Production-grade interactive web interface

---

## 🗺️ Roadmap

- [ ] Support for multiple PDFs simultaneously
- [ ] Add chat memory for multi-turn conversations
- [ ] Swap FAISS for Pinecone for cloud-native vector storage
- [ ] Add support for DOCX and TXT file formats
- [ ] Implement streaming responses
- [ ] Add user authentication for document privacy

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

---

## 👨‍💻 Author

**Shuaib Iqbal**
- GitHub: [@Shuaibiqbal](https://github.com/Shuaibiqbal)
- ORCID: [0000-0002-1894-8217](https://orcid.org/0000-0002-1894-8217)

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

> ⭐ If you found this project helpful, please consider giving it a star on GitHub!
