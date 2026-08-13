# Unit 2 Part 8: Set Operators and Subqueries

Welcome to Part 8! Up until now, we have been combining tables horizontally using JOINS. But what if you want to combine tables vertically? What if you want to use the result of one query as the filter for another query?

In this unit, we will explore **Set Operators** (combining results vertically) and **Subqueries** (queries inside queries).

---

# 🎯 Today's Goal

Before writing SQL, we are going to understand the ideas using simple real-world examples.

Then we will apply those ideas to our:

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

We will use the following students throughout this lesson:

- Rahul
- Roshini
- Yamini
- k_Ramya
- Reena
- m_Ramya
- Vaibhav
- Vishal

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

## 5. Check the inserted data

```sql
SELECT * FROM departments;
```

Expected:

| dept_id | dept_name |
|---:|---|
| 101 | Piet |
| 102 | PIT |
| 103 | PIN |

```sql
SELECT * FROM students;
```

Expected:

| student_id | first_name | dept_id | marks |
|---:|---|---:|---:|
| 1 | Rahul | 101 | 85 |
| 2 | Roshini | 102 | 92 |
| 3 | Yamini | 101 | 70 |
| 4 | k_Ramya | 103 | 88 |
| 5 | Reena | 102 | 60 |
| 6 | m_Ramya | 101 | 95 |
| 7 | Vaibhav | 102 | 78 |
| 8 | Vishal | 103 | 90 |

> **Important:** Run the `CREATE TABLE` statements first, then the `INSERT` statements. Once the data is inserted, we can perform Set Operations and Subqueries.

---


Welcome to Part 8! Up until now, we have been combining tables horizontally using JOINS. But what if you want to combine tables vertically? What if you want to use the result of one query as the filter for another query?

In this unit, we will explore **Set Operators** (combining results vertically) and **Subqueries** (queries inside queries).

---

# 🎯 Today's Goal

Before writing SQL, we are going to understand the ideas using simple real-world examples.

Then we will apply those ideas to our:

- `students` table
- `departments` table

By the end, you should be able to understand:

```
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

# PART 1 — SET OPERATORS

## 🧠 First, What Is a Set?

Don't worry about the mathematical definition.

For today, think of a **set as a group or collection of things**.

For example, imagine two groups of students.

### 🟤 Students Playing Carrom

```
Rahul
Roshini
Yamini
k_Ramya

```

### ♟️ Students Playing Chess

```
Roshini
Yamini
Reena
m_Ramya

```

Notice something.

Some students are playing **both** games.

```
Roshini
Yamini

```

Some students are only playing Carrom.

```
Rahul
k_Ramya

```

Some students are only playing Chess.

```
Reena
m_Ramya

```

Now we can ask different questions.

---

# 🎮 Interactive Question 1

Ask the students:

> "If I want a list of EVERY student who plays either Carrom OR Chess, what should I do?"

Let them answer.

Expected answer:

```
Rahul
Roshini
Yamini
k_Ramya
Reena
m_Ramya
Vaibhav
Vishal

```

We combined the two groups.

This is the idea behind:

# UNION

---

# 1. UNION

## 🧠 Simple Meaning

> **UNION combines the results of two queries and removes duplicates.**

Think:

```
Carrom
   +
Chess
   ↓
Everyone
without duplicates

```

Our example:

### Carrom

```
Rahul
Roshini
Yamini
k_Ramya

```

### Chess

```
Roshini
Yamini
Reena
m_Ramya

```

After UNION:

```
Rahul
Roshini
Yamini
k_Ramya
Reena
m_Ramya
Vaibhav
Vishal

```

Notice:

```
Roshini
Yamini

```

appear only once.

---

# 💻 SQL Example

Suppose we have two tables:

### `carrom_players`

| student\_name |
| ------------- |
| Rahul         |
| Roshini         |
| Yamini        |
| k_Ramya         |

### `chess_players`

| student\_name |
| ------------- |
| Roshini         |
| Yamini        |
| Reena         |
| m_Ramya          |

We can write:

```
SELECT student_name
FROM carrom_players

UNION

SELECT student_name
FROM chess_players;

