# from fastapi import FastAPI
# from app.api.auth import router as auth_router

# app = FastAPI(title="Movie Booking Backend")

# @app.get("/")
# def home():
#     return {"message": "Movie Booking Backend is running"}

# app.include_router(auth_router)
# from fastapi import FastAPI
# from app.api import auth

# app = FastAPI(title="Movie Booking Backend")

# app.include_router(auth.router)

# @app.get("/")
# def home():
#     return {"message": "Movie Booking Backend is running"}
# from fastapi import FastAPI
# from app.api import admin, public
# from app.api import screen, shows
# from app.api import booking
# from app.auth.routes import router as auth_router
# from app.admin.routes import router as admin_router
# from app.api.admin import router as admin_router


# app = FastAPI(title="Movie Booking Backend")

# # app.include_router(admin.router)
# # app.include_router(public.router)
# # app.include_router(screen.router)
# # app.include_router(shows.router)
# app.include_router(admin.router, prefix="/admin")
# app.include_router(public.router)
# app.include_router(auth_router)
# app.include_router(screen.router, prefix="/screen")
# app.include_router(shows.router, prefix="/show")
# app.include_router(booking.router)
# app.include_router(admin_router)
# @app.get("/")
# def health():
#     return {"status": "running"}

# from fastapi import FastAPI
# from app.api import admin, public, screen, shows, booking
# from app.auth.routes import router as auth_router

# app = FastAPI(title="Movie Booking Backend")

# # Include routers
# app.include_router(admin.router, prefix="/admin")   # admin routes
# app.include_router(public.router)                  # public routes
# app.include_router(auth_router)                    # auth routes
# app.include_router(screen.router, prefix="/screen") # screen routes
# app.include_router(shows.router)                   # shows router, already has /shows prefix
# app.include_router(booking.router)                 # booking routes

# @app.get("/")
# def health():
#     return {"status": "running"}


# from fastapi import FastAPI
# from app.api import admin, public, screen, shows, booking
# from app.auth.routes import router as auth_router

# # ✅ IMPORT ALL MODELS (VERY IMPORTANT)
# from app.models.user import User
# from app.models.movie import Movie
# from app.models.theater import Theater
# from app.models.screen import Screen
# from app.models.show import Show
# from app.models.booking import Booking

# app = FastAPI(title="Movie Booking Backend")

# # Include routers
# app.include_router(admin.router, prefix="/admin")
# app.include_router(public.router)
# app.include_router(auth_router)
# app.include_router(screen.router, prefix="/screen")
# app.include_router(shows.router)
# app.include_router(booking.router)

# @app.get("/")
# def health():
#     return {"status": "running"}

# from fastapi import Depends, HTTPException
# from sqlalchemy.orm import Session
# from app.core.database import get_db
# from app.models.user import User
# from pydantic import BaseModel, EmailStr
# from passlib.context import CryptContext

# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# # Schema
# class UserCreate(BaseModel):
#     name: str
#     email: EmailStr
#     password: str


# def hash_password(password: str):
#     return pwd_context.hash(password)


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

#     return {
#         "message": "User registered successfully",
#         "user_id": new_user.id
#     }
# from fastapi import FastAPI
# from app.api import admin, public, screen, shows, booking
# from app.auth.routes import router as auth_router

# from app.models.user import User
# from app.models.movie import Movie
# from app.models.theater import Theater
# from app.models.screen import Screen
# from app.models.show import Show
# from app.models.booking import Booking

# app = FastAPI(title="Movie Booking Backend")

# app.include_router(admin.router, prefix="/admin")
# app.include_router(public.router)
# app.include_router(auth_router)
# app.include_router(screen.router, prefix="/screen")
# app.include_router(shows.router)
# app.include_router(booking.router)

# @app.get("/")
# def health():
#     return {"status": "running"}



# from fastapi import FastAPI, Request
# from fastapi.responses import HTMLResponse
# from fastapi.templating import Jinja2Templates

