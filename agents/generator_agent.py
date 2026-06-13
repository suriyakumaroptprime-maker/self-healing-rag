from llm.groq_client import GroqClient

from agents.context_builder import (
    ContextBuilder
)


class GeneratorAgent:

    def __init__(self):

        self.llm = GroqClient()

        self.context_builder = (
            ContextBuilder()
        )

    def generate(
        self,
        query: str,
        documents: list[str]
    ):

        prompt = self.context_builder.build(
            query=query,
            documents=documents
        )

        answer = self.llm.generate(
            prompt=prompt
        )

        return answer