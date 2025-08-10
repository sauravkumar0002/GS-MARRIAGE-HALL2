import sqlite3

def get_availability():
    conn = sqlite3.connect('bookings.db')
    c = conn.cursor()
    c.execute("SELECT date FROM bookings")
    booked_dates = [row[0] for row in c.fetchall()]
    conn.close()
    return booked_dates
