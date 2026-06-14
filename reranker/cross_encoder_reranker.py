class CrossEncoderReranker:

    def __init__(self):
        pass

    def rerank(
        self,
        query: str,
        documents: list[str],
        top_k: int = 5
    ):

        return [
            (doc, 1.0)
            for doc in documents[:top_k]
        ]