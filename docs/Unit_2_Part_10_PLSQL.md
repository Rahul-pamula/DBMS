# Unit 2 Part 10: Introduction to PL/SQL

Welcome to Part 10!

Until now, we have mostly been using **SQL**.

SQL is very good at asking the database questions such as:

```sql
SELECT *
FROM students;
```

or changing data:

```sql
UPDATE students
SET marks = 90
WHERE student_id = 1;
```

But SQL mainly tells the database **WHAT we want**.

What if we want to tell the database:

* If marks are greater than 40, say "Pass"
* Otherwise, say "Fail"
* Repeat something 10 times
* Store a value in a variable
* Handle an error
* Process students one by one

Now we need **programming logic**.

That's where **PL/SQL** comes in.

---

# 🎯 Today's Goal

By the end of this lesson, we should understand:

```text
PL/SQL
   ↓
Blocks
   ↓
Variables
   ↓
IF / CASE
   ↓
Loops
   ↓
Nested Blocks
   ↓
Exception Handling
   ↓
Cursors
```

---

# PART 1 — What is PL/SQL?

## 🧠 First, understand the problem

Imagine I ask SQL:

> "Give me Rahul's marks."

SQL can do that:

```sql
SELECT marks
FROM students
WHERE first_name = 'Rahul';
```

But suppose I say:

> "Get Rahul's marks. If the marks are 40 or above, print `PASS`. Otherwise print `FAIL`."

Now we need **decision-making logic**.

SQL by itself is not designed for this kind of procedural programming.

We need something that combines:

```text
Database + Programming Logic
```

That is **PL/SQL**.

---

# 🧠 What does PL/SQL mean?

**PL/SQL = Procedural Language extension to SQL**

It allows us to write programming logic inside the Oracle database.

It gives us things such as:

* Variables
* IF / ELSE
* CASE
* Loops
* Exception handling
* Cursors
* SQL statements

So think:

```text
SQL
↓
Talk to the database

PL/SQL
↓
SQL + Programming Logic
```

---

# ⭐ Easy Definition

> **PL/SQL is Oracle's procedural programming language that extends SQL by adding programming features such as variables, conditions, loops, and exception handling.**

---

# 🧠 SQL vs PL/SQL

This is one of the most important things to understand.

### SQL

SQL mainly answers:

> **WHAT data do I want?**

Example:

```sql
SELECT marks
FROM students
WHERE student_id = 1;
```

We are saying:

> "Give me the marks of student 1."

---

### PL/SQL

PL/SQL can answer:

> **WHAT do I want AND WHAT SHOULD I DO WITH IT?**

Example:

```text
Get Rahul's marks
      ↓
Check marks
      ↓
If marks >= 40
      ↓
Print "PASS"
Otherwise
      ↓
Print "FAIL"
```

So:

```text
SQL
= WHAT

PL/SQL
= WHAT + LOGIC
```

---

# 🏗️ How PL/SQL Works

When we send a PL/SQL block to Oracle:

```text
Client
   ↓
Oracle Database
   ↓
PL/SQL Engine
   ↓
┌──────────────────────┐
│ Programming Logic    │
│ IF                   │
│ LOOP                 │
│ Variables            │
└──────────────────────┘
          +
┌──────────────────────┐
│ SQL Statements       │
│ SELECT               │
│ INSERT               │
│ UPDATE               │
│ DELETE               │
└──────────────────────┘
```

The PL/SQL engine handles the procedural logic and works with the SQL engine for SQL statements.

---

# PART 2 — PL/SQL Block Structure

## 🧠 What is a Block?

A **PL/SQL program is written inside a block**.

Think of a block as a **container for our program**.

A block can have four parts:

```text
┌──────────────────────────┐
│ DECLARE                  │
│ Variables                │
├──────────────────────────┤
│ BEGIN                    │
│ Actual program logic     │
├──────────────────────────┤
│ EXCEPTION                │
│ Error handling           │
├──────────────────────────┤
│ END;                     │
└──────────────────────────┘
```

Remember:

