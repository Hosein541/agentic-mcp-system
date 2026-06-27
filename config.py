from dataclasses import dataclass
import os

from dotenv import load_dotenv

load_dotenv()


@dataclass
class Settings:

    gemini_api_key: str

    model_name: str


settings = Settings(

    gemini_api_key=os.getenv("GEMINI_API_KEY"),

    model_name=os.getenv(
        "MODEL_NAME",
        "gemini-3.1-flash-lite"
    )
)