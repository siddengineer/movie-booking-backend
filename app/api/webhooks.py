# from fastapi import APIRouter, Request, HTTPException
# import hmac
# import hashlib
# import os

# router = APIRouter(prefix="/webhooks", tags=["Webhooks"])

# WEBHOOK_SECRET = os.getenv("RAZORPAY_WEBHOOK_SECRET")


# @router.post("/razorpay")
# async def razorpay_webhook(request: Request):

#     body = await request.body()
#     signature = request.headers.get("X-Razorpay-Signature")

#     expected = hmac.new(
#         WEBHOOK_SECRET.encode(),
#         body,
#         hashlib.sha256
#     ).hexdigest()

#     if not hmac.compare_digest(expected, signature):
#         raise HTTPException(status_code=400, detail="Invalid signature")

#     # update booking to confirmed
#     print("Payment success webhook received")

#     return {"status": "ok"}





from fastapi import APIRouter, Request, HTTPException
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.models.booking import Booking
import hmac
import hashlib
import os
import json

router = APIRouter(prefix="/webhooks", tags=["Webhooks"])

WEBHOOK_SECRET = os.getenv("RAZORPAY_WEBHOOK_SECRET")


@router.post("/razorpay")
async def razorpay_webhook(request: Request):

    body = await request.body()
    signature = request.headers.get("X-Razorpay-Signature")

    if not signature:
        raise HTTPException(status_code=400, detail="Missing signature")

    # Verify signature
    expected = hmac.new(
        WEBHOOK_SECRET.encode(),
        body,
        hashlib.sha256
    ).hexdigest()

    if not hmac.compare_digest(expected, signature):
        raise HTTPException(status_code=400, detail="Invalid signature")

    # Parse JSON body
    payload = json.loads(body)

    event = payload.get("event")

    # Only handle successful payment
    if event == "payment.captured":

        payment_entity = payload["payload"]["payment"]["entity"]

        order_id = payment_entity.get("order_id")

        # receipt format was: booking_12
        receipt = payment_entity.get("notes", {}).get("receipt")

        # Fallback: sometimes receipt is in order entity
        if not receipt:
            receipt = payload["payload"].get("order", {}).get("entity", {}).get("receipt")

        if receipt and receipt.startswith("booking_"):
            booking_id = int(receipt.split("_")[1])

            db: Session = SessionLocal()

            try:
                booking = db.query(Booking).filter(
                    Booking.id == booking_id
                ).first()

                if booking and not booking.paid:
                    booking.paid = True
                    booking.status = "confirmed"
                    db.commit()

                print(f"Booking {booking_id} confirmed via webhook")

            finally:
                db.close()

    return {"status": "ok"}