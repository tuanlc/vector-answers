from contextlib import asynccontextmanager
from fastapi import FastAPI
from db import init_db, health_connection, release_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield
    release_db()

app = FastAPI(lifespan=lifespan)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/healthz")
def health_check():
    health_connection()
    return {"status": "healthy"}