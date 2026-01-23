from pydantic import BaseModel
from datetime import datetime

class ShowCreate(BaseModel):
    movie_id: int
    screen_id: int
    start_time: datetime
    end_time: datetime
    price: float

class ShowResponse(ShowCreate):
    id: int

    class Config:
        from_attributes = True
