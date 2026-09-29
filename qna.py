from gemini_client import generate_text


def answer_question(question: str) -> str:
    prompt = f"""
You are EduGenie, an academic question-answering assistant.

Answer the student's question clearly and concisely.
If the question needs explanation, provide the key reasoning or steps.

Question:
{question}
"""
    try:
        return generate_text(prompt)
    except Exception as exc:
        return f"Q&A error: {exc}"
