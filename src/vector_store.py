from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

FAISS_INDEX_APTH = "faiss_index"

def build_vector_store(chunks):

    embeddings = OpenAIEmbeddings()

    vectore_store = FAISS.from_documents(chunks, embeddings)

    print(f" vector store build with {len(chunks)} chunks")
    vectore_store.save_local(FAISS_INDEX_APTH)

    print(f" Vectore store saved to '{FAISS_INDEX_APTH}/'")

    return vectore_store
def load_vector_store():
    embeddings = OpenAIEmbeddings()

    vector_store = FAISS.load_local(
        FAISS_INDEX_APTH,
        embeddings,
        allow_dangerous_deserialization=True
    )
    print("Vector store loaded")
    return vector_store
if __name__ == "__main__":
    from document_loader import load_and_chunk_pdf
    from dotenv import load_dotenv
    load_dotenv()

    chunks = load_and_chunk_pdf("data/sample.pdf")
    vector_store = build_vector_store(chunks)

    results = vector_store.similarity_search("what is this documnet about?", k=2)

    for i, doc in enumerate(results):
        print(f"\n-- Result {i+1} --")
        print(doc.page_content)