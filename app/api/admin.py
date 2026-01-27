from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.auth.dependencies import get_current_admin_user
from app.core.database import SessionLocal
from app.models.movie import Movie
from app.models.theater import Theater
from app.schemas.movie import MovieCreate, MovieResponse
from app.schemas.theater import TheaterCreate, TheaterResponse
from app.auth.dependencies import get_current_user  # from Day 4
from app.schemas.screen import ScreenCreate, ScreenResponse
from app.schemas.show import ShowCreate, ShowResponse

router = APIRouter(prefix="/admin", tags=["Admin"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/movies", response_model=MovieResponse)
def create_movie(
    movie: MovieCreate,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    new_movie = Movie(**movie.dict())
    db.add(new_movie)
    db.commit()
    db.refresh(new_movie)
    return new_movie

@router.post("/theaters", response_model=TheaterResponse)
def create_theater(
    theater: TheaterCreate,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    new_theater = Theater(**theater.dict())
    db.add(new_theater)
    db.commit()
    db.refresh(new_theater)
    return new_theater
