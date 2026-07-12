import numpy as np

from utils.vectordb import load_vector_db
from utils.embedd import embed_query
from utils.prompts import SYSTEM_PROMPT
from utils.llm import generate

TOP_K = 5

index, chunks = load_vector_db()

def retrieve(query):

    query_embedding = embed_query(query)

    query_embedding = np.array([query_embedding])

    distances, indices = index.search(query_embedding, TOP_K)

    results = []

    for idx, score in zip(indices[0], distances[0]):

        if idx == -1:
            continue

        results.append({
            "score": float(score),
            "text": chunks[idx]["text"],
            "page": chunks[idx]["page"],
            "source": chunks[idx]["source"]
        })

    return results

def build_context(results):
    """
    Convert retrieved chunks into a prompt context.
    """

    context = ""

    for chunk in results:
        context += (
            f"Source: {chunk['source']} "
            f"(Page {chunk['page']})\n"
            f"{chunk['text']}\n\n"
        )

    return context

def answer_question(question):

    retrieved = retrieve(question)

    context = build_context(retrieved)

    prompt = SYSTEM_PROMPT.format(
        context=context,
        question=question,
    )

    answer = generate(prompt)

    return answer, retrieved