from gemini_client import generate_text


def summarize_text(text: str) -> str:
    prompt = f"""
Summarize the following educational passage.
Keep the important ideas and remove repetition.
Use clear, concise language suitable for a student.

Passage:
{text}
"""
    try:
        return generate_text(prompt)
    except Exception as exc:
        return f"Summary error: {exc}"
