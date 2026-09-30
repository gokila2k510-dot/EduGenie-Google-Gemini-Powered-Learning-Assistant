import google.generativeai as genai
from config import get_settings

settings = get_settings()

if settings.GEMINI_API_KEY:
    genai.configure(api_key=settings.GEMINI_API_KEY)

def generate_text(
    prompt: str,
    temperature: float = 0.4,
    max_output_tokens: int = 1000
) -> str:

    if not settings.GEMINI_API_KEY:
        raise RuntimeError(
            "GEMINI_API_KEY is missing. Please add your Gemini API key to the .env file."
        )

    model = genai.GenerativeModel("gemini-1.5-pro")

    response = model.generate_content(
        prompt,
        generation_config={
            "temperature": temperature,
            "max_output_tokens": max_output_tokens,
        },
    )

    if not response or not response.text:
        raise RuntimeError("Gemini returned an empty response.")

    return response.text.strip()
