# import smtplib
# from email.mime.text import MIMEText

# def send_booking_email(to_email, booking_id):

#     from_email = "siddharth20online@gmail.com"
#     password = "jvgtefqukntnzmzd"

#     subject = "Booking Confirmed"
#     body = f"Your booking #{booking_id} is confirmed."

#     msg = MIMEText(body)
#     msg["Subject"] = subject
#     msg["From"] = from_email
#     msg["To"] = to_email

#     server = smtplib.SMTP("smtp.gmail.com", 587)
#     server.starttls()
#     server.login(from_email, password)

#     server.sendmail(from_email, to_email, msg.as_string())

#     server.quit()



# import smtplib
# import os
# from email.mime.text import MIMEText


# def send_booking_confirmation(to_email: str, booking_id: int):

#     from_email = "siddharth20online@gmail.com"

#     # Use Gmail App Password (16 characters)
#     password = "jvgtefqukntnzmzd"

#     subject = "Booking Confirmed 🎉"

#     body = f"""
# Hello,

# Your booking #{booking_id} is confirmed successfully.

# Enjoy your movie 🍿

# Thanks,
# Movie Booking Team
# """

#     msg = MIMEText(body)
#     msg["Subject"] = subject
#     msg["From"] = from_email
#     msg["To"] = to_email

#     try:
#         server = smtplib.SMTP("smtp.gmail.com", 587)
#         server.starttls()
#         server.login(from_email, password)
#         server.send_message(msg)
#         server.quit()

#         print("Email sent successfully ✅")

#     except Exception as e:
#         print("Email failed ❌")
#         print(e)



import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

load_dotenv()

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")


def send_booking_confirmation(to_email: str, booking_id: int):

    subject = "Booking Confirmed 🎉"

    body = f"""
    Your booking is confirmed!

    Booking ID: {booking_id}

    Thank you for using our Movie Booking System.
    """

    msg = MIMEMultipart()
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = to_email
    msg["Subject"] = subject

    msg.attach(MIMEText(body, "plain"))

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

        server.sendmail(EMAIL_ADDRESS, to_email, msg.as_string())

        server.quit()

        print("Email sent successfully ✅")

    except Exception as e:
        print("Email failed ❌")
        print(e)