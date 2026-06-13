from reranker.cross_encoder_reranker import (
    CrossEncoderReranker
)

query = "What is Machine Learning?"

documents = [

    "Machine Learning is a subset of Artificial Intelligence.",

    "Cricket is the most popular sport in India.",

    "Pizza is a famous Italian food."
]

reranker = CrossEncoderReranker()

results = reranker.rerank(
    query=query,
    documents=documents,
    top_k=3
)

for doc, score in results:

    print("\nDocument:")
    print(doc)

    print("Score:")
    print(score)

    print("-" * 50)