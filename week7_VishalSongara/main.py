from rag import answer_question

print("=" * 50)
print("Document RAG Assistant")
print("=" * 50)

while True:

    question = input("\nQuestion: ")

    if question.lower() in ["exit", "quit"]:
        break

    answer, sources = answer_question(question)

    print("\nAnswer:\n")
    print(answer)

    print("\nSources:\n")

    for src in sources:

        print(
            f"{src['source']} "
            f"(Page {src['page']})"
        )