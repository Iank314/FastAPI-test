# FastAPI-Test

A simple FastAPI application with JWT-protected endpoints for Users, Projects, Tasks and Comments, backed by SQLModel (SQLAlchemy + Pydantic).

## Prerequisites

- **Python 3.10+**  
- **pip** (comes with Python)  
- (optional) **Git**  

## Setup

1. **Clone the repo**  
   ```bash
   git clone https://github.com/yourusername/FastAPI-test.git
   cd FastAPI-test

Create through Windows
python -m venv .venv
.\.venv\Scripts\Activate.ps1

pip install --upgrade pip
pip install -r requirements.txt



By default this project uses SQLite. Create a file called .env in the project root (next to app/) with:

DATABASE_URL=sqlite:///./app.db
JWT_SECRET_KEY=your-super-secret-key

uvicorn app.main:app --reload --host 127.0.0.1 --port 8000

You can either curl the information you want to upload or directly add it on FastAPI