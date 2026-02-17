# from fastapi import APIRouter, Depends, HTTPException
# from sqlalchemy.orm import Session
# from app.core.database import SessionLocal
# from app.models.booking import Booking
# from app.models.show import Show
# from app.schemas.booking import BookingCreate, BookingResponse
# from app.auth.dependencies import get_current_user
# from app.models.user import User

# router = APIRouter(prefix="/bookings", tags=["Bookings"])

# # Dependency
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# @router.post("/", response_model=BookingResponse)
# def create_booking(
#     booking: BookingCreate,
#     db: Session = Depends(get_db),
#     current_user: User = Depends(get_current_user)
# ):
#     show = db.query(Show).filter(Show.id == booking.show_id).first()
#     if not show:
#         raise HTTPException(status_code=404, detail="Show not found")

#     if booking.seats_booked > show.available_seats:
#         raise HTTPException(status_code=400, detail="Not enough seats available")

#     total_price = booking.seats_booked * show.price_per_seat  # assuming show has price_per_seat

#     new_booking = Booking(
#         user_id=current_user.id,
#         show_id=show.id,
#         seats_booked=booking.seats_booked,
#         total_price=total_price,
#         status="confirmed"  # mark confirmed after “payment”
#     )
#     show.available_seats -= booking.seats_booked
#     db.add(new_booking)
#     db.commit()
#     db.refresh(new_booking)
#     return new_booking

# @router.get("/", response_model=list[BookingResponse])
# def get_user_bookings(
#     db: Session = Depends(get_db),
#     current_user: User = Depends(get_current_user)
# ):
#     return db.query(Booking).filter(Booking.user_id == current_user.id).all()

# @router.get("/{booking_id}", response_model=BookingResponse)
# def get_booking(
#     booking_id: int,
#     db: Session = Depends(get_db),
#     current_user: User = Depends(get_current_user)
# ):
#     booking = db.query(Booking).filter(Booking.id == booking_id, Booking.user_id == current_user.id).first()
#     if not booking:
#         raise HTTPException(status_code=404, detail="Booking not found")
#     return booking
# from fastapi import APIRouter, Depends, HTTPException
# from sqlalchemy.orm import Session
# from sqlalchemy.exc import SQLAlchemyError
# from app.core.database import SessionLocal
# from app.models.booking import Booking
# from app.models.show import Show
# from app.schemas.booking import BookingCreate, BookingResponse
# from app.auth.dependencies import get_current_user
# from app.models.user import User

# router = APIRouter(prefix="/bookings", tags=["Bookings"])

# # Dependency
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# # Helper function to check double booking
# def seats_available(show: Show, seats: list[int]):
#     booked_seats = []
#     for booking in show.bookings:
#         booked_seats.extend(booking.seat_numbers)
#     return all(seat not in booked_seats for seat in seats)

# @router.post("/", response_model=BookingResponse)
# def create_booking(
#     booking: BookingCreate,
#     db: Session = Depends(get_db),
#     current_user: User = Depends(get_current_user)
# ):
#     show = db.query(Show).filter(Show.id == booking.show_id).first()
#     if not show:
#         raise HTTPException(status_code=404, detail="Show not found")

#     # Prevent double booking of seats
#     if not seats_available(show, booking.seat_numbers):
#         raise HTTPException(status_code=400, detail="Some seats are already booked")

#     if len(booking.seat_numbers) > show.available_seats:
#         raise HTTPException(status_code=400, detail="Not enough seats available")

#     total_price = len(booking.seat_numbers) * show.price_per_seat

#     new_booking = Booking(
#         user_id=current_user.id,
#         show_id=show.id,
#         seat_numbers=booking.seat_numbers,
#         seats_booked=len(booking.seat_numbers),
#         total_price=total_price,
#         payment_status=booking.payment_status or "pending",  # "pending" or "paid"
#         status="confirmed" if booking.payment_status == "paid" else "reserved"
#     )

#     show.available_seats -= len(booking.seat_numbers)

#     try:
#         db.add(new_booking)
#         db.commit()
#         db.refresh(new_booking)
#     except SQLAlchemyError as e:
#         db.rollback()
#         raise HTTPException(status_code=500, detail="Failed to create booking")

#     return new_booking

# @router.get("/", response_model=list[BookingResponse])
# def get_user_bookings(
#     db: Session = Depends(get_db),
#     current_user: User = Depends(get_current_user)
# ):
#     return db.query(Booking).filter(Booking.user_id == current_user.id).all()

