class ContextBuilder:

    def build(
        self,
        query: str,
        documents: list[str]
    ) -> str:

        context = ""

        for idx, doc in enumerate(
            documents,
            start=1
        ):

            context += (
                f"[Document {idx}]\n"
                f"{doc}\n\n"
            )

        prompt = f"""
You are an intelligent RAG assistant.

Instructions:

1. Use the retrieved documents first.
2. If the answer exists in the documents,
   answer using those documents.
3. If the documents only partially answer
   the question, combine the document
   information with your own reasoning.
4. If the answer is not present in the
   documents, answer using your general
   knowledge.
5. At the end, specify one of:

   Source: Retrieved Documents

   OR

   Source: General Knowledge

Retrieved Context:

{context}

User Question:

{query}

Answer:
"""

        return prompt