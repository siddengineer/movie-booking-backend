# from sqlalchemy import Column, Integer, ForeignKey, String, DateTime
# from sqlalchemy.orm import relationship
# from datetime import datetime
# from app.core.database import Base

# class Booking(Base):
#     __tablename__ = "bookings"

#     id = Column(Integer, primary_key=True, index=True)
#     user_id = Column(Integer, ForeignKey("users.id"))
#     show_id = Column(Integer, ForeignKey("shows.id"))
#     seats_booked = Column(Integer)
#     total_price = Column(Integer)
#     status = Column(String, default="pending")  # pending / confirmed / canceled
#     created_at = Column(DateTime, default=datetime.utcnow)

#     user = relationship("User", back_populates="bookings")
#     show = relationship("Show", back_populates="bookings")
# from sqlalchemy import Column, Integer, ForeignKey
# from sqlalchemy.orm import relationship
# from app.core.database import Base

# class Booking(Base):
#     __tablename__ = "bookings"

#     id = Column(Integer, primary_key=True, index=True)
#     show_id = Column(Integer, ForeignKey("shows.id"), nullable=False)
#     user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
#     seats_booked = Column(Integer, nullable=False)

#     show = relationship("Show", back_populates="bookings")
#     user = relationship("User", back_populates="bookings")
# from sqlalchemy import Column, Integer, ForeignKey
# from sqlalchemy.orm import relationship
# from app.core.database import Base

# class Booking(Base):
#     __tablename__ = "bookings"

#     id = Column(Integer, primary_key=True, index=True)
#     user_id = Column(Integer, ForeignKey("users.id"))
#     show_id = Column(Integer, ForeignKey("shows.id"))
#     seats_booked = Column(Integer, nullable=False)

#     user = relationship("User", back_populates="bookings")
#     show = relationship("Show", back_populates="bookings")
from sqlalchemy import Column, Integer, ForeignKey,Float,String
from sqlalchemy.orm import relationship
from app.core.database import Base

# class Booking(Base):
#     __tablename__ = "bookings"

#     id = Column(Integer, primary_key=True, index=True)
#     user_id = Column(Integer, ForeignKey("users.id"))
#     show_id = Column(Integer, ForeignKey("shows.id"))
#     row = Column(Integer, nullable=False)
#     seat_number = Column(Integer, nullable=False)
#     paid = Column(Boolean, default=False)

#     user = relationship("User", back_populates="bookings")
#     show = relationship("Show", back_populates="bookings")
class Booking(Base):
    __tablename__ = "bookings"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    show_id = Column(Integer, ForeignKey("shows.id"))
    seats_booked = Column(Integer, nullable=False)
    total_price = Column(Float, nullable=False)
    status = Column(String(50), default="pending")  # pending / confirmed / canceled
