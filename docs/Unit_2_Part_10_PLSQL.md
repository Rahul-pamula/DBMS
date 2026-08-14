# Unit 2 Part 10: Introduction to MySQL Stored Programs (Procedural SQL)

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

* If marks are greater than 40, print "Pass"
* Otherwise, print "Fail"
* Repeat something 10 times
* Store a value in a variable
* Handle an error
* Process students one by one

Now we need **programming logic**. 

---

# 🚨 IMPORTANT TEACHING CLARIFICATION

You might have heard the term **PL/SQL** on the internet. 

**PL/SQL is Oracle's specific procedural language.**

Since we are using **MySQL**, we will use **MySQL Stored Programs** (often called Stored Procedures). 

The concepts are very similar, but the syntax is different. Do not confuse the two!

**Oracle Database** → PL/SQL
**MySQL Database** → Stored Programs / Stored Procedures

Both provide:
- Variables
- Conditions (IF / ELSE)
- Loops
- Error handling
- Cursors
- SQL + programming logic

In this lesson, **every example is written in MySQL.**

---

# 🎯 Today's Goal

By the end of this lesson, we should understand:

```text
MySQL Stored Procedures
   ↓
DELIMITER and Structure
   ↓
Variables
   ↓
SELECT ... INTO
   ↓
IF / CASE
   ↓
Loops (WHILE, LOOP, REPEAT)
   ↓
Exception Handling (Handlers)
   ↓
Cursors
```

---

# PART 1 — What is a Stored Program?

## 1. What is it?
A Stored Program is a block of programming logic that runs inside the MySQL database server.

## 2. Why do we need it?
Imagine I say:
> "Get Rahul's marks. If the marks are 40 or above, print `PASS`. Otherwise print `FAIL`."

SQL by itself is not designed for this kind of procedural decision-making. We need something that combines:

```text
Database + Programming Logic
```

## 3. Simple Real-World Analogy
Think of a standard SQL query as ordering food from a menu. You just point and say, "I want that." (WHAT).

A Stored Procedure is like giving the chef a **recipe**. You tell them, "Get these ingredients (variables), check if the oven is hot (IF), stir 10 times (LOOP), and if you drop an egg, get a new one (Error Handling)."

So:
```text
SQL
= WHAT

MySQL Stored Programs
= WHAT + LOGIC
```

---

# PART 2 — Block Structure & The DELIMITER

In MySQL, we put our logic inside a **Stored Procedure**. 

## 1. What is the DELIMITER?
Normally in MySQL, every statement ends with a semicolon `;`. 
When we write a Stored Procedure, we use many semicolons inside it. If we don't change the delimiter, MySQL will try to run the procedure before we finish writing it!

So we temporarily change the end-of-statement marker to `//`.

## 2. Basic Syntax
```sql
DELIMITER //

CREATE PROCEDURE procedure_name()
BEGIN
    -- Programming logic goes here
END //

DELIMITER ;
```

## 3. Simple Classroom Example

Let's write a procedure that prints "Hello Students". (Since MySQL doesn't have a built-in print command like Python, we use `SELECT` to print output to the screen).

```sql
DELIMITER //

CREATE PROCEDURE say_hello()
BEGIN
    SELECT 'Hello Students' AS Message;
END //

DELIMITER ;
```

To run it, we use the `CALL` command:
```sql
CALL say_hello();
```

## 4. Expected Output
| Message |
| --- |
| Hello Students |

## 5. 🧠 Remember This
> **Always use `DELIMITER //` before creating a procedure, and `DELIMITER ;` after. Run it using `CALL procedure_name();`**

---

# PART 3 — Variables

## 1. What is a variable?
A variable is like a box in memory that stores a value. The value inside the box can change while the program runs.

## 2. Why do we need it?
We need variables to temporarily hold math calculations, student IDs, or query results so we can check them later.

## 3. Basic Syntax
In MySQL, we prepare the variable using `DECLARE`, and we change its value using `SET`.

```sql
DECLARE variable_name DATATYPE DEFAULT value;
SET variable_name = new_value;
```

