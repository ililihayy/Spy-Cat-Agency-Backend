from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app import crud, schemas
from app.database import get_db

router = APIRouter()

@router.get("/", response_model=List[schemas.target.Target])
def list_targets(skip: int = 0, limit: int | None = 100, db: Session = Depends(get_db)):
    return crud.get_targets(db, skip=skip, limit=limit)

@router.get("/{target_id}", response_model=schemas.target.Target)
def get_target(target_id: int, db: Session = Depends(get_db)):
    target = crud.get_target(db, target_id)
    return target

@router.post("/", response_model=schemas.target.Target)
def create_target(target: schemas.target.TargetCreate, db: Session = Depends(get_db)):
    return crud.create_target(db, target)

@router.patch("/{target_id}", response_model=schemas.target.Target)
def update_target(target_id: int, target_update: schemas.target.TargetUpdate, db: Session = Depends(get_db)):
    updated = crud.update_target(db, target_id, target_update)
    return updated

@router.delete("/{target_id}", response_model=schemas.target.Target)
def delete_target(target_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_target(db, target_id)
    return deleted
