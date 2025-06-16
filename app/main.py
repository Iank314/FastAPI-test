from fastapi import FastAPI
from sqlmodel import SQLModel
from app.db.session import engine
import app.models  
from app.api import auth, projects, tasks, comments

app = FastAPI(debug=True)

@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)

app.include_router(auth.router)
app.include_router(projects.router, tags=["projects"])
app.include_router(tasks.router, tags=["tasks"])
app.include_router(comments.router, tags=["comments"])

for r in app.router.routes:
    if hasattr(r, "path"):
        print(r.methods, r.path)