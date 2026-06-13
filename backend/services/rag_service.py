from pipeline.rag_pipeline import (
    RAGPipeline
)


class RAGService:

    def __init__(self):

        self.pipeline = (
            RAGPipeline()
        )

    def chat(
        self,
        query: str
    ):

        return (
            self.pipeline.run(
                query=query
            )
        )