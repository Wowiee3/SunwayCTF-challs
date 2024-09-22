CREATE DATABASE IF NOT EXISTS tester;
USE tester;

CREATE TABLE users(
  id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
  username VARCHAR(256) NOT NULL,
  password VARCHAR(256) NOT NULL
);

INSERT INTO users (username, password) VALUES ('admin', 'admin');
