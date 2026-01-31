from dotenv import load_dotenv
import os

load_dotenv()  # reads .env and populates os.environ

DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")
DB_PORT = os.getenv("DB_PORT", "5432")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")