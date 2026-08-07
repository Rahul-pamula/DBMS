# Assignment 3: Data Definition Language (DDL) Commands

**Data Definition Language (DDL)** is a category of SQL commands used to define, manage, and modify the structure of database objects such as databases, tables, and columns. DDL commands alter the database schema permanently and are **auto-committed** (cannot be rolled back).

---

## Key DDL Commands & Syntax

### 1. `CREATE`
Used to create a new database or table structure.
```sql
CREATE DATABASE student_db;
USE student_db;

CREATE TABLE students (
    student_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    dob DATE
);
```

### 2. `ALTER`
Modifies an existing table structure (adding, modifying, renaming, or dropping columns).
```sql
-- Add a new column
ALTER TABLE students ADD email VARCHAR(100);

-- Modify column datatype
ALTER TABLE students MODIFY email VARCHAR(150);

-- Rename a column
ALTER TABLE students RENAME COLUMN dob TO date_of_birth;

-- Drop a column
ALTER TABLE students DROP COLUMN email;
```

### 3. `RENAME`
Renames an existing table.
```sql
RENAME TABLE students TO student_records;
```

### 4. `TRUNCATE`
Removes all records/rows from a table while preserving the table structure for future data.
```sql
TRUNCATE TABLE student_records;
```

### 5. `DROP`
Permanently deletes a table or database and all its structure and data.
```sql
DROP TABLE student_records;
```

---

## Proof of Work

![DDL Commands Screenshot](./images/roshini_screenshot.png)

---

## Conclusion
DDL commands form the foundation of database management. They allow developers and DBAs to design, evolve, and maintain database schemas efficiently.