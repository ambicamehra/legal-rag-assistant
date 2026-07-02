from langchain_core.prompts import  ChatPromptTemplate

from src.ingestion import data_ingestion
from src.chunking import document_chunking
from src.embedding import EmbeddingManager
from src.vectorstorage import VectorStorage
from src.retrieval import RAGRetrieval
from src.llm import LLMmodel

# llm=LLMmodel()

def legal_pipeline(query: str, llm: LLMmodel):
    #implementing the entire RAG legal pipeline to get a response

    file_docs=data_ingestion("./data")
    all_chunks=document_chunking(file_docs)

    doc_content=[doc.page_content for doc in all_chunks]

    embedding_manager=EmbeddingManager()
    all_embeddings=embedding_manager.generate_embeddings(doc_content)

    vector_storage=VectorStorage()
    vector_storage.store_vectors(embeddings=all_embeddings, documents=all_chunks)

    retriever=RAGRetrieval(vector_storage, embedding_manager)

    retrieved_docs=retriever.retrieve(query)

    for doc in retrieved_docs:
        print(doc)

    context="\n\n".join(
        doc["Content"] for doc in retrieved_docs
    )

    template="""
        You are an expert Legal Assistant

        Use ONLY the supplied context.

        If the answer is not found in the context,
        say "I don't have enough information."

        Context:
        {context}

        Query:
        {query}

        Answer:
    """
    prompt_template=ChatPromptTemplate.from_template(template)

    prompt=prompt_template.format(
        context=context,
        query=query
    )

    response=llm.generate_response(prompt=prompt)
    
    return response

# pipeline=legal_pipeline("What is the Annual payment to certain Devaswom Funds?")
# print(pipeline)