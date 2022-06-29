-- A query to create table users
-- with unique username and email
CREATE TABLE IF NOT EXISTS `users`(
        id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255) NOT NULL,
)
