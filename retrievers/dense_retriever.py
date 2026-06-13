from ingestion.embedding_generator import (
    EmbeddingGenerator
)

from ingestion.vector_store import (
    VectorStore
)


class DenseRetriever:

    def __init__(self):

        self.embedder = (
            EmbeddingGenerator()
        )

        self.vector_store = (
            VectorStore()
        )

    def retrieve(
        self,
        query: str,
        top_k: int = 5
    ):

        query_embedding = (
            self.embedder.generate_embedding(
                query
            )
        )

        results = (
            self.vector_store.search(
                query_embedding=query_embedding,
                top_k=top_k
            )
        )

        return results