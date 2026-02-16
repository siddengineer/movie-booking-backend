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
# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker

# # Your MySQL connection string
# SQLALCHEMY_DATABASE_URL = "mysql+pymysql://username:1234@localhost/movie_booking"

# # Engine
# engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_pre_ping=True)

# # Session factory
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# # ✅ Declarative base (needed for models)
# Base = declarative_base()

# # ✅ Dependency to use in routers
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()
# import os
# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker
# from dotenv import load_dotenv

# load_dotenv()  # loads .env variables

# SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")

# # Engine
# engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_pre_ping=True)

# # Session factory
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# # Declarative base
# Base = declarative_base()

# # Dependency
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL, pool_pre_ping=True)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


