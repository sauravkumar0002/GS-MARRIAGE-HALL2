from flask import Flask, render_template, request, redirect, url_for, flash, session
from config import Config
import sqlite3
from utils.email_service import send_confirmation_email
from utils.razorpay_service import create_order
from utils.calendar_service import get_availability

app = Flask(__name__)
app.config.from_object(Config)

def get_db_connection():
    conn = sqlite3.connect('bookings.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/booking', methods=['GET', 'POST'])
def booking():
    if request.method == 'POST':
        # Store booking in DB
        name = request.form['name']
        email = request.form['email']
        date = request.form['date']
        conn = get_db_connection()
        conn.execute("INSERT INTO bookings (name, email, date) VALUES (?, ?, ?)", (name, email, date))
        conn.commit()
        conn.close()
        send_confirmation_email(email, date)
        return redirect(url_for('payment'))
    return render_template('booking.html')

@app.route('/calendar')
def calendar():
    availability = get_availability()
    return render_template('calendar.html', availability=availability)

@app.route('/payment')
def payment():
    return render_template('payment.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Handle contact form logic here
        pass
    return render_template('contact.html')

@app.route('/admin')
def admin():
    # Fetch and display bookings
    conn = get_db_connection()
    bookings = conn.execute("SELECT * FROM bookings").fetchall()
    conn.close()
    return render_template('admin.html', bookings=bookings)

if __name__ == '__main__':
    app.run(debug=True)
