# Unit 3 Part 3: Relational Algebra & Calculus

Welcome to Part 3! 

Before SQL was invented, database scientists needed a mathematical way to describe how to retrieve data from tables. They created two formal languages: **Relational Algebra** and **Relational Calculus**.

Don't panic! It sounds like difficult math, but it is actually very simple. We just need to translate the math symbols into the SQL commands we already know.

---

# 1. Procedural vs. Declarative

There is a huge difference between Algebra and Calculus in databases.

### ⚙️ Relational Algebra is PROCEDURAL
It tells the database **HOW** to get the data, step-by-step. 
*(e.g., "First, go to the students table. Second, filter rows where marks > 80. Third, keep only the first_name column.")*

### 🗣️ Relational Calculus is DECLARATIVE (Non-Procedural)
It tells the database **WHAT** data you want, without caring about the steps to get it.
*(e.g., "Give me a list of student names who have marks greater than 80.")*

> **Fun Fact:** SQL is heavily based on Relational Calculus because you just say `SELECT first_name` (what you want) without telling the database the internal steps of how to find it!

---

# PART A: RELATIONAL ALGEBRA

Relational Algebra uses Greek symbols to perform operations on tables. There are **6 Fundamental Operators**. 

Let's learn them using our `students` table!

## 1. Selection ($\sigma$ - Sigma)
**What it does:** Filters specific **ROWS** based on a condition.
**SQL Equivalent:** The `WHERE` clause.

**Math Example:** 
Get all students who scored more than 80 marks.
> $\sigma_{marks > 80}(students)$

---

## 2. Projection ($\pi$ - Pi)
**What it does:** Selects specific **COLUMNS** and removes duplicates.
**SQL Equivalent:** The `SELECT` clause.

**Math Example:** 
Show only the first names and marks of the students.
> $\pi_{first\_name, marks}(students)$

### 🎮 Interactive Question 1

Ask the students:
> "If $\sigma$ (Sigma) filters ROWS, and $\pi$ (Pi) filters COLUMNS... How would I write the math formula to get just the **first names** of students who scored **more than 80 marks**?"

Let them try to guess!

Expected Answer:
> $\pi_{first\_name}(\sigma_{marks > 80}(students))$

**Teacher responds:**
"Exactly! You read it from the inside out. First, select the rows where marks > 80 ($\sigma$). Then, from that result, project only the first_name column ($\pi$)!"

---

## 3. Union ($\cup$)
**What it does:** Combines rows from two tables into one, removing duplicates.
**SQL Equivalent:** `UNION`.

**Math Example:** 
Get a list of all names from the `students` table and `alumni` table.
> $\pi_{first\_name}(students) \cup \pi_{first\_name}(alumni)$

---

## 4. Set Difference ($-$)
**What it does:** Returns rows that are in the first table, but NOT in the second table.
**SQL Equivalent:** `EXCEPT` or `NOT IN`.

**Math Example:** 
Find students in the computer club who are NOT in the sports club.
> $Computer\_Club - Sports\_Club$

---

## 5. Cartesian Product ($\times$ - Cross)
**What it does:** Combines EVERY row of Table A with EVERY row of Table B.
**SQL Equivalent:** `CROSS JOIN`.

**Math Example:** 
Combine the `students` table with the `departments` table. (If there are 10 students and 3 departments, this results in 30 rows).
> $students \times departments$

---

## 6. Rename ($\rho$ - Rho)
**What it does:** Renames a table or a column temporarily.
**SQL Equivalent:** `AS` (Aliasing).

**Math Example:** 
Rename the `students` table to `S`.
> $\rho_{S}(students)$

---

# 🎯 Summary for the Board (Algebra)

```text
RELATIONAL ALGEBRA → HOW to get data (Procedural)

1. Selection  (σ) : Filters ROWS (SQL: WHERE)
2. Projection (π) : Filters COLUMNS (SQL: SELECT)
3. Union      (∪) : Combines rows (SQL: UNION)
4. Difference (-) : Rows in A but not B (SQL: EXCEPT)
5. Cartesian  (×) : Combines everything (SQL: CROSS JOIN)
6. Rename     (ρ) : Renames tables/columns (SQL: AS)
```

---

# PART B: TUPLE RELATIONAL CALCULUS (TRC)

Unlike Algebra, **Calculus** does not tell the database *how* to filter the rows and columns. It just describes the final result you want.

## 🧠 Basic TRC Syntax

The basic formula looks like this:
> $\{t \mid P(t)\}$

**How to read it:**
- `{ }` means "A set of data".
- `t` means a "Tuple" (a row).
- `|` means "Such that".
- `P(t)` means the "Condition must be true".

So, read it in English:
> *"Give me a set of rows (`t`) such that (`|`) the condition is true (`P(t)`)."*

## 💻 TRC Example

Let's say we want all information about students who scored more than 80 marks.

In TRC, we write:
> $\{t \mid t \in students \text{ and } t.marks > 80 \}$

**Read in English:**
> *"Give me a set of rows (`t`), such that (`|`) the row belongs to the `students` table, AND the marks in that row are greater than 80."*

See? We didn't say "First go to the table, then use Sigma ($\sigma$) to filter." We just mathematically stated *what* we wanted! This is why SQL is so powerful—it is based on this declarative style!
