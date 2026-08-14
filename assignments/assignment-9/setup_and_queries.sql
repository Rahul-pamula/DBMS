-- =================================================================
-- Assignment 9: Set Operations and Subqueries - Setup Script & Solutions
-- Student Name: Roshini
-- =================================================================

-- -----------------------------------------------------------------
-- STEP 1: Database & Table Setup
-- -----------------------------------------------------------------
CREATE DATABASE IF NOT EXISTS university_db;
USE university_db;

-- Drop existing tables
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

-- Insert Sample Data into departments
INSERT INTO departments (dept_id, dept_name) VALUES
(1, 'Computer Science'),
(2, 'Electrical Engineering'),
(3, 'Mechanical'),
(4, 'Civil'); -- Unassigned department for testing EXCEPT simulation

-- Insert Sample Data into students
INSERT INTO students (student_id, first_name, last_name, marks, dept_id) VALUES
(101, 'Roshini', 'Akula', 85, 1),
(102, 'Rahul', 'Sharma', 92, 1),
(103, 'Priya', 'Verma', 78, 1),
(104, 'Amit', 'Kumar', 64, 2),
(105, 'Sneha', 'Reddy', 88, 3),
(106, 'Vikram', 'Singh', 55, 3),
(107, 'Ananya', 'Gupta', 91, NULL), -- Student with no department
(108, 'Karan', 'Mehta', 73, NULL);

-- -----------------------------------------------------------------
-- STEP 2: Assignment Queries
-- -----------------------------------------------------------------

-- Question 1: UNION of dept_id from departments and students
SELECT dept_id FROM departments
UNION
SELECT dept_id FROM students;

-- Question 2: UNION ALL of dept_id from departments and students
SELECT dept_id FROM departments
UNION ALL
SELECT dept_id FROM students;
-- Difference: UNION removes duplicates, UNION ALL keeps all duplicate rows.

-- Question 3: Single-row subquery for student with lowest marks
SELECT first_name, marks 
FROM students 
WHERE marks = (SELECT MIN(marks) FROM students);

-- Question 4: Multi-row subquery using IN for 'Mechanical' or 'Civil' departments
SELECT first_name 
FROM students 
WHERE dept_id IN (
    SELECT dept_id 
    FROM departments 
    WHERE dept_name IN ('Mechanical', 'Civil')
);

-- Question 5: Subquery to find students with marks > overall average marks
SELECT first_name, last_name, marks 
FROM students 
WHERE marks > (SELECT AVG(marks) FROM students);

-- Question 6: Simulate INTERSECT using IN to find dept_ids present in both tables
SELECT DISTINCT dept_id 
FROM departments 
WHERE dept_id IN (
    SELECT dept_id 
    FROM students 
    WHERE dept_id IS NOT NULL
);

-- Question 7: Simulate EXCEPT using NOT IN for unassigned departments
SELECT dept_id, dept_name 
FROM departments 
WHERE dept_id NOT IN (
    SELECT dept_id 
    FROM students 
    WHERE dept_id IS NOT NULL
);

-- Question 8: Subquery inside SELECT clause to display overall average marks
SELECT first_name, marks, 
       (SELECT AVG(marks) FROM students) AS overall_avg_marks 
FROM students;

-- Question 9: EXISTS subquery to list dept_names having at least one student
SELECT d.dept_name 
FROM departments d 
WHERE EXISTS (
    SELECT 1 
    FROM students s 
    WHERE s.dept_id = d.dept_id
);

-- Question 10: Subquery to find the second highest marks
SELECT MAX(marks) AS second_highest_marks 
FROM students 
WHERE marks < (SELECT MAX(marks) FROM students);