```text
DECLARE   → Prepare
BEGIN     → Execute
EXCEPTION → Handle errors
END       → Finish
```

---

# 1. DECLARE

`DECLARE` is where we create variables.

It is **optional**.

Example:

```sql
DECLARE
    v_name VARCHAR2(50);
```

We are basically saying:

> "Oracle, I need a box called `v_name` that can store text."

Think:

```text
DECLARE

v_name
┌─────────────┐
│             │
└─────────────┘
```

---

# 2. BEGIN

`BEGIN` is where the actual program starts running.

It is **mandatory**.

Example:

```sql
BEGIN
    DBMS_OUTPUT.PUT_LINE('Hello');
```

Think:

> "Now start executing my instructions."

---

# 3. EXCEPTION

`EXCEPTION` is used when something goes wrong.

It is **optional**.

Example:

```sql
EXCEPTION
    WHEN ZERO_DIVIDE THEN
        DBMS_OUTPUT.PUT_LINE('Cannot divide by zero');
```

Think:

> "If something goes wrong, come here and handle it."

---

# 4. END

`END;` tells Oracle:

> "The block is finished."

It is **mandatory**.

---

# ⭐ Easy Memory Trick

```text
DECLARE
   ↓
Prepare

BEGIN
   ↓
Do the work

EXCEPTION
   ↓
Handle problems

END;
   ↓
Finish
```

---

# Example 1 — Simplest PL/SQL Block

```sql
BEGIN
    DBMS_OUTPUT.PUT_LINE('Hello World');
END;
/
```

Let's understand it line by line.

### `BEGIN`

Start the PL/SQL program.

### `DBMS_OUTPUT.PUT_LINE`

Print something.

```sql
DBMS_OUTPUT.PUT_LINE('Hello World');
```

### `END;`

Finish the block.

### `/`

The `/` tells the Oracle client to execute the completed PL/SQL block.

---

# Example 2 — Using a Variable

```sql
DECLARE
    v_message VARCHAR2(50);
BEGIN
    v_message := 'Welcome to PL/SQL';

    DBMS_OUTPUT.PUT_LINE(v_message);
END;
/
```

Understand the flow:

```text
DECLARE
   ↓
Create v_message

BEGIN
   ↓
Put "Welcome to PL/SQL" inside it

   ↓
Print v_message

END
   ↓
Finish
```

---

# ⚠️ Important: `:=` vs `=`

This is very important.

In PL/SQL:

```sql
:=
```

means:

> **Assign a value**

Example:

```sql
v_marks := 90;
```

Means:

> Put `90` inside `v_marks`.

Whereas:

```sql
=
```

is used for comparison/equality.

Think:

```text
:=  → Give a value

=   → Compare
```

---

# Example 3 — Getting Data from a Table

PL/SQL can also execute SQL.

Suppose we want Rahul's name.

```sql
DECLARE
    v_student_name VARCHAR2(50);
BEGIN

    SELECT first_name
    INTO v_student_name
    FROM students
    WHERE student_id = 1;

    DBMS_OUTPUT.PUT_LINE(
        'Student is: ' || v_student_name
    );

END;
/
```

The important new concept is:

```sql
SELECT first_name
INTO v_student_name
FROM students
WHERE student_id = 1;
```

Normally in SQL we write:

```sql
SELECT first_name
FROM students;
```

But inside PL/SQL, if we want to put the result into a variable, we use:

```text
SELECT
   ↓
INTO variable
   ↓
FROM
```

So:

```text
Database
   ↓
first_name
   ↓
v_student_name
   ↓
PL/SQL variable
```

---

# 🧠 Why do we need INTO?

Because PL/SQL wants to know:

> "Where should I store the result?"

Example:

```sql
SELECT first_name
INTO v_student_name
FROM students
WHERE student_id = 1;
```

Means:

> Find the student's first name and put it into `v_student_name`.

---

# Example 4 — Doing Mathematics

```sql
DECLARE
    v_num1 NUMBER := 10;
    v_num2 NUMBER := 20;
    v_sum NUMBER;
BEGIN
    v_sum := v_num1 + v_num2;

    DBMS_OUTPUT.PUT_LINE(
        'Sum: ' || v_sum
    );
END;
/
```

