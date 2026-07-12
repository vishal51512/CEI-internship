import os

from utils.pdfloader import load_pdf
from utils.splitter import split_pages
from utils.embedd import embed_chunks
from utils.vectordb import save_vector_db

DATA_FOLDER = "data"

all_chunks = []

for file in os.listdir(DATA_FOLDER):

    if file.endswith(".pdf"):

        path = os.path.join(DATA_FOLDER, file)

        print(f"Processing {file}")

        pages = load_pdf(path)

        chunks = split_pages(pages, file)

        all_chunks.extend(chunks)

print(f"\nTotal Chunks: {len(all_chunks)}")

print("Generating embeddings...")

embeddings = embed_chunks(all_chunks)

print("Saving FAISS index...")

save_vector_db(embeddings, all_chunks)

print("Done!")