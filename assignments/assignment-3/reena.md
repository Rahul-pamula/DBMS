# Assignment 3: Data Definition Language (DDL) Commands

**Student Name:** Reena  
**Course:** Database Management System (DBMS)  
**Topic:** DDL Commands (`CREATE`, `ALTER`, `DROP`, `TRUNCATE`, `RENAME`)

---

## Overview

Data Definition Language (DDL) consists of SQL commands used to define, modify, and manage the structure of database objects (databases, tables, views, etc.). DDL statements are **Auto-Committed**, meaning changes are saved permanently upon execution.

---

## 1. `CREATE` Command

Used to create a new database or table schema.

```sql
-- Create Database
CREATE DATABASE student_db;
USE student_db;

-- Create Students Table
CREATE TABLE students (
    student_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100),
    enrollment_date DATE
);
```

---

## 2. `ALTER` Command

Used to modify existing table structures such as adding, modifying, or dropping columns.

```sql
-- Add a new column
ALTER TABLE students ADD phone_number VARCHAR(15);

-- Modify datatype of an existing column
ALTER TABLE students MODIFY email VARCHAR(150);

-- Drop a column
ALTER TABLE students DROP COLUMN enrollment_date;
```

---

## 3. `RENAME` Command

Used to rename an existing table.

```sql
-- Rename table
RENAME TABLE students TO student_records;
```

---

## 4. `TRUNCATE` Command

Used to remove all rows from a table while keeping the table structure intact.

```sql
-- Truncate table data
TRUNCATE TABLE student_records;
```

---

## 5. `DROP` Command

Used to permanently delete a table or database structure along with all its data.

```sql
-- Drop table
DROP TABLE student_records;

-- Drop database
DROP DATABASE student_db;
```

---

## Proof of Work / Screenshot

![DDL Commands Execution](./images/reena_ddl.png)
