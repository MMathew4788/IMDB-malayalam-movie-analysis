CREATE DATABASE IF NOT EXISTS imdb;
CREATE DATABASE IF NOT EXISTS imdb;
USE imdb;

CREATE TABLE IF NOT EXISTS movies (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255),
    year INT,
    rating VARCHAR(255),
    duration VARCHAR(50),
    votes VARCHAR(255)
)