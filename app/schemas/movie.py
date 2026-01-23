# from pydantic import BaseModel
# from datetime import date

# class MovieCreate(BaseModel):
#     title: str
#     description: str | None = None
#     language: str
#     duration: int
#     release_date: date

# class MovieResponse(MovieCreate):
#     id: int

#     class Config:
#         orm_mode = True
from pydantic import BaseModel

class MovieCreate(BaseModel):
    title: str
    description: str | None = None

class MovieResponse(MovieCreate):
    id: int

    class Config:
        from_attributes = True