Flow:

```text
v_num1 = 10
v_num2 = 20

      ↓

v_sum = 10 + 20

      ↓

v_sum = 30
```

---

# Example 5 — Handling an Error

Suppose:

```sql
10 / 0
```

This causes an error.

Instead of allowing the program to crash, we can handle it.

```sql
DECLARE
    v_result NUMBER;
BEGIN

    v_result := 10 / 0;

EXCEPTION

    WHEN ZERO_DIVIDE THEN
        DBMS_OUTPUT.PUT_LINE(
            'Cannot divide by zero!'
        );

END;
/
```

Flow:

```text
BEGIN
   ↓
10 / 0
   ↓
ERROR!
   ↓
EXCEPTION
   ↓
ZERO_DIVIDE
   ↓
Print message
```

---

# PART 3 — Variables, Constants and Operators

## 🧠 What is a Variable?

A variable is like a **box in memory that can hold a value**.

```text
v_marks
┌──────────┐
│    85    │
└──────────┘
```

We can later change it:

```text
v_marks
┌──────────┐
│    95    │
└──────────┘
```

So:

> **Variable = value can change.**

---

# Creating a Variable

```sql
DECLARE
    v_marks NUMBER;
```

Assigning a value:

```sql
v_marks := 85;
```

Changing it:

```sql
v_marks := 95;
```

---

# 🧠 What is a Constant?

A constant is a value that **cannot be changed after it is assigned**.

Example:

```sql
DECLARE
    c_pi CONSTANT NUMBER := 3.14159;
```

Think:

```text
Variable
   ↓
Can change

Constant
   ↓
Cannot change
```

---

# Common PL/SQL Operators

| Operator | Meaning             |   |                          |
| -------- | ------------------- | - | ------------------------ |
| `:=`     | Assignment          |   |                          |
| `=`      | Equality/comparison |   |                          |
| `<>`     | Not equal           |   |                          |
| `||`     | Join/concatenate strings |

*(Note: corrected the empty cell for `||` based on context)*

Example:

```sql
v_name := 'Rahul';
```

And:

```sql
'Student: ' || v_name
```

produces:

```text
Student: Rahul
```

---

# ⭐ `%TYPE`

Sometimes we don't want to manually specify a variable's datatype.

Suppose:

```text
students.student_id
```

has a particular datatype.

We can make our PL/SQL variable use the same datatype:

```sql
DECLARE
    v_id students.student_id%TYPE;
```

Think:

```text
students.student_id
        ↓
       %TYPE
        ↓
v_id uses the same datatype
```

This is useful because if the table column's datatype changes, our declaration can remain aligned with the column.

---

# PART 4 — Conditional Statements

Now PL/SQL becomes much more like normal programming.

## 🧠 What is a Condition?

A condition allows the program to **make a decision**.

Imagine:

```text
Student gets marks
       ↓
Are marks >= 40?
     /       \
   YES       NO
    ↓         ↓
  PASS       FAIL
```

This is an `IF`.

---

# Example 1 — IF

```sql
DECLARE
    v_score NUMBER := 85;
BEGIN

    IF v_score >= 40 THEN
        DBMS_OUTPUT.PUT_LINE('Pass');
    END IF;

END;
/
```

Read it like English:

> If the score is greater than or equal to 40, then print "Pass".

---

# Example 2 — IF ELSE

```sql
DECLARE
    v_score NUMBER := 30;
BEGIN

    IF v_score >= 40 THEN
        DBMS_OUTPUT.PUT_LINE('Pass');
    ELSE
        DBMS_OUTPUT.PUT_LINE('Fail');
    END IF;

END;
/
```

Flow:

```text
             v_score
                ↓
          Is score >= 40?
           /           \
        YES             NO
         ↓               ↓
       Pass             Fail
```

---

# Example 3 — IF ELSIF ELSE

Suppose we want grades:

