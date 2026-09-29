from gemini_client import generate_text


def explain_topic(topic: str) -> str:
    prompt = f"""
You are EduGenie, an educational assistant.

Explain the following topic in simple, beginner-friendly language.
Use short sections and examples where useful.
Avoid unnecessary technical jargon.

Topic:
{topic}
"""
    try:
        return generate_text(prompt)
    except Exception as exc:
        return f"Explanation error: {exc}"
