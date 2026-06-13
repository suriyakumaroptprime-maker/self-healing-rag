from agents.repair_agent import (
    RepairAgent
)

agent = RepairAgent()

query = "tell me about rag"

rewritten = agent.rewrite_query(
    query
)

print("\nOriginal Query:\n")
print(query)

print("\nRewritten Query:\n")
print(rewritten)