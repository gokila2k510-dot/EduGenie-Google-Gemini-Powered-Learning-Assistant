import json
import time

from config import GEMINI_API_KEY, GEMINI_MODEL, MAX_OUTPUT_TOKENS


_client = None


# --------------------------------------------------
# Gemini Client
# --------------------------------------------------

def get_client():
    global _client

    if _client is not None:
        return _client

    if not GEMINI_API_KEY:
        raise RuntimeError(
            "GEMINI_API_KEY is missing. "
            "Please add your Gemini API key to the .env file."
        )

    try:
        from google import genai

        _client = genai.Client(
            api_key=GEMINI_API_KEY
        )

        return _client

    except ImportError:
        raise RuntimeError(
            "google-genai package is not installed. "
            "Run: pip install -r requirements.txt"
        )


# --------------------------------------------------
# Generate Text
# --------------------------------------------------

def generate_text(prompt: str) -> str:

    client = get_client()

    max_retries = 3

    for attempt in range(max_retries):

        try:

            response = client.models.generate_content(
                model=GEMINI_MODEL,
                contents=prompt,
                config={
                    "temperature": 0.3,
                    "max_output_tokens": MAX_OUTPUT_TOKENS,
                },
            )

            text = getattr(response, "text", None)

            if not text:
                raise RuntimeError(
                    "Gemini returned an empty response."
                )

            return text.strip()

        except Exception as error:

            error_text = str(error).upper()

            temporary_error = (
                "503" in error_text
                or "UNAVAILABLE" in error_text
                or "500" in error_text
                or "INTERNAL" in error_text
                or "429" in error_text
                or "RESOURCE_EXHAUSTED" in error_text
            )

            if temporary_error and attempt < max_retries - 1:

                wait_time = 2 ** attempt

                print(
                    f"Gemini temporary error. "
                    f"Retrying in {wait_time} seconds..."
                )

                time.sleep(wait_time)

            else:

                raise RuntimeError(
                    f"Gemini API error: {error}"
                )


# --------------------------------------------------
# Clean JSON
# --------------------------------------------------

def clean_json_block(text: str) -> str:

    text = text.strip()

    if text.startswith("```"):

        lines = text.splitlines()

        if lines:
            lines = lines[1:]

        if lines and lines[-1].strip() == "```":
            lines = lines[:-1]

        text = "\n".join(lines)

    return text.strip()


# --------------------------------------------------
# Generate JSON
# --------------------------------------------------

def generate_json(prompt: str):

    raw_response = generate_text(prompt)

    cleaned_response = clean_json_block(
        raw_response
    )

    try:

        return json.loads(
            cleaned_response
        )

    except json.JSONDecodeError as error:

        raise RuntimeError(
            f"Gemini returned invalid JSON: {error}"
        )


# --------------------------------------------------
# Generate Structured Data
# --------------------------------------------------

def generate_structured(
    prompt: str,
    schema=None,
):

    client = get_client()

    max_retries = 3

    for attempt in range(max_retries):

        try:

            config = {
                "temperature": 0.3,
                "max_output_tokens": MAX_OUTPUT_TOKENS,
                "response_mime_type": "application/json",
            }

            if schema is not None:
                config["response_schema"] = schema

            response = client.models.generate_content(
                model=GEMINI_MODEL,
                contents=prompt,
                config=config,
            )

            text = getattr(response, "text", None)

            if not text:
                raise RuntimeError(
                    "Gemini returned an empty response."
                )

            cleaned_response = clean_json_block(
                text
            )

            try:

                result = json.loads(
                    cleaned_response
                )

            except json.JSONDecodeError as error:

                raise RuntimeError(
                    f"Gemini returned invalid JSON: {error}"
                )

            # If a Pydantic schema was supplied,
            # validate the returned JSON.
            if schema is not None:

                try:
                    return schema.model_validate(
                        result
                    )

                except AttributeError:
                    return result

            return result

        except Exception as error:

            error_text = str(error).upper()

            temporary_error = (
                "503" in error_text
                or "UNAVAILABLE" in error_text
                or "500" in error_text
                or "INTERNAL" in error_text
                or "429" in error_text
                or "RESOURCE_EXHAUSTED" in error_text
            )

            if temporary_error and attempt < max_retries - 1:

                wait_time = 2 ** attempt

                print(
                    f"Gemini temporary error. "
                    f"Retrying in {wait_time} seconds..."
                )

                time.sleep(wait_time)

            else:

                raise RuntimeError(
                    f"Gemini structured generation error: {error}"
                )