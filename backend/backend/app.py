from flask import Flask, render_template, request, redirect, session
import mysql.connector

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # For session management

# Database configuration
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="SC2004",
    database="internship_portal"
)

@app.route('/')
def home():
    return "Welcome to the Internship Portal Backend!"

if __name__ == '__main__':
    app.run(debug=True)
