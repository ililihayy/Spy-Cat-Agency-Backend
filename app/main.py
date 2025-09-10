from fastapi import FastAPI
from app.routers.api import api_router
from app.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Spy Cat Agency API")

app.include_router(api_router)