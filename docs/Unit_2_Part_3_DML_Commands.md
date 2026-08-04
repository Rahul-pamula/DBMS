# Unit 2 Part 3: Data Manipulation Language (DML) Commands

Welcome to Part 3! In the previous chapter, we acted as **Architects** using DDL to build the structure (tables) of our Student Management System. Now, we will act as **Data Entry Operators and Managers** using **DML (Data Manipulation Language)** to insert, modify, and remove actual data inside those structures.

---

## What is DML?

Data Manipulation Language (DML) commands are used to manage the actual records (rows) inside a database table.

**Key characteristics of DML:**
- **Not Auto-Committed:** Unlike DDL, DML commands are not automatically saved to the hard drive immediately (depending on database settings). They happen inside a **Transaction**. If you make a mistake, you can use the `ROLLBACK` command to undo the changes before you `COMMIT` them.

There are three primary DML commands we will cover:
1. `INSERT` (Putting data in)
2. `UPDATE` (Modifying existing data)
3. `DELETE` (Removing data)

---

## 1. The `INSERT` Command

### Definition & Purpose
The `INSERT INTO` command is used to add new rows of data into a table in the database.

### Internal Working
When you execute an INSERT command, the database engine:
1. Checks if the table exists.
2. Validates the data types (e.g., you are not trying to insert text into an integer column).
3. Checks for constraint violations (e.g., trying to insert a duplicate Primary Key).
4. Adds the row to the data pages in memory.

### Syntax Variations
```sql
-- Method 1: Specifying Column Names (Best Practice)
INSERT INTO table_name (column1, column2) VALUES (value1, value2);

-- Method 2: Without Specifying Column Names (Must match exact order)
INSERT INTO table_name VALUES (value1, value2, value3);

-- Method 3: Multiple Rows at Once
INSERT INTO table_name (column1) VALUES (value1), (value2), (value3);
```

### Visual Before & After: Insert
**Before Execution (Empty Table):**
| student_id | first_name | dept_id |
| :--- | :--- | :--- |
| *(Empty)* | | |

**Query Executed:**
```sql
INSERT INTO students (student_id, first_name, dept_id) VALUES (1, 'Rahul', 10);
```

**After Execution:**
| student_id | first_name | dept_id |
| :--- | :--- | :--- |
| 1 | Rahul | 10 |

---

### Examples 1-10: Beginner Level Insertions

#### Single Row Inserts
```sql
-- Ex 1: Standard single row insert into departments
INSERT INTO departments (dept_id, dept_name) VALUES (1, 'Computer Science');

-- Ex 2: Standard single row insert into courses
INSERT INTO courses (course_id, course_name, credits) VALUES (101, 'DBMS', 4);

-- Ex 3: Insert into faculty
INSERT INTO faculty (faculty_id, full_name, experience_years) VALUES (1, 'Dr. Smith', 10);

-- Ex 4: Standard single row insert into students
INSERT INTO students (student_id, first_name, last_name, dob) 
VALUES (1001, 'Priya', 'Sharma', '2004-05-15');

-- Ex 5: Standard single row insert into hostels
INSERT INTO hostels (hostel_id, hostel_name, room_number) VALUES (1, 'Boys Hostel A', 101);
```

#### Multiple Row Inserts
Inserting multiple rows in one query is much faster than running single queries because it reduces the communication overhead between the client and server.

```sql
-- Ex 6: Insert multiple departments
INSERT INTO departments (dept_id, dept_name) 
VALUES (2, 'Mechanical'), (3, 'Civil'), (4, 'Electrical');

-- Ex 7: Insert multiple courses
INSERT INTO courses (course_id, course_name, credits) 
VALUES (102, 'Data Structures', 4), (103, 'Operating Systems', 3);

-- Ex 8: Insert multiple students
INSERT INTO students (student_id, first_name, last_name) 
VALUES (1002, 'Amit', 'Verma'), (1003, 'Kavya', 'Rao'), (1004, 'Rohan', 'Das');

-- Ex 9: Insert multiple faculties
INSERT INTO faculty (faculty_id, full_name, experience_years) 
VALUES (2, 'Dr. Allen', 5), (3, 'Prof. Jane', 15);

-- Ex 10: Insert multiple marks
INSERT INTO marks (mark_id, student_id, score) 
VALUES (1, 1001, 85.5), (2, 1002, 92.0);
```

---

### Examples 11-20: Intermediate Insertions

#### Inserting with NULL values
Sometimes, you do not have all the data. If a column allows it, you can leave it empty by inserting `NULL` or simply omitting the column name.

