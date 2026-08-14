# Assignment 5: Constraints & Referential Integrity

**Student Name:** M. Ramya  
**Course:** Database Management Systems (DBMS)  
**Topic:** Unit 2 Part 4 - SQL Constraints & Referential Integrity  

---

## 📌 Introduction to SQL Constraints

**SQL Constraints** are rules enforced on database columns to restrict the type of data that can be inserted, updated, or manipulated in a table. They guarantee **data integrity**, **accuracy**, and **reliability**, preventing illegal or corrupted data from entering database tables.

### Key Types of SQL Constraints:
- **`NOT NULL`**: Ensures a column cannot contain `NULL` (empty) values.
- **`UNIQUE`**: Guarantees all values in a column are distinct and unique.
- **`DEFAULT`**: Automatically assigns a default value when no value is specified during `INSERT`.
- **`CHECK`**: Enforces specific logical conditions on column values (e.g., `age >= 0`).
- **`PRIMARY KEY`**: Uniquely identifies each record in a table (`NOT NULL` + `UNIQUE`).
- **`FOREIGN KEY`**: Enforces referential integrity between child and parent tables, with optional cascading rules (`ON DELETE CASCADE`).

---

## 🛠️ Assignment Questions & SQL Solutions

### Question 1: Create a table named `patients` with a primary key `patient_id` and a `NOT NULL` constraint on `first_name`.

**SQL Query:**
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

**SQL Query:**
```sql
ALTER TABLE patients
ADD CONSTRAINT unique_patient_email UNIQUE (email);
```

---

### Question 3: Create a table `appointments` with a `DEFAULT` constraint setting the `status` to 'Scheduled'.

**SQL Query:**
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

**SQL Query:**
```sql
ALTER TABLE patients
ADD CONSTRAINT chk_patient_age CHECK (age >= 0);
```

---

### Question 5: Create a table `doctors` with a primary key `doctor_id`. Then add a `FOREIGN KEY` in `appointments` that references `doctor_id` in `doctors`.

**SQL Query:**
```sql
-- Step 1: Create doctors table
CREATE TABLE doctors (
    doctor_id INT PRIMARY KEY,
    doctor_name VARCHAR(100) NOT NULL,
    specialization VARCHAR(50)
);

-- Step 2: Add Foreign Key constraint in appointments referencing doctors
ALTER TABLE appointments
ADD CONSTRAINT fk_doctor
FOREIGN KEY (doctor_id) REFERENCES doctors(doctor_id);
```

---

### Question 6: Write a query to drop the `FOREIGN KEY` constraint from the `appointments` table.

**SQL Query:**
```sql
ALTER TABLE appointments
DROP FOREIGN KEY fk_doctor;
```

---

### Question 7: Re-add the `FOREIGN KEY` constraint to `appointments` with `ON DELETE CASCADE`.

**SQL Query:**
```sql
ALTER TABLE appointments
ADD CONSTRAINT fk_doctor
FOREIGN KEY (doctor_id) REFERENCES doctors(doctor_id) ON DELETE CASCADE;
```

---

### Question 8: Attempt to insert a patient without a `first_name`. (Write the query that would cause this error).

**SQL Query:**
```sql
-- This query fails with ER_BAD_NULL_ERROR because first_name has a NOT NULL constraint
INSERT INTO patients (patient_id, last_name, age, email)
VALUES (101, 'Sharma', 30, 'sharma@example.com');
```

---

### Question 9: Create a table with a Composite Primary Key using `patient_id` and `doctor_id`.

**SQL Query:**
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

**SQL Query & Explanation:**
```sql
-- Query attempting to delete a doctor with linked appointments (when FK is set to RESTRICT/NO ACTION):
DELETE FROM doctors WHERE doctor_id = 1;

-- Explanation: MySQL rejects the DELETE statement and returns an error:
-- ERROR 1451 (23000): Cannot delete or update a parent row: a foreign key constraint fails (`appointments`, CONSTRAINT `fk_doctor` FOREIGN KEY (`doctor_id`) REFERENCES `doctors` (`doctor_id`))
```

---

## 📷 Proof of Work

Below is the verified MySQL terminal execution screenshot demonstrating all constraint creation, modification, and error enforcement queries:

![Execution Screenshot](./images/m_ramya_constraints.png)

---

## ✅ Conclusion
In this assignment, all fundamental SQL constraints (`NOT NULL`, `UNIQUE`, `DEFAULT`, `CHECK`, `PRIMARY KEY`, `COMPOSITE KEY`, `FOREIGN KEY`, `ON DELETE CASCADE`, and FK constraint violation handlings) were written, executed, verified, and documented.
