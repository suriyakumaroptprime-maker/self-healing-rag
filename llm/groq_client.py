from groq import Groq

from config.settings import settings


class GroqClient:

    def __init__(self):

        self.client = Groq(
            api_key=settings.GROQ_API_KEY
        )

        self.model = settings.GROQ_MODEL

    def generate(
        self,
        prompt: str,
        temperature: float = 0.2,
        max_tokens: int = 1000
    ) -> str:

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=temperature,
            max_completion_tokens=max_tokens
        )

        return response.choices[0].message.content