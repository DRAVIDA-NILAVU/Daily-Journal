from flask import Flask, request, jsonify, render_template
import pymysql
from flask_cors import CORS
import hashlib

app = Flask(__name__, template_folder='templates', static_folder='static')
CORS(app)

# Connect to MySQL
db = pymysql.connect(
    host="localhost",
    user="root",
    password="har7bts1nefftech",  # ✅ Confirm this password
    database="daily_journal",
    cursorclass=pymysql.cursors.DictCursor
)
cursor = db.cursor()

# Hash password
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Frontend routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login')
def login_page():
    return render_template('login.html')

@app.route('/register')
def register_page():
    return render_template('register.html')


# APIs
@app.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data['username']
    password = hash_password(data['password'])
    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
        db.commit()
        print(f"[DEBUG] Registered user: {username}")
        return jsonify({'message': 'User registered successfully'}), 201
    except pymysql.err.IntegrityError as e:
        print(f"[ERROR] Register failed: {e}")
        return jsonify({'error': 'Username already exists'}), 409

@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data['username']
    password = hash_password(data['password'])
    cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
    user = cursor.fetchone()
    if user:
        print(f"[DEBUG] Login successful for user: {username}")
        return jsonify({'message': 'Login successful', 'user_id': user['id']}), 200
    else:
        print(f"[ERROR] Login failed for user: {username}")
        return jsonify({'error': 'Invalid credentials'}), 401

@app.route('/api/add_entry', methods=['POST'])
def add_entry():
    data = request.get_json()
    user_id = data['user_id']
    title = data['title']
    content = data['content']
    try:
        cursor.execute(
            "INSERT INTO journal_entries (user_id, title, content) VALUES (%s, %s, %s)",
            (user_id, title, content)
        )
        db.commit()
        print(f"[DEBUG] Added entry for user_id={user_id}: {title}")
        return jsonify({'message': 'Entry added successfully'}), 201
    except Exception as e:
      print(f"[ERROR] Failed to add entry: {e}")  # 👈 This prints real error in console
      return jsonify({'error': str(e)}), 500

@app.route('/api/get_entries/<int:user_id>', methods=['GET'])
def get_entries(user_id):
    cursor.execute(
        "SELECT title, content, created_at FROM journal_entries WHERE user_id=%s ORDER BY created_at DESC",
        (user_id,)
    )
    entries = cursor.fetchall()
    print(f"[DEBUG] Retrieved {len(entries)} entries for user_id={user_id}")
    return jsonify(entries), 200

if __name__ == '__main__':
    app.run(debug=True)
