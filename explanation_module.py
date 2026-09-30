from gemini_client import generate_text


def explain_topic(topic: str, level: str = "beginner") -> str:
    prompt = f"""
You are EduGenie, an educational AI learning assistant.

Explain the following topic to a student in a simple and student-friendly way.

Topic:
{topic}

Student Level:
{level}

Include:
1. Simple definition
2. Key points
3. Easy example
4. Short summary
"""

    return generate_text(prompt)