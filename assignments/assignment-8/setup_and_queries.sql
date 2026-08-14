-- =================================================================
-- Assignment 8: SQL Joins - Setup Script & Solutions
-- Student Name: Roshini
-- =================================================================

-- -----------------------------------------------------------------
-- STEP 1: Database & Table Setup (Run this first)
-- -----------------------------------------------------------------
CREATE DATABASE IF NOT EXISTS university_db;
USE university_db;

-- Drop tables if they already exist
DROP TABLE IF EXISTS students;
DROP TABLE IF EXISTS departments;

-- Create departments table
CREATE TABLE departments (
    dept_id INT PRIMARY KEY,
    dept_name VARCHAR(50) NOT NULL
);

-- Create students table
CREATE TABLE students (
    student_id INT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    marks INT,
    dept_id INT,
    FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
);

-- Insert Sample Data into departments (3 departments)
INSERT INTO departments (dept_id, dept_name) VALUES
(1, 'Computer Science'),
(2, 'Electrical Engineering'),
(3, 'Mechanical Engineering'),
(4, 'Civil Engineering'); -- Department with 0 students to test LEFT/RIGHT/FULL joins

-- Insert Sample Data into students (8 students)
INSERT INTO students (student_id, first_name, last_name, marks, dept_id) VALUES
(101, 'Roshini', 'Akula', 85, 1),
(102, 'Rahul', 'Sharma', 92, 1),
(103, 'Priya', 'Verma', 78, 1),
(104, 'Amit', 'Kumar', 64, 2),
(105, 'Sneha', 'Reddy', 88, 2),
(106, 'Vikram', 'Singh', 55, 3),
(107, 'Ananya', 'Gupta', 91, NULL), -- Student with no department
(108, 'Karan', 'Mehta', 73, NULL); -- Student with no department

-- -----------------------------------------------------------------
-- STEP 2: Assignment Queries
-- -----------------------------------------------------------------

-- Question 1: INNER JOIN between students and departments
SELECT s.first_name, d.dept_name 
FROM students s
INNER JOIN departments d ON s.dept_id = d.dept_id;

-- Question 2: LEFT JOIN (List all departments and any students in them)
SELECT d.dept_name, s.first_name, s.last_name 
FROM departments d
LEFT JOIN students s ON d.dept_id = s.dept_id;

-- Question 3: RIGHT JOIN (List all students and their department names)
SELECT s.first_name, s.last_name, d.dept_name 
FROM departments d
RIGHT JOIN students s ON d.dept_id = s.dept_id;

-- Question 4: Find students who do not belong to any department
SELECT s.student_id, s.first_name, s.last_name 
FROM students s
LEFT JOIN departments d ON s.dept_id = d.dept_id
WHERE d.dept_id IS NULL;

-- Question 5: CROSS JOIN between students and departments
SELECT s.first_name, d.dept_name 
FROM students s
CROSS JOIN departments d;
-- Total rows returned: 24 (8 students * 3 departments = 24 rows)

-- Question 6: Average marks of students in 'Computer Science' department
SELECT d.dept_name, AVG(s.marks) AS avg_marks 
FROM students s
INNER JOIN departments d ON s.dept_id = d.dept_id
WHERE d.dept_name = 'Computer Science'
GROUP BY d.dept_name;

-- Question 7: Join students and departments, show students with marks > 80
SELECT s.first_name, s.last_name, s.marks, d.dept_name 
FROM students s
INNER JOIN departments d ON s.dept_id = d.dept_id
WHERE s.marks > 80;

-- Question 8: SELF JOIN to find pairs of students in the same department
SELECT s1.first_name AS student_1, s2.first_name AS student_2, s1.dept_id 
FROM students s1
INNER JOIN students s2 ON s1.dept_id = s2.dept_id AND s1.student_id != s2.student_id;

-- Question 9: INNER JOIN to list departments having more than 2 students
SELECT d.dept_id, d.dept_name, COUNT(s.student_id) AS total_students 
FROM departments d
INNER JOIN students s ON d.dept_id = s.dept_id
GROUP BY d.dept_id, d.dept_name
HAVING COUNT(s.student_id) > 2;

-- Question 10: FULL OUTER JOIN simulation using UNION in MySQL
SELECT s.first_name, d.dept_name 
FROM students s
LEFT JOIN departments d ON s.dept_id = d.dept_id
UNION
SELECT s.first_name, d.dept_name 
FROM students s
RIGHT JOIN departments d ON s.dept_id = d.dept_id;