# from app.api import admin, public, screen, shows, booking
# from app.auth.routes import router as auth_router

# from app.models.user import User
# from app.models.movie import Movie
# from app.models.theater import Theater
# from app.models.screen import Screen
# from app.models.show import Show
# from app.models.booking import Booking

# app = FastAPI(title="Movie Booking Backend")

# templates = Jinja2Templates(directory="app/templates")

# app.include_router(admin.router, prefix="/admin")
# app.include_router(public.router)
# app.include_router(auth_router)
# app.include_router(screen.router, prefix="/screen")
# app.include_router(shows.router)
# app.include_router(booking.router)

# @app.get("/")
# def health():
#     return {"status": "running"}

# @app.get("/pay", response_class=HTMLResponse)
# def pay_page(request: Request):
#     return templates.TemplateResponse("payment.html", {"request": request})



# from fastapi import FastAPI, Request
# from fastapi.responses import HTMLResponse
# from fastapi.templating import Jinja2Templates

# from app.api import admin, public, screen, shows, booking
# from app.auth.routes import router as auth_router

# from app.models.user import User
# from app.models.movie import Movie
# from app.models.theater import Theater
# from app.models.screen import Screen
# from app.models.show import Show
# from app.models.booking import Booking

# app = FastAPI(title="Movie Booking Backend")

# templates = Jinja2Templates(directory="app/templates")

# app.include_router(admin.router, prefix="/admin")
# app.include_router(public.router)
# app.include_router(auth_router)
# app.include_router(screen.router, prefix="/screen")
# app.include_router(shows.router)
# app.include_router(booking.router)


# @app.get("/")
# def health():
#     return {"status": "running"}


# # FIXED PAYMENT ROUTE
# @app.get("/pay", response_class=HTMLResponse)
# def pay_page(request: Request):

#     return templates.TemplateResponse(
#         "payment.html",
#         {
#             "request": request,
#             "amount": 1,   # 1 rupee
#             "booking_id": 1,
#             "order_id": "order_test_123",
#             "razorpay_key": "rzp_test_SHTEhFzarLWakV"
#         }
#     )


from fastapi import FastAPI, Request, Depends, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
import os

from app.api import admin, public, screen, shows, booking
from app.auth.routes import router as auth_router

from app.models.user import User
from app.models.movie import Movie
from app.models.theater import Theater
from app.models.screen import Screen
from app.models.show import Show
from app.models.booking import Booking

from app.core.database import SessionLocal
from app.services.payment_service import create_order

# FastAPI app
app = FastAPI(title="Movie Booking Backend")

# Templates folder
templates = Jinja2Templates(directory="app/templates")


# Database dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Routers
app.include_router(admin.router, prefix="/admin")
app.include_router(public.router)
app.include_router(auth_router)
app.include_router(screen.router, prefix="/screen")
app.include_router(shows.router)
app.include_router(booking.router)


# Health check
@app.get("/")
def health():
    return {"status": "running"}


# REAL PAYMENT PAGE (dynamic)
@app.get("/pay/{booking_id}", response_class=HTMLResponse)
def pay_page(
    booking_id: int,
    request: Request,
    db: Session = Depends(get_db)
):

    booking = db.query(Booking).filter(
        Booking.id == booking_id
    ).first()

    if not booking:
        raise HTTPException(
            status_code=404,
            detail="Booking not found"
        )

    # Convert rupees → paisa
    amount = int(booking.total_price * 100)

    # Create Razorpay order
    order = create_order(
        amount=amount,
        receipt=f"booking_{booking.id}"
    )

    return templates.TemplateResponse(
        "payment.html",
        {
            "request": request,
            "amount": booking.total_price,
            "booking_id": booking.id,
            "razorpay_order_id": order["id"],
            "razorpay_key": os.getenv("RAZORPAY_KEY_ID"),
            "token": ""  # paste JWT token here if needed
        }
    )