```sql
-- Ex 11: Explicitly inserting NULL for date of birth
INSERT INTO students (student_id, first_name, last_name, dob) 
VALUES (1005, 'Neha', 'Gupta', NULL);

-- Ex 12: Omitting the column entirely (It automatically becomes NULL)
INSERT INTO students (student_id, first_name, last_name) 
VALUES (1006, 'Vikram', 'Singh');

-- Ex 13: Faculty with unknown experience
INSERT INTO faculty (faculty_id, full_name, experience_years) 
VALUES (4, 'Mr. John', NULL);

-- Ex 14: Null score in marks (Student absent)
INSERT INTO marks (mark_id, student_id, score) 
VALUES (3, 1003, NULL);

-- Ex 15: Null credits in courses (To be decided)
INSERT INTO courses (course_id, course_name, credits) 
VALUES (104, 'Advanced AI', NULL);
```

#### Inserting without specifying column names
If you know the exact order of columns in the database, you can skip writing the column names. *(Not recommended for production code, but good to know!)*

```sql
-- Ex 16: Assuming departments has exactly 2 columns (dept_id, dept_name)
INSERT INTO departments VALUES (5, 'Biotechnology');

-- Ex 17: Assuming courses has (course_id, course_name, credits)
INSERT INTO courses VALUES (105, 'Networks', 3);

-- Ex 18: Assuming hostels has (hostel_id, hostel_name, room_number)
INSERT INTO hostels VALUES (2, 'Girls Hostel B', 205);

-- Ex 19: Full implicit insert for faculty
INSERT INTO faculty VALUES (5, 'Dr. Strange', 20);

-- Ex 20: Full implicit insert for marks
INSERT INTO marks VALUES (4, 1004, 75.0);
```

---

### Examples 21-30: Advanced Insertions (INSERT using SELECT)

Sometimes, you want to copy data from one table to another. Instead of manually typing values, you can use the output of a `SELECT` query as the input for your `INSERT`.

```sql
-- Assume we have an empty table called 'alumni' and we want to move graduated students there.
-- Ex 21: Copy all students born before 2000 into the alumni table
INSERT INTO alumni (student_id, name)
SELECT student_id, first_name FROM students WHERE dob < '2000-01-01';

-- Ex 22: Copy specific columns from departments into a backup table
INSERT INTO departments_backup (id, name)
SELECT dept_id, dept_name FROM departments;

-- Ex 23: Insert students who scored above 90 into an 'honors_students' table
INSERT INTO honors_students (student_id, score)
SELECT student_id, score FROM marks WHERE score > 90;

-- Ex 24: Copy active courses to next_semester_courses
INSERT INTO next_semester_courses (course_id, title)
SELECT course_id, course_name FROM courses;

-- Ex 25: Archiving attendance
INSERT INTO attendance_archive (date, student_id, status)
SELECT date, student_id, status FROM attendance WHERE date < '2023-01-01';

-- Ex 26: Duplicate a faculty record (for a new campus) by selecting and altering on the fly
-- Not directly possible in one pure INSERT without explicitly defining the new PK, but we can do:
INSERT INTO faculty (faculty_id, full_name, experience_years)
SELECT 100 + faculty_id, full_name, experience_years FROM faculty WHERE faculty_id = 1;

-- Ex 27: Copying only the names of students to a mailing_list table
INSERT INTO mailing_list (contact_name)
SELECT first_name FROM students;

-- Ex 28: Insert with hardcoded values alongside selected values
INSERT INTO scholarship_winners (student_id, award_amount)
SELECT student_id, 5000 FROM marks WHERE score >= 95;

-- Ex 29: Copying all data from an old table to a new one
INSERT INTO students_2024 SELECT * FROM students;

-- Ex 30: Using SELECT to insert a calculated value
INSERT INTO faculty_bonus (faculty_id, bonus_amount)
SELECT faculty_id, experience_years * 1000 FROM faculty;
```

---

## 2. The `UPDATE` Command

### Definition & Purpose
The `UPDATE` command modifies existing records in a table. 

> [!WARNING]
> **DANGER:** If you forget to use the `WHERE` clause in an UPDATE statement, it will update **EVERY SINGLE ROW** in the table! Always double-check your WHERE condition.

### Syntax
```sql
UPDATE table_name 
SET column1 = value1, column2 = value2 
WHERE condition;
```

### Visual Before & After: Update
**Before Execution:**
| student_id | first_name | score |
| :--- | :--- | :--- |
| 1 | Rahul | 80 |
| 2 | Priya | 75 |

