# Assignment 5: Constraints & Referential Integrity

**Student Name:** K. Ramya  
**Course:** Database Management Systems (DBMS)  
**Topic:** SQL Constraints & Referential Integrity  

---

## Overview

**SQL Constraints** are rules enforced on data columns in a database table. They guarantee data integrity, accuracy, and reliability by restricting the types of data that can be inserted, updated, or manipulated within a table.

Key constraints covered in this assignment:
- **`PRIMARY KEY`**: Uniquely identifies each record in a table.
- **`NOT NULL`**: Ensures a column cannot store `NULL` values.
- **`UNIQUE`**: Guarantees all values in a column are distinct.
- **`DEFAULT`**: Automatically assigns a default value when no value is provided.
- **`CHECK`**: Enforces specific logical conditions on column values.
- **`FOREIGN KEY`**: Maintains referential integrity between related tables, with cascading rules like `ON DELETE CASCADE`.

---

## Assignment Questions & SQL Solutions

### Question 1: Create a table named `patients` with a primary key `patient_id` and a `NOT NULL` constraint on `first_name`.

```sql
CREATE TABLE patients (
    patient_id INT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50),
    age INT,
    email VARCHAR(100)
);
```

---

### Question 2: Add a `UNIQUE` constraint to the `email` column in the `patients` table.

```sql
ALTER TABLE patients 
ADD CONSTRAINT unique_email UNIQUE (email);
```

---

### Question 3: Create a table `appointments` with a `DEFAULT` constraint setting the `status` to 'Scheduled'.

```sql
CREATE TABLE appointments (
    appointment_id INT PRIMARY KEY,
    patient_id INT,
    doctor_id INT,
    appointment_date DATE,
    status VARCHAR(20) DEFAULT 'Scheduled'
);
```

---

### Question 4: Add a `CHECK` constraint to the `patients` table to ensure `age` is greater than or equal to 0.

```sql
ALTER TABLE patients 
ADD CONSTRAINT chk_patient_age CHECK (age >= 0);
```

---

### Question 5: Create a table `doctors` with a primary key `doctor_id`. Then add a `FOREIGN KEY` in `appointments` that references `doctor_id` in `doctors`.

```sql
-- Step 1: Create parent table 'doctors'
CREATE TABLE doctors (
    doctor_id INT PRIMARY KEY,
    doctor_name VARCHAR(100) NOT NULL,
    specialization VARCHAR(50)
);

-- Step 2: Add foreign key constraint to child table 'appointments'
ALTER TABLE appointments 
ADD CONSTRAINT fk_appointments_doctor 
FOREIGN KEY (doctor_id) REFERENCES doctors(doctor_id);
```

---

### Question 6: Write a query to drop the `FOREIGN KEY` constraint from the `appointments` table.

```sql
ALTER TABLE appointments 
DROP FOREIGN KEY fk_appointments_doctor;
```

---

### Question 7: Re-add the `FOREIGN KEY` constraint to `appointments` with `ON DELETE CASCADE`.

```sql
ALTER TABLE appointments 
ADD CONSTRAINT fk_appointments_doctor 
FOREIGN KEY (doctor_id) REFERENCES doctors(doctor_id) 
ON DELETE CASCADE;
```

---

### Question 8: Attempt to insert a patient without a `first_name`. (Write the query that would cause this error).

```sql
-- This query fails because first_name has a NOT NULL constraint and no default value
INSERT INTO patients (patient_id, last_name, age, email) 
VALUES (101, 'Ketha', 22, 'ramya@example.com');
```

**Expected MySQL Error:**
```text
ERROR 1364 (HY000): Field 'first_name' doesn't have a default value
```

---

### Question 9: Create a table with a Composite Primary Key using `patient_id` and `doctor_id`.

```sql
CREATE TABLE patient_doctor_assignments (
    patient_id INT,
    doctor_id INT,
    assigned_date DATE,
    PRIMARY KEY (patient_id, doctor_id)
);
```

---

### Question 10: What happens if you try to delete a doctor who has existing appointments (without CASCADE)? (Write the DELETE query that would fail).

**Explanation:**  
When a foreign key is created without `ON DELETE CASCADE` (using default `RESTRICT` or `NO ACTION`), MySQL prevents the deletion of a parent record in `doctors` if matching child records exist in `appointments`. This maintains referential integrity and prevents orphaned records.

```sql
-- Query attempting to delete a doctor who has existing linked appointments:
DELETE FROM doctors WHERE doctor_id = 1;
```

**Expected MySQL Error:**
```text
ERROR 1451 (23000): Cannot delete or update a parent row: a foreign key constraint fails
```

---

## Proof of Work

![Execution Screenshot](./images/k_ramya_constraints.png)

---

## Conclusion
In this assignment, all fundamental SQL constraints (`NOT NULL`, `UNIQUE`, `DEFAULT`, `CHECK`, `PRIMARY KEY`, `COMPOSITE PRIMARY KEY`, `FOREIGN KEY`, `ON DELETE CASCADE`, and referential integrity violations) were defined, executed, tested, and verified in MySQL.
