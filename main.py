import uvicorn
from fastapi import FastAPI
from src.routes.routers import route

app = FastAPI()

app.include_router(route)

if __name__ == "__main__":
    uvicorn.run(
        app,
        host="127.0.0.1",
        port=5656,
    )