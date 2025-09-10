from pydantic import BaseModel
from typing import List, Optional
from .target import TargetCreate, Target

class MissionBase(BaseModel):
    is_completed: bool = False

class MissionCreate(MissionBase):
    cat_id: Optional[int] = None
    targets: List[TargetCreate]

class MissionUpdate(BaseModel):
    is_completed: Optional[bool] = None

class MissionInDB(MissionBase):
    id: int
    cat_id: Optional[int]
    targets: List[Target] = []

    class Config:
        orm_mode = True

class Mission(MissionInDB):
    pass
