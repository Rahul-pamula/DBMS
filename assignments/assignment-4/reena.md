# Assignment 4: Working on DML Commands

**Student Name:** Reena  
**Course:** Database Management System (DBMS)  
**Topic:** Data Manipulation Language (DML) Commands (`INSERT`, `UPDATE`, `DELETE`, Transactions)  

---

## Overview

Data Manipulation Language (DML) commands are used to manage, update, and manipulate records (rows) within existing database tables. Unlike DDL commands (which modify database structures and are auto-committed), DML commands operate on data rows and can be controlled using transactions (`COMMIT` and `ROLLBACK`).

The primary DML operations include:
- **`INSERT`**: Add new records into a table.
- **`UPDATE`**: Modify existing data values in a table.
- **`DELETE`**: Remove specific or all records from a table.
- **Transaction Control (`START TRANSACTION`, `ROLLBACK`, `COMMIT`)**: Manage groups of DML statements atomically.

---

## Assignment Questions & SQL Solutions

### Question 1
**Write an INSERT statement to add yourself to the students table.**

```sql
INSERT INTO students (student_id, first_name, last_name, email, dob) 
VALUES (1005, 'Reena', 'Thabassum', 'reena@example.com', '2004-01-15');
```
> **Explanation:** This query inserts a new row into the `students` table specifying explicit column values for `student_id`, `first_name`, `last_name`, `email`, and `dob`.

---

### Question 2
**The university has launched a new course: 'Cyber Security' with 4 credits. Insert it.**

```sql
INSERT INTO courses (course_id, course_name, credits) 
VALUES (104, 'Cyber Security', 4);
```
> **Explanation:** Inserts a new record into the `courses` table with `course_name` set to `'Cyber Security'` and `credits` set to `4`.

---

### Question 3
**Update the dob of student ID 1002 to '2005-02-28'.**

```sql
UPDATE students 
SET dob = '2005-02-28' 
WHERE student_id = 1002;
```
> **Explanation:** Uses the `UPDATE` statement filtered by `WHERE student_id = 1002` to safely update only the date of birth (`dob`) of student 1002.

---

### Question 4
**Dr. Smith (faculty_id = 1) just completed another year of teaching. Write an UPDATE statement to increment his experience_years by 1.**

```sql
UPDATE faculty 
SET experience_years = experience_years + 1 
WHERE faculty_id = 1;
```
> **Explanation:** Increments the existing value of `experience_years` by 1 for the record where `faculty_id = 1`.

---

### Question 5
**Write a query to delete all attendance records for the date '2023-12-25' (Holiday).**

```sql
DELETE FROM attendance 
WHERE attendance_date = '2023-12-25';
```
*(Note: If the date column in your table is named `date`, use `WHERE date = '2023-12-25'`)*

> **Explanation:** The `DELETE` command with a `WHERE` condition removes all rows from `attendance` where the attendance date falls on Christmas Holiday (`2023-12-25`).

---

### Question 6
**A student has changed their last name to 'Verma' and their phone number to '1234567890'. Update both in a single query for student ID 1004.**

```sql
UPDATE students 
SET last_name = 'Verma', 
    phone_number = '1234567890' 
WHERE student_id = 1004;
```
> **Explanation:** Modifies multiple columns simultaneously (`last_name` and `phone_number`) separated by a comma in a single `UPDATE` query for `student_id = 1004`.

---

### Question 7
**Write an INSERT statement using a SELECT query to copy all computer science faculty (dept_id = 1) into a new table called cs_faculty.**

```sql
INSERT INTO cs_faculty 
SELECT * FROM faculty 
WHERE dept_id = 1;
```
*(Alternative specifying columns explicitly:)*
```sql
INSERT INTO cs_faculty (faculty_id, full_name, experience_years, dept_id)
SELECT faculty_id, full_name, experience_years, dept_id 
FROM faculty 
WHERE dept_id = 1;
```
> **Explanation:** The `INSERT INTO ... SELECT` statement extracts all records from `faculty` matching `dept_id = 1` and inserts them directly into the `cs_faculty` table.

---

### Question 8
**Write a query to give a 10% bonus to the score of all students in the marks table.**

```sql
UPDATE marks 
SET score = score * 1.10;
```
> **Explanation:** Multiplies the existing `score` of every row in the `marks` table by `1.10`, effectively giving a 10% increase to all students.

---

### Question 9
**Delete all students who do not have an email address (i.e., email is NULL).**

```sql
DELETE FROM students 
WHERE email IS NULL;
```
> **Explanation:** Uses `IS NULL` operator in the `WHERE` clause to target and delete rows where the `email` field contains no value.

---

### Question 10
**Start a transaction, delete all records from courses, and then undo the operation. Write the exact 3 commands required.**

```sql
-- Step 1: Begin the transaction
START TRANSACTION;

-- Step 2: Delete all rows from the courses table
DELETE FROM courses;

-- Step 3: Rollback/undo the deletion operation
ROLLBACK;
```
> **Explanation:** 
> 1. `START TRANSACTION;` creates a save point and disables immediate autocommit for subsequent DML operations.
> 2. `DELETE FROM courses;` stages the removal of all records in the transaction buffer.
> 3. `ROLLBACK;` cancels all changes made during the active transaction, safely restoring all course records.

---

## Proof of Work / Screenshot

![DML Execution Screenshot](./images/reena_dml.png)
