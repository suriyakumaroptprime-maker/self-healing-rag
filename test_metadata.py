from ingestion.vector_store import (
    VectorStore
)

store = VectorStore()

results = store.collection.get()

print(
    results["metadatas"][:5]
)