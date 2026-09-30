from utils import validate_input


def generate_quiz(
    text: str,
    level: str = "beginner",
) -> dict:
    text = validate_input(text)

    return {
        "questions": [
            {
                "question": f"What is the main topic discussed in: {text[:80]}?",
                "options": [
                    "The topic provided",
                    "A different topic",
                    "An unrelated topic",
                    "None of these",
                ],
                "correct_answer": "The topic provided",
                "explanation": "The quiz is generated from the learning material provided by the student.",
            },
            {
                "question": "Why is learning the topic important?",
                "options": [
                    "It helps understand the subject",
                    "It has no purpose",
                    "It is unrelated to education",
                    "It should not be studied",
                ],
                "correct_answer": "It helps understand the subject",
                "explanation": "Understanding the topic helps the student learn the subject better.",
            },
            {
                "question": "What should a student do after learning a topic?",
                "options": [
                    "Practice the topic",
                    "Ignore the topic",
                    "Delete the notes",
                    "Stop learning",
                ],
                "correct_answer": "Practice the topic",
                "explanation": "Practice helps students remember and understand what they learned.",
            },
        ]
    }