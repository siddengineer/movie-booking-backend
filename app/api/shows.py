# from fastapi import APIRouter, HTTPException, Depends
# from sqlalchemy.orm import Session
# from datetime import datetime
# from app.core.database import SessionLocal
# from app.models.show import Show

# router = APIRouter(prefix="/shows", tags=["Shows"])

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# @router.post("/")
# def create_show(movie_id: int, screen_id: int, start_time: datetime, end_time: datetime, price: float, db: Session = Depends(get_db)):
#     # Check time conflict in the same screen
#     conflict = db.query(Show).filter(
#         Show.screen_id == screen_id,
#         Show.start_time < end_time,
#         Show.end_time > start_time
#     ).first()
#     if conflict:
#         raise HTTPException(status_code=400, detail="Time conflict with another show in this screen")
    
#     show = Show(movie_id=movie_id, screen_id=screen_id, start_time=start_time, end_time=end_time, price=price)
#     db.add(show)
#     db.commit()
#     db.refresh(show)
#     return show

# @router.get("/")
# def list_shows(db: Session = Depends(get_db)):
#     return db.query(Show).all()

# @router.get("/movie/{movie_id}")
# def get_shows_for_movie(movie_id: int, db: Session = Depends(get_db)):
#     return db.query(Show).filter(Show.movie_id == movie_id).all()
# from fastapi import APIRouter, HTTPException, Depends
# from sqlalchemy.orm import Session
# from app.core.database import SessionLocal
# from app.models.show import Show
# from app.schemas.show import ShowCreate, ShowResponse
# from typing import List

# router = APIRouter(prefix="/shows", tags=["Shows"])

# # Database dependency
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


# # Create a new show
# @router.post("/", response_model=ShowResponse)
# def create_show(show: ShowCreate, db: Session = Depends(get_db)):
#     # Check for time conflict in the same screen
#     conflict = db.query(Show).filter(
#         Show.screen_id == show.screen_id,
#         Show.start_time < show.end_time,
#         Show.end_time > show.start_time
#     ).first()
    
#     if conflict:
#         raise HTTPException(status_code=400, detail="Time conflict with another show in this screen")
    
#     new_show = Show(**show.dict())
#     db.add(new_show)
#     db.commit()
#     db.refresh(new_show)
#     return new_show


# # List all shows
# @router.get("/", response_model=List[ShowResponse])
# def list_shows(db: Session = Depends(get_db)):
#     return db.query(Show).all()


# # Get shows for a specific movie
# @router.get("/movie/{movie_id}", response_model=List[ShowResponse])
# def get_shows_for_movie(movie_id: int, db: Session = Depends(get_db)):
#     return db.query(Show).filte
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from datetime import datetime
from app.core.database import SessionLocal
from app.models.show import Show
from app.schemas.show import ShowCreate, ShowResponse  # import your schemas

router = APIRouter(prefix="/shows", tags=["Shows"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=ShowResponse)
def create_show(show: ShowCreate, db: Session = Depends(get_db)):
    # Check time conflict in the same screen
    conflict = db.query(Show).filter(
        Show.screen_id == show.screen_id,
        Show.start_time < show.end_time,
        Show.end_time > show.start_time
    ).first()
    if conflict:
        raise HTTPException(status_code=400, detail="Time conflict with another show in this screen")
    
    new_show = Show(**show.dict())
    db.add(new_show)
    db.commit()
    db.refresh(new_show)
    return new_show

@router.get("/", response_model=list[ShowResponse])
def list_shows(db: Session = Depends(get_db)):
    return db.query(Show).all()

@router.get("/movie/{movie_id}", response_model=list[ShowResponse])
def get_shows_for_movie(movie_id: int, db: Session = Depends(get_db)):
    return db.query(Show).filter(Show.movie_id == movie_id).all()
