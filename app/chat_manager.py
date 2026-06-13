from pipeline.rag_pipeline import (
    RAGPipeline
)


class ChatManager:

    def __init__(self):

        self.pipeline = (
            RAGPipeline()
        )

    def ask(
        self,
        query,
        documents
    ):

        return self.pipeline.run(
            query=query,
            documents=documents
        )