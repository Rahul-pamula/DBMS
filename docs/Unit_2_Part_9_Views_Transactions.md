# Unit 2 Part 9: Views and Transactions (TCL)

Welcome to Part 9! In this unit, we will cover two incredibly important concepts for real-world databases: **Views** (Virtual Tables for security and simplicity) and **Transactions** (ensuring our database never gets corrupted during power failures or errors).

---

# 🎯 Today's Goal

Before writing SQL, we are going to understand the ideas using simple real-world examples right from our classroom data.

We will apply these ideas to our:
- `students` table
- `departments` table

By the end, you should be able to understand:

```text
VIEWS
    ↓
Simple View
Complex View

TRANSACTIONS (TCL)
    ↓
ACID Properties
START TRANSACTION
COMMIT
ROLLBACK
SAVEPOINT
```

---

# 🗄️ PART 0 — CREATE OUR TABLES FIRST

Before performing any Views or Transactions, let's create our database tables.

To teach Transactions (which often deal with money), we are going to add one new column to our `students` table: **`fee_balance`**.

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
    fee_balance INT, -- Added for our transaction examples!
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
INSERT INTO students (student_id, first_name, dept_id, marks, fee_balance)
VALUES
(1, 'Rahul', 101, 85, 5000),
(2, 'Roshini', 102, 92, 5000),
(3, 'Yamini', 101, 70, 2000),
(4, 'k_Ramya', 103, 88, 3000),
(5, 'Reena', 102, 60, 1000),
(6, 'm_Ramya', 101, 95, 6000),
(7, 'Vaibhav', 102, 78, 4000),
(8, 'Vishal', 103, 90, 5000);
```

> **Important:** Run the `CREATE TABLE` statements first, then the `INSERT` statements.

---

# PART 1 — VIEWS

## 🧠 First, What Is a View?

A **View is a virtual table created from a SQL query.**

The most important thing to remember:

> **A View acts like a table, but it is NOT a new physical table.**

Think of a real table like a **room full of people**.

```text
students table
┌──────────────────────────────┐
│ Rahul                        │
│ Roshini                      │
│ Yamini                       │
│ Reena                        │
└──────────────────────────────┘
```

Now imagine we create a **window** to look into that room.

```text
students table
       ↓
   ┌─────────┐
   │ WINDOW  │
   └─────────┘
       ↓
      View
```

The window doesn't create another room or copy the people.

It simply gives us a different way to **look at the original room**.

That is exactly how a View works.

### Important:

A View:

* Does **not** create a new copy of the data.
* Does **not** store a separate set of rows like a normal table.
* Is basically a **saved SQL query**.
* Can be queried using `SELECT` just like a table.
* Shows data from the original/base table(s).

So we can say:

```text
TABLE
  ↓
Stores actual data

VIEW
  ↓
Stores the query
  ↓
Shows data from the original table(s)
```

### 🎯 Easy Definition

> **A View is a virtual table created from a saved SQL query. It behaves like a table when we query it, but it does not create a new physical table or copy the data.**

---

## 🎮 Interactive Question 1

Ask the students:

> "I want to hire a junior assistant to update student names, but I don't want them to see your `marks` or your `fee_balance`. How can I give them access to the data without compromising your privacy?"

Let them answer.

Expected answer:

> "Make a new table without those columns?"

**Teacher responds:**

"But if we make a new table, we have to copy all the data! And if a name changes in the new table, it won't automatically update the original table."

The better solution is to create a **VIEW**!

A View allows us to show only the columns we want without creating a completely new copy of the data.

---

# 1. Simple View

A **Simple View** is created from a **single base table**.

Think of it like:

```text
students table
      ↓
   Simple View
```

Only **one table** is involved.

### 💻 SQL Example: Creating a Secure View

Let's create a View that hides the sensitive columns (`marks` and `fee_balance`).

```sql
CREATE VIEW public_student_info AS
SELECT student_id, first_name, dept_id
FROM students;
```

Now the junior assistant can query the View just like a table:

```sql
SELECT * FROM public_student_info;
```

### Result:

| student_id | first_name | dept_id |
| ---------- | ---------- | ------: |
| 1          | Rahul      |     101 |
| 2          | Roshini    |     102 |
| 3          | Yamini     |     101 |
| ...        | ...        |     ... |

Notice:

```text
marks        → Hidden
fee_balance  → Hidden
```

The data is still inside the original `students` table.

We are simply using the View to show only the information we want.

---

## 🎤 Ask the Students

Ask:

> "Since this View is looking directly at the `students` table, what happens if I run an `UPDATE` on the View?"

```sql
UPDATE public_student_info
SET first_name = 'Rahul Sharma'
WHERE student_id = 1;
```

Expected answer:

> "The original `students` table should be updated!"

Exactly!

Because this is a **Simple View** based directly on one table, it can generally be updated.

So:

```text
UPDATE VIEW
     ↓
