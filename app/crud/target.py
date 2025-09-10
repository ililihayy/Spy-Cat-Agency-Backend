from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models import Target, Mission
from app.schemas.target import TargetCreate, TargetUpdate


def get_targets(db: Session, skip: int = 0, limit: int | None = None):
    query = db.query(Target).offset(skip)
    if limit is not None:
        query = query.limit(limit)
    return query.all()


def get_target(db: Session, target_id: int):
    return db.query(Target).filter(Target.id == target_id).first()


def create_target(db: Session, target: TargetCreate):
    mission = db.query(Mission).filter(Mission.id == target.mission_id).first()
    if not mission:
        raise HTTPException(status_code=404, detail="Mission not found.")
    db_target = Target(
        name=target.name,
        country=target.country,
        notes=target.notes,
        mission=mission,
        is_completed=False
    )
    db.add(db_target)
    db.commit()
    db.refresh(db_target)
    return db_target


def update_target(db: Session, target_id: int, target_update: TargetUpdate):
    db_target = get_target(db, target_id)
    if not db_target:
        return None
    if target_update.notes is not None:
        if db_target.is_completed or db_target.mission.is_completed:
            raise HTTPException(status_code=400, detail="Cannot update notes for completed target or mission.")
        db_target.notes = target_update.notes
    if target_update.is_completed is not None:
        db_target.is_completed = target_update.is_completed
    db.commit()
    db.refresh(db_target)
    return db_target


def delete_target(db: Session, target_id: int):
    db_target = get_target(db, target_id)
    if not db_target:
        raise HTTPException(status_code=404, detail="Target not found.")
    db.delete(db_target)
    db.commit()
    return db_target
