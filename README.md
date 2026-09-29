# EduGenie: Google Gemini Powered Learning Assistant

EduGenie is an AI-powered educational assistant documented in the accompanying project report. It provides:

- Question & Answer
- Simple topic explanations
- MCQ quiz generation
- Text summarization
- Personalized learning-path recommendations

## Architecture

The project follows the report's documented structure:

```text
EduGenie/
├── main.py
├── gemini_client.py
├── explanation_module.py
├── qna.py
├── quiz_module.py
├── summary_module.py
├── learning_path.py
├── templates/
│   └── index.html
├── static/
│   └── style.css
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

The report specifies FastAPI for the backend, HTML/CSS for the frontend, Gemini for Q&A/quiz/summary/learning paths, and a lightweight local explanation model. This GitHub package implements the documented application flow with Gemini-backed modules. The original source code was not included in the supplied PDF, so this is a reconstructed implementation rather than the original source.

## Prerequisites

- Python 3.10+
- Google Gemini API key
- Internet connection for Gemini API requests

## Installation

### 1. Create a virtual environment

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

macOS/Linux:

```bash
source .venv/bin/activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure the API key

Copy `.env.example` to `.env`:

```text
GEMINI_API_KEY=your_real_key
GEMINI_MODEL=gemini-1.5-pro
```

Never commit `.env` to GitHub.

### 4. Run the application

```bash
uvicorn main:app --reload
```

Open:

```text
http://127.0.0.1:8000
```

## API Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| POST | `/qa` | Question answering |
| POST | `/explain` | Explain a topic |
| POST | `/quiz` | Generate 3 MCQs |
| POST | `/summarize` | Summarize educational text |
| POST | `/learn/recommendations` | Generate a learning path |

## Example API request

```json
{
  "text": "Explain the Pythagoras theorem."
}
```

## GitHub upload

From the project folder:

```bash
git init
git add .
git commit -m "Initial EduGenie project"
git branch -M main
git remote add origin YOUR_GITHUB_REPOSITORY_URL
git push -u origin main
```

## Security

- Keep your Gemini API key in `.env`.
- `.env` is included in `.gitignore`.
- Do not paste API keys into source files or public GitHub repositories.

## Source basis

This implementation was reconstructed from the supplied EduGenie project document, which describes the folder architecture, FastAPI endpoints, frontend flow, Gemini-powered modules, and deployment command.