Underlying students table
     ↓
Data changes
```

### 🔥 Important Concept

The View is **not another copy of the data**.

For example:

```text
students table
┌─────────────────────────────┐
│ 1 | Rahul | 101 | 85 | 5000│
└─────────────────────────────┘
             ↑
             │
             │ View looks at this data
             │
┌─────────────────────────────┐
│ public_student_info         │
│ 1 | Rahul | 101             │
└─────────────────────────────┘
```

There aren't two separate copies of Rahul's data.

The View is simply showing selected information from the original table.

---

# 2. Complex View

If a Simple View is a window into **one room**, a **Complex View** is like creating a combined picture using information from **multiple rooms**.

In SQL, a Complex View can involve:

* Multiple tables
* `JOIN`
* Calculations
* Aggregations or other complex query logic

For our example, we have:

```text
students table
      +
departments table
      ↓
     JOIN
      ↓
Complex View
```

### 💻 SQL Example

Writing this JOIN every time can become annoying:

```sql
SELECT
    s.student_id,
    s.first_name,
    d.dept_name,
    s.marks
FROM students s
INNER JOIN departments d
    ON s.dept_id = d.dept_id;
```

Instead, we can save the query as a View:

```sql
CREATE VIEW student_department_view AS
SELECT
    s.student_id,
    s.first_name,
    d.dept_name,
    s.marks
FROM students s
INNER JOIN departments d
    ON s.dept_id = d.dept_id;
```

Now we can simply write:

```sql
SELECT *
FROM student_department_view;
```

We don't have to write the JOIN again.

### Think about it like this:

```text
students                    departments
   │                              │
   │                              │
   └────────── JOIN ──────────────┘
                  ↓
        student_department_view
```

The View gives us a convenient way to look at the combined information.

---

## 🔎 Filtering a Complex View

Because the View acts like a table when we query it, we can use `WHERE`:

```sql
SELECT *
FROM student_department_view
WHERE marks > 80;
```

So we can use the View almost like a normal table when retrieving data.

---

# ❓ Why is a Complex View Different?

The important difference is that the View is combining information from multiple tables.

For example:

```text
students
   │
   │ student information
   │
   ├──────── JOIN ────────┐
   │                      │
   │                      │
departments               │
   │                      │
   │ department info      │
   └──────────────────────┘
              ↓
       Complex View
```

If we try to update the Complex View, the database may not know exactly what we want to change.

For example:

```sql
UPDATE student_department_view
SET dept_name = 'Science'
WHERE first_name = 'Roshini';
```

What exactly do we mean?

Do we want:

```text
Roshini's department to change?
```

or:

```text
The entire department name "PIT" to change to "Science"?
```

Because the View combines information from `students` and `departments`, the operation can become ambiguous.

Therefore, **for this course, we treat Complex Views as read-only.**

---

# 🧠 Simple Way to Remember

```text
                VIEW
                  │
        ┌─────────┴─────────┐
        ↓                   ↓
   SIMPLE VIEW         COMPLEX VIEW
        ↓                   ↓
    1 TABLE          Multiple Tables
        ↓                   ↓
  Simple Query       JOIN / Complex Query
        ↓                   ↓
  Can generally       Mainly used for
    be updated          reading
```

### ⭐ One-Line Memory Trick

> **Simple View = One Table → Window into one table**

> **Complex View = Multiple Tables → Combined/Collage View**

### 🚨 Most Important Point

> **A View is NOT a new table. It is a saved query that behaves like a table when we use `SELECT`.**

```text
Normal Table
    ↓
Stores actual data

View
    ↓
Stores the query definition
    ↓
