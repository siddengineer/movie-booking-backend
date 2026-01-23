# from sqlalchemy import Column, Integer, String
# from app.core.database import Base

# class Theater(Base):
#     __tablename__ = "theaters"

#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, nullable=False)
#     city = Column(String, nullable=False)
#     address = Column(String)
from sqlalchemy import Column, Integer, String
from app.core.database import Base
from sqlalchemy.orm import relationship
class Theater(Base):
    __tablename__ = "theaters"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    city = Column(String(100), nullable=False)
    address = Column(String(500))
    screens = relationship("Screen", back_populates="theater")
