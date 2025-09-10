from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app import crud, schemas
from app.database import get_db

router = APIRouter()

@router.get("/", response_model=List[schemas.mission.Mission])
def list_missions(skip: int = 0, limit: int | None = 100, db: Session = Depends(get_db)):
    return crud.get_missions(db, skip=skip, limit=limit)

@router.get("/{mission_id}", response_model=schemas.mission.Mission)
def get_mission(mission_id: int, db: Session = Depends(get_db)):
    return crud.get_mission(db, mission_id)

@router.post("/", response_model=schemas.mission.Mission)
def create_mission(mission: schemas.mission.MissionCreate, db: Session = Depends(get_db)):
    return crud.create_mission(db, mission)

@router.patch("/{mission_id}", response_model=schemas.mission.Mission)
def update_mission(mission_id: int, mission_update: schemas.mission.MissionUpdate, db: Session = Depends(get_db)):
    return crud.update_mission(db, mission_id, mission_update)

@router.delete("/{mission_id}")
def delete_mission(mission_id: int, db: Session = Depends(get_db)):
    return crud.delete_mission(db, mission_id)

@router.post("/{mission_id}/assign_cat/{cat_id}", response_model=schemas.mission.Mission)
def assign_cat_to_mission(mission_id: int, cat_id: int, db: Session = Depends(get_db)):
    return crud.assign_cat_to_mission(db, mission_id, cat_id)
