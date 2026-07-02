from langchain_text_splitters import RecursiveCharacterTextSplitter

# from .ingestion import data_ingestion

# all_pdfs=data_ingestion("./data")

def document_chunking(docs, chunk_size=1500, chunk_overlap=200):
    print(f"Chunking {len(docs)} documents...")

    text_splitter=RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=["\n\n", "\n", " ", ""]
    )

    try:
        chunks=text_splitter.split_documents(docs)
        if chunks:
            print(f"Successfully created {len(chunks)} chunks for {len(docs)} Documents")
    except Exception as e:
        print(f"Error creating chunks: {e}")
        raise

    return chunks

# chunks = document_chunking(all_pdfs)
# print("Exmample of a chunk:")
# print(f"Content: {chunks[0].page_content[:200]}")
# print(f"Metadata: {chunks[0].metadata}")