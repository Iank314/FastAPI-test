from sqlalchemy.orm import Session
from typing import List
from app.models.project import Project
from app.schemas.project import ProjectCreate, ProjectUpdate

def create_project(db: Session, owner_id: str, proj_in: ProjectCreate) -> Project:
    proj = Project(owner_id=owner_id, **proj_in.dict())
    db.add(proj)
    db.commit()
    db.refresh(proj)
    return proj


def get_project(db: Session, project_id: str) -> Project | None:
    return db.query(Project).get(project_id)


def get_projects_by_owner(db: Session, owner_id: str) -> List[Project]:
    return db.query(Project).filter(Project.owner_id == owner_id).all()


def update_project(db: Session, proj: Project, proj_in: ProjectUpdate) -> Project:
    for field, val in proj_in.dict(exclude_unset=True).items():
        setattr(proj, field, val)
    db.commit()
    db.refresh(proj)
    return proj


def delete_project(db: Session, proj: Project) -> None:
    db.delete(proj)
    db.commit()
