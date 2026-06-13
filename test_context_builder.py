from agents.context_builder import ContextBuilder


builder = ContextBuilder()

documents = [

    "Machine Learning is a subset of Artificial Intelligence.",

    "Deep Learning is a branch of Machine Learning."
]

prompt = builder.build(
    query="What is Machine Learning?",
    documents=documents
)

print("=" * 80)

print(prompt)

print("=" * 80)

print("\nPrompt Length:")

print(len(prompt))