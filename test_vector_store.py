from ingestion.embedding_generator import EmbeddingGenerator
from ingestion.vector_store import VectorStore


embedder = EmbeddingGenerator()

store = VectorStore()

# Clean collection before testing
try:
    store.delete_collection()
except:
    pass


text = "Artificial Intelligence is transforming the world."

embedding = embedder.generate_embedding(
    text
)

store.add_documents(
    ids=["doc_1"],
    documents=[text],
    embeddings=[embedding]
)

query_embedding = embedder.generate_embedding(
    "What is AI?"
)

results = store.search(
    query_embedding=query_embedding,
    top_k=1
)

print("\nRetrieved Document:\n")

print(
    results["documents"][0][0]
)

print("\nDocument Count:")

print(
    store.count()
)