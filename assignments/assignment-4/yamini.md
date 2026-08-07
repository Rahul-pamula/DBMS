# Assignment 4: Working on DML Commands

**Student Name:** Yamini Vatturi  
**Course:** Database Management Systems (DBMS)  
**Topic:** Data Manipulation Language (DML) Commands  

---

## Assignment Questions & SQL Solutions

### Question 1: Write an INSERT statement to add yourself to the students table.

**SQL Query:**
```sql
INSERT INTO students (student_id, first_name, last_name, dob, email)
VALUES (1005, 'Yamini', 'Vatturi', '2004-08-15', 'yamini@university.edu');
```

---

### Question 2: The university has launched a new course: 'Cyber Security' with 4 credits. Insert it.

**SQL Query:**
```sql
INSERT INTO courses (course_name, credits)
VALUES ('Cyber Security', 4);
```
*(If `course_id` is required and not auto-incremented, include `course_id` e.g., `INSERT INTO courses (course_id, course_name, credits) VALUES (104, 'Cyber Security', 4);`)*

---

### Question 3: Update the dob of student ID 1002 to '2005-02-28'.

**SQL Query:**
```sql
UPDATE students
SET dob = '2005-02-28'
WHERE student_id = 1002;
```

---

### Question 4: Dr. Smith (faculty_id = 1) just completed another year of teaching. Write an UPDATE statement to increment his experience_years by 1.

**SQL Query:**
```sql
UPDATE faculty
SET experience_years = experience_years + 1
WHERE faculty_id = 1;
```

---

### Question 5: Write a query to delete all attendance records for the date '2023-12-25' (Holiday).

**SQL Query:**
```sql
DELETE FROM attendance
WHERE date = '2023-12-25';
```

---

### Question 6: A student has changed their last name to 'Verma' and their phone number to '1234567890'. Update both in a single query for student ID 1004.

**SQL Query:**
```sql
UPDATE students
SET last_name = 'Verma', phone_number = '1234567890'
WHERE student_id = 1004;
```

---

### Question 7: Write an INSERT statement using a SELECT query to copy all computer science faculty (dept_id = 1) into a new table called cs_faculty.

**SQL Query:**
```sql
INSERT INTO cs_faculty
SELECT * FROM faculty
WHERE dept_id = 1;
```

---

### Question 8: Write a query to give a 10% bonus to the score of all students in the marks table.

**SQL Query:**
```sql
UPDATE marks
SET score = score * 1.10;
```

---

### Question 9: Delete all students who do not have an email address (i.e., email is NULL).

**SQL Query:**
```sql
DELETE FROM students
WHERE email IS NULL;
```

---

### Question 10: Start a transaction, delete all records from courses, and then undo the operation. Write the exact 3 commands required.

**SQL Commands:**
```sql
-- Step 1: Start the transaction
START TRANSACTION;

-- Step 2: Delete all records from courses
DELETE FROM courses;

-- Step 3: Undo (rollback) the delete operation
ROLLBACK;
```
