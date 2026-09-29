import json
import re
from gemini_client import generate_text


def clean_json_block(text: str) -> str:
    """Remove Markdown code fences before JSON parsing."""
    text = text.strip()
    text = re.sub(r"^```(?:json)?\s*", "", text, flags=re.IGNORECASE)
    text = re.sub(r"\s*```$", "", text)
    return text.strip()


def generate_quiz(passage: str):
    prompt = f"""
Create exactly 3 multiple-choice questions from the passage below.

Return ONLY valid JSON in this structure:
[
  {{
    "question": "Question text",
    "options": ["A", "B", "C", "D"],
    "answer": "A"
  }}
]

The answer must be the exact option text, not the letter.

Passage:
{passage}
"""
    try:
        raw = generate_text(prompt)
        cleaned = clean_json_block(raw)
        data = json.loads(cleaned)

        if not isinstance(data, list):
            raise ValueError("Quiz response is not a JSON list.")

        return data
    except Exception as exc:
        return {"error": f"Quiz generation/parsing error: {exc}"}
