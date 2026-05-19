from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

def build_qa_chain(vector_store):
    
    model = "gpt-5.4-mini"
    llm = ChatOpenAI(model=model, temperature=0)

    retriever = vector_store.as_retriever(search_kwargs={"k": 3})

    prompt = ChatPromptTemplate.from_template(
        """
        Answer the question using only the context below.
        If you don't know the answer, say "I don't know".
        Context: {context}
        Question: {question}
        """
    )
    chain = ({
        "context": retriever,
        "question": RunnablePassthrough()
    } 
    | prompt 
    | llm 
    | StrOutputParser())

    return chain
if __name__ == "__main__":
    from dotenv import load_dotenv
    from document_loader import load_and_chunk_pdf
    from vector_store import build_vector_store
    
    load_dotenv()

    chunks = load_and_chunk_pdf("data/sample.pdf")
    vector_store = build_vector_store(chunks)

    chain = build_qa_chain(vector_store)

    query = "What is this document about?"
    answer = chain.invoke(query)

    print(f"\n Answer: {answer}")