**Query Executed:**
```sql
UPDATE marks SET score = 95 WHERE student_id = 1;
```

**After Execution:**
| student_id | first_name | score |
| :--- | :--- | :--- |
| 1 | Rahul | 95 |
| 2 | Priya | 75 |

---

### Examples 31-40: Beginner & Intermediate Updates

#### Updating a single record
```sql
-- Ex 31: Update a student's last name
UPDATE students SET last_name = 'Kumar' WHERE student_id = 1001;

-- Ex 32: Correct a spelling mistake in a department name
UPDATE departments SET dept_name = 'Information Technology' WHERE dept_id = 1;

-- Ex 33: Update a course's credits
UPDATE courses SET credits = 5 WHERE course_id = 101;

-- Ex 34: Change faculty experience
UPDATE faculty SET experience_years = 11 WHERE faculty_id = 1;

-- Ex 35: Update hostel room assignment
UPDATE hostels SET room_number = 102 WHERE hostel_id = 1;
```

#### Updating multiple columns at once
```sql
-- Ex 36: Update both first name and last name for a student
UPDATE students 
SET first_name = 'Raj', last_name = 'Malhotra' 
WHERE student_id = 1002;

-- Ex 37: Update course name and credits simultaneously
UPDATE courses 
SET course_name = 'Advanced DBMS', credits = 4 
WHERE course_id = 101;

-- Ex 38: Update faculty name and experience
UPDATE faculty 
SET full_name = 'Dr. Alan Turing', experience_years = 30 
WHERE faculty_id = 2;

-- Ex 39: Update marks and change exam status (hypothetical column)
UPDATE marks 
SET score = 88.5, status = 'Pass' 
WHERE mark_id = 1;

-- Ex 40: Correcting multiple null values for a specific student
UPDATE students 
SET dob = '2004-10-10', phone = '9876543210' 
WHERE student_id = 1005;
```

---

### Examples 41-50: Advanced Updates

#### Updating multiple rows based on a condition
```sql
-- Ex 41: Give 5 extra grace marks to everyone who scored below 40 (Math calculation inside SQL!)
UPDATE marks 
SET score = score + 5 
WHERE score < 40;

-- Ex 42: Increment all faculty experience by 1 year at the end of the academic year
UPDATE faculty 
SET experience_years = experience_years + 1; -- (No WHERE clause, updates ALL rows!)

-- Ex 43: Change the status to 'Absent' for all attendance records on a specific strike day
UPDATE attendance 
SET status = 'A' 
WHERE date = '2023-09-15';

-- Ex 44: Update all 3-credit courses to 4 credits
UPDATE courses 
SET credits = 4 
WHERE credits = 3;

-- Ex 45: Set email domain for all students
UPDATE students 
SET email = concat(first_name, '@university.edu');

-- Ex 46: Halve the credits for a specific short-term course
UPDATE courses 
SET credits = credits / 2 
WHERE course_name = 'Workshop';

-- Ex 47: Apply a penalty of 2 marks for late submission (Student IDs 1002 and 1004)
UPDATE marks 
SET score = score - 2 
WHERE student_id IN (1002, 1004);

-- Ex 48: Mark students as 'Adult' if they were born before 2005 (Assuming an is_adult column)
UPDATE students 
SET is_adult = 1 
WHERE dob < '2005-01-01';

-- Ex 49: Reset all room numbers to NULL before the start of the semester
UPDATE hostels 
SET room_number = NULL;

-- Ex 50: Nullify the score of a student caught cheating
UPDATE marks 
SET score = NULL 
WHERE student_id = 1004;
```

---

## 3. The `DELETE` Command

### Definition & Purpose
The `DELETE` command removes existing records from a table. 

Unlike `DROP` (which destroys the whole table) and `TRUNCATE` (which instantly wipes the table without logging), `DELETE` removes rows one by one. This means it generates a log in the database, allowing you to use `ROLLBACK` to undo the deletion if you make a mistake.

### Syntax
```sql
DELETE FROM table_name WHERE condition;
```

### Visual Before & After: Delete
**Before Execution:**
| student_id | first_name |
| :--- | :--- |
| 1 | Rahul |
| 2 | Priya |

**Query Executed:**
```sql
DELETE FROM students WHERE student_id = 2;
```

**After Execution:**
| student_id | first_name |
| :--- | :--- |
| 1 | Rahul |

---

### Examples 51-65: Using DELETE

