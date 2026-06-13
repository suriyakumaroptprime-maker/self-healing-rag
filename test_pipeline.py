from pipeline.rag_pipeline import (
    RAGPipeline
)

pipeline = RAGPipeline()

result = pipeline.run(
    "What is Artificial Intelligence?"
)

print("\nRESULT\n")

for key, value in result.items():

    print(
        f"{key}: {value}"
    )

    print()