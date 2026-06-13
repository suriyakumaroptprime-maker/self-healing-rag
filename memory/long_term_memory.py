import chromadb

from config.settings import settings

from ingestion.embedding_generator import (
    EmbeddingGenerator
)


class LongTermMemory:

    def __init__(self):

        self.embedder = (
            EmbeddingGenerator()
        )

        self.client = (
            chromadb.PersistentClient(
                path=settings.CHROMA_PATH
            )
        )

        self.collection = (
            self.client.get_or_create_collection(
                name="memory"
            )
        )

    def add_memory(
        self,
        memory_id: str,
        text: str
    ):

        embedding = (
            self.embedder.generate_embedding(
                text
            )
        )

        self.collection.add(
            ids=[memory_id],
            documents=[text],
            embeddings=[
                embedding.tolist()
            ]
        )

    def search_memory(
        self,
        query: str,
        top_k: int = 3
    ):

        query_embedding = (
            self.embedder.generate_embedding(
                query
            )
        )

        results = (
            self.collection.query(
                query_embeddings=[
                    query_embedding.tolist()
                ],
                n_results=top_k
            )
        )

        return results

    def count(self):

        return self.collection.count()