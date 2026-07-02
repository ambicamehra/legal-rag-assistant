import chromadb
import uuid
import numpy as np
from typing import List, Dict, Any, Tuple

# from src.ingestion import data_ingestion
# from src.chunking import document_chunking
# from src.embedding import EmbeddingManager

class VectorStorage:
    #to store vector embeddings in ChromaDB

    def __init__(self, collection_name="law_files", persistent_path="./data/vector_files"):
        self.collection_name=collection_name
        self.persistent_path=persistent_path
        self.client=None
        self.collection=None
        self._initialise_store()

    def _initialise_store(self):
        try:
            self.client=chromadb.PersistentClient(self.persistent_path)
            self.collection=self.client.get_or_create_collection(self.collection_name)
            print(f"Successfuly created ChromaDB collection: {self.collection_name}")
            print(f"Total files present: {self.collection.count()}")
        except Exception as e:
            print(f"Error initialising ChromaDB: {e}")
            raise
    
    def store_vectors(self, embeddings: np.ndarray, documents: List[Any]):
        if not self.collection:
            raise ValueError("Collection not created")
        
        if len(documents)!=len(embeddings):
            raise ValueError("No. of embeddings must match No. of Documents")
        
        print(f"Adding vector embeddings for {len(documents)} documents...")
        
        ids=[]
        doc_embeddings=[]
        doc_content=[]
        metadatas=[]
        
        for (i,(doc,embedding)) in enumerate(zip(documents, embeddings)):
            #storing ids for all docs + embeddings
            doc_id=f"doc_{doc.metadata["title"]}_{i}"
            ids.append(doc_id)

            #storing page content for all docs
            doc_content.append(doc.page_content)

            #storing metadata for all docs
            metadata=dict(doc.metadata)
            metadata["index"]=i
            metadata["content_len"]=len(doc.page_content)
            metadatas.append(metadata)

            #storing embeddings for all docs
            doc_embeddings.append(embedding.tolist())
        
        try:
            self.collection.upsert(
                ids=ids,
                embeddings=doc_embeddings,
                metadatas=metadatas,
                documents=doc_content
            )
            print(f"Successfully added vectors to the collection")
            print(f"Total files present: {self.collection.count()}")
        except Exception as e:
            print(f"Error storing document emebeddings in VectorDB: {e}")
            raise

# all_pdf_files=data_ingestion("./data")
# all_chunks=document_chunking(all_pdf_files)

# texts=[doc.page_content for doc in all_chunks]

# embedding_manager=EmbeddingManager()
# embeddings=embedding_manager.generate_embeddings(texts)

# vector_storage=VectorStorage()
# vector_storage.store_vectors(embeddings,all_chunks)
