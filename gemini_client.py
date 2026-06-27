from google import genai

from config import settings


class GeminiClient:

    def __init__(self):

        self.client = genai.Client(
            api_key=settings.gemini_api_key
        )

        self.model = settings.model_name

    def generate(
        self,
        messages,
        tools=None
    ):

        return self.client.models.generate_content(

            model=self.model,

            contents=messages,

            config={

                "tools": tools or []

            }

        )