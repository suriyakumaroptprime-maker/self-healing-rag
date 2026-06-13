import uuid

from pathlib import Path

from ingestion.document_router import (
    DocumentRouter
)

from ingestion.text_splitter import (
    TextSplitter
)

from ingestion.embedding_generator import (
    EmbeddingGenerator
)

from ingestion.vector_store import (
    VectorStore
)


class IndexBuilder:

    def __init__(self):

        self.router = (
            DocumentRouter()
        )

        self.splitter = (
            TextSplitter()
        )

        self.embedder = (
            EmbeddingGenerator()
        )

        self.vector_store = (
            VectorStore()
        )

    def index_document(
        self,
        file_path: str
    ):

        # ------------------------
        # Load Document
        # ------------------------

        text = self.router.load_document(
            file_path
        )

        # ------------------------
        # Split Into Chunks
        # ------------------------

        chunks = self.splitter.split(
            text
        )

        # ------------------------
        # Generate Embeddings
        # ------------------------

        embeddings = (
            self.embedder.generate_embeddings(
                chunks
            )
        )

        # ------------------------
        # Generate IDs
        # ------------------------

        ids = [

            str(uuid.uuid4())

            for _ in chunks
        ]

        # ------------------------
        # Metadata
        # ------------------------

        file_name = (
            Path(file_path).name
        )

        metadatas = []

        for idx, chunk in enumerate(
            chunks,
            start=1
        ):

            metadatas.append(

                {
                    "source_file":
                        file_name,

                    "chunk_id":
                        idx
                }

            )

        # ------------------------
        # Store In ChromaDB
        # ------------------------

        self.vector_store.add_documents(

            ids=ids,

            documents=chunks,

            embeddings=embeddings,

            metadatas=metadatas
        )

        # ------------------------
        # Return Stats
        # ------------------------

        return {

            "file_name":
                file_name,

            "chunks":
                len(chunks),

            "stored":
                len(ids)
        }