# tutor
This a step by step learning for an app that is a visual learning concepts - 
Objective:
Building a tutoring platform using:

Flask for backend (API, user management).
Three.js for interactive 3D visualizations.
Python APIs to handle math problems and other functionalities.
A user-friendly, visual, interactive UI aimed at K-12 students.
High-Level Design & Flow:
User Authentication: We’ll use a simple authentication flow using Flask.
Math Problem API: Flask will generate math problems dynamically and send them to the frontend.
3D Visualization with Three.js: Mathematical concepts like addition, subtraction, fractions, geometry, etc., will be visually represented in 3D using Three.js.
User Interaction: Users can interact with the visualizations (e.g., drag cubes, manipulate numbers), enhancing their learning experience.
Front-End and Back-End Communication: JavaScript (AJAX) will request math problems from the Flask backend dynamically.


1. Setting Up the Flask Backend (app.py)
Step-by-Step Explanation:
In this section, we’ll set up the Flask backend that will handle user management, math problem generation, and other functionalities.


** app.py ** 

Key Points:
Secret Key for Sessions:

app.secret_key = 'your-secret-key': Flask uses the secret key to sign session cookies. This is crucial for security (avoid using a hardcoded value in production).
Math Problem Generator:

The generate_math_problem function randomly generates a math problem with one of four basic operators: addition, subtraction, multiplication, or division.
It also includes logic to ensure division problems always result in an integer answer (num1 * num2 ensures a divisible result).
Session Management for User Login:

The session object is used to store the logged-in user's data (e.g., username). This prevents unauthorized access and keeps the user logged in after authentication.
API for Dynamic Problem Generation:

We use @app.route('/api/math_problem', methods=['GET']) to define an API endpoint that dynamically generates a new math problem every time it’s accessed. This problem is returned as JSON for the frontend to handle.

2. Building the Frontend: HTML + Three.js for Visual Learning
The frontend of this platform will leverage Three.js for 3D rendering, with visual learning techniques for interactive math problem-solving.

** index.html **
