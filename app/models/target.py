from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Target(Base):
    name = Column(String, nullable=False)
    country = Column(String, nullable=False)
    notes = Column(String, default="", nullable=True)
    is_completed = Column(Boolean, default=False, nullable=False)

    mission_id = Column(Integer, ForeignKey("missions.id"), nullable=False)
    mission = relationship("Mission", back_populates="targets")