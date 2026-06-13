from rank_bm25 import BM25Okapi


class BM25Retriever:

    def __init__(self):

        self.documents = []

        self.tokenized_documents = []

        self.bm25 = None

    def fit(
        self,
        documents: list[str]
    ):

        self.documents = documents

        self.tokenized_documents = [

            doc.lower().split()

            for doc in documents
        ]

        self.bm25 = BM25Okapi(
            self.tokenized_documents
        )

    def retrieve(
        self,
        query: str,
        top_k: int = 5
    ):

        tokenized_query = query.lower().split()

        scores = self.bm25.get_scores(
            tokenized_query
        )

        ranked = sorted(
            zip(
                self.documents,
                scores
            ),
            key=lambda x: x[1],
            reverse=True
        )

        return ranked[:top_k]