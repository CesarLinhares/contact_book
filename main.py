import uvicorn
from fastapi import FastAPI
from src.routes.routers import route
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=['*'],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(route)

if __name__ == "__main__":
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=5656,
    )