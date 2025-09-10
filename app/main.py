from fastapi import FastAPI
from app.routers.api import api_router

app = FastAPI(title="Spy Cat Agency API")

app.include_router(api_router)