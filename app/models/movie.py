# from sqlalchemy import Column, Integer, String, Date
# from app.core.database import Base

# class Movie(Base):
#     __tablename__ = "movies"

#     id = Column(Integer, primary_key=True, index=True)
#     title = Column(String, nullable=False)
#     description = Column(String)
#     language = Column(String)
#     duration = Column(Integer)  # minutes
#     release_date = Column(Date)
from sqlalchemy import Column, Integer, String, Date
from app.core.database import Base

class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(String(500))
    language = Column(String(50))
    duration = Column(Integer)
    release_date = Column(Date)
