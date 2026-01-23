from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.models.screen import Screen

router = APIRouter(prefix="/screens", tags=["Screens"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def create_screen(name: str, theater_id: int, capacity: int, db: Session = Depends(get_db)):
    screen = Screen(name=name, theater_id=theater_id, capacity=capacity)
    db.add(screen)
    db.commit()
    db.refresh(screen)
    return screen

@router.get("/")
def list_screens(db: Session = Depends(get_db)):
    return db.query(Screen).all()
