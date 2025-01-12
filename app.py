from flask import Flask, render_template, request, redirect, url_for, jsonify, session
from flask_cors import CORS
import random
import json

app = Flask(__name__)
CORS(app)

# Secret key for session management (important for handling user sessions securely)
app.secret_key = 'your-secret-key'

# Dummy user database (for the sake of demonstration, you could extend this)
users = {"user1": "password1", "user2": "password2"}

# Math problem generation API
@app.route('/api/math_problem', methods=['GET'])
def generate_math_problem():
    """
    This API endpoint generates a random math problem for the user. 
    The problems vary in complexity based on the grade level (K-12).
    """
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    operator = random.choice(['+', '-', '*', '/'])
    
    if operator == '+':
        problem = f"{num1} + {num2} = ?"
        answer = num1 + num2
    elif operator == '-':
        problem = f"{num1} - {num2} = ?"
        answer = num1 - num2
    elif operator == '*':
        problem = f"{num1} * {num2} = ?"
        answer = num1 * num2
    elif operator == '/':
        problem = f"{num1 * num2} ÷ {num1} = ?"
        answer = num2  # Ensure that the division is always whole

    # Return both the problem and the answer in the response
    return jsonify({"problem": problem, "answer": answer})

# User Authentication Route
@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    A simple user login system to authenticate users. 
    In a production system, this should use proper encryption & authentication mechanisms.
    """
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if users.get(username) == password:
            session['username'] = username  # Store the username in the session
            return redirect(url_for('dashboard'))
        else:
            return "Invalid credentials, please try again."
    return render_template('login.html')

# Dashboard Route (Math Dashboard)
@app.route('/dashboard')
def dashboard():
    """
    This is the main user dashboard. After logging in, the user is redirected here 
    to interact with math problems and visualizations.
    """
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('dashboard.html')

# Log out route
@app.route('/logout')
def logout():
    """
    A simple logout function that clears the session data.
    """
    session.clear()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