```

Result:

| student\_name |
| ------------- |
| Rahul         |
| Roshini         |
| Yamini        |
| k_Ramya         |
| Reena         |
| m_Ramya          |

---

# 🎤 Ask the Students

Ask:

> "Why didn't Roshini appear twice?"

Expected answer:

> Because `UNION` removes duplicate rows.

Exactly!

---

# 2. UNION ALL

Now change the question.

Ask:

> "What if I want ALL the rows from both groups, even if a student appears in both groups?"

Then we use:

```
UNION ALL

```

SQL:

```
SELECT student_name
FROM carrom_players

UNION ALL

SELECT student_name
FROM chess_players;

```

Result:

| student\_name |
| ------------- |
| Rahul         |
| Roshini         |
| Yamini        |
| k_Ramya         |
| Roshini         |
| Yamini        |
| Reena         |
| m_Ramya          |

Now:

```
Roshini
Roshini

```

and:

```
Yamini
Yamini

```

appear twice.

---

# 🧠 UNION vs UNION ALL

Write this on the board:

```
UNION
↓
Combine
+
Remove duplicates

```

```
UNION ALL
↓
Combine
+
Keep duplicates

```

### Easy Memory Trick

> **UNION = Everyone, but unique.**

> **UNION ALL = Everyone, including duplicates.**

---

# 🎮 Interactive Question 2

Give them:

### Carrom

```
Roshini
Yamini
m_Ramya

```

### Chess

```
Yamini
m_Ramya
Reena

```

Ask:

> "What will UNION return?"

Give them a few seconds.

Answer:

```
Roshini
Yamini
m_Ramya
Reena

```

Then ask:

> "What will UNION ALL return?"

Answer:

```
Roshini
Yamini
m_Ramya
Yamini
m_Ramya
Reena

```

---

# 3. INTERSECT

Now change the question again.

Ask:

> "Who plays BOTH Carrom AND Chess?"

Look at the groups:

### Carrom

```
Rahul
Roshini
Yamini
k_Ramya

```

### Chess

```
Roshini
Yamini
Reena
m_Ramya

```

Who appears in both?

```
Roshini
Yamini

```

This is called:

# INTERSECT

---

# 🧠 Simple Meaning

> **INTERSECT gives the common rows between two results.**

Think:

```
Carrom
   +
Chess
   ↓
Common Students

```

Mathematically:

```
A ∩ B

```

---

# 💻 SQL Concept

In databases that support `INTERSECT`:

```
SELECT student_name
FROM carrom_players

INTERSECT

SELECT student_name
FROM chess_players;

```

Result:

```
Roshini
Yamini

```

---

# ⚠️ Important for MySQL

We are using **MySQL**.

MySQL does not directly support the `INTERSECT` keyword.

So this:

```
SELECT student_name
FROM carrom_players

INTERSECT

SELECT student_name
FROM chess_players;

```

will not work directly in MySQL.

For today, focus on understanding the **idea**:

```
INTERSECT
=
COMMON

```

Later, we can achieve the same result using other SQL techniques.

For example:

```
SELECT student_name
FROM carrom_players
WHERE student_name IN (
    SELECT student_name
    FROM chess_players
);

```

---

# 🎮 Interactive Question 3

Ask:

### Carrom

```
Roshini
Yamini
k_Ramya
Reena

```

### Chess

```
Yamini
Reena
m_Ramya

```

Question:

> "Who plays both games?"

Answer:

```
Yamini
Reena

```

Ask:

> "Which Set Operator represents this?"

Answer:

```
INTERSECT

```

---

# 4. EXCEPT

Now ask:

> "Who plays Carrom but does NOT play Chess?"

### Carrom

```
Rahul
Roshini
Yamini
k_Ramya

```

### Chess

```
Roshini
Yamini
Reena
m_Ramya

```

Let's check one by one:

```
Rahul
→ Carrom only
→ KEEP

Roshini
→ Both
→ REMOVE

Yamini
→ Both
→ REMOVE

k_Ramya
→ Carrom only
→ KEEP

```

Answer:

```
Rahul
k_Ramya

```

This idea is called:

# EXCEPT

---

# 🧠 Simple Meaning

> **EXCEPT gives us the rows that are in the first result but NOT in the second result.**

Think:

```
Carrom
   -
Chess
   ↓
Carrom-only students

