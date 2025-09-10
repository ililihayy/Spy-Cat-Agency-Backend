from pydantic import BaseModel
from typing import Optional

class TargetBase(BaseModel):
    name: str
    country: str
    notes: Optional[str] = ""
    is_completed: bool = False

class TargetCreate(TargetBase):
    pass

class TargetUpdate(BaseModel):
    notes: Optional[str] = None
    is_completed: Optional[bool] = None

class TargetInDB(TargetBase):
    id: int
    mission_id: int

    class Config:
        orm_mode = True

class Target(TargetInDB):
    pass
