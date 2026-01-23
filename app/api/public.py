from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.models.movie import Movie
from app.models.theater import Theater
from app.schemas.movie import MovieResponse
from app.schemas.theater import TheaterResponse

router = APIRouter(tags=["Public"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/movies", response_model=list[MovieResponse])
def list_movies(db: Session = Depends(get_db)):
    return db.query(Movie).all()

@router.get("/theaters", response_model=list[TheaterResponse])
def list_theaters(db: Session = Depends(get_db)):
    return db.query(Theater).all()
