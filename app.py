from flask import Flask, render_template, request, redirect
import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)
# Get the database configuration from environment variables
DB_HOST = os.getenv('DB_HOST')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_NAME = os.getenv('DB_NAME')

# MySQL configuration
db = mysql.connector.connect(
    host=DB_HOST,
    user=DB_USER,
    password=DB_PASSWORD,
    database=DB_NAME
)

@app.route('/')
def index():
    # Fetch all donations from the database
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM donations ORDER BY created_at DESC")
    donations = cursor.fetchall()
    cursor.close()
    return render_template('index.html', donations=donations)

@app.route('/add_donation', methods=['POST'])
def add_donation():
    food_type = request.form['food_type']
    quantity = request.form['quantity']
    conditions = request.form['conditions']

    cursor = db.cursor()
    query = "INSERT INTO donations (food_type, quantity, `conditions`) VALUES (%s, %s, %s)"
    cursor.execute(query, (food_type, quantity, conditions))
    db.commit()
    cursor.close()

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
