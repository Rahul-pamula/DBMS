# Assignment 9: Set Operations and Subqueries

**Student Name:** Roshini

**Set Operations** (`UNION`, `UNION ALL`, `INTERSECT`, `EXCEPT`) allow combining result sets vertically, while **Subqueries** (nested queries inside `SELECT`, `FROM`, `WHERE`, or `HAVING`) allow using the result of one query as an input condition for another query.

---

### Questions & SQL Solutions

**1. Write a query using `UNION` to combine the `dept_id` from the `departments` table and `dept_id` from the `students` table.**
```sql
SELECT dept_id FROM departments
UNION
SELECT dept_id FROM students;
```
*Explanation:* Combines the `dept_id` values from both `departments` and `students` tables vertically into a single column, removing all duplicate values from the final result.

---

**2. Write a query using `UNION ALL` for the same operation as question 1. Write a short comment explaining the difference.**
```sql
SELECT dept_id FROM departments
UNION ALL
SELECT dept_id FROM students;

-- Difference: 
-- 1. UNION combines results and performs a distinct sort to eliminate duplicate rows.
-- 2. UNION ALL combines results while preserving all duplicate rows, making it significantly faster.
```
*Explanation:* Combines `dept_id` entries from both tables while retaining duplicate entries and `NULL` values.

---

**3. Write a single-row subquery to find the `first_name` of the student with the lowest `marks`.**
```sql
SELECT first_name, marks 
FROM students 
WHERE marks = (SELECT MIN(marks) FROM students);
```
*Explanation:* The inner subquery `(SELECT MIN(marks) FROM students)` returns a single scalar value representing the minimum score, which the outer query matches against `marks`.

---

**4. Write a multi-row subquery using `IN` to find the `first_name` of students who are in the 'Mechanical' or 'Civil' departments.**
```sql
SELECT first_name 
FROM students 
WHERE dept_id IN (
    SELECT dept_id 
    FROM departments 
    WHERE dept_name IN ('Mechanical', 'Civil')
);
```
*Explanation:* The inner subquery returns a list (set) of department IDs matching 'Mechanical' or 'Civil', and the outer query uses `IN` to match students belonging to those departments.

---

**5. Write a query using a subquery to find students whose marks are greater than the average marks of all students.**
```sql
SELECT first_name, last_name, marks 
FROM students 
WHERE marks > (SELECT AVG(marks) FROM students);
```
*Explanation:* Computes the overall class average using the inner subquery `(SELECT AVG(marks) FROM students)` and filters for students scoring strictly above this average.

---

**6. Write a query to simulate `INTERSECT` using `INNER JOIN` or `IN` to find `dept_id`s present in both `departments` and `students` tables.**
```sql
SELECT DISTINCT dept_id 
FROM departments 
WHERE dept_id IN (
    SELECT dept_id 
    FROM students 
    WHERE dept_id IS NOT NULL
);

-- Alternative using INNER JOIN:
-- SELECT DISTINCT d.dept_id 
-- FROM departments d 
-- INNER JOIN students s ON d.dept_id = s.dept_id;
```
*Explanation:* Returns department IDs that exist in both `departments` and `students` tables, simulating the `INTERSECT` set operator in DBMS engines like MySQL.

---

**7. Write a query to simulate `EXCEPT` using `NOT IN` to find `dept_id`s in `departments` that are not assigned to any student.**
```sql
SELECT dept_id, dept_name 
FROM departments 
WHERE dept_id NOT IN (
    SELECT dept_id 
    FROM students 
    WHERE dept_id IS NOT NULL
);
```
*Explanation:* Simulates the `EXCEPT` / `MINUS` operator by finding department IDs present in the `departments` table that do not exist in the `students` table.

---

**8. Write a subquery inside the `SELECT` clause to display each student's `first_name`, their `marks`, and the overall average marks of the class.**
```sql
SELECT first_name, marks, 
       (SELECT AVG(marks) FROM students) AS overall_avg_marks 
FROM students;
```
*Explanation:* Places an independent subquery directly inside the `SELECT` projection list, appending the calculated overall average marks column alongside each individual student record.

---

**9. Write a query using an `EXISTS` subquery to list `dept_name`s that have at least one student.**
```sql
SELECT d.dept_name 
FROM departments d 
WHERE EXISTS (
    SELECT 1 
    FROM students s 
    WHERE s.dept_id = d.dept_id
);
```
*Explanation:* Uses a correlated subquery with `EXISTS` to check for the existence of at least one student record matching each department ID, short-circuiting as soon as a match is found.

---

**10. Write a query using a subquery to find the second highest marks in the `students` table.**
```sql
SELECT MAX(marks) AS second_highest_marks 
FROM students 
WHERE marks < (SELECT MAX(marks) FROM students);
```
*Explanation:* The subquery `(SELECT MAX(marks) FROM students)` returns the highest score. The outer query finds the maximum score strictly less than that highest score, which yields the 2nd highest mark.

---

### Proof of Work
*(Replace the image link below with your actual screenshot from the `images` folder)*

![Set Ops Execution Screenshot](./images/roshini_set_ops_subqueries.png)

---

## Conclusion
- **Set Operations (`UNION`, `UNION ALL`)**: Combine rows vertically across queries. `UNION` removes duplicate rows, whereas `UNION ALL` retains all rows.
- **Subqueries**: Allow nesting queries to perform multi-stage filtering:
  - **Single-row subqueries**: Return one value (e.g. `MIN`, `MAX`, `AVG`).
  - **Multi-row subqueries**: Return multiple values using operators like `IN`.
  - **Correlated subqueries (`EXISTS`)**: Evaluate row-by-row against the outer query.
