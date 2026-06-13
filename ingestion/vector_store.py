import chromadb

from config.settings import settings


class VectorStore:

    def __init__(self):

        self.client = chromadb.PersistentClient(
            path=settings.CHROMA_PATH
        )

        self.collection = (
            self.client.get_or_create_collection(
                name=settings.COLLECTION_NAME
            )
        )

    def add_documents(
        self,
        ids,
        documents,
        embeddings,
        metadatas
    ):

        self.collection.add(
            ids=ids,
            documents=documents,
            embeddings=embeddings.tolist(),
            metadatas=metadatas
        )

    def search(
        self,
        query_embedding,
        top_k=5
    ):

        return self.collection.query(
            query_embeddings=[
                query_embedding.tolist()
            ],
            n_results=top_k
        )

    def count(self):

        return self.collection.count()