```

---

# 5. EXCEPT and MINUS

Different databases use different names.

```
EXCEPT
MINUS

```

They represent the same basic idea:

> **Give me the rows from the first result that don't exist in the second result.**

For example:

```
Carrom
-
Chess
=
Students who only play Carrom

```

---

# ⚠️ Important for MySQL

MySQL does not directly provide the standard `EXCEPT` / `MINUS` syntax.

So for today's class, remember the **concept** rather than memorizing the syntax.

---

# 🎯 All Four Set Operators Together

Let's use our two groups again.

### 🟤 Carrom

```
Rahul
Roshini
Yamini
k_Ramya

```

### ♟️ Chess

```
Roshini
Yamini
Reena
m_Ramya

```

---

## UNION

Question:

> Who plays at least one of the games?

```
Rahul
Roshini
Yamini
k_Ramya
Reena
m_Ramya
Vaibhav
Vishal

```

---

## UNION ALL

Question:

> Combine both lists and keep duplicates.

```
Rahul
Roshini
Yamini
k_Ramya
Roshini
Yamini
Reena
m_Ramya

```

---

## INTERSECT

Question:

> Who plays both?

```
Roshini
Yamini

```

---

## EXCEPT

Question:

> Who plays Carrom but not Chess?

```
Rahul
k_Ramya

```

---

# 🧠 SET OPERATOR CHEAT SHEET

```
UNION
↓
EVERYONE
WITHOUT DUPLICATES


UNION ALL
↓
EVERYONE
WITH DUPLICATES


INTERSECT
↓
COMMON


EXCEPT
↓
ONLY FIRST

```

---

# 💻 Practical Set Operations Using `students`

Now that the data is inserted, let's perform Set Operations directly on our `students` table.

> **Important MySQL note:** MySQL supports `UNION` and `UNION ALL`, but standard `INTERSECT` and `EXCEPT` are not the operators to rely on in beginner MySQL examples. We will first understand their concepts and then use MySQL-friendly queries to achieve the same results.

## UNION — Students from Piet or PIT

```sql
SELECT first_name
FROM students
WHERE dept_id = 101

UNION

SELECT first_name
FROM students
WHERE dept_id = 102;
```

Expected students:

```text
Rahul
Yamini
m_Ramya
Roshini
Reena
Vaibhav
```

`UNION` combines both result sets and removes duplicate rows.

## UNION ALL — Keep every row

```sql
SELECT first_name
FROM students
WHERE dept_id = 101

UNION ALL

SELECT first_name
FROM students
WHERE dept_id = 102;
```

Because each student belongs to only one department in this dataset, this particular query does not create duplicate names. To clearly demonstrate duplicates, use overlapping conditions:

```sql
SELECT first_name
FROM students
WHERE marks >= 80

UNION ALL

SELECT first_name
FROM students
WHERE marks >= 85;
```

Here, students satisfying both conditions appear twice.

## INTERSECT concept in MySQL

Question:

> Which students have marks at least 80 **and** also belong to PIT?

The set idea is an intersection. In MySQL, a simple equivalent can be written with `AND`:

```sql
SELECT first_name
FROM students
WHERE marks >= 80
  AND dept_id = 102;
```

Result:

```text
Roshini
```

You can also demonstrate the same intersection pattern with a subquery:

```sql
SELECT first_name
FROM students
WHERE first_name IN (
    SELECT first_name
    FROM students
    WHERE marks >= 80
)
AND dept_id = 102;
```

## EXCEPT concept in MySQL

Question:

> Which students are in Piet but are **not** students with marks 90 or above?

A MySQL-friendly way is:

```sql
SELECT first_name
FROM students
WHERE dept_id = 101
  AND marks < 90;
```

Result:

```text
Rahul
Yamini
```

The general idea of `EXCEPT` is:

```text
First result
    -
Second result
    ↓
Rows that exist only in the first result
```

---

# PART 2 — SET OPERATORS WITH OUR SQL TABLES

Now we move from our Carrom and Chess example to our actual database.

We will mainly use:

```
students
departments

