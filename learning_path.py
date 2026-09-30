from gemini_client import generate_text


def get_learning_recommendations(
    topic: str,
    level: str = "beginner",
    timeline: str = "4 weeks",
) -> str:

    prompt = f"""
You are EduGenie, an AI learning assistant.

Create a simple and practical learning path for the following topic.

Topic:
{topic}

Student Level:
{level}

Available Timeline:
{timeline}

Include:

1. Beginner Topics
2. Intermediate Topics
3. Advanced Topics
4. Practice Suggestions
5. Recommended Learning Order
6. A simple timeline-based study plan

Requirements:
- Keep the explanation student-friendly.
- Use simple and clear language.
- Arrange topics in a logical order.
- Give practical practice suggestions.
- Match the learning path to the student's level.
- Match the plan to the available timeline.
"""

    return generate_text(prompt)