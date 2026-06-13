from agents.retriever_agent import (
    RetrieverAgent
)

documents = [

    "Artificial Intelligence is transforming industries.",

    "Machine Learning is a subset of AI.",

    "Deep Learning is a branch of Machine Learning.",

    "Neural Networks are used in Deep Learning.",

    "Cricket is a popular sport in India.",

    "FAISS is a vector database library."
]
agent = RetrieverAgent()

results = agent.retrieve(

    query="What is Machine Learning?",

    documents=documents,

    top_k=3
)

print("\nRetrieved Documents:\n")

for doc, score in results:

    print(doc)

    print("Score:", score)

    print("-" * 50)