## 4. Simple Classroom Example

```sql
DELIMITER //

CREATE PROCEDURE check_math()
BEGIN
    -- Create variables
    DECLARE v_score INT DEFAULT 85;
    DECLARE v_bonus INT DEFAULT 5;
    DECLARE v_total INT;

    -- Change value using SET
    SET v_total = v_score + v_bonus;

    -- Print the result
    SELECT v_total AS FinalScore;
END //

DELIMITER ;

CALL check_math();
```

## 5. Line-by-Line Explanation
- `DECLARE v_score INT DEFAULT 85;` → Creates a box named `v_score`, sets it to integer, and puts 85 inside it.
- `SET v_total = v_score + v_bonus;` → Adds the two boxes together and stores the answer (90) inside `v_total`.

## 6. Expected Output
| FinalScore |
| --- |
| 90 |

## 7. 🧠 Remember This
> **Use `DECLARE` to create the box. Use `SET` to change what is inside the box.**

---

# PART 4 — SELECT ... INTO

## 1. What is it?
It is a way to grab data from a real database table and put it straight into a variable box.

## 2. Why do we need it?
If we want to make a decision based on Rahul's real marks, we must first pull his marks out of the `students` table and store them in a variable.

## 3. Simple Classroom Example

```sql
DELIMITER //

CREATE PROCEDURE get_rahul_marks()
BEGIN
    DECLARE v_student_marks INT;

    -- Fetch from table INTO variable
    SELECT marks 
    INTO v_student_marks
    FROM students 
    WHERE first_name = 'Rahul';

    -- Print the variable
    SELECT v_student_marks AS RahulMarks;
END //

DELIMITER ;

CALL get_rahul_marks();
```

## 4. Line-by-Line Explanation
- `DECLARE v_student_marks INT;` → Prepare an empty box.
- `SELECT marks INTO v_student_marks` → Find Rahul's marks in the database and push that number directly into our box.

## 5. Expected Output
| RahulMarks |
| --- |
| 85 |

## 6. 🧠 Remember This
> **Normally `SELECT` shows data on the screen. `SELECT ... INTO` hides the data and secretly stores it in a variable.**

---

# PART 5 — Conditional Statements (IF / CASE)

## 1. What is it?
A condition allows the program to make a decision based on the data.

## 2. Why do we need it?
To run different code for different situations. 
*If score >= 40 → Pass. Else → Fail.*

## 3. Basic Syntax
```sql
IF condition THEN
    -- do something
ELSEIF another_condition THEN
    -- do something else
ELSE
    -- do this if everything else fails
END IF;
```

## 4. Simple Classroom Example
Let's pass the student's name into the procedure as an **Input Parameter**, fetch their marks, and grade them!

```sql
DELIMITER //

-- p_name is an input parameter we provide when we CALL the procedure
CREATE PROCEDURE grade_student(IN p_name VARCHAR(50))
BEGIN
    DECLARE v_marks INT;

    SELECT marks INTO v_marks
    FROM students
    WHERE first_name = p_name;

    IF v_marks >= 90 THEN
        SELECT 'Grade: A' AS Result;
    ELSEIF v_marks >= 70 THEN
        SELECT 'Grade: B' AS Result;
    ELSEIF v_marks >= 40 THEN
        SELECT 'Grade: C' AS Result;
    ELSE
        SELECT 'Grade: FAIL' AS Result;
    END IF;

END //

DELIMITER ;

-- Let's test it on Roshini and Reena!
CALL grade_student('Roshini');
CALL grade_student('Reena');
```

## 5. Expected Output
For Roshini (92 marks):
| Result |
| --- |
| Grade: A |

For Reena (60 marks):
| Result |
| --- |
| Grade: C |

## 6. 🧠 Remember This
> **MySQL uses `ELSEIF` (all one word). Don't forget `END IF;` at the end!**

---

# PART 6 — Loops

## 1. What is a Loop?
A loop repeats a section of code multiple times.

## 2. Why do we need it?
If you need to print something 5 times, you don't want to type the `SELECT` command 5 times. 

