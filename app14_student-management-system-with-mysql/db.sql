DROP DATABASE IF EXISTS app14_school_python_course;
DROP USER IF EXISTS 'python-course'@'localhost';

CREATE DATABASE app14_school_python_course;

USE app14_school_python_course;

CREATE TABLE students(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    course VARCHAR(255),
    mobile VARCHAR(255)
);

INSERT INTO students(name, course, mobile) VALUES ("John", "Math", "12345");
INSERT INTO students(name, course, mobile) VALUES ("Jane", "Biology", "67890");
INSERT INTO students(name, course, mobile) VALUES ("Jeffrey", "Physics", "54321");
INSERT INTO students(name, course, mobile) VALUES ("Jenny", "Astronomy", "09876");
INSERT INTO students(name, course, mobile) VALUES ("Mati", "Math", "13579");


CREATE USER 'python-course'@'localhost' IDENTIFIED BY 'python';
GRANT ALL ON app14_school_python_course TO 'python-course'@'localhost';
GRANT SELECT ON app14_school_python_course.students TO 'python-course'@'localhost';
GRANT INSERT ON app14_school_python_course.students TO 'python-course'@'localhost';
GRANT DELETE ON app14_school_python_course.students TO 'python-course'@'localhost';
GRANT UPDATE ON app14_school_python_course.students TO 'python-course'@'localhost';


