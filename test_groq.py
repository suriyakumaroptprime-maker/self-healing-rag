from llm.groq_client import GroqClient


client = GroqClient()

response = client.generate(
    "What is Python?"
)

print(response)