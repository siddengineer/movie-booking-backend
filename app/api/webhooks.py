from fastapi import APIRouter, Request, HTTPException
import hmac
import hashlib
import os

router = APIRouter(prefix="/webhooks", tags=["Webhooks"])

WEBHOOK_SECRET = os.getenv("RAZORPAY_WEBHOOK_SECRET")


@router.post("/razorpay")
async def razorpay_webhook(request: Request):

    body = await request.body()
    signature = request.headers.get("X-Razorpay-Signature")

    expected = hmac.new(
        WEBHOOK_SECRET.encode(),
        body,
        hashlib.sha256
    ).hexdigest()

    if not hmac.compare_digest(expected, signature):
        raise HTTPException(status_code=400, detail="Invalid signature")

    # update booking to confirmed
    print("Payment success webhook received")

    return {"status": "ok"}