# Assignment 6: SQL Built-in & Aggregate Functions

**Student Name:** Yamini Vatturi  
**Course:** Database Management Systems (DBMS)  
**Topic:** Unit 2 Part 5 - Built-in & Aggregate Functions in SQL  

---

## 📌 Introduction to SQL Functions

**SQL Built-in Functions** are predefined formulas in SQL that operate on data to perform calculations, format text, and manipulate dates directly inside the database engine.

### Classification of Functions:
1. **Aggregate Functions:** Summarize multiple rows of a column into a single output value (`COUNT`, `SUM`, `AVG`, `MAX`, `MIN`).
2. **Scalar Functions:** Process individual data values to return a single output:
   - **Numeric Functions:** Mathematical operations (`ROUND`, `MOD`, `POWER`, `ABS`, `CEIL`, `FLOOR`).
   - **String Functions:** Text manipulation (`UPPER`, `LOWER`, `LENGTH`, `CONCAT`, `SUBSTRING`, `REPLACE`, `TRIM`).
   - **Date & Time Functions:** Temporal operations (`NOW`, `CURRENT_DATE`, `DATEDIFF`, `DATE_ADD`, `MONTH`, `YEAR`).

---

## 🛠️ Assignment Questions & SQL Solutions

### Question 1: Write a query using `COUNT()` to find the total number of students and the number of unique departments in the `students` table.

**SQL Query:**
```sql
SELECT 
    COUNT(*) AS total_students,
    COUNT(DISTINCT dept_id) AS unique_departments
FROM students;
```

---

### Question 2: Write a query using `SUM()` and `AVG()` to calculate the total credits offered across all courses and the average score of all students rounded to 2 decimal places.

**SQL Query:**
```sql
SELECT 
    SUM(credits) AS total_credits,
    ROUND(AVG(score), 2) AS average_score
FROM marks;
```

---

### Question 3: Write a query using `MAX()` and `MIN()` to find the highest score, the lowest score, the oldest student's date of birth, and the youngest student's date of birth.

**SQL Query:**
```sql
SELECT 
    MAX(score) AS highest_score,
    MIN(score) AS lowest_score,
    MIN(dob) AS oldest_student_dob,
    MAX(dob) AS youngest_student_dob
FROM marks m
JOIN students s ON m.student_id = s.student_id;
```

---

### Question 4: Demonstrate `ROUND()`, `ABS()`, and `MOD()` functions by rounding `-4.56` to 1 decimal place, taking the absolute value of `-15`, and finding the remainder of `10` divided by `3`.

**SQL Query:**
```sql
SELECT 
    ROUND(-4.56, 1) AS rounded_value,
    ABS(-15) AS absolute_value,
    MOD(10, 3) AS remainder_value;
```

---

### Question 5: Write a query using `CEIL()` and `FLOOR()` to calculate the minimum number of 50-seater buses required for 225 students and to extract the completed full years of experience from `10.9`.

**SQL Query:**
```sql
SELECT 
    CEIL(225 / 50.0) AS buses_required,
    FLOOR(10.9) AS completed_years;
```

---

### Question 6: Write a query using `UPPER()` and `LOWER()` to display student first names in uppercase and faculty emails in lowercase.

**SQL Query:**
```sql
SELECT 
    UPPER(first_name) AS upper_first_name,
    LOWER(email) AS lower_email
FROM students s
LEFT JOIN faculty f ON s.dept_id = f.dept_id;
```

---

### Question 7: Write a query using `CONCAT()` to combine `first_name` and `last_name` into a single column `full_name`, and auto-generate an official university email ID formatted as `firstname.lastname@univ.edu`.

**SQL Query:**
```sql
SELECT 
    CONCAT(first_name, ' ', last_name) AS full_name,
    LOWER(CONCAT(first_name, '.', last_name, '@univ.edu')) AS official_email
FROM students;
```

---

### Question 8: Write a query using `LENGTH()` and `SUBSTRING()` to find students whose phone number length is less than 10 characters and extract the first 3 letters of each department name.

**SQL Query:**
```sql
-- Find invalid phone numbers
SELECT student_id, first_name, phone_number 
FROM students 
WHERE LENGTH(phone_number) < 10;

-- Extract department name initials
SELECT dept_name, SUBSTRING(dept_name, 1, 3) AS dept_code 
FROM departments;
```

---

### Question 9: Write a query using `REPLACE()` and `TRIM()` to replace `@olduniv.edu` with `@newuniv.edu` in email addresses and remove leading/trailing whitespace from student names.

**SQL Query:**
```sql
SELECT 
    TRIM(first_name) AS cleaned_first_name,
    REPLACE(email, '@olduniv.edu', '@newuniv.edu') AS updated_email
FROM faculty;
```

---

### Question 10: Write a query using Date functions (`CURRENT_DATE()`, `DATEDIFF()`, `DATE_ADD()`, `YEAR()`) to calculate the age of each student in days, their expected graduation date (4 years from enrollment), and extract their birth year.

**SQL Query:**
```sql
SELECT 
    student_id,
    first_name,
    YEAR(dob) AS birth_year,
    DATEDIFF(CURRENT_DATE(), dob) AS age_in_days,
    DATE_ADD(enrollment_date, INTERVAL 4 YEAR) AS expected_graduation
FROM students s
JOIN enrollments e ON s.student_id = e.student_id;
```

---

## 📷 Screenshot Proof of Work

Below is the execution screenshot demonstrating successful query runs in MySQL terminal:

![Execution Screenshot](./images/yamini_functions.png)

---

## ✅ Conclusion
In this assignment, all 10 SQL function queries covering Aggregate Functions (`COUNT`, `SUM`, `AVG`, `MAX`, `MIN`), Numeric Functions (`ROUND`, `ABS`, `MOD`, `CEIL`, `FLOOR`), String Functions (`UPPER`, `LOWER`, `CONCAT`, `LENGTH`, `SUBSTRING`, `REPLACE`, `TRIM`), and Date/Time Functions (`CURRENT_DATE`, `DATEDIFF`, `DATE_ADD`, `YEAR`) were successfully written, executed, and verified.
