from src.embedding import EmbeddingManager
from src.vectorstorage import VectorStorage

# from src.ingestion import data_ingestion
# from src.chunking import document_chunking

class RAGRetrieval:
    def __init__(self, vectorstorage: VectorStorage, embeddingmanager: EmbeddingManager):
        self.embeddingmanager=embeddingmanager
        self.vectorstorage=vectorstorage
    
    def retrieve(self, query: str, top_k: int=5, score_threshold: float=0.0):
        print(f"Retrieving documents for query: {query}")
        print(f"Top_k: {top_k}, Score_threshold: {score_threshold}")

        query_embedding=self.embeddingmanager.generate_embeddings([query])[0]

        try:
            result=self.vectorstorage.collection.query(
                query_embeddings=[query_embedding.tolist()],
                n_results=top_k
                )
            
            retrieved_docs=[]
            
            if result['documents'] and result['documents'][0]:
                distances=result['distances'][0]
                metadatas=result['metadatas'][0]
                documents=result['documents'][0]
                ids=result['ids'][0]
            
            for (i,(doc_id, distance, metadata, doc)) in enumerate(zip(ids,distances,metadatas,documents)):
                similarity_score = 1-distance

                if similarity_score>=score_threshold:
                    retrieved_docs.append({
                        "Ids":doc_id,
                        "Content":doc,
                        "Metadata":metadata,
                        "Similarity Score":similarity_score,
                        "Rank":i+1
                    })
                
            if not retrieved_docs:
                raise ValueError("No documents retrieved")
            
            print(f"Retrieved {len(retrieved_docs)} documents")
        except Exception as e:
            print(f"Error retrieving documents: {e}")
            raise

        return retrieved_docs       

# all_pdf_files=data_ingestion("./data")
# all_chunks=document_chunking(all_pdf_files)

# texts=[doc.page_content for doc in all_chunks]

# embedding_manager=EmbeddingManager()
# embeddings=embedding_manager.generate_embeddings(texts)

# vector_storage=VectorStorage()
# vector_storage.store_vectors(embeddings,all_chunks)

# retriever=RAGRetrieval(vector_storage, embedding_manager)
# query="What is patronage bonus?"
# docs_retrieved=retriever.retrieve(query=query)

# for doc in docs_retrieved:
#     print(doc)