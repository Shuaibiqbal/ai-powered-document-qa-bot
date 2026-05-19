from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter


def load_and_chunk_pdf(file_path: str):
    
    loader = PyPDFLoader(file_path=file_path)

    documents = loader.lazy_load()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 500,
        chunk_overlap=50,
    )
    chunks = text_splitter.split_documents(documents)
    print(f" Total chunks created: {len(chunks)}")
    return chunks
if __name__ == "__main__":

    chunks = load_and_chunk_pdf("data/sample.pdf")

    print(f"\n📄 Total chunks: {len(chunks)}")
    print(f"\n🔍 First chunk preview:")
    print(chunks[0].page_content)
    print(f"\n📌 Page number: {chunks[0].metadata}")