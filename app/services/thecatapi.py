import requests
from fastapi import HTTPException
from app.config import CAT_API_URL

def is_valid_breed(breed_name: str) -> bool:
    response = requests.get(CAT_API_URL)
    if response.status_code != 200:
        raise HTTPException(status_code=502, detail="CatAPI unavailable.")
    breeds = [b["name"] for b in response.json()]
    return breed_name in breeds