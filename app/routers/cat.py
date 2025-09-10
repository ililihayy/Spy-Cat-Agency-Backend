from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app import crud, schemas
from app.database import get_db

router = APIRouter()
@router.get("/", response_model=List[schemas.cat.Cat])
def list_cats(skip: int = 0, limit: int | None = 100, db: Session = Depends(get_db)):
    return crud.get_cats(db, skip=skip, limit=limit)

@router.get("/{cat_id}", response_model=schemas.cat.Cat)
def get_cat(cat_id: int, db: Session = Depends(get_db)):
    return crud.get_cat(db, cat_id)

@router.post("/", response_model=schemas.cat.Cat)
def create_cat(cat: schemas.cat.CatCreate, db: Session = Depends(get_db)):
    return crud.create_cat(db, cat)

@router.patch("/{cat_id}", response_model=schemas.cat.Cat)
def update_cat(cat_id: int, cat_update: schemas.cat.CatUpdate, db: Session = Depends(get_db)):
    return crud.update_cat(db, cat_id, cat_update)

@router.delete("/{cat_id}")
def delete_cat(cat_id: int, db: Session = Depends(get_db)):
    return crud.delete_cat(db, cat_id)
