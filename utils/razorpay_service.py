import razorpay
from flask import current_app

client = razorpay.Client(auth=(current_app.config['RAZORPAY_KEY_ID'], current_app.config['RAZORPAY_KEY_SECRET']))

def create_order(amount):
    data = { "amount": int(amount)*100, "currency": "INR", "payment_capture": 1 }
    return client.order.create(data=data)
