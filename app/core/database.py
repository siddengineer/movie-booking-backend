# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker, declarative_base
# import os
# from dotenv import load_dotenv

# load_dotenv()  # <--- load .env file

# DATABASE_URL = os.getenv("DATABASE_URL")
# if DATABASE_URL is None:
#     raise ValueError("DATABASE_URL is not set in .env")

# engine = create_engine(DATABASE_URL)
# SessionLocal = sessionmaker(bind=engine)
# Base = declarative_base()
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy import create_engine
# from sqlalchemy.orm import Session

# SQLALCHEMY_DATABASE_URL = "mysql+pymysql://username:1234@localhost/movie_booking"  # your DB URL

# engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_pre_ping=True)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# # ✅ Add this function
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Your MySQL connection string
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://username:1234@localhost/movie_booking"

# Engine
engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_pre_ping=True)

# Session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# ✅ Declarative base (needed for models)
Base = declarative_base()

# ✅ Dependency to use in routers
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
