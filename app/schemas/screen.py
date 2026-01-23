from pydantic import BaseModel

class ScreenCreate(BaseModel):
    name: str
    theater_id: int
    capacity: int

class ScreenResponse(ScreenCreate):
    id: int

    class Config:
        from_attributes = True
