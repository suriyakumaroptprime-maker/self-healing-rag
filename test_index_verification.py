from ingestion.vector_store import (
    VectorStore
)

store = VectorStore()

print()

print(
    "Total Documents:"
)

print(
    store.count()
)