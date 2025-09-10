from pydantic import BaseModel, Field
from typing import Optional

class CatBase(BaseModel):
    name: str
    years_experience: int
    breed: str
    salary: float

class CatCreate(CatBase):
    pass

class CatUpdate(BaseModel):
    salary: float

class CatInDB(CatBase):
    id: int
    assigned_mission_id: Optional[int]

    class Config:
        orm_mode = True

class Cat(CatInDB):
    pass
