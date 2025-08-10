from flask_mail import Mail, Message
from flask import current_app

mail = Mail()

def send_confirmation_email(to_email, date):
    msg = Message("Booking Confirmation", recipients=[to_email])
    msg.body = f"Your booking for {date} is confirmed."
    mail.send(msg)
