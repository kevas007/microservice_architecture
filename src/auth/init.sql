CREATE DATABASE auth;

GRANT ALL PRIVILEGES ON auth.* TO 'root'@'localhost';

USE auth;

CREATE TABLE user (
id INT AUTO_INCREMENT PRIMARY KEY,
email VARCHAR(255) NOT NULL,
password VARCHAR(255) NOT NULL
);

INSERT INTO user (email,password) VALUES ('kev@gmail.com', 'Admin123')
