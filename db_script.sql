CREATE DATABASE music_school;

CREATE USER 'music_school'@'localhost' IDENTIFIED BY 'Music_school123';
GRANT DELETE, INSERT, SELECT, UPDATE ON music_school.* TO 'music_school'@'localhost';

USE music_school;
CREATE TABLE course (name VARCHAR(50), course_id INTEGER AUTO_INCREMENT PRIMARY KEY);
CREATE TABLE instructor (name VARCHAR(50), instructor_id INTEGER AUTO_INCREMENT PRIMARY KEY);
CREATE TABLE student (name VARCHAR(50), student_id INTEGER AUTO_INCREMENT PRIMARY KEY);
