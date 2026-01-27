# from pydantic import BaseModel
# from datetime import datetime

# class ShowCreate(BaseModel):
#     movie_id: int
#     screen_id: int
#     start_time: datetime
#     end_time: datetime
#     price: float

# class ShowResponse(ShowCreate):
#     id: int

#     class Config:
#         from_attributes = True

# from pydantic import BaseModel
# from datetime import datetime

# class ShowCreate(BaseModel):
#     movie_id: int
#     screen_id: int
#     start_time: datetime
#     end_time: datetime
#     price: float

# class ShowResponse(BaseModel):
#     id: int
#     movie_id: int
#     screen_id: int
#     start_time: datetime
#     end_time: datetime
#     price: float

#     class Config:
#         orm_mode = True
# from pydantic import BaseModel
# from datetime import datetime

# class ShowCreate(BaseModel):
#     movie_id: int
#     screen_id: int
#     start_time: datetime
#     end_time: datetime
#     price: float

# class ShowResponse(BaseModel):
#     id: int
#     movie_id: int
#     screen_id: int
#     start_time: datetime
#     end_time: datetime
#     price: float

#     class Config:
#         orm_mode = True

from pydantic import BaseModel
from datetime import datetime

class ShowCreate(BaseModel):
    movie_id: int
    screen_id: int
    start_time: datetime
    end_time: datetime
    total_seats: int
    available_seats: int
    price_per_seat: float  # ✅ match your SQLAlchemy model

class ShowResponse(ShowCreate):
    id: int

    class Config:
        from_attributes = True  # updated for Pydantic v2 (was orm_mode)
