from sqlalchemy import Column, Integer, ForeignKey, Float, String, DateTime, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime
from app.core.database import Base


class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    show_id = Column(Integer, ForeignKey("shows.id"), nullable=False)

    seats_booked = Column(Integer, nullable=False)

    seat_row = Column(Integer, nullable=False)

    seat_number = Column(Integer, nullable=False)

    total_price = Column(Float, nullable=False)

    status = Column(String(50), default="confirmed")

    created_at = Column(DateTime, default=datetime.utcnow)   # MUST be inside class

    paid = Column(Boolean, default=False)                     # MUST be inside class

    show = relationship("Show", back_populates="bookings")

    user = relationship("User", back_populates="bookings")