## 3. MySQL Loop Types
*(Note: Oracle has a `FOR` loop, but MySQL uses `WHILE`, `REPEAT`, or `LOOP` for stored programs).*

### A. The WHILE Loop (Checks condition first)
```sql
DELIMITER //
CREATE PROCEDURE test_while()
BEGIN
    DECLARE v_counter INT DEFAULT 1;

    WHILE v_counter <= 3 DO
        SELECT v_counter AS Count;
        SET v_counter = v_counter + 1;
    END WHILE;
END //
DELIMITER ;
```
*Flow: "While the counter is less than or equal to 3, keep DOING this."*

### B. The LOOP with LEAVE (Infinite loop until we break out)
```sql
DELIMITER //
CREATE PROCEDURE test_loop()
BEGIN
    DECLARE v_counter INT DEFAULT 1;

    my_loop: LOOP
        SELECT v_counter AS Count;
        SET v_counter = v_counter + 1;

        IF v_counter > 3 THEN
            LEAVE my_loop; -- This breaks the loop
        END IF;
    END LOOP my_loop;
END //
DELIMITER ;
```
*Flow: "Keep looping forever! But wait, if we hit 3, LEAVE."*

### C. The REPEAT Loop (Checks condition at the end)
```sql
DELIMITER //
CREATE PROCEDURE test_repeat()
BEGIN
    DECLARE v_counter INT DEFAULT 1;

    REPEAT
        SELECT v_counter AS Count;
        SET v_counter = v_counter + 1;
    UNTIL v_counter > 3
    END REPEAT;
END //
DELIMITER ;
```
*Flow: "Repeat this action UNTIL the counter is greater than 3."*

## 4. 🧠 Remember This
> **A loop always needs a way to stop! If you forget `SET v_counter = v_counter + 1`, the loop will run forever and crash your server!**

---

# PART 7 — Error Handling (Handlers)

## 1. What is an Error Handler?
It is a safety net. If a SQL command causes a crash, the Handler catches the error and decides what to do.

## 2. Why do we need it?
If we do a `SELECT ... INTO` but the student doesn't exist, MySQL will throw an error and stop the entire program. We want to catch that error and print a friendly message instead.

## 3. Basic Syntax
In MySQL, we use `DECLARE ... HANDLER`.

## 4. Simple Classroom Example
Let's try to find a student who is not in our database.

```sql
DELIMITER //

CREATE PROCEDURE find_student_safe()
BEGIN
    DECLARE v_marks INT;
    
    -- If a NOT FOUND error happens, CONTINUE running the code, but execute the SELECT first.
    DECLARE CONTINUE HANDLER FOR NOT FOUND 
    BEGIN
        SELECT 'Error: Student does not exist!' AS Warning;
    END;

    -- This will fail because student 999 doesn't exist!
    SELECT marks INTO v_marks
    FROM students
    WHERE student_id = 999;

END //

DELIMITER ;

CALL find_student_safe();
```

## 5. Expected Output
| Warning |
| --- |
| Error: Student does not exist! |

## 6. 🧠 Remember This
> **Without a handler, an error crashes the procedure. With a handler, we catch the error gracefully.**

---

# PART 8 — Cursors

## 1. What is a Cursor?
A Cursor is a pointer that moves through a list of rows, **one row at a time**.

## 2. Why do we need it?
Remember `SELECT ... INTO`? It only works if your query returns **exactly ONE row**. 
If you write `SELECT first_name INTO v_name FROM students;`, MySQL will panic because there are 8 students! A single variable box cannot hold 8 names at once.

To process all 8 students, we must open a Cursor, fetch the first student, do something, fetch the second student, do something, and so on.

## 3. Simple Real-World Analogy
Think of a Cursor like a **Teacher reading a class attendance sheet**. 
The teacher opens the list, looks at row 1 (Rahul), reads it, moves their finger down to row 2 (Roshini), reads it, until they reach the end of the page.

