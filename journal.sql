CREATE DATABASE IF NOT EXISTS daily_journal;
USE daily_journal;

CREATE TABLE IF NOT EXISTS journal_entries (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    content TEXT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
INSERT INTO journal_entries (title, content)
VALUES
('Day 1', 'Started my new journal project.'),
('Day 2', 'Learned about SQL and Flask integration.');