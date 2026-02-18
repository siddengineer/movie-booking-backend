# import razorpay
# import os
# from dotenv import load_dotenv

# load_dotenv()

# client = razorpay.Client(
#     auth=(
#         os.getenv("rzp_test_SHTEhFzarLWakV"),
#         os.getenv("rV6eQgmB7Ui7x3p71aINGsoC")
#     )
# )

# def create_payment_order(amount, booking_id):

#     order = client.order.create({
#         "amount": int(amount * 100),
#         "currency": "INR",
#         "receipt": f"booking_{booking_id}",
#         "payment_capture": 1
#     })

#     return order
# import razorpay
# import os
# from dotenv import load_dotenv

# load_dotenv()

# RAZORPAY_KEY_ID = os.getenv("rzp_test_SHTEhFzarLWakV")
# RAZORPAY_KEY_SECRET = os.getenv("rV6eQgmB7Ui7x3p71aINGsoC")

# client = razorpay.Client(auth=(RAZORPAY_KEY_ID, RAZORPAY_KEY_SECRET))


# def create_order(amount: float, currency: str = "INR"):
#     """
#     Create Razorpay order
#     amount in rupees → convert to paise
#     """
#     order = client.order.create({
#         "amount": int(amount * 100),  # paise
#         "currency": currency,
#         "payment_capture": 1
#     })

#     return order


# def verify_payment(razorpay_order_id, razorpay_payment_id, razorpay_signature):
#     """
#     Verify payment signature
#     """
#     try:
#         client.utility.verify_payment_signature({
#             "razorpay_order_id": razorpay_order_id,
#             "razorpay_payment_id": razorpay_payment_id,
#             "razorpay_signature": razorpay_signature
#         })
#         return True
#     except:
#         return False



import razorpay
import os
from dotenv import load_dotenv

load_dotenv()

RAZORPAY_KEY_ID = os.getenv("RAZORPAY_KEY_ID")
RAZORPAY_SECRET = os.getenv("RAZORPAY_SECRET")

client = razorpay.Client(auth=(RAZORPAY_KEY_ID, RAZORPAY_SECRET))


# CREATE ORDER
def create_order(amount: int, receipt: str):
    """
    amount in paise
    receipt = booking id
    """

    order = client.order.create({
        "amount": amount,
        "currency": "INR",
        "receipt": receipt,
        "payment_capture": 1
    })

    return order


# VERIFY PAYMENT
def verify_payment(razorpay_order_id, razorpay_payment_id, razorpay_signature):

    try:
        client.utility.verify_payment_signature({
            "razorpay_order_id": razorpay_order_id,
            "razorpay_payment_id": razorpay_payment_id,
            "razorpay_signature": razorpay_signature
        })
        return True

    except:
        return False