## 4. The 5 Steps of a MySQL Cursor
1. **DECLARE**: Define the query.
2. **DECLARE HANDLER**: Tell MySQL how to know when we reach the end of the list.
3. **OPEN**: Run the query and prepare the list.
4. **FETCH in a LOOP**: Grab one row at a time.
5. **CLOSE**: Close the list.

## 5. Simple Classroom Example

Let's loop through all our students and print their names.

```sql
DELIMITER //

CREATE PROCEDURE print_all_students()
BEGIN
    -- 1. Create variables to hold the data
    DECLARE v_name VARCHAR(50);
    DECLARE v_finished INT DEFAULT 0;

    -- 2. DECLARE the cursor (The query)
    DECLARE student_cursor CURSOR FOR 
        SELECT first_name FROM students;

    -- 3. DECLARE the handler (When we run out of rows, set v_finished to 1)
    DECLARE CONTINUE HANDLER FOR NOT FOUND 
        SET v_finished = 1;

    -- 4. OPEN the cursor
    OPEN student_cursor;

    -- 5. Loop through the rows
    read_loop: LOOP
        -- FETCH the next row into our variable
        FETCH student_cursor INTO v_name;

        -- If the handler triggered and we are out of rows, LEAVE the loop
        IF v_finished = 1 THEN
            LEAVE read_loop;
        END IF;

        -- Do something with the data
        SELECT v_name AS StudentName;

    END LOOP read_loop;

    -- 6. CLOSE the cursor
    CLOSE student_cursor;

END //

DELIMITER ;

CALL print_all_students();
```

## 6. 🧠 Remember This
> **A Cursor requires a Loop and a `NOT FOUND` Handler so it knows exactly when to stop fetching.**

---

# 🎯 FINAL COMBINED EXAMPLE

Let's combine everything we've learned (Variables, Cursor, Loop, IF condition) into one final Stored Procedure. 

We will loop through every student. If their marks are >= 80, we will label them 'HONORS'. Otherwise, 'REGULAR'.

```sql
DELIMITER //

CREATE PROCEDURE process_student_honors()
BEGIN
    DECLARE v_name VARCHAR(50);
    DECLARE v_marks INT;
    DECLARE v_finished INT DEFAULT 0;

    -- The Cursor
    DECLARE c_students CURSOR FOR 
        SELECT first_name, marks FROM students;

    -- The Handler
    DECLARE CONTINUE HANDLER FOR NOT FOUND 
        SET v_finished = 1;

    OPEN c_students;

    honor_loop: LOOP
        -- Fetch two columns into two variables!
        FETCH c_students INTO v_name, v_marks;

        IF v_finished = 1 THEN
            LEAVE honor_loop;
        END IF;

        -- The IF/ELSE Condition
        IF v_marks >= 80 THEN
            SELECT CONCAT(v_name, ' -> HONORS (', v_marks, ')') AS Result;
        ELSE
            SELECT CONCAT(v_name, ' -> REGULAR (', v_marks, ')') AS Result;
        END IF;

    END LOOP honor_loop;

    CLOSE c_students;

END //

DELIMITER ;

CALL process_student_honors();
```

### This is the real purpose of Stored Programs:
> **Instead of just asking the database for data, we can write actual programming logic that processes database data row by row, automatically!**

---

# 🎓 Teacher's Quick Summary

When teaching this chapter, explain it in this simple flow:

1. **Why do we need this?** → SQL is great for fetching data, but terrible at making decisions (IF/ELSE) or looping.
2. **What is it?** → Stored Procedures allow us to write traditional programming logic inside MySQL.
3. **Variables** → We need boxes to hold temporary data.
4. **SELECT ... INTO** → We need to pull data from our tables into those boxes.
5. **Conditions** → We use `IF / ELSEIF` to make decisions based on what's in the box.
6. **Loops** → We use `WHILE` or `LOOP` to repeat actions.
7. **Error Handlers** → We need a safety net so the program doesn't crash when data is missing.
8. **Cursors** → If a query returns 100 rows, a cursor is the "finger" that points to one row at a time so our loop can process them individually.

**If you can explain this story to your students, they will understand the foundation of MySQL Procedural Programming!**
