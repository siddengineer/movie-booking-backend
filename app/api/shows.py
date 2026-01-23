from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from datetime import datetime
from app.core.database import SessionLocal
from app.models.show import Show

router = APIRouter(prefix="/shows", tags=["Shows"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def create_show(movie_id: int, screen_id: int, start_time: datetime, end_time: datetime, price: float, db: Session = Depends(get_db)):
    # Check time conflict in the same screen
    conflict = db.query(Show).filter(
        Show.screen_id == screen_id,
        Show.start_time < end_time,
        Show.end_time > start_time
    ).first()
    if conflict:
        raise HTTPException(status_code=400, detail="Time conflict with another show in this screen")
    
    show = Show(movie_id=movie_id, screen_id=screen_id, start_time=start_time, end_time=end_time, price=price)
    db.add(show)
    db.commit()
    db.refresh(show)
    return show

@router.get("/")
def list_shows(db: Session = Depends(get_db)):
    return db.query(Show).all()

@router.get("/movie/{movie_id}")
def get_shows_for_movie(movie_id: int, db: Session = Depends(get_db)):
    return db.query(Show).filter(Show.movie_id == movie_id).all()
