from retrievers.bm25_retriever import BM25Retriever


documents = [

    "Artificial Intelligence is transforming industries.",

    "Machine Learning is a subset of AI.",

    "Cricket is a popular sport in India.",

    "FAISS is a vector database library."
]


retriever = BM25Retriever()

retriever.fit(
    documents
)

results = retriever.retrieve(
    "FAISS",
    top_k=2
)

for doc, score in results:

    print(doc)

    print("Score:", score)

    print("-" * 50)