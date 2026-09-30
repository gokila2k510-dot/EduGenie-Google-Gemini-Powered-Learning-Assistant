from gemini_client import generate_text
from utils import validate_input

def answer_question(question: str, level: str = "beginner") -> str:

    question = validate_input(question)

    prompt = f"""
You are EduGenie, an educational tutor.

Answer the student's question clearly.

Student level:
{level}

Question:
{question}

Instructions:
- Give a direct answer.
- Explain the concept simply.
- Use an example when useful.
- Avoid unnecessary advanced terminology.
- Make the answer educational and easy to understand.
"""

    return generate_text(
        prompt,
        temperature=0.4,
        max_output_tokens=1000
    )
