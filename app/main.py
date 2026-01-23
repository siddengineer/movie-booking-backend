# from fastapi import FastAPI
# from app.api.auth import router as auth_router

# app = FastAPI(title="Movie Booking Backend")

# @app.get("/")
# def home():
#     return {"message": "Movie Booking Backend is running"}

# app.include_router(auth_router)
# from fastapi import FastAPI
# from app.api import auth

# app = FastAPI(title="Movie Booking Backend")

# app.include_router(auth.router)

# @app.get("/")
# def home():
#     return {"message": "Movie Booking Backend is running"}
from fastapi import FastAPI
from app.api import admin, public
from app.api import screen, shows


app = FastAPI(title="Movie Booking Backend")

# app.include_router(admin.router)
# app.include_router(public.router)
# app.include_router(screen.router)
# app.include_router(shows.router)
app.include_router(admin.router, prefix="/admin")
app.include_router(public.router)
app.include_router(screen.router, prefix="/screen")
app.include_router(shows.router, prefix="/show")
@app.get("/")
def health():
    return {"status": "running"}
