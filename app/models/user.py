# from sqlalchemy import Column, Integer, String
# from app.core.database import Base

# class User(Base):
#     __tablename__ = "users"

#     id = Column(Integer, primary_key=True, index=True)
#     username = Column(String(50), unique=True, nullable=False)
#     email = Column(String(100), unique=True, nullable=False)
#     password = Column(String(255), nullable=False)
#     bookings = relationship("Booking", back_populates="user")
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship  # ✅ import relationship
from app.core.database import Base
from app.models.booking import Booking  # ✅ import Booking model

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(255), nullable=False)

    bookings = relationship("Booking", back_populates="user")  # links to Booking.user
