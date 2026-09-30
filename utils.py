def validate_input(text: str) -> str:
    if not text or not text.strip():
        raise ValueError("Input cannot be empty.")

    return text.strip()