--DROP DATABASE IF EXISTS Passwords;

CREATE DATABASE py_password;

USE py_password;

CREATE TABLE `user`(
    `user_id` INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    `username` VARCHAR(10) NOT NULL,
    `password` VARCHAR(64) NOT NULL
);