# Unit 3 Part 1: Relational Model Basics

Welcome to Unit 3! Until now, we have been focusing on writing SQL code. 

But where did SQL come from? SQL is based on a mathematical theory called the **Relational Model**, invented by Edgar F. Codd in 1970. 

In this unit, we are going to learn the theoretical and academic terms used to describe databases. 

---

# 1. The Vocabulary Translation

In academic exams and textbooks, they don't use simple words like "Table" or "Row". They use mathematical terms. 

You need to know how to translate them in your head.

### 🎯 The Big 4 Terms

| Academic Term | Simple English Meaning |
|---|---|
| **Relation** | A **Table** |
| **Tuple** | A **Row** (or a single record) |
| **Attribute** | A **Column** (or a field) |
| **Domain** | The **Allowed Values** for a column |

Let's look at our classroom table to see these in action.

---

# 2. Classroom Example

Look at this `students` table:

```text
┌────────────────────────────────────────────────────────┐
│                        RELATION                        │
├────────────┬─────────────┬─────────┬───────┬───────────┤
│ student_id │ first_name  │ dept_id │ marks │ fee_balance│  ← ATTRIBUTES
├────────────┼─────────────┼─────────┼───────┼───────────┤
│ 1          │ Rahul       │ 101     │ 85    │ 5000      │  ← TUPLE 1
│ 2          │ Roshini     │ 102     │ 92    │ 5000      │  ← TUPLE 2
│ 3          │ Yamini      │ 101     │ 70    │ 2000      │  ← TUPLE 3
└────────────┴─────────────┴─────────┴───────┴───────────┘
```

### Breakdown:
1. **Relation:** The entire `students` table is called a Relation. Why? Because it relates specific data together.
2. **Attributes:** The columns `first_name`, `marks`, etc., are Attributes. They describe the properties of a student.
3. **Tuple:** A single row (e.g., `1 | Rahul | 101 | 85 | 5000`) is a Tuple. (Pronounced *tu-puhl* or *too-puhl*). 

## 🧠 What is a Domain?

A **Domain** is the set of all possible, valid values that an Attribute (column) can hold. 

For example, look at the `marks` attribute. 
Can a student get "Apple" marks? No. 
Can a student get -50 marks? No.
Can a student get 101 marks? Usually, no (if the exam is out of 100).

Therefore, the **Domain** of the `marks` attribute is:
> *Whole numbers between 0 and 100.*

If you try to insert `marks = 999`, the database should reject it because it violates the Domain constraints.

---

# 3. Schema vs. Instance

This is a very common exam question. What is the difference between a Schema and an Instance?

## 🏛️ The Schema (The Blueprint)

The **Schema** is the logical structure or design of the database. 
- It defines the table names, column names, and their data types.
- It is created using `CREATE TABLE`.
- **It rarely changes.**

Think of the Schema as the **blueprint of a classroom**. It says "There are 30 desks, a whiteboard, and a projector."

Example of the `students` Schema:
```text
students (student_id INT, first_name VARCHAR, dept_id INT, marks INT)
```

## 📸 The Instance (The Snapshot)

The **Instance** is the actual data stored in the database **at a specific moment in time**.
- It is modified using `INSERT`, `UPDATE`, and `DELETE`.
- **It changes constantly.**

Think of the Instance as a **photograph of the classroom taken today at 10:00 AM**. Yesterday, Rahul was sitting in the front row. Today, Rahul is absent. The blueprint of the room (Schema) is exactly the same, but the people inside it (Instance) have changed!

---

# 🎮 Interactive Question 1

Ask the students:

> "If I run the command `TRUNCATE TABLE students;`, which deletes all the rows inside the table... did I just destroy the **Schema** or the **Instance**?"

Let them answer.

Expected answer:
> "You destroyed the Instance!"

**Teacher responds:**
"Exactly! The blueprint (Schema) of the `students` table is still there, ready to accept new data. But the snapshot of the data (Instance) is completely empty!"

---

# 🎯 Summary for the Board

Write this on the board for quick memorization:

```text
Relation  = Table
Tuple     = Row
Attribute = Column
Domain    = Allowed rules for the column

Schema    = The Blueprint (Does not change)
Instance  = The Live Data (Changes every second)
```
