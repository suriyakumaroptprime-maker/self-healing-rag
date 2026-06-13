from pipeline.rag_pipeline import (
    RAGPipeline
)

documents = [

    "Artificial Intelligence is transforming industries.",

    "Machine Learning is a subset of AI.",

    "Deep Learning is a branch of Machine Learning.",

    "Neural Networks are used in Deep Learning.",

    "FAISS is a vector database library."
]

pipeline = RAGPipeline()

result = pipeline.run(

    query=
    "What is Machine Learning?",

    documents=documents
)

print()

print("=" * 60)

for key, value in result.items():

    print()

    print(key)

    print(value)

print()

print("=" * 60)