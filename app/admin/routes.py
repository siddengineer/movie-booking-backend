# # app/admin/routes.py
# from fastapi import APIRouter

# router = APIRouter(prefix="/admin", tags=["Admin"])

# @router.get("/ping")
# def ping():
#     return {"message": "Admin route works!"}
# from fastapi import APIRouter

# router = APIRouter(prefix="/admin", tags=["Admin"])

# @router.post("/movies")
# def create_movie():
#     return {"msg": "Movie created"}
# from fastapi import APIRouter, Depends
# from app.auth.dependencies import get_current_admin_user

# router = APIRouter(prefix="/admin", tags=["Admin"])

# @router.post("/movies")
# def create_movie(movie: MovieSchema, admin_user: User = Depends(get_current_admin_user), db: Session = Depends(get_db)):
#     # Now admin_user is guaranteed to be an admin
#     new_movie = Movie(title=movie.title, description=movie.description)
#     db.add(new_movie)
#     db.commit()
#     db.refresh(new_movie)
#     return new_movie
# app/admin/routes.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.auth.dependencies import get_current_admin_user
from app.core.database import get_db
from app.models.user import User
from app.models.movie import Movie
from pydantic import BaseModel

router = APIRouter(prefix="/admin", tags=["Admin"])

# Pydantic schema for input validation
class MovieSchema(BaseModel):
    title: str
    description: str

# Admin-only route to create a movie
@router.post("/movies", response_model=MovieSchema)
def create_movie(
    movie: MovieSchema,
    admin_user: User = Depends(get_current_admin_user),  # ensures only admin can access
    db: Session = Depends(get_db)
):
    # Check if movie with same title exists
    existing_movie = db.query(Movie).filter(Movie.title == movie.title).first()
    if existing_movie:
        raise HTTPException(status_code=400, detail="Movie already exists")

    # Create new movie
    new_movie = Movie(title=movie.title, description=movie.description)
    db.add(new_movie)
    db.commit()
    db.refresh(new_movie)

    return MovieSchema(title=new_movie.title, description=new_movie.description)
