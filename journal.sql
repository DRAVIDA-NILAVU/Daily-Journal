-- Create the database
CREATE DATABASE IF NOT EXISTS daily_journal;
USE daily_journal;

-- Create the users table
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create the journal_entries table
CREATE TABLE IF NOT EXISTS journal_entries (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    title VARCHAR(100) NOT NULL,
    content TEXT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Add some dummy journal entries (linked to user_id=1 for testing)
-- Make sure a user with id=1 exists before running this
INSERT INTO journal_entries (user_id, title, content)
VALUES
(1, 'Day 1', 'Started my new journal project.'),
(1, 'Day 2', 'Learned about SQL and Flask integration.');

-- Show all tables
SHOW TABLES;

-- View all users
SELECT * FROM users;

-- View all journal entries
SELECT * FROM journal_entries ORDER BY created_at DESC;