# @router.get("/{booking_id}", response_model=BookingResponse)
# def get_booking(
#     booking_id: int,
#     db: Session = Depends(get_db),
#     current_user: User = Depends(get_current_user)
# ):
#     booking = db.query(Booking).filter(
#         Booking.id == booking_id,
#         Booking.user_id == current_user.id
#     ).first()
#     if not booking:
#         raise HTTPException(status_code=404, detail="Booking not found")
#     return booking

# @router.get("/show/{show_id}", response_model=list[BookingResponse])
# def get_show_bookings(
#     show_id: int,
#     db: Session = Depends(get_db),
#     current_user: User = Depends(get_current_user)
# ):
#     show = db.query(Show).filter(Show.id == show_id).first()
#     if not show:
#         raise HTTPException(status_code=404, detail="Show not found")
#     return show.bookings
# from fastapi import APIRouter, Depends, HTTPException
# from sqlalchemy.orm import Session
# from app.core.database import SessionLocal
# from app.models.booking import Booking
# from app.models.show import Show
# from app.schemas.booking import BookingCreate, BookingResponse
# from app.auth.dependencies import get_current_user
# from app.models.user import User

# router = APIRouter(prefix="/bookings", tags=["Bookings"])

# # Dependency
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# # -----------------------------
# # Create Booking
# # -----------------------------
# @router.post("/", response_model=BookingResponse)
# def create_booking(
#     booking: BookingCreate,
#     db: Session = Depends(get_db),
#     current_user: User = Depends(get_current_user)
# ):
#     show = db.query(Show).filter(Show.id == booking.show_id).first()
#     if not show:
#         raise HTTPException(status_code=404, detail="Show not found")

#     # Prevent double booking
#     existing_seats = []
#     for b in db.query(Booking).filter(Booking.show_id == show.id).all():
#         existing_seats.extend(b.seat_numbers or [])

#     for seat in booking.seat_numbers:
#         if seat in existing_seats:
#             raise HTTPException(
#                 status_code=400,
#                 detail=f"Seat {seat} is already booked"
#             )

#     if len(booking.seat_numbers) > show.available_seats:
#         raise HTTPException(status_code=400, detail="Not enough seats available")

#     total_price = len(booking.seat_numbers) * show.price_per_seat  # assuming price_per_seat exists

#     new_booking = Booking(
#         user_id=current_user.id,
#         show_id=show.id,
#         seats_booked=len(booking.seat_numbers),
#         seat_numbers=booking.seat_numbers,  # track per-seat
#         total_price=total_price,
#         status="confirmed",
#         payment_status="pending"  # default pending
#     )

#     show.available_seats -= len(booking.seat_numbers)

#     db.add(new_booking)
#     db.commit()
#     db.refresh(new_booking)

#     # Simulate payment (can be replaced with real payment logic)
#     new_booking.payment_status = "paid"
#     db.commit()
#     db.refresh(new_booking)

#     return new_booking

# # -----------------------------
# # Get current user's bookings
# # -----------------------------
# @router.get("/", response_model=list[BookingResponse])
# def get_user_bookings(
#     db: Session = Depends(get_db),
#     current_user: User = Depends(get_current_user)
# ):
#     return db.query(Booking).filter(Booking.user_id == current_user.id).all()

# # -----------------------------
# # Get booking by ID
# # -----------------------------
# @router.get("/{booking_id}", response_model=BookingResponse)
# def get_booking(
#     booking_id: int,
#     db: Session = Depends(get_db),
#     current_user: User = Depends(get_current_user)
# ):
#     booking = db.query(Booking).filter(
#         Booking.id == booking_id,
#         Booking.user_id == current_user.id
#     ).first()
#     if not booking:
#         raise HTTPException(status_code=404, detail="Booking not found")
#     return booking

# # -----------------------------
# # Get all booked seats for a show
# # -----------------------------
# @router.get("/show/{show_id}", response_model=list[str])
# def get_booked_seats(show_id: int, db: Session = Depends(get_db)):
#     booked_seats = []
#     for b in db.query(Booking).filter(Booking.show_id == show_id).all():
#         booked_seats.extend(b.seat_numbers or [])
#     return booked_seats

# # -----------------------------
# # Cancel a booking
# # -----------------------------
# @router.delete("/{booking_id}", response_model=dict)
# def cancel_booking(
#     booking_id: int,
#     db: Session = Depends(get_db),
#     current_user: User = Depends(get_current_user)
# ):
#     booking = db.query(Booking).filter(
#         Booking.id == booking_id,
#         Booking.user_id == current_user.id
#     ).first()
#     if not booking:
#         raise HTTPException(status_code=404, detail="Booking not found")

