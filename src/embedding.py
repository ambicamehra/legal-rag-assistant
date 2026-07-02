from typing import List, Dict, Tuple, Any
from sentence_transformers import SentenceTransformer
import numpy as np

# from src.ingestion import data_ingestion
# from src.chunking import document_chunking

class EmbeddingManager:
    #to manage the embedding of the documents

    def __init__(self, model_name: str="all-MiniLM-L6-v2"):
        self.model_name=model_name
        self.model=None
        self._load_model()
    
    def _load_model(self):
        print(f"Loading Embedding model...")
        try:
            self.model=SentenceTransformer(self.model_name)
            print(f"Successfully loaded Embedding model: {self.model_name}")
            print(f"Model dimensions: {self.model.get_embedding_dimension()}")
        except Exception as e:
            print(f"Error loading embedding model: {e}")
            raise

    def generate_embeddings(self, texts: List[str]) -> np.ndarray:
        #creating embedding vectors for all the chunks using all-MiniLM-L6-v2 embedding model of Sentence Transformers from HuggingFace
        if not self.model:
            raise ValueError("Error loading embedding model")
        try:
            vectors=self.model.encode(texts, show_progress_bar=True)
            print(f"Successfully created {len(vectors)} embeddings for {len(texts)} Documents")
        except Exception as e:
            print(f"Error generating embeddings: {e}")
            raise

        return vectors


# all_pdf_docs=data_ingestion("./data")
# all_chunks=document_chunking(all_pdf_docs)

# text=[doc.page_content for doc in all_chunks]       #its 'doc.page_content' because all_chunks returns Document objects which are not dictionaries

# embedding_manager=EmbeddingManager()
# embedding_manager.generate_embeddings(text)