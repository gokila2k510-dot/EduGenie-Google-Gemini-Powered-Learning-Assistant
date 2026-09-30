from gemini_client import generate_text
from utils import validate_input, parse_json_response

def generate_quiz(topic: str, level: str = "beginner"):

    topic = validate_input(topic)

    prompt = f"""
You are EduGenie, an educational quiz generator.

Create a quiz about:

Topic:
{topic}

Student level:
{level}

Create exactly 3 multiple-choice questions.

Each question must have:
- question
- 4 options
- correct_answer
- explanation

Return ONLY valid JSON.

Use this exact format:

[
  {{
    "question": "Question 1",
    "options": [
      "Option A",
      "Option B",
      "Option C",
      "Option D"
    ],
    "correct_answer": "Option A",
    "explanation": "Short explanation"
  }}
]
"""

    response = generate_text(
        prompt,
        temperature=0.4,
        max_output_tokens=1800
    )

    return parse_json_response(response)
