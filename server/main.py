from typing import Union

from fastapi import FastAPI
from db import init_db, health_connection

app = FastAPI()
init_db()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/healthz")
def health_check():
    health_connection()
    return {"status": "healthy"}