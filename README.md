# Legal Research Assistant using RAG

An AI-powered legal question-answering system that enables users to query Indian legal documents in natural language and receive context-aware responses. The system uses Retrieval-Augmented Generation (RAG) to retrieve relevant legal provisions and generate accurate answers using a Large Language Model (LLM).

## Features

- Ingests and processes legal PDF documents
- Performs intelligent text chunking for efficient retrieval
- Generates vector embeddings for semantic search
- Retrieves contextually relevant legal responses
- Produces grounded responses using an LLM
- Modular architecture for easy maintenance and scalability

## Architecture

PDF Documents
→ Ingestion
→ Chunking
→ Embeddings
→ Vector Store
→ Semantic Retrieval
→ LLM
→ Response Generation

## Tech Stack

- Python
- LangChain
- ChromaDB
- FAISS
- Sentence Transformers
- Ollama
- Streamlit
- PyMuPDF / PyPDF

## Project Structure

```text
src/
├── ingestion.py
├── chunking.py
├── embedding.py
├── vectorstorage.py
├── retrieval.py
├── llm.py
└── pipeline.py

data/
└── Law/

main.py
```

## Legal Corpus

The system currently supports question answering across multiple Indian legal documents, including:

- The Constitution of India
- The Companies Act, 2013
- The Competition Act, 2002
- The Indian Contract Act, 1872
- Insolvency and Bankruptcy Code (IBC)
- SEBI Regulations

## Installation

Clone the repository:

```bash
git clone https://github.com/ambicamehra/legal-rag-assistant.git
cd legal-rag-assistant
```

Install dependencies:

```bash
pip install -r rqmts.txt
```

## Usage

Run the application:

```bash
streamlit run main.py
```
The application will launch in your browser.

Enter a legal query such as:

```text
When does the Adjudicating Authority convert the creditor-initiated insolvency resolution process to corporate insolvency resolution?
```
```text
What is the creditor-initiated insolvency commencement date 
```
```text
How should a listed entity declare dividends?
```
```text
when should a creditor-initiated insolvency resolution process not be initiated in respect of a corporate debtor? 
```
The system retrieves relevant legal provisions and generates a context-aware response.

## Future Enhancements

- Improved embedding models
- Cross-encoder reranking
- Citation-based answers
