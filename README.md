Food Waste Tracker App
This app helps manage food donations, tracking donated food items from restaurants and stores to food banks, contributing to reducing food waste. The app allows users to add food donations, view all donations, and track the availability of food items.

Tech Stack
Frontend: HTML, CSS, JavaScript
Backend: Python (Flask)
Database: MySQL
Environment Variables: Python-dotenv

Setup Instructions
Prerequisites
Make sure you have the following installed:

Python 3.x
MySQL
pip (Python package manager)
MySQL Workbench or another database management tool (optional for testing)
Steps to Run the Application
Clone the repository:

bash
Copy code
git clone https://github.com/your-username/food-waste-tracker.git
cd food-waste-tracker
Create a virtual environment (optional but recommended):

bash
Copy code
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install the dependencies:

bash
Copy code
pip install -r requirements.txt
Create a .env file: In the root directory, create a .env file with the following variables:

env
Copy code
DB_HOST=localhost
DB_USER=your_mysql_username
DB_PASSWORD=your_mysql_password
DB_NAME=food_waste_db
Create the MySQL database: In MySQL Workbench or using the command line, run the following SQL command to create the database:

sql
Copy code
CREATE DATABASE food_waste_db;
Run the Flask app:

bash
Copy code
python app.py
Open the app in your browser: Navigate to http://localhost:5000 to view and interact with the app.

Features
Add new food donations.
View a list of all food donations.
Database storage for food items, quantity, and condition.
Simple UI with forms for donation submission.
Usage
Once the app is running, you can:

Add Donations: Submit food donations via a simple form.
View Donations: The app will display all donations in a list.
Database Interaction: All submitted donations are stored in the MySQL database.
Contributing
If you'd like to contribute to this project, please follow these steps:

Fork the repository.
Create a new branch (git checkout -b feature-branch).
Make your changes.
Commit your changes (git commit -m 'Add feature').
Push to the branch (git push origin feature-branch).
Open a pull request.

