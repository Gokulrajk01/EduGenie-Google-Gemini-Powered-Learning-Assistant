from gemini_client import generate_text


def get_learning_recommendations(topic: str) -> str:
    prompt = f"""
Create a personalized learning path for the topic below.

Organize it from beginner to advanced.
For each stage, include:
1. Topics to learn
2. A suggested sequence
3. Practice suggestions
4. Useful resource types such as videos, articles, documentation, or books

Keep the plan practical and easy to follow.

Topic:
{topic}
"""
    try:
        return generate_text(prompt)
    except Exception as exc:
        return f"Learning-path error: {exc}"
