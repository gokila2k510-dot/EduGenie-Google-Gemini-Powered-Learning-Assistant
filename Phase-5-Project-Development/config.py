import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
    EXPLANATION_PROVIDER = os.getenv("EXPLANATION_PROVIDER", "gemini")
    LOCAL_MODEL_NAME = os.getenv(
        "LOCAL_MODEL_NAME",
        "MBZUAI/LaMini-Flan-T5-783M"
    )

def get_settings():
    return Settings()
