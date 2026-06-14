from sentence_transformers import CrossEncoder


class CrossEncoderReranker:

    def __init__(self):

        self.model = CrossEncoder(
            "cross-encoder/ms-marco-TinyBERT-L-2-v2"
        )

    def rerank(
        self,
        query: str,
        documents: list[str],
        top_k: int = 5
    ):

        pairs = [

            (query, doc)

            for doc in documents
        ]

        scores = self.model.predict(
            pairs
        )

        ranked = sorted(
            zip(documents, scores),
            key=lambda x: x[1],
            reverse=True
        )

        return ranked[:top_k]