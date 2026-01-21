from fastapi import FastAPI
from app.api.auth import router as auth_router

app = FastAPI(title="Movie Booking Backend")

@app.get("/")
def home():
    return {"message": "Movie Booking Backend is running"}

app.include_router(auth_router)
