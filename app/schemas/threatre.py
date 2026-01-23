from pydantic import BaseModel

class TheaterCreate(BaseModel):
    name: str
    city: str
    address: str | None = None

class TheaterResponse(TheaterCreate):
    id: int

    class Config:
        orm_mode = True
