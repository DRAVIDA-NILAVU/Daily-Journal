from flask import Flask, request, jsonify
import mysql.connector
from flask_cors import CORS
import hashlib

app = Flask(__name__)
CORS(app)

# Connect to MySQL
db = mysql.connector.connect(
    host="localhost:3306",
    user="root",
    password="8122655232",  # 🔥 change this
    database="journal.sql"
)
cursor = db.cursor(dictionary=True)

# Hash password
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# API: Register
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data['username']
    password = hash_password(data['password'])
    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
        db.commit()
        return jsonify({'message': 'User registered successfully'}), 201
    except mysql.connector.IntegrityError:
        return jsonify({'error': 'Username already exists'}), 409

# API: Login
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data['username']
    password = hash_password(data['password'])
    cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
    user = cursor.fetchone()
    if user:
        return jsonify({'message': 'Login successful', 'user_id': user['id']}), 200
    else:
        return jsonify({'error': 'Invalid credentials'}), 401

# API: Add Journal Entry
@app.route('/add_entry', methods=['POST'])
def add_entry():
    data = request.get_json()
    user_id = data['user_id']
    title = data['title']
    content = data['content']
    cursor.execute("INSERT INTO journal_entries (user_id, title, content) VALUES (%s, %s, %s)",
                   (user_id, title, content))
    db.commit()
    return jsonify({'message': 'Entry added successfully'}), 201

# API: Get Entries
@app.route('/get_entries/<int:user_id>', methods=['GET'])
def get_entries(user_id):
    cursor.execute("SELECT title, content, created_at FROM journal_entries WHERE user_id=%s ORDER BY created_at DESC", (user_id,))
    entries = cursor.fetchall()
    return jsonify(entries), 200

if __name__ == '__main__':
    app.run(debug=True)