```

---

# 6. Our Students Table

Suppose our `students` table contains:

| student\_idfirst\_namedept\_id |        |     |
| ------------------------------ | ------ | --- |
| 1                              | Rahul  | 101 |
| 2                              | Roshini  | 102 |
| 3                              | Yamini | 101 |
| 4                              | k_Ramya  | 103 |
| 5                              | Reena  | 102 |
| 6                              | m_Ramya   | 101 |

---

# 7. Our Departments Table

| dept_id | dept_name |
|---:|---|
| 101 | Piet |
| 102 | PIT |
| 103 | PIN |

---

# 🎮 Interactive Question

Ask:

> "If I run this query, what will I get?"

```
SELECT first_name
FROM students;

```

Answer:

```
Rahul
Roshini
Yamini
k_Ramya
Reena
m_Ramya
Vaibhav
Vishal

```

Now ask:

> "What if I want another list and combine it with this one?"

This is where Set Operators become useful.

---

# 8. Combining Results from SELECT Queries

Suppose we want:

> Students whose department ID is 101 OR students whose department ID is 103.

We could write:

```
SELECT first_name
FROM students
WHERE dept_id = 101

UNION

SELECT first_name
FROM students
WHERE dept_id = 103;

```

First query:

```
Rahul
Yamini
m_Ramya

```

Second query:

```
k_Ramya

```

Final result:

```
Rahul
Yamini
m_Ramya
k_Ramya

```

---

# 🧠 Important Idea

Notice that we are not joining two tables.

We are combining the results of:

```
Query 1
+
Query 2

```

That's a Set Operator.

---

# 9. UNION with Students

Question:

> Find students who belong to either department 101 or department 102.

```
SELECT first_name
FROM students
WHERE dept_id = 101

UNION

SELECT first_name
FROM students
WHERE dept_id = 102;

```

Result:

```
Rahul
Yamini
m_Ramya
Roshini
Reena

```

---

# 10. UNION ALL with Students

Now:

```
SELECT first_name
FROM students
WHERE dept_id = 101

UNION ALL

SELECT first_name
FROM students
WHERE dept_id = 102;

```

Since a student can only have one department in our example, there may not be duplicates.

This is a good teaching point:

> `UNION ALL` only shows a difference when duplicate rows exist.

---

# 11. Important Rules for Set Operators

Before using:

```
UNION
UNION ALL
INTERSECT
EXCEPT

```

there are some basic rules.

---

## Rule 1 — Same Number of Columns

This is correct:

```
SELECT first_name
FROM students

UNION

SELECT dept_name
FROM departments;

```

Both queries return **one column**.

But this is not:

```
SELECT first_name, dept_id
FROM students

UNION

SELECT dept_name
FROM departments;

```

First query:

```
2 columns

```

Second query:

```
1 column

```

The number of columns doesn't match.

---

# Rule 2 — Columns Should Have Compatible Data Types

For example:

```
Text + Text

```

is sensible.

```
Number + Number

```

is sensible.

The corresponding columns should contain compatible types of information.

---

# Rule 3 — Column Order Matters

Suppose:

```
SELECT first_name, dept_id
FROM students

```

Then the second query should have:

```
first column → similar type of information
second column → similar type of information

```

The positions matter.

---

# 🧠 JOIN vs SET OPERATOR

You have already learned JOINs.

So this is very important.

## JOIN

JOIN combines related data **side by side**.

Example:

```
students                  departments

Rahul | 101       →       101 | Piet

```

Result:

```
Rahul | Piet

```

Think:

```
→ → →

```

---

## SET OPERATOR

Set Operators combine query results **vertically**.

```
Query 1

Rahul
Roshini
Yamini

+

Query 2

k_Ramya
Reena
m_Ramya

```

Result:

```
Rahul
Roshini
Yamini
k_Ramya
Reena
m_Ramya
Vaibhav
Vishal

```

Think:

```
↓
↓
↓

```

---

# PART 3 — SUBQUERIES

Now we move to the second half of today's lesson.

Ask:

> "What if one SQL query needs the answer from another SQL query?"

For example:

> Find students who scored higher than the class average.

To solve this, we first need to know:

> What is the average?

Then we need to find:

> Who scored higher than that average?

This is where **Subqueries** come in.

---

# 12. What Is a Subquery?

A **subquery** is:

> **A query inside another query.**

Think:

```
MAIN QUERY
    ↓
contains
    ↓
SUBQUERY

