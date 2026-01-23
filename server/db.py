import os

from sqlmodel import create_engine, SQLModel, Session
from sqlalchemy import text
from config import DB_USERNAME, DB_PASSWORD, DB_NAME, DB_PORT

DATABASE_URL = f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@localhost:{DB_PORT}/{DB_NAME}"
engine = create_engine(DATABASE_URL, echo=True)

def init_db():
    SQLModel.metadata.create_all(engine)

def health_connection():
    with Session(engine) as session:
        result = session.execute(text("SELECT 1"))
        for row in result:
            print(row)