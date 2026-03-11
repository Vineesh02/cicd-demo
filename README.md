# CI/CD Demo

Simple FastAPI application used to test CI/CD pipelines.

## Project Structure

- `app/main.py`: FastAPI application factory and ASGI app.
- `app/routes.py`: Basic API routes.
- `tests/test_api.py`: Pytest tests for the API.
- `requirements.txt`: Python dependencies.
- `Dockerfile`: Container image definition.
- `.gitignore`: Standard Python ignores.

## Local Setup

```bash
cd cicd-demo
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

Run the app:

```bash
uvicorn app.main:app --reload
```

Run tests:

```bash
pytest
```

## Docker

Build the image:

```bash
docker build -t cicd-demo .
```

Run the container:

```bash
docker run -p 8000:8000 cicd-demo
```

