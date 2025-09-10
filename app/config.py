import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", f"sqlite:///cat.db")
CAT_API_URL = os.getenv("CAT_API_URL", "https://api.thecatapi.com/v1/breeds")