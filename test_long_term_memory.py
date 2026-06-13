from memory.long_term_memory import (
    LongTermMemory
)

memory = LongTermMemory()

memory.add_memory(

    memory_id="1",

    text="""
    User is building a
    Self-Healing RAG project.
    """
)

memory.add_memory(

    memory_id="2",

    text="""
    User is using Groq API.
    """
)

results = memory.search_memory(
    "What project am I building?"
)

print(
    results["documents"][0]
)

print()

print(
    "Memory Count:",
    memory.count()
)