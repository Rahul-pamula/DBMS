# Assignment 5: SQL Constraints & Referential Integrity

**Student Name:** Yamini Vatturi  
**Course:** Database Management Systems (DBMS)  
**Topic:** Unit 2 Part 4 - SQL Constraints & Referential Integrity  

---

## 📌 Introduction to SQL Constraints

**SQL Constraints** are rules enforced on database columns to restrict the type of data that can be inserted, updated, or manipulated within a table. They ensure **data integrity**, **accuracy**, and **reliability**, preventing invalid or bad data from entering the database.

### Key Types of Constraints:
1. **`NOT NULL`**: Ensures that a column cannot store `NULL` (empty) values.
2. **`UNIQUE`**: Guarantees that all values in a column are distinct.
3. **`DEFAULT`**: Provides a default value when no value is specified during insertion.
4. **`CHECK`**: Restricts the range or format of values that can be entered based on a logical condition.
5. **`PRIMARY KEY`**: Uniquely identifies each record in a table (combination of `NOT NULL` and `UNIQUE`).
6. **`FOREIGN KEY`**: Enforces referential integrity by linking a column to the primary key of another table.

---

## 🛠️ Assignment Questions & SQL Solutions

### Question 1: Create a `students` table where `student_id` is the Primary Key, and `first_name` and `email` are enforced with `NOT NULL` constraints.

**SQL Query:**
```sql
CREATE TABLE students (
    student_id INT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50),
    email VARCHAR(100) NOT NULL
);
```

---

### Question 2: Create a `faculty` table ensuring that every faculty member has a `UNIQUE` email address and a `UNIQUE` phone number.

**SQL Query:**
```sql
CREATE TABLE faculty (
    faculty_id INT PRIMARY KEY,
    faculty_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    phone_number VARCHAR(15) UNIQUE
);
```

---

### Question 3: Create an `attendance` table where the `status` column defaults to `'P'` (Present) if no status value is explicitly passed during `INSERT`.

**SQL Query:**
```sql
CREATE TABLE attendance (
    attendance_id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT NOT NULL,
    attendance_date DATE NOT NULL,
    status CHAR(1) DEFAULT 'P'
);

-- Insert example demonstrating DEFAULT constraint
INSERT INTO attendance (student_id, attendance_date) 
VALUES (101, '2026-08-10');
```

---

### Question 4: Create a `marks` table with a `CHECK` constraint ensuring `score` is between `0` and `100` and `age` is greater than or equal to `18`.

**SQL Query:**
```sql
CREATE TABLE marks (
    mark_id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT NOT NULL,
    score DECIMAL(5,2) CHECK (score >= 0 AND score <= 100),
    age INT CHECK (age >= 18)
);
```

---

### Question 5: Define a `departments` table with `dept_id` as the `PRIMARY KEY` and show how duplicate insertion is rejected by MySQL.

**SQL Query:**
```sql
CREATE TABLE departments (
    dept_id INT PRIMARY KEY,
    dept_name VARCHAR(50) NOT NULL
);

-- Valid Insert
INSERT INTO departments (dept_id, dept_name) VALUES (1, 'Computer Science');

-- Attempting duplicate PK insertion (Will fail with duplicate key error)
-- INSERT INTO departments (dept_id, dept_name) VALUES (1, 'Mechanical');
```

---

### Question 6: Create an `enrollments` table using a `COMPOSITE PRIMARY KEY` composed of `student_id` and `course_id`.

**SQL Query:**
```sql
CREATE TABLE enrollments (
    student_id INT,
    course_id INT,
    enrollment_date DATE DEFAULT (CURRENT_DATE),
    PRIMARY KEY (student_id, course_id)
);
```

---

### Question 7: Establish a `FOREIGN KEY` relationship between `student_records` (child table) and `departments` (parent table) to enforce Referential Integrity.

**SQL Query:**
```sql
CREATE TABLE student_records (
    student_id INT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    dept_id INT,
    FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
);
```

---

### Question 8: Write a query creating a child table `course_enrollments` with `ON DELETE CASCADE` so that deleting a student automatically removes their course enrollment records.

**SQL Query:**
```sql
CREATE TABLE course_enrollments (
    enrollment_id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT,
    course_id INT NOT NULL,
    FOREIGN KEY (student_id) REFERENCES student_records(student_id) ON DELETE CASCADE
);
```

---

### Question 9: Demonstrate `ON DELETE SET NULL` on a `faculty_dept` table linked to `departments` so that if a department is deleted, the faculty member's `dept_id` becomes `NULL`.

**SQL Query:**
```sql
CREATE TABLE faculty_dept (
    faculty_id INT PRIMARY KEY,
    faculty_name VARCHAR(100) NOT NULL,
    dept_id INT,
    FOREIGN KEY (dept_id) REFERENCES departments(dept_id) ON DELETE SET NULL
);
```

---

### Question 10: Use `ALTER TABLE` to add a `CHECK` constraint `chk_experience` to the `faculty` table ensuring `experience_years >= 0`, and write the command to drop a constraint.

**SQL Query:**
```sql
-- Add CHECK constraint using ALTER TABLE
ALTER TABLE faculty 
ADD CONSTRAINT chk_experience CHECK (experience_years >= 0);

-- Drop Constraint using ALTER TABLE
ALTER TABLE faculty 
DROP CONSTRAINT chk_experience;
```

---

## 📷 Screenshot Proof of Work

Below is the execution screenshot demonstrating successful query runs in MySQL terminal:

![Execution Screenshot](./images/yamini_constraints.png)

---

## ✅ Conclusion
In this assignment, all 10 SQL constraint queries (`NOT NULL`, `UNIQUE`, `DEFAULT`, `CHECK`, `PRIMARY KEY`, `COMPOSITE KEY`, `FOREIGN KEY`, `ON DELETE CASCADE`, `ON DELETE SET NULL`, and `ALTER TABLE ADD/DROP CONSTRAINT`) were designed, executed, and verified.
