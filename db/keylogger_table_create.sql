USE
keylogger_db;

CREATE TABLE keystrokes
(
    id          INT AUTO_INCREMENT PRIMARY KEY,
    key_pressed VARCHAR(255),
    timestamp   TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
