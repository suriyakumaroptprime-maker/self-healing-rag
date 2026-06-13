class FusionRetriever:

    def __init__(
        self,
        rrf_k: int = 60
    ):

        self.rrf_k = rrf_k

    def fuse(
        self,
        dense_results,
        bm25_results,
        top_k: int = 5
    ):

        fused_scores = {}

        # Dense Retriever Results
        if "documents" in dense_results:

            dense_docs = (
                dense_results["documents"][0]
            )

            for rank, doc in enumerate(
                dense_docs,
                start=1
            ):

                score = (
                    1 /
                    (self.rrf_k + rank)
                )

                fused_scores[doc] = (
                    fused_scores.get(
                        doc,
                        0
                    )
                    + score
                )

        # BM25 Results
        for rank, (
            doc,
            _
        ) in enumerate(
            bm25_results,
            start=1
        ):

            score = (
                1 /
                (self.rrf_k + rank)
            )

            fused_scores[doc] = (
                fused_scores.get(
                    doc,
                    0
                )
                + score
            )

        ranked = sorted(
            fused_scores.items(),
            key=lambda x: x[1],
            reverse=True
        )

        return ranked[:top_k]