```

Example:

```
SELECT first_name, marks
FROM students
WHERE marks > (
    SELECT AVG(marks)
    FROM students
);

```

The inner query:

```
SELECT AVG(marks)
FROM students

```

is the **subquery**.

The outer query is the **main query**.

---

# 🎮 Interactive Question

Look at:

```
SELECT first_name, marks
FROM students
WHERE marks > (
    SELECT AVG(marks)
    FROM students
);

```

Ask:

### Question 1

> Which part is the subquery?

Answer:

```
SELECT AVG(marks)
FROM students

```

### Question 2

> What does it calculate?

Answer:

```
The average marks.

```

### Question 3

> What does the outer query do?

Answer:

```
Finds students whose marks are greater than the average.

```

Excellent!

---

# 13. Understanding the Query Step by Step

Suppose our students have:

| StudentMarks |    |
| ------------ | -- |
| Rahul        | 85 |
| Roshini        | 92 |
| Yamini       | 70 |
| k_Ramya        | 88 |
| Reena        | 60 |
| m_Ramya         | 95 |

First SQL calculates:

```
SELECT AVG(marks)
FROM students;

```

Suppose the result is:

```
81.67

```

Then the outer query effectively becomes:

```
SELECT first_name, marks
FROM students
WHERE marks > 81.67;

```

Result:

```
Rahul   85
Roshini   92
k_Ramya   88
m_Ramya    95

```

---

# 🧠 The Mental Model

Always think:

```
SUBQUERY
   ↓
Find an answer
   ↓
MAIN QUERY uses that answer
   ↓
Final result

```

---

# 14. Subquery with MAX()

Now ask:

> "How can we find the highest marks?"

Students should already know:

```
MAX()

```

So:

```
SELECT MAX(marks)
FROM students;

```

Suppose the result is:

```
95

```

Now:

```
SELECT first_name, marks
FROM students
WHERE marks = 95;

```

But we don't want to manually type `95`.

Instead:

```
SELECT first_name, marks
FROM students
WHERE marks = (
    SELECT MAX(marks)
    FROM students
);

```

---

# 🎮 Ask the Students

Ask:

> "What does the inner query find?"

Answer:

```
Highest mark.

```

Ask:

> "What does the outer query find?"

Answer:

```
Student who has that mark.

```

---

# 15. Finding the Lowest Marks

Same idea.

```
SELECT first_name, marks
FROM students
WHERE marks = (
    SELECT MIN(marks)
    FROM students
);

```

Inner query:

```
SELECT MIN(marks)
FROM students;

```

Finds:

```
Lowest mark

```

Outer query:

```
SELECT first_name, marks
FROM students
WHERE marks = (...);

```

Finds:

```
Student with the lowest mark

```

---

# 16. Subquery with Students and Departments

Now we use our two main tables.

## Students

| student\_idfirst\_namedept\_id |        |     |
| ------------------------------ | ------ | --- |
| 1                              | Rahul  | 101 |
| 2                              | Roshini  | 102 |
| 3                              | Yamini | 101 |
| 4                              | k_Ramya  | 103 |
| 5                              | Reena  | 102 |
| 6                              | m_Ramya   | 101 |

## Departments

| dept_id | dept_name |
|---:|---|
| 101 | Piet |
| 102 | PIT |
| 103 | PIN |

---

# 🎮 Real-World Question

Ask:

> "I want the names of all students who belong to Piet."

But imagine:

> I don't know the department ID.

I only know:

```
Piet

```

How do we solve this?

---

# Step 1 — Find Department ID

```
SELECT dept_id
FROM departments
WHERE dept_name = 'Piet';

```

Result:

```
101

```

---

# Step 2 — Find Students

```
SELECT first_name
FROM students
WHERE dept_id = 101;

```

Result:

```
Rahul
Yamini
m_Ramya

```

---

# Step 3 — Put the First Query Inside the Second Query

Now we can write:

```
SELECT first_name
FROM students
WHERE dept_id = (
    SELECT dept_id
    FROM departments
    WHERE dept_name = 'Piet'
);

```

---

# 🧠 Read It Like English

Start from the inside:

```
SELECT dept_id
FROM departments
WHERE dept_name = 'Piet'

