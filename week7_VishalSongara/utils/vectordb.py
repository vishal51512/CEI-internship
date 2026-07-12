import faiss
import numpy as np
import pickle
import os

VECTOR_DIR = "vectorstore"

def save_vector_db(embeddings, chunks):
    os.makedirs(VECTOR_DIR, exist_ok=True)

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)

    index.add(np.array(embeddings))

    faiss.write_index(index, f"{VECTOR_DIR}/faiss.index")

    with open(f"{VECTOR_DIR}/chunks.pkl", "wb") as f:
        pickle.dump(chunks, f)


def load_vector_db():
    index = faiss.read_index(f"{VECTOR_DIR}/faiss.index")

    with open(f"{VECTOR_DIR}/chunks.pkl", "rb") as f:
        chunks = pickle.load(f)

    return index, chunks