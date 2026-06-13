from agents.evaluator_agent import (
    EvaluatorAgent
)

query = (
    "What is Machine Learning?"
)

documents = [

    "Machine Learning is a subset of Artificial Intelligence."
]

answer = """
Machine Learning is a subset of
Artificial Intelligence that
allows systems to learn from data.
"""

agent = EvaluatorAgent()

result = agent.evaluate(
    query=query,
    documents=documents,
    answer=answer
)

print(result)