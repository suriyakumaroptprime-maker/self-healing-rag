import json

from llm.groq_client import GroqClient


class QueryAgent:

    def __init__(self):

        self.llm = GroqClient()

    def process(
        self,
        query: str
    ):

        prompt = f"""
You are a query understanding agent.

Analyze the user query.

Return ONLY valid JSON.

Format:

{{
    "cleaned_query": "...",
    "intent": "...",
    "needs_retrieval": true
}}

User Query:

{query}
"""

        response = self.llm.generate(
            prompt
        )

        try:

            return json.loads(
                response
            )

        except:

            return {

                "cleaned_query": query,

                "intent": "unknown",

                "needs_retrieval": True
            }