Shows data from original table(s)
```

---

# PART 2 — TRANSACTIONS (TCL)

Now we enter the world of Transaction Control Language (TCL).

## 🧠 First, What Is a Transaction?

Let's look at a real-world scenario using our `fee_balance`.

Imagine **Rahul** (ID 1) wants to transfer 1,000 rupees of his fee balance to his friend **Yamini** (ID 3) to help her out. 

To do this in SQL, we need **TWO** queries:
1. Deduct 1000 from Rahul.
2. Add 1000 to Yamini.

```sql
UPDATE students SET fee_balance = fee_balance - 1000 WHERE student_id = 1; -- Step 1
UPDATE students SET fee_balance = fee_balance + 1000 WHERE student_id = 3; -- Step 2
```

## 🎮 Interactive Question 2

Ask the students:
> "What happens if Step 1 executes perfectly (Rahul loses 1000), but right before Step 2 executes, the POWER GOES OUT and the server crashes?"

Let them answer.

Expected answer:
> "Rahul lost his money, but Yamini never got it! The money vanished into thin air!"

Exactly! This is a database nightmare. To prevent this, SQL uses **Transactions**. 

A transaction treats multiple SQL statements as a **single unit of work**. Either ALL steps succeed, or NONE of them succeed. **All or Nothing.**

---

# 1. The ACID Properties

To guarantee our money doesn't vanish, databases follow 4 rules called ACID:

1. **A - Atomicity:** "All or Nothing." If one step fails, the entire transaction rolls back.
2. **C - Consistency:** The database rules are never broken (e.g., fee_balance can't be negative).
3. **I - Isolation:** If two people try to transfer money at the exact same time, they won't interfere with each other.
4. **D - Durability:** Once the transaction is saved (Committed), it survives even if the power goes out a second later.

---

# 2. Transaction Commands (The Magic Words)

To use transactions, we use these commands:
1. `START TRANSACTION;` (Begins the safe zone)
2. `COMMIT;` (Saves the changes permanently)
3. `ROLLBACK;` (Undoes the changes like an "Undo" button)
4. `SAVEPOINT;` (A checkpoint)

Let's see them in action!

## 💻 Successful Transaction (COMMIT)

Let's safely transfer 1000 from Rahul to Yamini.

```sql
-- Open the safe zone
START TRANSACTION;

-- Step 1: Deduct from Rahul
UPDATE students SET fee_balance = fee_balance - 1000 WHERE first_name = 'Rahul';

-- Step 2: Add to Yamini
UPDATE students SET fee_balance = fee_balance + 1000 WHERE first_name = 'Yamini';

-- Both queries worked perfectly without power failure! Lock it in!
COMMIT;
```
Once we type `COMMIT`, the data is permanently saved to the hard drive. 

## 💻 Failed Transaction (ROLLBACK)

Let's say Roshini wants to transfer 2000 to Reena.

```sql
-- Open the safe zone
START TRANSACTION;

-- Step 1: Deduct from Roshini
UPDATE students SET fee_balance = fee_balance - 2000 WHERE first_name = 'Roshini';

-- OH NO! We just realized Reena's account is frozen or we made a typo!
-- Press the UNDO button!
ROLLBACK;
```

When we type `ROLLBACK`, the database completely undoes Step 1. Roshini gets her 2000 back instantly. The database is safe!

## 💻 Using SAVEPOINT (Checkpoints)

Sometimes a transaction is very long (e.g., grading 10 students). If the 10th one fails, you don't want to `ROLLBACK` and undo the first 9. You use a **Savepoint**!

```sql
START TRANSACTION;

-- Grade student 1
UPDATE students SET marks = 90 WHERE first_name = 'Rahul';

-- Create a checkpoint!
SAVEPOINT after_rahul;

-- Grade student 2
UPDATE students SET marks = 85 WHERE first_name = 'Yamini';

-- Create another checkpoint!
SAVEPOINT after_yamini;

-- Oops, we accidentally typed a letter instead of a number for Reena, this query fails!
UPDATE students SET marks = 'A+' WHERE first_name = 'Reena'; 

-- We only want to undo Reena's mistake, not Rahul and Yamini!
ROLLBACK TO after_yamini;

-- Now we can fix Reena's marks correctly
UPDATE students SET marks = 95 WHERE first_name = 'Reena';

-- Save everything to the hard drive
COMMIT;
```

---

# 🎯 Summary for the Board (TCL)

Write this on the board at the end of class:

1. **TRANSACTION:** A group of queries treated as "All or Nothing".
2. **ACID:** Atomicity, Consistency, Isolation, Durability.
3. **START TRANSACTION:** Begins the process.
4. **COMMIT:** "Save my work permanently."
5. **ROLLBACK:** "Undo everything since I started."
6. **SAVEPOINT:** "Create a checkpoint so I only have to undo a little bit."
