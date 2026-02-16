# from fastapi import APIRouter, Depends, HTTPException
# from sqlalchemy.orm import Session
# from fastapi.security import OAuth2PasswordRequestForm

# from app.core.database import get_db
# from app.models.user import User
# from app.auth.utils import verify_password, create_access_token, get_password_hash
# from app.auth.dependencies import oauth2_scheme

# router = APIRouter(prefix="/auth", tags=["Authentication"])

# @router.post("/login")
# def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
#     user = db.query(User).filter(User.username == form_data.username).first()
#     if not user or not verify_password(form_data.password, user.password):
#         raise HTTPException(status_code=401, detail="Invalid credentials")
#     token = create_access_token({"user_id": user.id, "is_admin": getattr(user, "is_admin", 0)})
#     return {"access_token": token, "token_type": "bearer"}

# @router.post("/register")
# def register_user(username: str, email: str, password: str, db: Session = Depends(get_db)):
#     db_user = db.query(User).filter(User.email == email).first()
#     if db_user:
#         raise HTTPException(status_code=400, detail="Email already registered")
#     hashed_password = get_password_hash(password)
#     new_user = User(username=username, email=email, password=hashed_password)
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return {"username": new_user.username, "email": new_user.email}
# from fastapi import APIRouter, Depends, HTTPException
# from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
# from datetime import datetime, timedelta
# import jwt
# from app.core.database import get_db
# from sqlalchemy.orm import Session
# from app.models.user import User

# SECRET_KEY = "YOUR_SECRET_KEY"
# ALGORITHM = "HS256"

# router = APIRouter(prefix="/auth", tags=["Auth"])
# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

# def authenticate_user(db: Session, username: str, password: str):
#     user = db.query(User).filter(User.username == username).first()
#     if user and user.password == password:  # you can hash later
#         return user
#     return False

# @router.post("/login")
# def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
#     user = authenticate_user(db, form_data.username, form_data.password)
#     if not user:
#         raise HTTPException(status_code=401, detail="Incorrect username or password")
#     token_data = {"sub": user.username, "exp": datetime.utcnow() + timedelta(hours=1)}
#     token = jwt.encode(token_data, SECRET_KEY, algorithm=ALGORITHM)
#     return {"access_token": token, "token_type": "bearer"}

# from fastapi import APIRouter, Depends, HTTPException
# from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
# from sqlalchemy.orm import Session
# from datetime import datetime, timedelta
# from pydantic import BaseModel, EmailStr
# from passlib.context import CryptContext
# import jwt

# from app.core.database import get_db
# from app.models.user import User

# # JWT settings
# SECRET_KEY = "mysecretkey"
# ALGORITHM = "HS256"

# router = APIRouter(prefix="/auth", tags=["Auth"])

# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# # Password hash functions
# def hash_password(password: str):
#     return pwd_context.hash(password)

# def verify_password(plain_password, hashed_password):
#     return pwd_context.verify(plain_password, hashed_password)


# # Schema for register
# class UserCreate(BaseModel):
#     name: str
#     email: EmailStr
#     password: str


# # REGISTER route
# @router.post("/register")
# def register(user: UserCreate, db: Session = Depends(get_db)):

#     existing_user = db.query(User).filter(User.email == user.email).first()

#     if existing_user:
#         raise HTTPException(status_code=400, detail="Email already exists")

#     new_user = User(
#         name=user.name,
#         email=user.email,
#         password=hash_password(user.password),
#         is_admin=False
#     )

#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)

#     return {"message": "User registered successfully"}


# # LOGIN route
# @router.post("/login")
# def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):

#     user = db.query(User).filter(User.email == form_data.username).first()

#     if not user or not verify_password(form_data.password, user.password):
#         raise HTTPException(status_code=401, detail="Invalid email or password")

#     token_data = {
#         "sub": str(user.id),
#         "exp": datetime.utcnow() + timedelta(hours=10)
#     }

#     token = jwt.encode(token_data, SECRET_KEY, algorithm=ALGORITHM)

#     return {
#         "access_token": token,
#         "token_type": "bearer"
#     }
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from pydantic import BaseModel, EmailStr
from passlib.context import CryptContext
import jwt

from app.core.database import get_db
from app.models.user import User

# JWT settings
SECRET_KEY = "mysecretkey"
ALGORITHM = "HS256"

router = APIRouter(prefix="/auth", tags=["Auth"])

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# Password hash functions
def hash_password(password: str):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


# Register schema
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str


# REGISTER route
@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):

    # check if email exists
    existing_email = db.query(User).filter(User.email == user.email).first()
    if existing_email:
        raise HTTPException(status_code=400, detail="Email already exists")

    # check if username exists
    existing_username = db.query(User).filter(User.username == user.username).first()
    if existing_username:
        raise HTTPException(status_code=400, detail="Username already exists")

    # create new user
    new_user = User(
        username=user.username,
        email=user.email,
        password=hash_password(user.password),
        is_admin=False
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "message": "User registered successfully",
        "user_id": new_user.id
    }


# LOGIN route
@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):

    # login using email
    user = db.query(User).filter(User.email == form_data.username).first()

    if not user:
        raise HTTPException(status_code=401, detail="Invalid email or password")

    if not verify_password(form_data.password, user.password):
        raise HTTPException(status_code=401, detail="Invalid email or password")

    # create token
    token_data = {
        "sub": str(user.id),
        "exp": datetime.utcnow() + timedelta(hours=10)
    }

    token = jwt.encode(token_data, SECRET_KEY, algorithm=ALGORITHM)

    return {
        "access_token": token,
        "token_type": "bearer"
    }