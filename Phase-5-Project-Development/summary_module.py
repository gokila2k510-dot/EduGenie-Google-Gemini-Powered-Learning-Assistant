from gemini_client import generate_text
from utils import validate_input

def summarize_text(text: str) -> str:

    text = validate_input(text, max_length=10000)

    prompt = f"""
You are EduGenie, an educational tutor.

Summarize the following educational text.

Text:
{text}

Instructions:

1. Identify the main idea.
2. Include the most important points.
3. Remove unnecessary repetition.
4. Use simple and clear language.
5. Present the summary in an easy-to-read format.
"""

    return generate_text(
        prompt,
        temperature=0.3,
        max_output_tokens=1200
    )
