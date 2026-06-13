from memory.short_term_memory import (
    ShortTermMemory
)

from memory.long_term_memory import (
    LongTermMemory
)


class MemoryAgent:

    def __init__(self):

        self.short_memory = (
            ShortTermMemory()
        )

        self.long_memory = (
            LongTermMemory()
        )

    def add_interaction(
        self,
        user_message: str,
        assistant_message: str
    ):

        # Short Term

        self.short_memory.add_message(
            role="user",
            content=user_message
        )

        self.short_memory.add_message(
            role="assistant",
            content=assistant_message
        )

        # Long Term

        memory_text = f"""
User:
{user_message}

Assistant:
{assistant_message}
"""

        memory_id = str(
            self.long_memory.count() + 1
        )

        self.long_memory.add_memory(
            memory_id=memory_id,
            text=memory_text
        )

    def get_short_term_context(
        self
    ):

        return self.short_memory.get_messages()

    def get_long_term_context(
        self,
        query: str
    ):

        results = (
            self.long_memory.search_memory(
                query=query
            )
        )

        return results["documents"][0]