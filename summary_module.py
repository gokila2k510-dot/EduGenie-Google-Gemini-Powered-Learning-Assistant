from gemini_client import generate_text
from utils import validate_input


def summarize_text(
    text: str,
    level: str = "beginner",
) -> str:

    # Validate input
    text = validate_input(text)

    # Create prompt
    prompt = f"""
You are EduGenie, an educational summarization assistant.

Summarize the following educational material.

Student level:
{level}

Text:
{text}

Requirements:
- Preserve the important facts and ideas.
- Remove unnecessary repetition.
- Use clear and concise language.
- Organize the summary into short sections or bullet points
  when useful.
- Do not introduce facts that are not supported by the source.
- Make the result useful for revision.
"""

    # Generate summary using Gemini
    return generate_text(prompt)