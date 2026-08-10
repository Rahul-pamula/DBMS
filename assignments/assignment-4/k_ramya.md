# Assignment 4: Working on DML Commands

**Student Name:** K. Ramya  
**Course:** Database Management Systems (DBMS)  
**Topic:** Data Manipulation Language (DML) Commands  

---

## Solutions & SQL Queries

### Question 1
**Write an `INSERT` statement to add yourself to the `students` table.**

```sql
INSERT INTO students (student_id, first_name, last_name, email, dob) 
VALUES (1007, 'Ramya', 'K', 'ramya@university.edu', '2004-08-15');
```

---

### Question 2
**The university has launched a new course: 'Cyber Security' with 4 credits. Insert it.**

```sql
INSERT INTO courses (course_id, course_name, credits) 
VALUES (106, 'Cyber Security', 4);
```

---

### Question 3
**Update the `dob` of student ID 1002 to '2005-02-28'.**

```sql
UPDATE students 
SET dob = '2005-02-28' 
WHERE student_id = 1002;
```

---

### Question 4
**Dr. Smith (faculty_id = 1) just completed another year of teaching. Write an `UPDATE` statement to increment his `experience_years` by 1.**

```sql
UPDATE faculty 
SET experience_years = experience_years + 1 
WHERE faculty_id = 1;
```

---

### Question 5
**Write a query to delete all attendance records for the date '2023-12-25' (Holiday).**

```sql
DELETE FROM attendance 
WHERE date = '2023-12-25';
```

---

### Question 6
**A student has changed their last name to 'Verma' and their phone number to '1234567890'. Update both in a single query for student ID 1004.**

```sql
UPDATE students 
SET last_name = 'Verma', phone_number = '1234567890' 
WHERE student_id = 1004;
```

---

### Question 7
**Write an `INSERT` statement using a `SELECT` query to copy all computer science faculty (dept_id = 1) into a new table called `cs_faculty`.**

```sql
INSERT INTO cs_faculty 
SELECT * FROM faculty 
WHERE dept_id = 1;
```

*Alternative (specifying column names explicitly):*
```sql
INSERT INTO cs_faculty (faculty_id, full_name, experience_years, dept_id)
SELECT faculty_id, full_name, experience_years, dept_id 
FROM faculty 
WHERE dept_id = 1;
```

---

### Question 8
**Write a query to give a 10% bonus to the score of all students in the `marks` table.**

```sql
UPDATE marks 
SET score = score * 1.10;
```

---

### Question 9
**Delete all students who do not have an email address (i.e., email is NULL).**

```sql
DELETE FROM students 
WHERE email IS NULL;
```

---

### Question 10
**Start a transaction, delete all records from `courses`, and then undo the operation. Write the exact 3 commands required.**

```sql
-- Command 1: Start transaction
START TRANSACTION;

-- Command 2: Delete all records from courses
DELETE FROM courses;

-- Command 3: Undo (Rollback) deletion
ROLLBACK;
```

---

## Key DML Concepts Demonstrated

1. **`INSERT`**: Used to insert new rows individually or copy filtered rows from another table using `INSERT INTO ... SELECT`.
2. **`UPDATE`**: Modifies existing table data using expressions (e.g., `experience_years + 1`, `score * 1.10`) and single/multiple column update sets.
3. **`DELETE`**: Removes records filtered by a `WHERE` clause (e.g., date constraints, `IS NULL` checks).
4. **Transactions**: Enables ACID compliance, allowing modifications made by DML operations to be safely rolled back before `COMMIT`.
