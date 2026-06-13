from ingestion.embedding_generator import EmbeddingGenerator
from ingestion.vector_store import VectorStore

from retrievers.dense_retriever import DenseRetriever


store = VectorStore()
embedder = EmbeddingGenerator()

try:
    store.delete_collection()
except:
    pass


documents = [

    "Artificial Intelligence is transforming industries.",

    "Machine Learning is a subset of AI.",

    "Cricket is a popular sport in India."
]


embeddings = embedder.generate_embeddings(
    documents
)

ids = [

    "doc_1",
    "doc_2",
    "doc_3"
]

store.add_documents(
    ids=ids,
    documents=documents,
    embeddings=embeddings
)


retriever = DenseRetriever()

results = retriever.retrieve(
    "What is Artificial Intelligence?",
    top_k=2
)

print("\nRetrieved Documents:\n")

for doc in results["documents"][0]:

    print(doc)
    print("-" * 50)