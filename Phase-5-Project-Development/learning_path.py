from gemini_client import generate_text
from utils import validate_input

def generate_learning_path(
    topic: str,
    level: str = "beginner"
) -> str:

    topic = validate_input(topic)

    prompt = f"""
You are EduGenie, an educational learning-path assistant.

Create a learning path for:

Topic:
{topic}

Student level:
{level}

The learning path should progress from beginner to advanced.

Include:

1. Prerequisites
2. Beginner topics
3. Intermediate topics
4. Advanced topics
5. Practice activities
6. Suggested learning resources
7. Final project or practical activity

Use clear and simple language.
Format the answer using headings and bullet points.
"""

    return generate_text(
        prompt,
        temperature=0.4,
        max_output_tokens=1800
    )
