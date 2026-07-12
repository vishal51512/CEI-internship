# Document Question Answering System (RAG)

A Retrieval-Augmented Generation (RAG) system that answers questions from custom PDF documents using **Gemma (GGUF)**, **llama.cpp**, **FAISS**, and **Sentence Transformers**. The project runs completely offline.

## Features

* Load PDF documents
* Split documents into text chunks
* Generate embeddings
* Store embeddings in FAISS
* Retrieve relevant document chunks
* Answer questions using a local Gemma model
* Display document source and page number

## Project Structure

```text
.
├── data/
├── models/
├── utils/
├── vectorstore/
├── app.py
├── chat.py
├── config.py
├── ingest.py
├── prompts.py
├── rag.py
└── requirements.txt
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/vishal51512/CEI-internship.git
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

## Add Documents

Place your PDF files inside the `data/` folder.

```text
data/
├── notes.pdf
├── resume.pdf
└── research.pdf
```

## Add the Model

Place your Gemma GGUF model inside the `models/` folder.

Example:

```text
models/
└── gemma-3-4b-it-Q4_K_M.gguf
```

Update the model path in `config.py` if necessary.

## Build the Vector Database

Run:

```bash
python ingest.py
```

This will:

* Read PDFs
* Extract text
* Split text into chunks
* Generate embeddings
* Create the FAISS index

## Ask Questions

Run:

```bash
python main.py
```

Example:

```text
Question:
What is Retrieval-Augmented Generation?

Answer:
Retrieval-Augmented Generation (RAG) combines document retrieval with a language model to generate answers based on the retrieved context.
```

## Technologies Used

* Python
* Gemma (GGUF)
* llama.cpp
* FAISS
* Sentence Transformers
* LangChain
* PyMuPDF

## Author

**Vishal Songara**
