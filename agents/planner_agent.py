import json

from llm.groq_client import GroqClient


class PlannerAgent:

    def __init__(self):

        self.llm = GroqClient()

    def create_plan(
        self,
        query: str,
        intent: str
    ):

        prompt = f"""
You are a retrieval planner.

Analyze the query and intent.

Return ONLY valid JSON.

Format:

{{
    "use_dense": true,
    "use_bm25": true,
    "rerank": true,
    "top_k": 10
}}

Query:
{query}

Intent:
{intent}
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

                "use_dense": True,

                "use_bm25": True,

                "rerank": True,

                "top_k": 10
            }