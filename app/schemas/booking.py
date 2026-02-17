
from pydantic import BaseModel
from datetime import datetime


class BookingCreate(BaseModel):
    show_id: int
    seats_booked: int
    seat_row: int
    seat_number: int


class BookingResponse(BaseModel):
    id: int
    user_id: int
    show_id: int
    seats_booked: int
    total_price: int
    status: str
    created_at: datetime
    paid: bool

    class Config:
        from_attributes = True