```text
90+ → A
70+ → B
50+ → C
Below 50 → F
```

```sql
DECLARE
    v_score NUMBER := 75;
BEGIN

    IF v_score >= 90 THEN
        DBMS_OUTPUT.PUT_LINE('Grade: A');

    ELSIF v_score >= 70 THEN
        DBMS_OUTPUT.PUT_LINE('Grade: B');

    ELSIF v_score >= 50 THEN
        DBMS_OUTPUT.PUT_LINE('Grade: C');

    ELSE
        DBMS_OUTPUT.PUT_LINE('Grade: F');

    END IF;

END;
/
```

### ⚠️ Remember

In PL/SQL it is:

```text
ELSIF
```

Not:

```text
ELSE IF
```

---

# Checking NULL

Never write:

```sql
v_name = NULL
```

Instead use:

```sql
v_name IS NULL
```

Example:

```sql
IF v_name IS NULL THEN
    DBMS_OUTPUT.PUT_LINE('Name is missing');
END IF;
```

---

# CASE

`CASE` is another way of making decisions.

Example:

```sql
DECLARE
    v_grade CHAR(1) := 'B';
BEGIN

    CASE v_grade

        WHEN 'A' THEN
            DBMS_OUTPUT.PUT_LINE('Excellent');

        WHEN 'B' THEN
            DBMS_OUTPUT.PUT_LINE('Good');

        WHEN 'C' THEN
            DBMS_OUTPUT.PUT_LINE('Average');

        ELSE
            DBMS_OUTPUT.PUT_LINE('Unknown Grade');

    END CASE;

END;
/
```

Think:

```text
grade
  ↓
 A → Excellent
 B → Good
 C → Average
```

---

# PART 5 — Loops

## 🧠 What is a Loop?

A loop means:

> **Repeat something multiple times.**

Real-life example:

```text
Print "Hello" 5 times
```

Instead of writing:

```text
Print
Print
Print
Print
Print
```

we can use a loop.

PL/SQL provides:

1. Basic `LOOP`
2. `WHILE LOOP`
3. `FOR LOOP`

---

# 1. Basic LOOP

```sql
DECLARE
    v_counter NUMBER := 1;
BEGIN

    LOOP

        DBMS_OUTPUT.PUT_LINE(
            'Counter: ' || v_counter
        );

        v_counter := v_counter + 1;

        EXIT WHEN v_counter > 5;

    END LOOP;

END;
/
```

Flow:

```text
1
↓
2
↓
3
↓
4
↓
5
↓
STOP
```

The important part is:

```sql
EXIT WHEN v_counter > 5;
```

Without an exit condition, a basic loop can continue indefinitely.

---

# 2. WHILE LOOP

A `WHILE` loop means:

> Keep running **while the condition is TRUE**.

```sql
DECLARE
    v_counter NUMBER := 1;
BEGIN

    WHILE v_counter <= 5 LOOP

        DBMS_OUTPUT.PUT_LINE(
            'Counter: ' || v_counter
        );

        v_counter := v_counter + 1;

    END LOOP;

END;
/
```

Think:

```text
Is condition TRUE?
      ↓
     YES
      ↓
Run code
      ↓
Check again
```

---

# 3. FOR LOOP

A `FOR` loop is useful when we know how many times we want to repeat something.

```sql
BEGIN

    FOR i IN 1..5 LOOP

        DBMS_OUTPUT.PUT_LINE(i);

    END LOOP;

END;
/
```

Output:

```text
1
2
3
4
5
```

The `FOR` loop automatically handles the counter.

So:

```text
Basic LOOP
→ You control everything

WHILE
→ Condition controls the loop

FOR
→ Range controls the loop
```

---

# PART 6 — Nested Blocks

## 🧠 What is a Nested Block?

A nested block means:

> **A PL/SQL block inside another PL/SQL block.**

Think:

```text
Outer Block
┌──────────────────────────┐
│                          │
│   Inner Block            │
│   ┌──────────────────┐   │
│   │                  │   │
│   └──────────────────┘   │
│                          │
└──────────────────────────┘
```

Example:

