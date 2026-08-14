# Assignment 7: Grouping and Ordering Data

**Student Name:** Reena

Please write the SQL queries for the following questions below each question.

### Questions:

**1. Write a query to sort the `students` table by `last_name` in descending order.**
```sql
SELECT * FROM students 
ORDER BY last_name DESC;
```

**2. Write a query to sort `courses` by `credits` in descending order, and then by `course_name` in ascending order.**
```sql
SELECT * FROM courses 
ORDER BY credits DESC, course_name ASC;
```

**3. Write a query to count the total number of students in each `dept_id` using `GROUP BY`.**
```sql
SELECT dept_id, COUNT(*) AS total_students 
FROM students 
GROUP BY dept_id;
```

**4. Write a query to find the maximum `score` for each `course_id` from the `marks` table.**
```sql
SELECT course_id, MAX(score) AS max_score 
FROM marks 
GROUP BY course_id;
```

**5. Write a query to find the average `experience_years` per `dept_id` in the `faculty` table.**
```sql
SELECT dept_id, AVG(experience_years) AS avg_experience 
FROM faculty 
GROUP BY dept_id;
```

**6. Write a query to group the `students` table by `gender` and count how many students are in each group, but only for those born after '2000-01-01' (Use `WHERE`).**
```sql
SELECT gender, COUNT(*) AS student_count 
FROM students 
WHERE dob > '2000-01-01' 
GROUP BY gender;
```

**7. Write a query to find `dept_id`s that have more than 10 students. (Use `HAVING`).**
```sql
SELECT dept_id, COUNT(*) AS total_students 
FROM students 
GROUP BY dept_id 
HAVING COUNT(*) > 10;
```

**8. Write a query to find `course_id`s where the average score is greater than 80.**
```sql
SELECT course_id, AVG(score) AS avg_score 
FROM marks 
GROUP BY course_id 
HAVING AVG(score) > 80;
```

**9. Write a query that groups `marks` by `dept_id`, calculates the sum of `score`, and sorts the result by the sum of `score` in descending order.**
```sql
SELECT dept_id, SUM(score) AS total_score 
FROM marks 
GROUP BY dept_id 
ORDER BY total_score DESC;
```

**10. Write a query that finds the total credits offered by each `faculty_id`, but only include courses with `credits > 2`, and only show `faculty_id`s whose total credits exceed 10.**
```sql
SELECT faculty_id, SUM(credits) AS total_credits 
FROM courses 
WHERE credits > 2 
GROUP BY faculty_id 
HAVING SUM(credits) > 10;
```

---

### Proof of Work

![Execution Screenshot](./images/reena_grouping_ordering.png)

