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
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import datetime, timedelta
import jwt
from app.core.database import get_db
from sqlalchemy.orm import Session
from app.models.user import User

SECRET_KEY = "YOUR_SECRET_KEY"
ALGORITHM = "HS256"

router = APIRouter(prefix="/auth", tags=["Auth"])
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")  # <-- fixed

def authenticate_user(db: Session, username: str, password: str):
    user = db.query(User).filter(User.username == username).first()
    if user and user.password == password:  # simple check
        return user
    return False

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Incorrect username or password")
    token_data = {"sub": user.username, "exp": datetime.utcnow() + timedelta(hours=1)}
    token = jwt.encode(token_data, SECRET_KEY, algorithm=ALGORITHM)
    return {"access_token": token, "token_type": "bearer"}
