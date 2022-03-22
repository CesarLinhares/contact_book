from fastapi import FastAPI
from src.routes.routers import route

app = FastAPI()

app.include_router(route)
