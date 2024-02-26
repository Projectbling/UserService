from dotenv import load_dotenv
import os
from pydantic_settings import BaseSettings
# Load environment variables from .env file
load_dotenv()

# Get PostgreSQL connection details from environment variables

POSTGRES_USER = os.getenv("USER")
POSTGRES_PASSWORD = os.getenv("PASSWORD")
POSTGRES_SERVER = os.getenv("HOST")
POSTGRES_PORT = os.getenv("PORT")
POSTGRES_DB = os.getenv("DB")

class GetSettings(BaseSettings):
    
    DATABASE_URL:str = f"asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"
    