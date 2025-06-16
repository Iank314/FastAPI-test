from sqlalchemy.orm import Session
from typing import List
from app.models.task import Task, TaskStatus
from app.schemas.task import TaskCreate, TaskUpdate

def create_task(db: Session, project_id: str, task_in: TaskCreate) -> Task:
    task = Task(project_id=project_id, **task_in.dict())
    db.add(task)
    db.commit()
    db.refresh(task)
    return task


def get_task(db: Session, task_id: str) -> Task | None:
    return db.query(Task).get(task_id)


def get_tasks(db: Session, project_id: str, status: str | None = None) -> List[Task]:
    q = db.query(Task).filter(Task.project_id == project_id)
    if status:
        q = q.filter(Task.status == status)
    return q.all()


def update_task(db: Session, task: Task, task_in: TaskUpdate) -> Task:
    for field, val in task_in.dict(exclude_unset=True).items():
        setattr(task, field, val)
    db.commit()
    db.refresh(task)
    return task


def delete_task(db: Session, task: Task) -> None:
    db.delete(task)
    db.commit()
