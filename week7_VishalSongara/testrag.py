from rag import retrieve

question = input("Question:  what is technical communication? ")

results = retrieve(question)

print()

for i, chunk in enumerate(results, 1):

    print("=" * 60)

    print(f"Result {i}")

    print(f"Source : {chunk['source']}")

    print(f"Page   : {chunk['page']}")

    print(f"Score  : {chunk['score']:.4f}")

    print()

    print(chunk["text"])