#### Deleting specific rows
```sql
-- Ex 51: Delete a specific student who dropped out
DELETE FROM students WHERE student_id = 1006;

-- Ex 52: Delete a department that closed down
DELETE FROM departments WHERE dept_id = 5;

-- Ex 53: Remove a specific course
DELETE FROM courses WHERE course_id = 105;

-- Ex 54: Remove faculty member who retired
DELETE FROM faculty WHERE faculty_id = 5;

-- Ex 55: Remove a specific attendance record (wrong entry)
DELETE FROM attendance WHERE student_id = 1001 AND date = '2023-10-01';
```

#### Deleting multiple rows using conditions
```sql
-- Ex 56: Delete all students born before 1990
DELETE FROM students WHERE dob < '1990-01-01';

-- Ex 57: Remove all courses that have less than 2 credits
DELETE FROM courses WHERE credits < 2;

-- Ex 58: Clear all marks that are exactly 0
DELETE FROM marks WHERE score = 0;

-- Ex 59: Delete students whose last name is NULL
DELETE FROM students WHERE last_name IS NULL;

-- Ex 60: Delete faculty who have no experience listed
DELETE FROM faculty WHERE experience_years IS NULL;
```

#### Deleting ALL rows (DML approach)
```sql
-- Ex 61: Delete all records from attendance table (Slower than TRUNCATE, but can be rolled back)
DELETE FROM attendance;

-- Ex 62: Delete all marks
DELETE FROM marks;

-- Ex 63: Delete all enrollments
DELETE FROM enrollments;

-- Ex 64: Delete all hostels
DELETE FROM hostels;

-- Ex 65: Delete all courses
DELETE FROM courses;
```

---

## 4. Transactions: `COMMIT` and `ROLLBACK`

DML commands operate within a transaction state. Think of it like typing an essay in MS Word.
- Doing an `INSERT`, `UPDATE`, or `DELETE` is like typing text.
- Running `COMMIT` is like pressing "Save". The changes are written to the hard drive permanently.
- Running `ROLLBACK` is like pressing "Ctrl + Z" (Undo). It cancels all unsaved changes.

> Note: Many modern SQL editors (like MySQL Workbench) have "Auto-Commit" turned on by default. You have to turn it off or explicitly start a transaction to use Rollback.

### Examples 66-70: Understanding Transactions

```sql
-- Ex 66: Start a transaction explicitly (Syntax varies slightly by DB, e.g., START TRANSACTION in MySQL)
START TRANSACTION;

-- Ex 67: We accidentally delete all students!
DELETE FROM students;

-- Ex 68: Oh no! We realize the mistake. We use ROLLBACK to bring them all back.
ROLLBACK;

-- Ex 69: Let's do a correct update.
UPDATE faculty SET experience_years = 12 WHERE faculty_id = 1;

-- Ex 70: We are happy with this change. Save it permanently to the disk.
COMMIT;
```

---

## 5. Summary and Comparison: DELETE vs TRUNCATE

| Feature | `DELETE` | `TRUNCATE` |
| :--- | :--- | :--- |
| **Command Type** | DML (Data Manipulation) | DDL (Data Definition) |
| **Condition filtering** | Supports `WHERE` clause. | Does NOT support `WHERE`. |
| **Transaction Logs** | Logs every single row deletion. | Logs only the page deallocation. |
| **Speed** | Very slow for large tables. | Extremely fast. |
| **Undo (Rollback)** | Yes, can be rolled back. | No, cannot be rolled back. |
| **Identity/Auto_Increment**| Does not reset the counter. | Resets the counter to 1. |

---

## End of Unit Assessments

### Practice Problems

*Write the SQL commands for the following scenarios based on the Student Management System.*

1. Write an `INSERT` statement to add yourself to the `students` table.
2. The university has launched a new course: 'Cyber Security' with 4 credits. Insert it.
3. Update the `dob` of student ID 1002 to '2005-02-28'.
4. Dr. Smith (faculty_id = 1) just completed another year of teaching. Write an `UPDATE` statement to increment his `experience_years` by 1.
5. Write a query to delete all attendance records for the date '2023-12-25' (Holiday).
6. A student has changed their last name to 'Verma' and their phone number to '1234567890'. Update both in a single query for student ID 1004.
7. Write an `INSERT` statement using a `SELECT` query to copy all computer science faculty (dept_id = 1) into a new table called `cs_faculty`.
8. Write a query to give a 10% bonus to the `score` of all students in the `marks` table.
9. Delete all students who do not have an email address (i.e., email is NULL).
10. Start a transaction, delete all records from `courses`, and then undo the operation. Write the exact 3 commands required.

*(Answers can be verified by running them in your SQL environment!)*
