# Assignment 8: SQL Joins

**Student Name:** Roshini

**SQL Joins** are used to combine rows from two or more tables based on a related column between them (typically a Primary Key - Foreign Key relationship). Joins enable querying normalized relational database tables efficiently.

---

### Questions & SQL Solutions

**1. Write a query to perform an `INNER JOIN` between the `students` and `departments` tables to get the `first_name` and `dept_name` for all students.**
```sql
SELECT s.first_name, d.dept_name 
FROM students s
INNER JOIN departments d ON s.dept_id = d.dept_id;
```
*Explanation:* Returns only the records where there is a matching `dept_id` present in both `students` and `departments` tables.

---

**2. Write a query using a `LEFT JOIN` to list all departments and any students in them. If a department has no students, the student columns should be NULL.**
```sql
SELECT d.dept_name, s.first_name, s.last_name 
FROM departments d
LEFT JOIN students s ON d.dept_id = s.dept_id;
```
*Explanation:* Lists all departments from the left table (`departments`). If a department does not have any enrolled students, the student columns (`first_name`, `last_name`) will display `NULL`.

---

**3. Write a query using a `RIGHT JOIN` to list all students and their department names. If a student is not assigned to a department, the department name should be NULL.**
```sql
SELECT s.first_name, s.last_name, d.dept_name 
FROM departments d
RIGHT JOIN students s ON d.dept_id = s.dept_id;
```
*Explanation:* Returns all student records from the right table (`students`). If a student is not assigned to any department, the `dept_name` column will display `NULL`.

---

**4. Write a query to find students who do not belong to any department using a `LEFT JOIN` or `RIGHT JOIN`.**
```sql
SELECT s.student_id, s.first_name, s.last_name 
FROM students s
LEFT JOIN departments d ON s.dept_id = d.dept_id
WHERE d.dept_id IS NULL;
```
*Explanation:* Performs a `LEFT JOIN` from `students` to `departments` and filters rows where `d.dept_id IS NULL`, identifying orphan student records that lack a valid department association.

---

**5. Perform a `CROSS JOIN` between `students` and `departments`. How many rows are returned if there are 8 students and 3 departments? (Write the query and the answer as a comment).**
```sql
SELECT s.first_name, d.dept_name 
FROM students s
CROSS JOIN departments d;

-- Answer: 24 rows are returned.
-- A CROSS JOIN generates a Cartesian Product where each row from the first table is paired with every row from the second table (8 students * 3 departments = 24 rows).
```

---

**6. Write a query using an `INNER JOIN` to find the average marks of students in the 'Computer Science' department.**
```sql
SELECT d.dept_name, AVG(s.marks) AS avg_marks 
FROM students s
INNER JOIN departments d ON s.dept_id = d.dept_id
WHERE d.dept_name = 'Computer Science'
GROUP BY d.dept_name;

-- Alternative if marks are stored in a separate 'marks' table:
-- SELECT d.dept_name, AVG(m.score) AS avg_marks
-- FROM students s
-- INNER JOIN departments d ON s.dept_id = d.dept_id
-- INNER JOIN marks m ON s.student_id = m.student_id
-- WHERE d.dept_name = 'Computer Science'
-- GROUP BY d.dept_name;
```
*Explanation:* Joins `students` and `departments`, filters for the `'Computer Science'` department using `WHERE`, and computes the average score using `AVG()`.

---

**7. Write a query to join `students` and `departments`, but only show students whose `marks` are greater than 80.**
```sql
SELECT s.first_name, s.last_name, s.marks, d.dept_name 
FROM students s
INNER JOIN departments d ON s.dept_id = d.dept_id
WHERE s.marks > 80;

-- Alternative if marks are stored in a separate 'marks' table:
-- SELECT s.first_name, s.last_name, m.score AS marks, d.dept_name
-- FROM students s
-- INNER JOIN departments d ON s.dept_id = d.dept_id
-- INNER JOIN marks m ON s.student_id = m.student_id
-- WHERE m.score > 80;
```
*Explanation:* Joins `students` and `departments` on `dept_id` and uses `WHERE s.marks > 80` to filter only high-scoring students.

---

**8. Write a query using a `SELF JOIN` on the `students` table to find pairs of students who are in the same department (excluding pairing a student with themselves).**
```sql
SELECT s1.first_name AS student_1, s2.first_name AS student_2, s1.dept_id 
FROM students s1
INNER JOIN students s2 ON s1.dept_id = s2.dept_id AND s1.student_id != s2.student_id;
```
*Explanation:* Uses two table aliases (`s1` and `s2`) for `students` to join the table with itself on matching `dept_id` while ensuring `s1.student_id != s2.student_id` so no student is paired with themselves.

---

**9. Write a query using `INNER JOIN` to list only those departments that have more than 2 students.**
```sql
SELECT d.dept_id, d.dept_name, COUNT(s.student_id) AS total_students 
FROM departments d
INNER JOIN students s ON d.dept_id = s.dept_id
GROUP BY d.dept_id, d.dept_name
HAVING COUNT(s.student_id) > 2;
```
*Explanation:* Joins `departments` and `students`, groups the results by department using `GROUP BY`, and filters groups having more than 2 students using `HAVING COUNT(s.student_id) > 2`.

---

**10. Write a query to perform a `FULL OUTER JOIN` between `students` and `departments`. If MySQL doesn't support it, write the equivalent query using `UNION`.**
```sql
-- MySQL does not natively support FULL OUTER JOIN syntax.
-- Equivalent query using LEFT JOIN, RIGHT JOIN, and UNION:

SELECT s.first_name, d.dept_name 
FROM students s
LEFT JOIN departments d ON s.dept_id = d.dept_id

UNION

SELECT s.first_name, d.dept_name 
FROM students s
RIGHT JOIN departments d ON s.dept_id = d.dept_id;
```
*Explanation:* Combines a `LEFT JOIN` (all students with their departments) and a `RIGHT JOIN` (all departments with their students) using `UNION` to remove duplicates and simulate a `FULL OUTER JOIN`.

---

### Proof of Work
*(Replace the image link below with your actual screenshot from the `images` folder)*

![Joins Execution Screenshot](./images/roshini_joins.png)

---

## Conclusion
SQL Joins are fundamental operations for relational data analysis:
- **`INNER JOIN`**: Returns matching records from both tables.
- **`LEFT JOIN`**: Returns all records from the left table and matched records from the right.
- **`RIGHT JOIN`**: Returns all records from the right table and matched records from the left.
- **`FULL OUTER JOIN`**: Returns all records from both tables (simulated in MySQL using `UNION`).
- **`CROSS JOIN`**: Produces a Cartesian Product of both tables.
- **`SELF JOIN`**: Joins a table with itself to compare rows within the same dataset.
