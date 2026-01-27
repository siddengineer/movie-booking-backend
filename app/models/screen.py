# from sqlalchemy import Column, Integer, String, ForeignKey
# from sqlalchemy.orm import relationship
# from app.core.database import Base

# class Screen(Base):
#     __tablename__ = "screens"

#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, nullable=False)
#     theater_id = Column(Integer, ForeignKey("theaters.id"))
#     capacity = Column(Integer, nullable=False)

#     theater = relationship("Theater", back_populates="screens")
#     shows = relationship("Show", back_populates="screen")
# from sqlalchemy import Column, Integer, String, ForeignKey
# from sqlalchemy.orm import relationship
# from app.core.database import Base

# class Screen(Base):
#     __tablename__ = "screens"

#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String(255), nullable=False)  # added length
#     theater_id = Column(Integer, ForeignKey("theaters.id"))
#     capacity = Column(Integer, nullable=False)

#     theater = relationship("Theater", back_populates="screens")
#     shows = relationship("Show", back_populates="screen")
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base

class Screen(Base):
    __tablename__ = "screens"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    theater_id = Column(Integer, ForeignKey("theaters.id"))
    capacity = Column(Integer, nullable=False)

    theater = relationship("Theater", back_populates="screens")
    shows = relationship("Show", back_populates="screen")  # ✅ This matches Show.screen
