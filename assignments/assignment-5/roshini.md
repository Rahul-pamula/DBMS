# Assignment 5: SQL Constraints & Referential Integrity

**SQL Constraints** are rules enforced on data columns in a database table to ensure the accuracy, reliability, and integrity of data stored within the database. Constraints prevent invalid data entry and maintain logical relationships between tables.

---

## SQL Questions & Query Solutions

### Question 1: Create Table with NOT NULL Constraint
*Scenario:* Create a table named `patients` with a primary key `patient_id` and a `NOT NULL` constraint on `first_name`.

```sql
CREATE TABLE patients (
    patient_id INT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50),
    email VARCHAR(100),
    age INT
);
```

---

### Question 2: Add UNIQUE Constraint to Existing Column
*Scenario:* Add a `UNIQUE` constraint to the `email` column in the `patients` table.

```sql
ALTER TABLE patients 
ADD CONSTRAINT unique_email UNIQUE (email);
```

---

### Question 3: Create Table with DEFAULT Constraint
*Scenario:* Create a table `appointments` with a `DEFAULT` constraint setting the status to `'Scheduled'`.

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

### Question 4: Add CHECK Constraint to Table
*Scenario:* Add a `CHECK` constraint to the `patients` table to ensure `age` is greater than or equal to 0.

```sql
ALTER TABLE patients 
ADD CONSTRAINT chk_patient_age CHECK (age >= 0);
```

---

### Question 5: Create Foreign Key Reference
*Scenario:* Create a table `doctors` with a primary key `doctor_id`. Then add a `FOREIGN KEY` in `appointments` that references `doctor_id` in `doctors`.

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

### Question 6: Drop Foreign Key Constraint
*Scenario:* Write a query to drop the `FOREIGN KEY` constraint from the `appointments` table.

```sql
ALTER TABLE appointments 
DROP FOREIGN KEY fk_appointments_doctor;
```

---

### Question 7: Re-add Foreign Key with ON DELETE CASCADE
*Scenario:* Re-add the `FOREIGN KEY` constraint to `appointments` with `ON DELETE CASCADE`.

```sql
ALTER TABLE appointments 
ADD CONSTRAINT fk_appointments_doctor 
FOREIGN KEY (doctor_id) REFERENCES doctors(doctor_id) 
ON DELETE CASCADE;
```

---

### Question 8: Attempting Invalid Insert (NOT NULL Violation)
*Scenario:* Attempt to insert a patient without a `first_name`. (Write the query that would cause this error).

```sql
-- Query that fails due to missing NOT NULL column 'first_name':
INSERT INTO patients (patient_id, last_name, email, age) 
VALUES (101, 'Doe', 'john.doe@example.com', 30);
```

*Expected Error Output:*
```text
ERROR 1048 (23000): Column 'first_name' cannot be null
```

---

### Question 9: Create Table with Composite Primary Key
*Scenario:* Create a table with a Composite Primary Key using `patient_id` and `doctor_id`.

```sql
CREATE TABLE patient_doctor_assignments (
    patient_id INT,
    doctor_id INT,
    assigned_date DATE,
    PRIMARY KEY (patient_id, doctor_id),
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id),
    FOREIGN KEY (doctor_id) REFERENCES doctors(doctor_id)
);
```

---

### Question 10: Deleting Parent Record with Dependent Child Records (Without CASCADE)
*Scenario:* What happens if you try to delete a doctor who has existing appointments (without CASCADE)? (Write the DELETE query that would fail).

*Explanation:* 
When a parent record in `doctors` is referenced by child records in `appointments` without `ON DELETE CASCADE` enabled (i.e., default `RESTRICT` / `NO ACTION`), the DBMS blocks the operation to preserve referential integrity and prevent orphaned records.

```sql
-- Query that fails because dependent appointment records reference doctor_id = 1:
DELETE FROM doctors WHERE doctor_id = 1;
```

*Expected Error Output:*
```text
ERROR 1451 (23000): Cannot delete or update a parent row: a foreign key constraint fails
```

---

## Proof of Work

![Constraints Execution Screenshot](./images/roshini_constraints.png)

---

## Conclusion
SQL constraints (`NOT NULL`, `UNIQUE`, `DEFAULT`, `CHECK`, `PRIMARY KEY`, `FOREIGN KEY`, and Composite Primary Keys) enforce data integrity, validate business logic, and maintain referential integrity across related tables in a database.
