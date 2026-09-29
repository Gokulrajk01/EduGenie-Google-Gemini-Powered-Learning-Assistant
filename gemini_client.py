import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
MODEL_NAME = os.getenv("GEMINI_MODEL", "gemini-1.5-pro")

try:
    import google.generativeai as genai
except ImportError:
    genai = None


def get_model():
    """Create a Gemini model client using the API key in .env."""
    if not API_KEY:
        raise RuntimeError(
            "GEMINI_API_KEY is missing. Add it to your .env file."
        )

    if genai is None:
        raise RuntimeError(
            "google-generativeai is not installed. Run: pip install -r requirements.txt"
        )

    genai.configure(api_key=API_KEY)
    return genai.GenerativeModel(MODEL_NAME)


def generate_text(prompt: str) -> str:
    model = get_model()
    response = model.generate_content(prompt)

    text = getattr(response, "text", None)
    if not text:
        raise RuntimeError("Gemini returned an empty response.")
    return text.strip()
