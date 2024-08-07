-- Ensure compatibility with various SQL modes
SET sql_mode = '';

-- Check if the 'users' table exists
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255)
);

-- Ensure the attributes are unique directly in the table schema to enforce business rules and avoid application bugs
ALTER TABLE users 
    ADD CONSTRAINT uq_email UNIQUE (email);

