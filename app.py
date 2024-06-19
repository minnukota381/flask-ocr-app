import os
from flask import Flask, render_template, request, redirect, url_for, session, flash
import easyocr
from PIL import Image
import io
import numpy as np
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')

reader = easyocr.Reader(['en'])

# Function to establish connection to SQLite database
def create_connection():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fullname TEXT NOT NULL,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

create_connection()

# Function to upload image and convert to text
def convert_image_to_text(image_file):
    image = Image.open(io.BytesIO(image_file.read()))
    image_np = np.array(image)
    result = reader.readtext(image_np)
    text = " ".join([res[1] for res in result])
    return text

# Route for home page (login)
@app.route('/')
def login():
    # if 'username' in session:
    #     return redirect(url_for('index'))
    return render_template('login.html')

# Route for login form submission
@app.route('/login', methods=['POST'])
def login_post():
    username = request.form['username']
    password = request.form['password']

    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
    user = cursor.fetchone()
    conn.close()

    if user and check_password_hash(user[3], password):
        session['username'] = user[2]  # store username in session
        return redirect(url_for('index'))  # redirect to index.html upon successful login
    else:
        flash('Login Unsuccessful. Please check username and password', 'danger')
        return redirect(url_for('login'))

# Route for registration form
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        fullname = request.form['fullname']
        username = request.form['username']
        password = generate_password_hash(request.form['password'], method='pbkdf2:sha256', salt_length=8)
        
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        try:
            cursor.execute('INSERT INTO users (fullname, username, password) VALUES (?, ?, ?)', (fullname, username, password))
            conn.commit()
            flash('Registration successful! Please login.', 'success')
            conn.close()
            return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            flash('Username already exists. Please choose a different username.', 'danger')
            conn.close()

    return render_template('register.html')

# Route for logging out
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

# Route for index page (image upload and conversion)
@app.route('/index', methods=['GET', 'POST'])
def index():
    if 'username' not in session:
        return redirect(url_for('login'))

    text = None
    image_file = None

    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part', 'danger')
            return redirect(request.url)

        file = request.files['file']
        if file.filename == '':
            flash('No selected file', 'danger')
            return redirect(request.url)

        image_file = file
        text = convert_image_to_text(file)

    return render_template('index.html', text=text, image_file=image_file)

if __name__ == '__main__':
    app.run(debug=True)