```sql
DECLARE
    v_outer VARCHAR2(20) := 'Outer Value';

BEGIN

    DBMS_OUTPUT.PUT_LINE(v_outer);

    DECLARE
        v_inner VARCHAR2(20) := 'Inner Value';

    BEGIN

        DBMS_OUTPUT.PUT_LINE(v_outer);
        DBMS_OUTPUT.PUT_LINE(v_inner);

    END;

END;
/
```

---

# 🧠 Scoping Rule

This is very important.

### Inner can see Outer

```text
Outer variable
      ↓
Inner can use it
```

### Outer cannot see Inner

```text
Inner variable
      ↓
Outer cannot use it
```

Think of it like rooms:

```text
OUTER ROOM
┌─────────────────────────┐
│ v_outer                 │
│                         │
│   INNER ROOM             │
│   ┌─────────────────┐   │
│   │ v_inner         │   │
│   └─────────────────┘   │
│                         │
└─────────────────────────┘
```

The person inside the inner room can see the outer room.

But someone outside cannot see what's inside the private inner room.

---

# Variable Shadowing

Suppose both blocks have a variable called `v_name`.

```sql
DECLARE
    v_name VARCHAR2(20) := 'Rahul';

BEGIN

    DECLARE
        v_name VARCHAR2(20) := 'Amit';

    BEGIN
        DBMS_OUTPUT.PUT_LINE(v_name);
    END;

    DBMS_OUTPUT.PUT_LINE(v_name);

END;
/
```

Output:

```text
Amit
Rahul
```

Why?

Inside the inner block:

```text
v_name → Amit
```

Outside:

```text
v_name → Rahul
```

The inner variable temporarily **shadows** the outer variable.

---

# PART 7 — Exception Handling

## 🧠 What is an Exception?

An exception is an **error that occurs while the PL/SQL program is running**.

Examples:

```text
Divide by zero
       ↓
ZERO_DIVIDE

No matching row
       ↓
NO_DATA_FOUND

Too many rows
       ↓
TOO_MANY_ROWS
```

---

# Why do we need Exception Handling?

Imagine:

```sql
v_result := 10 / 0;
```

The program encounters an error.

Without exception handling:

```text
Program
   ↓
ERROR
   ↓
Crash
```

With exception handling:

```text
Program
   ↓
ERROR
   ↓
EXCEPTION section
   ↓
Handle the problem
   ↓
Display useful message
```

---

# Common Exceptions

### 1. `NO_DATA_FOUND`

A `SELECT INTO` doesn't find a row.

```sql
SELECT first_name
INTO v_name
FROM students
WHERE student_id = 99999;
```

If that student doesn't exist:

```text
NO_DATA_FOUND
```

---

### 2. `TOO_MANY_ROWS`

`SELECT INTO` expects a single result, but the query returns multiple rows.

```sql
SELECT first_name
INTO v_name
FROM students;
```

If multiple students exist:

```text
TOO_MANY_ROWS
```

---

### 3. `ZERO_DIVIDE`

```sql
10 / 0
```

produces:

```text
ZERO_DIVIDE
```

---

### 4. `OTHERS`

```sql
WHEN OTHERS THEN
```

This is used to catch other errors that weren't handled specifically.

---

# Example — Handling NO_DATA_FOUND

```sql
DECLARE
    v_name students.first_name%TYPE;

BEGIN

    SELECT first_name
    INTO v_name
    FROM students
    WHERE student_id = 99999;

    DBMS_OUTPUT.PUT_LINE(v_name);

EXCEPTION

    WHEN NO_DATA_FOUND THEN
        DBMS_OUTPUT.PUT_LINE(
            'Error: Student does not exist!'
        );

END;
/
```

Flow:

```text
SELECT
  ↓
No student found
  ↓
NO_DATA_FOUND
  ↓
EXCEPTION
  ↓
Print message
```

---

# User-Defined Exception

We can also create our own exception.

Example:

```sql
DECLARE

    e_invalid_age EXCEPTION;
    v_age NUMBER := 16;

BEGIN

    IF v_age < 18 THEN
        RAISE e_invalid_age;
    END IF;

    DBMS_OUTPUT.PUT_LINE(
        'Admission Granted'
    );

EXCEPTION

    WHEN e_invalid_age THEN
        DBMS_OUTPUT.PUT_LINE(
            'Error: Student is under 18!'
        );

END;
/
```

Think:

```text
Our condition
     ↓
We don't like the value
     ↓
RAISE our own exception
     ↓
EXCEPTION section
     ↓
Handle it
```

---

# PART 8 — Cursors

## 🧠 Why do we need a Cursor?

This is where students usually get confused, so let's start with the problem.

Suppose we write:

```sql
SELECT first_name
FROM students;
```

What if there are 1,000 students?

We cannot put 1,000 names into one normal variable.

Remember:

```sql
SELECT first_name
INTO v_name
FROM students;
```

`v_name` is designed to hold one value.

So if the query returns many rows, we need another mechanism.

That mechanism is a **Cursor**.

---

# 🧠 What is a Cursor?

A Cursor allows PL/SQL to process the rows returned by a query **one row at a time**.

Think of a cursor like a **pointer moving through a list**.

```text
Students:

Row 1 → Rahul
          ↑
        Cursor

Row 2 → Roshini

Row 3 → Yamini

Row 4 → Reena
```

Then the cursor moves:

```text
Rahul
  ↓
Roshini
  ↓
Yamini
  ↓
Reena
```

---

# Two Types of Cursors

```text
CURSORS
   │
   ├── Implicit
   │
   └── Explicit
```

---

# 1. Implicit Cursor

Oracle creates it automatically when we execute DML such as:

```sql
UPDATE
INSERT
DELETE
```

Example:

```sql
BEGIN

    UPDATE students
    SET marks = marks + 5
    WHERE dept_id = 1;

    DBMS_OUTPUT.PUT_LINE(
        SQL%ROWCOUNT || ' rows updated.'
    );

    COMMIT;

END;
/
```

Oracle automatically keeps information about the operation.

For example:

```sql
SQL%ROWCOUNT
```

tells us how many rows were affected.

---

# 2. Explicit Cursor

An Explicit Cursor is created manually by the programmer.

We use it when we want to process multiple rows one by one.

Example:

```sql
DECLARE

    CURSOR c_students IS
        SELECT first_name
        FROM students
        WHERE dept_id = 1;

    v_name students.first_name%TYPE;

BEGIN

    OPEN c_students;

    LOOP

        FETCH c_students INTO v_name;

        EXIT WHEN c_students%NOTFOUND;

        DBMS_OUTPUT.PUT_LINE(
            'Student: ' || v_name
        );

    END LOOP;

    CLOSE c_students;

END;
/
```

---

# 🧠 Understand Cursor Using 5 Steps

Don't memorize the code blindly.

Remember:

```text
1. DECLARE
       ↓
   Create cursor

2. OPEN
       ↓
   Run the query

3. FETCH
       ↓
   Get one row

4. CHECK
       ↓
   Are there more rows?

5. CLOSE
       ↓
   Finish
```

So:

```text
DECLARE
   ↓
OPEN
   ↓
FETCH
   ↓
FETCH
   ↓
FETCH
   ↓
...
   ↓
CLOSE
```

---

# Cursor FOR LOOP

PL/SQL gives us a much easier way.

Instead of manually doing:

```text
OPEN
FETCH
EXIT
CLOSE
```

we can use a Cursor `FOR` loop.

```sql
DECLARE

    CURSOR c_students IS
        SELECT first_name
        FROM students
        WHERE dept_id = 2;

BEGIN

    FOR student_rec IN c_students LOOP

        DBMS_OUTPUT.PUT_LINE(
            'Student: ' || student_rec.first_name
        );

    END LOOP;

END;
/
```

Oracle automatically handles the cursor operations for us.

Think:

```text
Normal Explicit Cursor

DECLARE
OPEN
FETCH
EXIT
CLOSE


Cursor FOR LOOP

FOR
 ↓
Oracle handles
OPEN + FETCH + EXIT + CLOSE
```

