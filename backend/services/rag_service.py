from pipeline.rag_pipeline import (
    RAGPipeline
)


class RAGService:

    def __init__(self):

        self.pipeline = None

    def get_pipeline(self):

        if self.pipeline is None:

            self.pipeline = (
                RAGPipeline()
            )

        return self.pipeline

    def chat(
        self,
        query: str
    ):

        pipeline = (
            self.get_pipeline()
        )

        return (
            pipeline.run(
                query=query
            )
        )