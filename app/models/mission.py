from sqlalchemy import Column, Boolean
from sqlalchemy.orm import relationship
from app.database import Base

class Mission(Base):
    is_completed = Column(Boolean, default=False, nullable=False)
    
    cat = relationship("Cat", back_populates="assigned_mission", uselist=False)
    targets = relationship("Target", back_populates="mission", cascade="all, delete-orphan")
    