from retrievers.dense_retriever import (
    DenseRetriever
)

from reranker.cross_encoder_reranker import (
    CrossEncoderReranker
)


class RetrieverAgent:

    def __init__(self):

        self.dense = DenseRetriever()

        self.reranker = (
            CrossEncoderReranker()
        )

    def retrieve(
        self,
        query: str,
        top_k: int = 5
    ):

        results = self.dense.retrieve(
            query=query,
            top_k=top_k
        )

        documents = (
            results["documents"][0]
        )

        metadatas = (
            results["metadatas"][0]
        )

        reranked = (
            self.reranker.rerank(
                query=query,
                documents=documents,
                top_k=top_k
            )
        )

        return {
            "documents": reranked,
            "metadatas": metadatas
        }