import json

from llm.groq_client import GroqClient


class EvaluatorAgent:

    def __init__(self):

        self.llm = GroqClient()

    def evaluate(
        self,
        query: str,
        documents: list[str],
        answer: str
    ):

        context = "\n".join(
            documents
        )

        prompt = f"""
You are an evaluation system.

Evaluate the answer.

Question:
{query}

Context:
{context}

Answer:
{answer}

Return ONLY valid JSON.

Format:

{{
    "relevancy": 0.0,
    "faithfulness": 0.0,
    "confidence": 0.0
}}
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

                "relevancy": 0.5,

                "faithfulness": 0.5,

                "confidence": 0.5
            }