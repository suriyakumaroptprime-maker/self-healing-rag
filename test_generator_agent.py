from agents.generator_agent import (
    GeneratorAgent
)


documents = [

    "Machine Learning is a subset of Artificial Intelligence.",

    "Deep Learning is a branch of Machine Learning.",

    "Neural Networks are commonly used in Deep Learning."
]

query = "What is Machine Learning?"


agent = GeneratorAgent()

answer = agent.generate(
    query=query,
    documents=documents
)

print("\nGenerated Answer:\n")

print(answer)