```

Meaning:

> Find the department ID of Piet.

It gives:

```
101

```

Then the outer query becomes:

```
SELECT first_name
FROM students
WHERE dept_id = 101;

```

Result:

```
Rahul
Yamini
m_Ramya

```

---

# 🎮 Interactive Question

Ask:

> "If Piet has department ID 101, which students will we get?"

Look at the table:

```
Rahul   → 101
Roshini   → 102
Yamini  → 101
k_Ramya   → 103
Reena   → 102
m_Ramya    → 101

```

Answer:

```
Rahul
Yamini
m_Ramya

```

---

# 17. Subquery with IN

Now imagine the question changes:

> Find students from Piet OR PIN.

We need two department IDs:

```
Piet → 101
PIN            → 103

```

The inner query can find both:

```
SELECT dept_id
FROM departments
WHERE dept_name IN ('Piet', 'PIN');

```

Result:

```
101
103

```

Now we need students whose `dept_id` is one of those values.

Use `IN`:

```
SELECT first_name
FROM students
WHERE dept_id IN (
    SELECT dept_id
    FROM departments
    WHERE dept_name IN ('Piet', 'PIN')
);

```

Result:

```
Rahul
Yamini
k_Ramya
m_Ramya

```

---

# 🧠 Why IN?

Because the subquery can return more than one value:

```
101
103

```

We are asking:

> Is this student's department ID **IN** the list?

```
(101, 103)

```

---

# 18. One Value vs Multiple Values

This is a very important beginner concept.

If the subquery returns **one value**:

```
101

```

we can use:

```
WHERE dept_id = (
    SELECT ...
);

```

If the subquery returns **multiple values**:

```
101
103

```

we can use:

```
WHERE dept_id IN (
    SELECT ...
);

```

Think:

```
One value
    ↓
=

Multiple values
    ↓
IN

```

---

# 19. Another Real-World Subquery

Question:

> Find students who scored higher than the highest mark of another group.

For today's class, we don't need a complicated example.

The important pattern is:

```
First find something
      ↓
Use that answer
      ↓
Find the final result

```

That's the main idea of a subquery.

---

# 20. Main Query vs Subquery

Look at:

```
SELECT first_name, marks
FROM students
WHERE marks > (
    SELECT AVG(marks)
    FROM students
);

```

### Main Query

```
SELECT first_name, marks
FROM students
WHERE marks > (...);

```

It gives the final answer.

### Subquery

```
SELECT AVG(marks)
FROM students;

```

It helps the main query.

---

# 🧠 Easy Memory Trick

> **Main Query = What I finally want.**

> **Subquery = Information I need to find it.**

---

# 21. Independent Subquery

There is a type called an **independent subquery**.

For example:

```
SELECT first_name, marks
FROM students
WHERE marks > (
    SELECT AVG(marks)
    FROM students
);

```

The inner query:

```
SELECT AVG(marks)
FROM students;

```

can run by itself.

It doesn't need information from the outer query.

So we can simply think:

> **Independent subquery = The inner query can run independently.**

---

# ⚠️ Advanced Topics — Not Today

There are more advanced types of subqueries, such as:

```
Correlated Subqueries
EXISTS
NOT EXISTS
ANY
ALL

```

These are useful, but we don't need to go deeply into them in today's beginner session.

First make sure the basic idea is clear:

```
Query inside another query

```

---

# 🎯 SET OPERATORS vs SUBQUERIES

This is one of the most important things to understand.

## Set Operators

We have:

```
Query A
   +
Query B
   ↓
Combine / Compare Results

```

Examples:

```
UNION
UNION ALL
INTERSECT
EXCEPT

```

---

## Subquery

We have:

```
Main Query
    ↓
uses
    ↓
Subquery

```

Example:

```
SELECT first_name
FROM students
WHERE marks > (
    SELECT AVG(marks)
    FROM students
);

```

---

# 🧠 SUPER SIMPLE DIFFERENCE

Write this on the board:

```
SET OPERATORS

Query A + Query B
        ↓
Combine / Compare

```

```
SUBQUERY

Main Query
    ↓
Query inside Query

```

---

# 🎮 FINAL INTERACTIVE GAME

Now don't show them the SQL.

Give them the problem and ask:

> **"Which SQL concept would you use?"**

---

## Question 1

> I have a list of Carrom players and a list of Chess players. I want everyone from both groups without duplicates.

Answer:

```
UNION

