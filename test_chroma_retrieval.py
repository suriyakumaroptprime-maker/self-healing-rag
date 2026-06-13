from retrievers.dense_retriever import (
    DenseRetriever
)

retriever = DenseRetriever()

results = retriever.retrieve(
    "What is the name of the candidate?"
)

print()

print("DOCUMENTS:")

for doc in results["documents"][0]:

    print()
    print(doc[:300])

print()

print("METADATA:")

for meta in results["metadatas"][0]:

    print(meta)