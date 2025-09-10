from fastapi import APIRouter
from app.routers import cat, mission, target

api_router = APIRouter()

api_router.include_router(cat.router, prefix="/cats", tags=["Cats"])
api_router.include_router(mission.router, prefix="/missions", tags=["Missions"])
api_router.include_router(target.router, prefix="/targets", tags=["Targets"])