```

---

## Question 2

> I want everyone from both groups, including students who appear in both lists twice.

Answer:

```
UNION ALL

```

---

## Question 3

> I want students who play both Carrom and Chess.

Answer:

```
INTERSECT

```

---

## Question 4

> I want students who play Carrom but don't play Chess.

Answer:

```
EXCEPT

```

---

## Question 5

> I want students who scored above the class average.

Answer:

```
SUBQUERY

```

---

## Question 6

> I want the student who got the highest marks.

Answer:

```
SUBQUERY + MAX()

```

---

## Question 7

> I want students from the Piet department, but I only know the department name.

Answer:

```
SUBQUERY

```

---

## Question 8

> I want students from Piet OR PIN, and I don't know their department IDs.

Answer:

```
SUBQUERY + IN

```

---

# 🏆 FINAL PRACTICE

Use these tables:

## Students

| student\_idfirst\_namedept\_idmarks |        |     |    |
| ----------------------------------- | ------ | --- | -- |
| 1                                   | Rahul  | 101 | 85 |
| 2                                   | Roshini  | 102 | 92 |
| 3                                   | Yamini | 101 | 70 |
| 4                                   | k_Ramya  | 103 | 88 |
| 5                                   | Reena  | 102 | 60 |
| 6                                   | m_Ramya   | 101 | 95 |

## Departments

| dept_id | dept_name |
|---:|---|
| 101 | Piet |
| 102 | PIT |
| 103 | PIN |

---

# Challenge 1

### Question

Find students who scored higher than the average.

### Think first!

What do we need to find first?

```
Average marks

```

Therefore:

```
SELECT first_name, marks
FROM students
WHERE marks > (
    SELECT AVG(marks)
    FROM students
);

```

---

# Challenge 2

### Question

Find the student with the highest marks.

```
SELECT first_name, marks
FROM students
WHERE marks = (
    SELECT MAX(marks)
    FROM students
);

```

---

# Challenge 3

### Question

Find the student with the lowest marks.

```
SELECT first_name, marks
FROM students
WHERE marks = (
    SELECT MIN(marks)
    FROM students
);

```

---

# Challenge 4

### Question

Find students from Piet.

```
SELECT first_name
FROM students
WHERE dept_id = (
    SELECT dept_id
    FROM departments
    WHERE dept_name = 'Piet'
);

```

Expected result:

```
Rahul
Yamini
m_Ramya

```

---

# Challenge 5

### Question

Find students from Piet OR PIN.

```
SELECT first_name
FROM students
WHERE dept_id IN (
    SELECT dept_id
    FROM departments
    WHERE dept_name IN ('Piet', 'PIN')
);

```

Expected result:

```
Rahul
Yamini
k_Ramya
m_Ramya

```

---

# Challenge 6

### Question

Find students who belong to PIT.

Don't directly use:

```
WHERE dept_id = 102

```

Instead, use the department name and a subquery.

```
SELECT first_name
FROM students
WHERE dept_id = (
    SELECT dept_id
    FROM departments
    WHERE dept_name = 'PIT'
);

```

Expected result:

```
Roshini
Reena

```

---

# 🧠 FINAL REVISION

## SET OPERATORS

### UNION

```
Combine
+
Remove duplicates

```

### UNION ALL

```
Combine
+
Keep duplicates

```

### INTERSECT

```
Find common

```

### EXCEPT

```
First result
but NOT second result

```

---

# SUBQUERIES

### Subquery

```
Query inside another query

```

### Main Query

```
The query that gives the final answer

```

### Subquery

```
The query that helps the main query

```

### `=`

Use when the subquery gives one value.

```
WHERE dept_id = (
    SELECT ...
);

```

### `IN`

Use when the subquery can give multiple values.

```
WHERE dept_id IN (
    SELECT ...
);

```

---

# 🎓 Final Takeaway

If you remember only these things from today's class, that's enough:

```
UNION
→ Everyone from both results, without duplicates.

UNION ALL
→ Everyone from both results, including duplicates.

INTERSECT
→ Common results.

EXCEPT
→ Results in the first query but not the second.

