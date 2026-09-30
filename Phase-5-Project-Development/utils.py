import json
import re

def validate_input(value: str, max_length: int = 5000) -> str:
    if value is None:
        raise ValueError("Input cannot be empty.")

    value = value.strip()

    if not value:
        raise ValueError("Input cannot be empty.")

    if len(value) > max_length:
        raise ValueError(
            f"Input is too long. Maximum allowed length is {max_length} characters."
        )

    return value

def clean_json_response(text: str) -> str:
    text = text.strip()
    text = re.sub(r"^`(?:json)?\s*", "", text, flags=re.IGNORECASE)
    text = re.sub(r"\s*`$", "", text)
    return text.strip()

def parse_json_response(text: str):
    cleaned = clean_json_response(text)

    try:
        return json.loads(cleaned)
    except json.JSONDecodeError as exc:
        raise ValueError(
            "The AI returned an invalid JSON response."
        ) from exc
