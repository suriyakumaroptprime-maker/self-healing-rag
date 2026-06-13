from agents.query_agent import (
    QueryAgent
)

agent = QueryAgent()

result = agent.process(
    "tell me about rag"
)

print(type(result))

print()

print(result)