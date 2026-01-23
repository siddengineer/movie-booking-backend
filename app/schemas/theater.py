# from pydantic import BaseModel

# class TheaterCreate(BaseModel):
#     name: str
#     city: str
#     address: str | None = None

# class TheaterResponse(TheaterCreate):
#     id: int

#     class Config:
#         orm_mode = True
from pydantic import BaseModel

# Request model for creating a theater
class TheaterCreate(BaseModel):
    name: str
    location: str

# Response model
class TheaterResponse(TheaterCreate):
    id: int

    class Config:
        from_attributes = True  # replaces orm_mode in Pydantic v2
