from memory.short_term_memory import (
    ShortTermMemory
)

memory = ShortTermMemory()

memory.add_message(

    role="user",

    content="What is RAG?"
)

memory.add_message(

    role="assistant",

    content="RAG means Retrieval Augmented Generation."
)

memory.add_message(

    role="user",

    content="Explain it again."
)

messages = memory.get_messages()

for msg in messages:

    print(msg)

print()

print(
    "Total Messages:",
    len(messages)
)