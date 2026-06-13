from agents.memory_agent import (
    MemoryAgent
)

memory = MemoryAgent()

memory.add_interaction(
    user_message="I am building a Self-Healing RAG.",
    assistant_message="That sounds like a great project."
)

memory.add_interaction(
    user_message="I am using Groq API.",
    assistant_message="Groq is very fast."
)

print("\nSHORT TERM MEMORY\n")

for message in memory.get_short_term_context():

    print(
        f"{message['role']}: "
        f"{message['content']}"
    )

print("\nLONG TERM MEMORY\n")

results = memory.get_long_term_context(
    "What project am I building?"
)

for item in results:

    print(item)

    print("-" * 50)