from agents.planner_agent import (
    PlannerAgent
)

agent = PlannerAgent()

result = agent.create_plan(
    query="What is Retrieval Augmented Generation?",
    intent="provide_info"
)

print(type(result))

print()

print(result)