Simple Daily Journal
A minimal and secure web application for writing, saving, and managing personal journal entries. Built with Flask and MySQL, it provides user authentication, private data storage, and a lightweight frontend for ease of use.

*Features*
User registration and authentication with hashed passwords
Create, view, and manage journal entries
User-specific data isolation to ensure privacy
Backend powered by Flask and MySQL
Clean, responsive user interface

*Tech Stack*
Frontend: HTML5, CSS3, JavaScript
Backend: Python (Flask)
Database: MySQL
Additional Libraries: Flask-CORS, PyMySQL, hashlib

*Setup Instructions*
Prerequisites
Python 3.x
MySQL server
pip (Python package manager)

1. Clone the repository
git clone https://github.com/<your-username>/daily-journal.git
cd daily-journal

2. Install dependencies
pip install -r requirements.txt

4. Configure the database
Start your MySQL server.
Create the database and tables using the provided SQL script (schema.sql).
Update the database credentials in app.py if necessary.

4. Run the application
python app.py
Open http://127.0.0.1:5000 in your web browser.

Directory Structure
csharp
daily-journal/
├── app.py               # Flask backend
├── requirements.txt     # Python dependencies
├── templates/           # HTML templates (frontend)
├── static/              # Static files (CSS, JS)
├── schema.sql           # Database schema
└── README.md            # Project documentation

Future Enhancements
Deployment to cloud platforms (Heroku, Render, AWS)
Mobile-friendly responsive design
Password reset and account management features
Rich text editor for journal entries

License
This project is licensed under the MIT License.