#     # Release seats
#     show = db.query(Show).filter(Show.id == booking.show_id).first()
#     show.available_seats += booking.seats_booked

#     db.delete(booking)
#     db.commit()
#     return {"detail": "Booking cancelled successfully"}
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import relationship
from app.core.database import Base
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.core.redis_client import redis_client
from app.models.booking import Booking
from app.models.show import Show
from app.models.user import User
from app.schemas.booking import BookingCreate, BookingResponse
from app.auth.dependencies import get_current_user
import time

router = APIRouter(prefix="/bookings", tags=["Bookings"])

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_available_seats(show_id: int, db: Session):
    """Fetch available seats, using Redis cache."""
    available_seats = redis_client.get(f"show:{show_id}:available_seats")
    if available_seats is None:
        show = db.query(Show).filter(Show.id == show_id).first()
        if not show:
            raise HTTPException(status_code=404, detail="Show not found")
        available_seats = show.available_seats
        redis_client.set(f"show:{show_id}:available_seats", available_seats)
    return int(available_seats)


def lock_seats(show_id: int, seats: int, timeout: int = 5):
    """Try to lock seats using Redis to avoid double booking."""
    lock_key = f"show:{show_id}:lock"
    # Use SETNX to lock
    locked = redis_client.set(lock_key, "locked", nx=True, ex=timeout)
    if not locked:
        raise HTTPException(status_code=409, detail="Another booking in progress. Try again.")
    return lock_key


def unlock_seats(lock_key: str):
    """Release Redis lock."""
    redis_client.delete(lock_key)


@router.post("/", response_model=BookingResponse)
def create_booking(
    booking: BookingCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    # Check available seats using Redis
    available_seats = get_available_seats(booking.show_id, db)
    if booking.seats_booked > available_seats:
        raise HTTPException(status_code=400, detail="Not enough seats available")

    # Lock seats to prevent double booking
    lock_key = lock_seats(booking.show_id, booking.seats_booked)

    try:
        show = db.query(Show).filter(Show.id == booking.show_id).first()
        if booking.seats_booked > show.available_seats:
            raise HTTPException(status_code=400, detail="Not enough seats available")

        total_price = booking.seats_booked * show.price_per_seat

        new_booking = Booking(
            user_id=current_user.id,
            show_id=show.id,
            seats_booked=booking.seats_booked,
            seat_row=booking.seat_row,
            seat_number=booking.seat_number,
            total_price=total_price,
            status="pending"  # you can update to "confirmed" after payment
        )

        # Deduct seats
        show.available_seats -= booking.seats_booked
        db.add(new_booking)
        db.commit()
        db.refresh(new_booking)

        # Update Redis cache
        redis_client.set(f"show:{show.id}:available_seats", show.available_seats)

        # Simulate payment success
        new_booking.status = "confirmed"
        db.commit()
        db.refresh(new_booking)

        return new_booking
    finally:
        unlock_seats(lock_key)


@router.get("/", response_model=list[BookingResponse])
def get_user_bookings(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return db.query(Booking).filter(Booking.user_id == current_user.id).all()


@router.get("/{booking_id}", response_model=BookingResponse)
def get_booking(
    booking_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    booking = db.query(Booking).filter(
        Booking.id == booking_id, Booking.user_id == current_user.id
    ).first()
    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")
    return booking


@router.get("/show/{show_id}/seats")
def get_booked_seats(show_id: int, db: Session = Depends(get_db)):
    """Optional: fetch booked seats for a show"""
    bookings = db.query(Booking).filter(Booking.show_id == show_id).all()
    booked = sum(b.seats_booked for b in bookings)
    show = db.query(Show).filter(Show.id == show_id).first()
    if not show:
        raise HTTPException(status_code=404, detail="Show not found")
    return {"total_seats": show.total_seats, "available_seats": show.available_seats, "booked_seats": booked}


@router.delete("/{booking_id}")
def cancel_booking(
    booking_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Optional: cancel a booking"""
    booking = db.query(Booking).filter(
        Booking.id == booking_id, Booking.user_id == current_user.id
    ).first()
    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")

    # Restore seats
    show = db.query(Show).filter(Show.id == booking.show_id).first()
    show.available_seats += booking.seats_booked
    redis_client.set(f"show:{show.id}:available_seats", show.available_seats)

    db.delete(booking)
    db.commit()
    return {"detail": "Booking canceled successfully"}
