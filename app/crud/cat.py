from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models import Cat
from app.schemas.cat import CatCreate, CatUpdate
from app.services import is_valid_breed


def get_cats(db: Session, skip: int = 0, limit: int | None = None):
    query = db.query(Cat).offset(skip)
    if limit is not None:
        query = query.limit(limit)
    cats = query.all()
    return cats


def get_cat(db: Session, cat_id: int):
    cat = db.query(Cat).filter(Cat.id == cat_id).first()
    if not cat:
        raise HTTPException(status_code=404, detail="Cat not found.")
    return cat


def create_cat(db: Session, cat: CatCreate):
    if not is_valid_breed(cat.breed):
        raise HTTPException(status_code=400, detail="Invalid cat breed.")
    
    cat_create = cat.model_dump(exclude_unset=True)

    if "salary" in cat_create and cat_create["salary"] < 0:
        raise HTTPException(status_code=400, detail="Salary must be at least 0.")

    if "years_experience" in cat_create and cat_create["years_experience"] < 0:
        raise HTTPException(status_code=400, detail="Years experience must be at least 0.")
    
    db_cat = Cat(**cat.model_dump())
    db.add(db_cat)
    db.commit()
    db.refresh(db_cat)
    return db_cat


def update_cat(db: Session, cat_id: int, cat_update: CatUpdate):
    if cat_id <= 0:
        raise HTTPException(status_code=400, detail="Invalid cat ID.")

    db_cat = db.query(Cat).filter(Cat.id == cat_id).first()
    if not db_cat:
        raise HTTPException(status_code=404, detail="Cat not found.")

    update_data = cat_update.model_dump(exclude_unset=True)

    if "salary" in update_data and update_data["salary"] < 0:
        raise HTTPException(status_code=400, detail="Salary must be at least 0.")

    for key, value in update_data.items():
        setattr(db_cat, key, value)

    db.commit()
    db.refresh(db_cat)
    return db_cat


def delete_cat(db: Session, cat_id: int):
    db_cat = db.query(Cat).filter(Cat.id == cat_id).first()
    if not db_cat:
        raise HTTPException(status_code=404, detail="Cat not found.")

    db.delete(db_cat)
    db.commit()
    return {"detail": f"Cat with id {cat_id} deleted successfully."}
