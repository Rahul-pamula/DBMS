# Assignment 7: Grouping and Ordering Data
**Student Name:** Roshini

**Grouping and Ordering Data** in SQL allows us to organize, aggregate, and structure query results efficiently. The `ORDER BY` clause sorts data in ascending or descending order, `GROUP BY` aggregates rows sharing common values, `WHERE` filters raw records before grouping, and `HAVING` filters aggregated groups after calculation.

---

## SQL Assignment Questions & Solutions

### Question 1: Sort Students by Last Name Descending
*Scenario:* Write a query to sort the `students` table by `last_name` in descending order.

```sql
SELECT * 
FROM students 
ORDER BY last_name DESC;
```

*Explanation:* The `ORDER BY last_name DESC` clause sorts the student records alphabetically by `last_name` in descending (Z to A) order.

---

### Question 2: Sort Courses by Credits (DESC) and Course Name (ASC)
*Scenario:* Write a query to sort `courses` by `credits` in descending order, and then by `course_name` in ascending order.

```sql
SELECT * 
FROM courses 
ORDER BY credits DESC, course_name ASC;
```

*Explanation:* Multi-column sorting first orders courses by `credits` from highest to lowest. If two or more courses have the same number of credits, it resolves ties by sorting `course_name` alphabetically (A to Z).

---

### Question 3: Count Students in Each Department
*Scenario:* Write a query to count the total number of students in each `dept_id` using `GROUP BY`.

```sql
SELECT dept_id, COUNT(*) AS total_students 
FROM students 
GROUP BY dept_id;
```

*Explanation:* `GROUP BY dept_id` collects rows with matching department IDs into separate groups, and `COUNT(*)` counts the number of student records inside each department group.

---

### Question 4: Maximum Score per Course
*Scenario:* Write a query to find the maximum score for each `course_id` from the `marks` table.

```sql
SELECT course_id, MAX(score) AS max_score 
FROM marks 
GROUP BY course_id;
```

*Explanation:* Groups mark records by `course_id` and calculates the highest score achieved in each course using the `MAX()` aggregate function.

---

### Question 5: Average Faculty Experience per Department
*Scenario:* Write a query to find the average `experience_years` per `dept_id` in the `faculty` table.

```sql
SELECT dept_id, AVG(experience_years) AS avg_experience 
FROM faculty 
GROUP BY dept_id;
```

*Explanation:* Groups faculty members by department (`dept_id`) and computes the average teaching experience using `AVG(experience_years)`.

---

### Question 6: Group Students by Gender with WHERE Filter
*Scenario:* Write a query to group the `students` table by gender and count how many students are in each group, but only for those born after '2000-01-01' (Use `WHERE`).

```sql
SELECT gender, COUNT(*) AS total_students 
FROM students 
WHERE dob > '2000-01-01' 
GROUP BY gender;
```

*Explanation:* The `WHERE dob > '2000-01-01'` clause filters out students born on or before Jan 1, 2000 *before* grouping. `GROUP BY gender` then counts the remaining male and female students separately.

---

### Question 7: Departments with More Than 10 Students (HAVING)
*Scenario:* Write a query to find `dept_ids` that have more than 10 students. (Use `HAVING`).

```sql
SELECT dept_id, COUNT(*) AS total_students 
FROM students 
GROUP BY dept_id 
HAVING COUNT(*) > 10;
```

*Explanation:* The `HAVING COUNT(*) > 10` clause filters the aggregated groups *after* `GROUP BY dept_id` is executed, excluding departments with 10 or fewer students.

---

### Question 8: Courses with Average Score Greater Than 80
*Scenario:* Write a query to find `course_ids` where the average score is greater than 80.

```sql
SELECT course_id, AVG(score) AS avg_score 
FROM marks 
GROUP BY course_id 
HAVING AVG(score) > 80;
```

*Explanation:* Groups test scores by `course_id`, calculates the average score for each course, and uses `HAVING AVG(score) > 80` to keep only high-performing courses.

---

### Question 9: Total Score per Department Sorted Descending
*Scenario:* Write a query that groups marks by `dept_id`, calculates the sum of score, and sorts the result by the sum of score in descending order.

```sql
SELECT dept_id, SUM(score) AS total_score 
FROM marks 
GROUP BY dept_id 
ORDER BY total_score DESC;
```

*Explanation:* `GROUP BY dept_id` aggregates score records by department, `SUM(score)` computes total department points, and `ORDER BY total_score DESC` sorts departments from highest total score to lowest.

---

### Question 10: Total Faculty Credits with WHERE and HAVING Filters
*Scenario:* Write a query that finds the total credits offered by each `faculty_id`, but only include courses with `credits > 2`, and only show `faculty_ids` whose total credits exceed 10.

```sql
SELECT faculty_id, SUM(credits) AS total_credits 
FROM courses 
WHERE credits > 2 
GROUP BY faculty_id 
HAVING SUM(credits) > 10;
```

*Explanation:* 
1. `WHERE credits > 2`: Filters out minor courses before grouping.
2. `GROUP BY faculty_id`: Buckets remaining qualifying courses by faculty member.
3. `HAVING SUM(credits) > 10`: Filters the summary groups, displaying only faculty members teaching more than 10 total credits.

---

## Proof of Work

![Grouping and Ordering Execution Screenshot](./images/roshini_grouping_ordering.png)

---

## Conclusion
Understanding SQL's `ORDER BY`, `GROUP BY`, `WHERE`, and `HAVING` clauses provides the foundation for data aggregation and analysis:
- **`WHERE` vs `HAVING`:** `WHERE` filters individual records *before* aggregation, whereas `HAVING` filters aggregated groups *after* `GROUP BY`.
- **Execution Order:** `FROM` → `WHERE` → `GROUP BY` → `HAVING` → `SELECT` → `ORDER BY`.
