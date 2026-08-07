# Assignment 3: Data Definition Language (DDL) Commands

## 1. Overview & Definition

**Data Definition Language (DDL)** is a subset of SQL used to define, manage, and alter the structure of database objects (such as databases, tables, columns, indexes, and views). Unlike DML (Data Manipulation Language), DDL commands affect the **schema** of the database rather than the data records stored within it.

> **Key Characteristic:** DDL commands are **Auto-Committed**. Once executed, changes to the database structure are permanent and cannot be rolled back.

---

## 2. Key DDL Commands & Syntax with Examples

### A. `CREATE` Command
Used to create a new database or table structure.

#### Syntax:
```sql
CREATE DATABASE database_name;

CREATE TABLE table_name (
    column1 datatype constraints,
    column2 datatype constraints,
    ...
);
```

#### Example:
```sql
-- Create database
CREATE DATABASE student_db;
USE student_db;

-- Create table
CREATE TABLE students (
    student_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100),
    enrollment_date DATE
);
```

---

### B. `ALTER` Command
Used to modify the structure of an existing table without deleting its existing data.

#### 1. `ADD` Column
Adds a new column to an existing table.
```sql
ALTER TABLE students 
ADD phone_number VARCHAR(15);
```

#### 2. `MODIFY` / `ALTER COLUMN` Data Type
Changes the data type or constraints of an existing column.
```sql
ALTER TABLE students 
MODIFY email VARCHAR(150);
```

#### 3. `RENAME COLUMN`
Renames an existing column.
```sql
ALTER TABLE students 
RENAME COLUMN phone_number TO contact_no;
```

#### 4. `DROP COLUMN`
Removes a column permanently from a table.
```sql
ALTER TABLE students 
DROP COLUMN contact_no;
```

---

### C. `RENAME` Command
Used to rename an existing table.

#### Syntax & Example:
```sql
RENAME TABLE students TO student_records;
```

---

### D. `TRUNCATE` Command
Removes **all rows** from a table while preserving the table structure for future data insertion. It is faster than `DELETE` because it deallocates the data pages rather than deleting rows individually.

#### Syntax & Example:
```sql
TRUNCATE TABLE student_records;
```

---

### E. `DROP` Command
Deletes a table, index, or entire database permanently from the database engine along with all its structure and data.

#### Syntax & Example:
```sql
-- Drop table
DROP TABLE student_records;

-- Drop database
DROP DATABASE student_db;
```

---

## 3. Comparison: `DROP` vs `TRUNCATE` vs `DELETE`

| Feature | `DROP` (DDL) | `TRUNCATE` (DDL) | `DELETE` (DML) |
| :--- | :--- | :--- | :--- |
| **Action** | Removes table structure and data | Deletes all rows, keeps table structure | Deletes specific or all rows |
| **Rollback** | Cannot be rolled back | Cannot be rolled back | Can be rolled back (if inside transaction) |
| **Speed** | Very Fast | Fast | Slower (logs row by row) |
| **`WHERE` Clause** | No | No | Yes |

---

## 4. Proof of Work

Below is the screenshot showing the execution of DDL commands in MySQL/Database terminal:

![DDL Commands Screenshot](./images/ramya.screenshot.png)

---

## 5. Conclusion

DDL commands form the backbone of database design. Mastering `CREATE`, `ALTER`, `RENAME`, `TRUNCATE`, and `DROP` allows developers and database administrators to efficiently design, maintain, and evolve relational database schemas.