from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models import Mission, Target, Cat
from app.schemas.mission import MissionCreate, MissionUpdate


def get_missions(db: Session, skip: int = 0, limit: int | None = None):
    query = db.query(Mission).offset(skip)
    if limit is not None:
        query = query.limit(limit)
    missions = query.all()
    if not missions:
        raise HTTPException(status_code=404, detail="No missions found.")
    return missions


def get_mission(db: Session, mission_id: int):
    mission = db.query(Mission).filter(Mission.id == mission_id).first()
    if not mission:
        raise HTTPException(status_code=404, detail="Mission not found.")
    return mission


def create_mission(db: Session, mission: MissionCreate):
    db_mission = Mission(is_completed=False)
    if mission.cat_id:
        cat = db.query(Cat).filter(Cat.id == mission.cat_id).first()
        if not cat:
            raise HTTPException(status_code=404, detail="Cat not found for this mission.")
        db_mission.cat = cat

    for t in mission.targets:
        db_mission.targets.append(Target(**t.model_dump()))

    db.add(db_mission)
    db.commit()
    db.refresh(db_mission)
    return db_mission


def update_mission(db: Session, mission_id: int, mission_update: MissionUpdate):
    if mission_id <= 0:
        raise HTTPException(status_code=400, detail="Invalid mission ID.")

    mission = db.query(Mission).filter(Mission.id == mission_id).first()
    if not mission:
        raise HTTPException(status_code=404, detail="Mission not found.")

    update_data = mission_update.model_dump(exclude_unset=True)

    if "is_completed" in update_data:
        mission.is_completed = update_data["is_completed"]

    db.commit()
    db.refresh(mission)
    return mission


def delete_mission(db: Session, mission_id: int):
    mission = db.query(Mission).filter(Mission.id == mission_id).first()
    if not mission:
        raise HTTPException(status_code=404, detail="Mission not found.")

    if mission.cat:
        raise HTTPException(status_code=400, detail="Mission is assigned to a cat and cannot be deleted.")

    db.delete(mission)
    db.commit()
    return {"detail": f"Mission with id {mission_id} deleted successfully."}


def assign_cat_to_mission(db: Session, mission_id: int, cat_id: int):
    mission = db.query(Mission).filter(Mission.id == mission_id).first()
    if not mission:
        raise HTTPException(status_code=404, detail="Mission not found.")

    cat = db.query(Cat).filter(Cat.id == cat_id).first()
    if not cat:
        raise HTTPException(status_code=404, detail="Cat not found.")

    mission.cat = cat
    db.commit()
    db.refresh(mission)
    return mission
