# Unit 2 Part 8: Set Operators and Subqueries

Welcome to Part 8! Up until now, we have been combining tables horizontally using JOINS. But what if you want to combine tables vertically? What if you want to use the result of one query as the filter for another query?

In this unit, we will explore **Set Operators** (combining results vertically) and **Subqueries** (queries inside queries).

---

# 🎯 Today's Goal

Before writing SQL, we are going to understand the ideas using simple real-world examples right from our classroom data.

We will apply these ideas to our:
- `students` table
- `departments` table

By the end, you should be able to understand:

```text
SET OPERATORS
    ↓
UNION
UNION ALL
INTERSECT
EXCEPT

SUBQUERIES
    ↓
Main Query
Subquery
IN with Subquery
```

---

# 🗄️ PART 0 — CREATE OUR TABLES FIRST

Before performing any Set Operators or Subqueries, let's create our database tables and insert our data.

We will use these three departments:
- `Piet`
- `PIT`
- `PIN`

## 1. Create the `departments` table
```sql
CREATE TABLE departments (
    dept_id INT PRIMARY KEY,
    dept_name VARCHAR(50) NOT NULL
);
```

## 2. Create the `students` table
```sql
CREATE TABLE students (
    student_id INT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    dept_id INT,
    marks INT,
    FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
);
```

## 3. Insert the departments
```sql
INSERT INTO departments (dept_id, dept_name)
VALUES
(101, 'Piet'),
(102, 'PIT'),
(103, 'PIN');
```

## 4. Insert the students
```sql
INSERT INTO students (student_id, first_name, dept_id, marks)
VALUES
(1, 'Rahul', 101, 85),
(2, 'Roshini', 102, 92),
(3, 'Yamini', 101, 70),
(4, 'k_Ramya', 103, 88),
(5, 'Reena', 102, 60),
(6, 'm_Ramya', 101, 95),
(7, 'Vaibhav', 102, 78),
(8, 'Vishal', 103, 90);
```

> **Important:** Run the `CREATE TABLE` statements first, then the `INSERT` statements.

---

# PART 1 — SET OPERATORS

## 🧠 First, What Is a Set?

Don't worry about the mathematical definition. For today, think of a **set as a group or collection of things**.

Let's create two groups of students from our class.

### 🔵 Group A: Students in Dept 'Piet' (Dept 101)
```text
Rahul
Yamini
m_Ramya
```

### 🟢 Group B: High Achievers (Marks >= 90)
```text
Roshini
m_Ramya
Vishal
```

Notice something?
Some students are in **both** groups!
```text
m_Ramya
```

Some students are only in Group A:
```text
Rahul
Yamini
```

Some students are only in Group B:
```text
Roshini
Vishal
```

Now we can ask different questions to the class.

---

# 🎮 Interactive Question 1

Ask the students:

> "If I want a list of EVERY student who is EITHER in Dept 101 OR a High Achiever, what should I do?"

Let them answer.

Expected answer:
```text
Rahul
Yamini
m_Ramya
Roshini
Vishal
```

We combined the two groups together.
This is the idea behind:

# UNION

---

# 1. UNION

## 🧠 Simple Meaning
> **UNION combines the results of two queries and removes duplicates.**

Think:
```text
Group A
   +
Group B
   ↓
Everyone (without duplicates)
```

Notice that `m_Ramya` was in both groups, but in the final list, she only appears **once**.

## 💻 SQL Example

In SQL, we can combine two completely separate queries into one list.

```sql
-- Query 1: Students in Dept 101
SELECT first_name FROM students WHERE dept_id = 101

UNION

-- Query 2: Students with Marks >= 90
SELECT first_name FROM students WHERE marks >= 90;
```

**Result:**
| first_name |
|---|
| Rahul |
| Yamini |
| m_Ramya |
| Roshini |
| Vishal |

---

# 🎤 Ask the Students

Ask:
> "Why didn't `m_Ramya` appear twice in the output?"

Expected answer:
> Because `UNION` automatically removes duplicate rows.

Exactly!

---

# 2. UNION ALL

Now change the question. Ask:

> "What if I want ALL the rows from both queries, even if a student appears twice?"

Then we use:
```sql
UNION ALL
```

## 💻 SQL Example

```sql
SELECT first_name FROM students WHERE dept_id = 101

UNION ALL

SELECT first_name FROM students WHERE marks >= 90;
```

**Result:**
| first_name |
|---|
| Rahul |
| Yamini |
| m_Ramya |  <-- (From Dept 101 query)
| Roshini |
| m_Ramya |  <-- (From High Achievers query)
| Vishal |

Now `m_Ramya` appears **twice**.

---

# 🧠 UNION vs UNION ALL

Write this on the board:

```text
UNION
↓
Combine + Remove duplicates
```

```text
UNION ALL
↓
Combine + Keep duplicates
```

### Easy Memory Trick
> **UNION = Everyone, but unique.**
> **UNION ALL = Everyone, including duplicates.**

---

# 🎮 Interactive Question 2

Ask the students:

> "Who is in BOTH Group A (Dept 101) AND Group B (High Achiever)?"

