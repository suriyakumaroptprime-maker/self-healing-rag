from agents.citation_agent import (
    CitationAgent
)

answer = """
Machine Learning is a subset of
Artificial Intelligence.
"""

documents = [

    "Machine Learning is a subset of AI.",

    "Deep Learning is a branch of ML."
]

agent = CitationAgent()

result = agent.add_citations(
    answer=answer,
    documents=documents
)

print(result)