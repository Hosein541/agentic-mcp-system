from collections import deque
from google.genai import types


class Memory:

    def __init__(self, max_size=20):
        self.messages = deque(maxlen=max_size)

    def add_user(self, text: str):
        self.messages.append(
            types.Content(
                role="user",
                parts=[types.Part.from_text(text=text)]
            )
        )

    def add_assistant(self, text: str):
        self.messages.append(
            types.Content(
                role="model",
                parts=[types.Part.from_text(text=text)]
            )
        )

    def get(self):
        return list(self.messages)