from pathlib import Path

from ingestion.index_builder import (
    IndexBuilder
)


class IngestionService:

    def __init__(self):

        self.index_builder = (
            IndexBuilder()
        )

    def ingest_file(
        self,
        file_path: str
    ):

        return (
            self.index_builder
            .index_document(
                file_path
            )
        )