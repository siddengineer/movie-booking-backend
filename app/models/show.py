# from sqlalchemy import Column, Integer, ForeignKey, DateTime, Float
# from sqlalchemy.orm import relationship
# from app.core.database import Base

# class Show(Base):
#     __tablename__ = "shows"

#     id = Column(Integer, primary_key=True, index=True)
#     movie_id = Column(Integer, ForeignKey("movies.id"), nullable=False)
#     screen_id = Column(Integer, ForeignKey("screens.id"), nullable=False)
#     start_time = Column(DateTime, nullable=False)
#     end_time = Column(DateTime, nullable=False)
#     price = Column(Float, nullable=False)

#     movie = relationship("Movie", back_populates="shows")
#     screen = relationship("Screen", back_populates="shows")
from sqlalchemy import Column, Integer, ForeignKey, DateTime, Float
from sqlalchemy.orm import relationship
from app.core.database import Base

class Show(Base):
    __tablename__ = "shows"

    id = Column(Integer, primary_key=True, index=True)
    movie_id = Column(Integer, ForeignKey("movies.id"), nullable=False)
    screen_id = Column(Integer, ForeignKey("screens.id"), nullable=False)
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=False)
    price = Column(Float, nullable=False)

    movie = relationship("Movie", back_populates="shows")
    screen = relationship("Screen", back_populates="shows")
