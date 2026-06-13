class CitationAgent:

    def add_citations(
        self,
        answer,
        metadatas
    ):

        citations = []

        for metadata in metadatas:

            source = (
                f"{metadata['source_file']} "
                f"(Chunk {metadata['chunk_id']})"
            )

            if source not in citations:

                citations.append(
                    source
                )

        final_answer = answer

        final_answer += "\n\nSources:\n"

        for citation in citations:

            final_answer += (
                f"- {citation}\n"
            )

        return final_answer