Look at the groups:
**Group A:** Rahul, Yamini, m_Ramya
**Group B:** Roshini, m_Ramya, Vishal

Answer:
```text
m_Ramya
```

This idea is called:

# 3. INTERSECT

---

## 🧠 Simple Meaning
> **INTERSECT gives the common rows between two results.**

Think:
```text
Group A
   +
Group B
   ↓
Common Students
```

## 💻 SQL Concept

In databases that support `INTERSECT`:
```sql
SELECT first_name FROM students WHERE dept_id = 101

INTERSECT

SELECT first_name FROM students WHERE marks >= 90;
```

**Result:**
| first_name |
|---|
| m_Ramya |

## ⚠️ Important for MySQL

We are using **MySQL**. Older versions of MySQL do not directly support the `INTERSECT` keyword. 
But the idea is important! In MySQL, we usually find the intersection using `INNER JOIN` or `IN` subqueries (which we will learn below).

---

# 4. EXCEPT

Now ask:

> "Who is in Group A (Dept 101) but NOT in Group B (High Achiever)?"

Look at Group A:
`Rahul`, `Yamini`, `m_Ramya`

Check who is also in Group B: `m_Ramya`. Remove her!

Answer:
```text
Rahul
Yamini
```

This idea is called:

# EXCEPT (or MINUS)

## 🧠 Simple Meaning
> **EXCEPT gives us the rows that are in the first result but NOT in the second result.**

Think:
```text
Group A
   -
Group B
   ↓
Group A only students
```

## 💻 SQL Concept

```sql
SELECT first_name FROM students WHERE dept_id = 101

EXCEPT

SELECT first_name FROM students WHERE marks >= 90;
```

**Result:**
| first_name |
|---|
| Rahul |
| Yamini |

*(Note: Just like INTERSECT, EXCEPT is not natively supported in older MySQL, but we can use `NOT IN` to get the same result!)*

---

# PART 2 — SUBQUERIES

Now we enter the world of Subqueries.

## 🧠 First, What Is a Subquery?

Ask the students:
> "If I ask you to find all students who scored more than Yamini, what do you need to know first?"

Expected answer:
> "We need to know Yamini's marks first!"

Exactly! We have to run TWO queries in our brain:
1. What are Yamini's marks? (Answer: 70)
2. Who scored more than 70? 

A **Subquery** lets us do both steps in one single SQL statement!

```text
Main Query (Outer)
    |
    ↳ Subquery (Inner) -> Runs first and passes data to the Main Query
```

---

# 1. Single-Row Subquery

Let's solve the Yamini problem in SQL.

```sql
-- Step 1 (Inner Query): Find Yamini's marks
-- SELECT marks FROM students WHERE first_name = 'Yamini'; (Returns 70)

-- Step 2 (Outer Query): Put it all together!
SELECT first_name, marks 
FROM students 
WHERE marks > (SELECT marks FROM students WHERE first_name = 'Yamini');
```

**Result:** Returns everyone who scored more than 70! (Rahul, Roshini, k_Ramya, m_Ramya, Vaibhav, Vishal).

### Another Example: The Highest Scorer
How do we find the details of the student with the highest marks?
We can't just type `WHERE marks = 95` because the data might change tomorrow!

```sql
SELECT first_name, marks 
FROM students 
WHERE marks = (SELECT MAX(marks) FROM students);
```
*(The inner query `SELECT MAX(marks)` finds 95. Then the outer query finds the student with 95).*

---

# 2. Multi-Row Subquery (Using IN)

What if the inner query returns **more than one row**? 
You can't use `=` anymore (because a value can't be equal to a list of values). Instead, we use `IN`.

## 🎮 Interactive Question 3

Ask the students:
> "I want to find the names of all students who belong to the 'PIT' department. But I only know the department name, not the ID. How can I find them?"

**Step 1:** Find the `dept_id` for 'PIT'.
```sql
SELECT dept_id FROM departments WHERE dept_name = 'PIT';
-- This returns 102
```

**Step 2:** Find students in that department.
```sql
SELECT first_name 
FROM students 
WHERE dept_id IN (
    SELECT dept_id 
    FROM departments 
    WHERE dept_name = 'PIT'
);
```

**Result:**
| first_name |
|---|
| Roshini |
| Reena |
| Vaibhav |

### Why use `IN` instead of `=`?
Because sometimes an inner query returns multiple IDs! 

For example, what if we want to find all students in departments that start with 'P'?
```sql
SELECT first_name 
FROM students 
WHERE dept_id IN (
    SELECT dept_id 
    FROM departments 
    WHERE dept_name LIKE 'P%'
);
```
The inner query returns a list: `(101, 102, 103)`. The outer query uses `IN` to check if a student's `dept_id` is inside that list.

---

# 🎯 Summary for the Board

Write this on the board at the end of class:

1. **UNION:** Combine lists, remove duplicates.
2. **UNION ALL:** Combine lists, keep duplicates.
3. **INTERSECT:** Only keep common rows.
4. **EXCEPT:** Subtract the second list from the first.
5. **Subquery:** A query inside another query. 
   - Runs from the **inside out**.
   - Use `=` for single values.
   - Use `IN` for multiple values.
