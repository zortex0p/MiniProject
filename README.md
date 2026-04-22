# LegalDocSimplifier

LegalDocSimplifier is a lightweight web app for helping users understand legal documents in simpler language.

This repository now contains the cleaned source for the app that is currently running locally:
- `frontend/` for the webpage
- `backend/` for the Flask API
- `run-local-backend.cmd` to start the API on Windows
- `run-local-frontend.cmd` to start the frontend on Windows

## Features

- Paste legal text into the webpage
- Upload PDF files for extraction
- Detect common contract clause categories
- Show plain-English explanations
- Assign risk labels
- Suggest negotiation tips

## Project Structure

```text
LegalDocSimplifier/
  backend/
    .env.example
    app.py
    config.py
    README.md
    requirements.txt
    test_api.py
    wsgi.py
  frontend/
    index.html
  .gitignore
  README.md
  run-local-backend.cmd
  run-local-frontend.cmd
```

## Run Locally

Start the backend:

```bat
run-local-backend.cmd
```

Start the frontend in a second terminal:

```bat
run-local-frontend.cmd
```

Then open:

```text
http://127.0.0.1:8000
```

## Manual Setup

If you want to run it without the helper scripts:

```bat
cd backend
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
set ANTHROPIC_API_KEY=your_key_here
python app.py
```

In another terminal:

```bat
cd frontend
python -m http.server 8000
```

## API Endpoints

- `GET /api/health`
- `POST /api/simplify`
- `POST /api/upload-pdf`
- `POST /api/translate`

## Notes

- The backend can fall back to pattern-based clause extraction if the full transformer stack is not available.
- A real `ANTHROPIC_API_KEY` gives the best results for analysis and translation.
- This project is for educational use and is not legal advice.
