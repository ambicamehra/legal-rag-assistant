from langchain_core.documents import Document
from langchain_community.document_loaders import PyMuPDFLoader, PyPDFLoader

from pathlib import Path
import os

def data_ingestion(directory):
    directory_path = Path(directory)

    files=list(directory_path.glob("**/*.pdf"))         # glob() returns a generator, but we need a list of files
    print(f"Found {len(files)} in the directory")

    all_docs=[]

    for file in files:
        filename=os.path.basename(str(file))            #to get filename with extension
        print(f"Processing {filename} File...")

        try:
            loader = PyMuPDFLoader(str(file))
            file_documents = loader.load()      #returns a list of documents created for a particular file

            for doc in file_documents:
                doc.metadata["title"]=filename

            print(f"Created {len(file_documents)} documents")
            all_docs.extend(file_documents)
        except Exception as e:
            print(f"Error loading documents: {e}")
            raise
         
    print(f"Total {len(all_docs)} documents created")
    return all_docs

# pdf_files=data_ingestion("./data")
