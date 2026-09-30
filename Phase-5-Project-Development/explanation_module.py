from gemini_client import generate_text
from utils import validate_input

def explain_topic(topic: str, level: str = "beginner") -> str:

    topic = validate_input(topic)

    prompt = f"""
You are EduGenie, an educational tutor.

Explain the following topic to a student.

Topic:
{topic}

Student level:
{level}

Your explanation should:

1. Start with a simple definition.
2. Explain the main idea clearly.
3. Break difficult parts into small steps.
4. Give one simple example.
5. Mention common mistakes or misunderstandings.
6. End with a short recap.

Use clear and simple educational language.
Avoid unnecessary advanced terminology.
"""

    return generate_text(
        prompt,
        temperature=0.35,
        max_output_tokens=1400
    )
