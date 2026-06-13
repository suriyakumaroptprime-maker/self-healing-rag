from llm.groq_client import GroqClient


class RepairAgent:

    def __init__(self):

        self.llm = GroqClient()

    def rewrite_query(
        self,
        query: str
    ) -> str:

        prompt = f"""
You are a query rewriting agent.

Rewrite the user's query to make it:

1. More specific
2. More searchable
3. Better for retrieval

Return ONLY the rewritten query.

User Query:

{query}
"""

        rewritten_query = self.llm.generate(
            prompt
        )

        return rewritten_query.strip()