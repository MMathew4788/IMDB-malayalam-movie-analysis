CREATE DATABASE IF NOT EXISTS imdb;
USE imdb;

CREATE TABLE IF NOT EXISTS movies (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255),
    year INT,
    rating FLOAT,
    director VARCHAR(255),
    genres VARCHAR(255),
    duration VARCHAR(50),
    votes INT,
    metascore INT,
    description TEXT
);
