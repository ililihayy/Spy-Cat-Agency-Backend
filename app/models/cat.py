from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Cat(Base):
    name = Column(String, nullable=False)
    years_experience = Column(Integer, nullable=False)
    breed = Column(String, nullable=False)
    salary = Column(Float, nullable=False)

    assigned_mission_id = Column(Integer, ForeignKey("missions.id"), nullable=True)
    assigned_mission = relationship("Mission", back_populates="cat")