---

# 🎯 FINAL BIG PICTURE

Don't try to memorize 60 examples.

First understand **why each feature exists**.

```text
                    PL/SQL
                       │
          ┌────────────┴────────────┐
          │                         │
        SQL                   Programming Logic
          │                         │
     SELECT/INSERT             Variables
     UPDATE/DELETE             IF / CASE
                               LOOPS
                               EXCEPTIONS
                               CURSORS
```

Then:

```text
PL/SQL BLOCK
     │
     ├── DECLARE
     │      ↓
     │   Variables
     │
     ├── BEGIN
     │      ↓
     │   Actual logic
     │
     ├── EXCEPTION
     │      ↓
     │   Error handling
     │
     └── END
```

---

# 🧠 The 7 Things You Must Remember

### 1. PL/SQL

> **SQL + Programming Logic**

---

### 2. DECLARE

> **Create variables before using them.**

---

### 3. BEGIN

> **The actual program execution starts here.**

---

### 4. IF / CASE

> **Used for decision making.**

---

### 5. LOOP

> **Used for repetition.**

---

### 6. EXCEPTION

> **Used to handle errors.**

---

### 7. CURSOR

> **Used to process multiple rows one by one.**

---

# ⭐ One Final Example Combining Everything

Now let's put the ideas together.

Suppose we want to process students and determine whether they passed.

```sql
DECLARE

    CURSOR c_students IS
        SELECT first_name, marks
        FROM students;

BEGIN

    FOR student_rec IN c_students LOOP

        IF student_rec.marks >= 40 THEN

            DBMS_OUTPUT.PUT_LINE(
                student_rec.first_name || ' → PASS'
            );

        ELSE

            DBMS_OUTPUT.PUT_LINE(
                student_rec.first_name || ' → FAIL'
            );

        END IF;

    END LOOP;

EXCEPTION

    WHEN OTHERS THEN
        DBMS_OUTPUT.PUT_LINE(
            'Something went wrong.'
        );

END;
/
```

Look at what we just used:

```text
PL/SQL
  │
  ├── DECLARE
  │      ↓
  │   Cursor
  │
  ├── BEGIN
  │      ↓
  │   FOR LOOP
  │      ↓
  │   IF / ELSE
  │
  ├── EXCEPTION
  │      ↓
  │   Error handling
  │
  └── END
```

This is the real purpose of PL/SQL:

> **Instead of only asking the database for data, we can write actual programming logic that works with the database data.**

---

# 🎓 Teacher's Quick Explanation

When teaching this chapter, say it in this order:

> "Until now, we used SQL to communicate with the database. SQL is excellent for retrieving and changing data, but we also need programming logic."

> "For example, if marks are greater than 40, print PASS; otherwise print FAIL. That's programming logic."

> "Oracle gives us PL/SQL, which combines SQL with programming features."

Then draw:

```text
SQL
+
Programming Logic
=
PL/SQL
```

Then explain:

```text
DECLARE   → What do I need?
BEGIN     → What should I do?
EXCEPTION → What if something goes wrong?
END       → I'm finished.
```

Then teach:

```text
Variables → Store information

IF/CASE  → Make decisions

Loops    → Repeat work

Exceptions → Handle errors

Cursors  → Process many rows
```

If students understand **why each feature exists**, the syntax becomes much easier to learn.

# 🚨 Don't Memorize — Understand

For this chapter, the most important thing is not memorizing 60 programs.

Remember this story:

```text
I need programming logic inside my database
                ↓
             PL/SQL
                ↓
          I need variables
                ↓
          DECLARE
                ↓
          I need to execute
                ↓
            BEGIN
                ↓
          I need decisions
                ↓
          IF / CASE
                ↓
          I need repetition
                ↓
             LOOPS
                ↓
          Something failed
                ↓
          EXCEPTION
                ↓
       I have many rows
                ↓
            CURSOR
                ↓
             END
```

**If you can explain that story to your students, you understand the foundation of PL/SQL.**
