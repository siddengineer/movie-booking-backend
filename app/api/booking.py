from fastapi import APIRouter, Depends, HTTPException, Body
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.core.redis_client import redis_client

from app.models.booking import Booking
from app.models.show import Show
from app.models.user import User

from app.schemas.booking import BookingCreate, BookingResponse
from app.auth.dependencies import get_current_user

from app.services.payment_service import create_order, verify_payment
from app.services.email_service import send_booking_confirmation


router = APIRouter(
    prefix="/bookings",
    tags=["Bookings"]
)

# ==========================
# DATABASE DEPENDENCY
# ==========================

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ==========================
# GET AVAILABLE SEATS (REDIS CACHE)
# ==========================

def get_available_seats(show_id: int, db: Session):

    cache_key = f"show:{show_id}:available_seats"
    cached = redis_client.get(cache_key)

    if cached is not None:
        return int(cached)

    show = db.query(Show).filter(
        Show.id == show_id
    ).first()

    if not show:
        raise HTTPException(
            status_code=404,
            detail="Show not found"
        )

    redis_client.set(cache_key, show.available_seats)
    return show.available_seats


# ==========================
# REDIS LOCK (PREVENT DOUBLE BOOKING)
# ==========================

def lock_seats(show_id: int):

    lock_key = f"show:{show_id}:lock"

    locked = redis_client.set(
        lock_key,
        "locked",
        nx=True,
        ex=5
    )

    if not locked:
        raise HTTPException(
            status_code=409,
            detail="Another booking in progress"
        )

    return lock_key


def unlock_seats(lock_key: str):
    redis_client.delete(lock_key)


# ==========================
# CREATE BOOKING + CREATE PAYMENT ORDER
# ==========================

@router.post("/")
def create_booking(

    booking: BookingCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)

):

    available_seats = get_available_seats(
        booking.show_id,
        db
    )

    if booking.seats_booked > available_seats:
        raise HTTPException(
            status_code=400,
            detail="Not enough seats available"
        )

    lock_key = lock_seats(booking.show_id)

    try:

        show = db.query(Show).filter(
            Show.id == booking.show_id
        ).first()

        if not show:
            raise HTTPException(
                status_code=404,
                detail="Show not found"
            )

        total_price = booking.seats_booked * show.price_per_seat

        new_booking = Booking(
            user_id=current_user.id,
            show_id=show.id,
            seats_booked=booking.seats_booked,
            seat_row=booking.seat_row,
            seat_number=booking.seat_number,
            total_price=total_price,
            paid=False,
            status="pending"
        )

        show.available_seats -= booking.seats_booked

        db.add(new_booking)
        db.commit()
        db.refresh(new_booking)

        redis_client.set(
            f"show:{show.id}:available_seats",
            show.available_seats
        )

        razorpay_order = create_order(
            amount=int(total_price * 100),
            receipt=f"booking_{new_booking.id}"
        )

        return {
            "booking_id": new_booking.id,
            "razorpay_order_id": razorpay_order["id"],
            "amount": razorpay_order["amount"],
            "currency": razorpay_order["currency"],
            "razorpay_key": "rzp_test_SHTEhFzarLWakV",
            "paid": new_booking.paid,
            "status": new_booking.status
        }

    finally:
        unlock_seats(lock_key)


# ==========================
# VERIFY PAYMENT
# ==========================

@router.post("/verify-payment")
def verify_booking_payment(

    booking_id: int = Body(...),
    razorpay_order_id: str = Body(...),
    razorpay_payment_id: str = Body(...),
    razorpay_signature: str = Body(...),

    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)

):

    is_valid = verify_payment(
        razorpay_order_id,
        razorpay_payment_id,
        razorpay_signature
    )

    if not is_valid:
        raise HTTPException(
            status_code=400,
            detail="Payment verification failed"
        )

    booking = db.query(Booking).filter(
        Booking.id == booking_id,
        Booking.user_id == current_user.id
    ).first()

    if not booking:
        raise HTTPException(
            status_code=404,
            detail="Booking not found"
        )

    booking.paid = True
    booking.status = "confirmed"

    db.commit()
    db.refresh(booking)

    # ✅ SEND EMAIL AFTER SUCCESS
    send_booking_confirmation(
        current_user.email,
        booking.id
    )

    return {
        "message": "Payment successful",
        "booking_id": booking.id,
        "paid": booking.paid,
        "status": booking.status
    }


# ==========================
# GET USER BOOKINGS
# ==========================

@router.get("/", response_model=list[BookingResponse])
def get_user_bookings(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return db.query(Booking).filter(
        Booking.user_id == current_user.id
    ).all()


# ==========================
# GET SINGLE BOOKING
# ==========================

@router.get("/{booking_id}", response_model=BookingResponse)
def get_booking(
    booking_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    booking = db.query(Booking).filter(
        Booking.id == booking_id,
        Booking.user_id == current_user.id
    ).first()

    if not booking:
        raise HTTPException(
            status_code=404,
            detail="Booking not found"
        )

    return booking


# ==========================
# GET SEAT STATUS
# ==========================

@router.get("/show/{show_id}/seats")
def get_seat_status(
    show_id: int,
    db: Session = Depends(get_db)
):

    show = db.query(Show).filter(
        Show.id == show_id
    ).first()

    if not show:
        raise HTTPException(
            status_code=404,
            detail="Show not found"
        )

    booked = show.total_seats - show.available_seats

    return {
        "show_id": show.id,
        "total_seats": show.total_seats,
        "available_seats": show.available_seats,
        "booked_seats": booked
    }


# ==========================
# CANCEL BOOKING
# ==========================

@router.delete("/{booking_id}")
def cancel_booking(
    booking_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    booking = db.query(Booking).filter(
        Booking.id == booking_id,
        Booking.user_id == current_user.id
    ).first()

    if not booking:
        raise HTTPException(
            status_code=404,
            detail="Booking not found"
        )

    show = db.query(Show).filter(
        Show.id == booking.show_id
    ).first()

    show.available_seats += booking.seats_booked

    redis_client.set(
        f"show:{show.id}:available_seats",
        show.available_seats
    )

    db.delete(booking)
    db.commit()

    return {
        "message": "Booking cancelled successfully"
    }
    
@router.post("/verify-payment")
def verify_booking_payment(
    booking_id: int = Body(...),
    razorpay_order_id: str = Body(...),
    razorpay_payment_id: str = Body(...),
    razorpay_signature: str = Body(...),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    # This will raise error automatically if invalid
    verify_payment(
        razorpay_order_id,
        razorpay_payment_id,
        razorpay_signature
    )

    booking = db.query(Booking).filter(
        Booking.id == booking_id,
        Booking.user_id == current_user.id
    ).first()

    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")

    booking.paid = True
    booking.status = "confirmed"

    db.commit()
    db.refresh(booking)

    send_booking_confirmation(
        current_user.email,
        booking.id
    )

    return {
        "message": "Payment successful",
        "booking_id": booking.id,
        "paid": booking.paid,
        "status": booking.status
    }    