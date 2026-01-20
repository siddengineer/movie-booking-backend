from fastapi import FastAPI

app = FastAPI(title="Movie Booking Backend")

@app.get("/")
def home():
    return {"message": "Movie Booking Backend is running"}
