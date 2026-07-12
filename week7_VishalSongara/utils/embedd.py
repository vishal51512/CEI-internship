from sentence_transformers import SentenceTransformer

model = SentenceTransformer("BAAI/bge-small-en-v1.5")

def embed_chunks(chunks):
    texts = [chunk["text"] for chunk in chunks]

    return model.encode(
        texts,
        convert_to_numpy=True,
        show_progress_bar=True
    )

def embed_query(query):
    return model.encode(
        query,
        convert_to_numpy=True
    )