SUBQUERY
→ A query inside another query.

```

And remember this mental model:

```
                 SQL SET OPERATORS
                       │
          ┌────────────┼────────────┐
          ↓            ↓            ↓
       UNION       INTERSECT      EXCEPT
          │            │            │
      Combine       Common       First only
          │
      UNION ALL
          │
   Combine + duplicates


                 SQL SUBQUERY
                       │
                       ↓
                Main Query
                       │
                       ↓
                  Subquery
                       │
                       ↓
                  Gives answer
                       │
                       ↓
                Final Result

```

---

# 🚀 What Comes Next?

Once you are comfortable with today's basic subqueries, the next step is to learn:

```
Simple Subqueries
       ↓
IN with Subqueries
       ↓
NOT IN
       ↓
EXISTS
       ↓
NOT EXISTS
       ↓
Correlated Subqueries

```

But don't rush.

The most important question to ask whenever you see a subquery is:

> **"What does the inner query need to find first, and how will the outer query use that answer?"**

If you can answer that, you understand the basic idea of subqueries.

---

# 🧪 COMPLETE RUNNABLE SQL — FROM TABLE CREATION TO SUBQUERIES

If you want to practice this lesson from the beginning, run the following script in order.

```sql
CREATE TABLE departments (
    dept_id INT PRIMARY KEY,
    dept_name VARCHAR(50) NOT NULL
);

CREATE TABLE students (
    student_id INT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    dept_id INT,
    marks INT,
    FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
);

INSERT INTO departments (dept_id, dept_name)
VALUES
(101, 'Piet'),
(102, 'PIT'),
(103, 'PIN');

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

-- View the data
SELECT * FROM departments;
SELECT * FROM students;

-- UNION
SELECT first_name
FROM students
WHERE dept_id = 101
UNION
SELECT first_name
FROM students
WHERE dept_id = 102;

-- UNION ALL
SELECT first_name
FROM students
WHERE marks >= 80
UNION ALL
SELECT first_name
FROM students
WHERE marks >= 85;

-- Subquery: students above average
SELECT first_name, marks
FROM students
WHERE marks > (
    SELECT AVG(marks)
    FROM students
);

-- Subquery: highest marks
SELECT first_name, marks
FROM students
WHERE marks = (
    SELECT MAX(marks)
    FROM students
);

-- Subquery: lowest marks
SELECT first_name, marks
FROM students
WHERE marks = (
    SELECT MIN(marks)
    FROM students
);

-- Subquery: students from Piet
SELECT first_name
FROM students
WHERE dept_id = (
    SELECT dept_id
    FROM departments
    WHERE dept_name = 'Piet'
);

-- Subquery + IN: students from Piet or PIN
SELECT first_name
FROM students
WHERE dept_id IN (
    SELECT dept_id
    FROM departments
    WHERE dept_name IN ('Piet', 'PIN')
);
```

---

# 🎓 Final Takeaway

If you remember only these things from today's class, that's enough:

```text
UNION
→ Everyone from both results, without duplicates.

UNION ALL
→ Everyone from both results, including duplicates.

INTERSECT
→ Common results.

EXCEPT
→ Results in the first query but not the second.

SUBQUERY
→ A query inside another query.
```

And remember this mental model:

```text
                 SQL SET OPERATORS
                       │
           ┌───────────┼───────────┐
           ↓           ↓           ↓
        UNION      INTERSECT     EXCEPT
           │           │           │
        Combine      Common     First only
           │
       UNION ALL
           │
   Combine + duplicates


                 SQL SUBQUERY
                       │
                       ↓
                  Main Query
                       │
                       ↓
                    Subquery
                       │
                       ↓
                  Gives answer
                       │
                       ↓
                  Final Result
```

---

# 🚀 What Comes Next?

Once you are comfortable with today's basic subqueries, the next step is to learn:

```text
Simple Subqueries
       ↓
IN with Subqueries
       ↓
NOT IN
       ↓
EXISTS
       ↓
NOT EXISTS
       ↓
Correlated Subqueries
```

But don't rush.

The most important question to ask whenever you see a subquery is:

> **"What does the inner query need to find first, and how will the outer query use that answer?"**

If you can answer that, you understand the basic idea of subqueries.
