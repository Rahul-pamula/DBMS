# Unit 3 Part 2: Codd's Rules

Welcome to Part 2! 

If you want to build a database and call it a "Relational Database Management System" (RDBMS), you can't just throw data into a file and claim it's relational. 

In 1985, Dr. Edgar F. Codd (the creator of the relational model) got annoyed that companies were selling fake "relational" databases. So, he published **Codd's 12 Rules**. 

If a database follows these rules, it is a true RDBMS. (Technically there are 13 rules, numbered 0 to 12).

We are not going to memorize all 12 rules blindly. We are going to look at the **5 most important rules** and understand them using our `students` table!

---

# 1. Rule 0: The Foundation Rule

> *"For any system that is advertised as, or claimed to be, a relational data base management system, that system must be able to manage data bases entirely through its relational capabilities."*

### 🧠 Simple Meaning
This is the boss rule. It means the database must use **Tables (Relations)** to manage everything. If the database secretly relies on you searching through text files on your hard drive, it's not a real RDBMS!

---

# 2. Rule 1: The Information Rule

> *"All information in a relational database is represented explicitly at the logical level and in exactly one way - by values in tables."*

### 🧠 Simple Meaning
**Everything is a Table.**
There are no secret folders, no hidden lists. If data exists in the database, it MUST be inside a row and a column of a table. 

If we want to know Rahul's marks, we look at the `students` table. It's explicitly written there as `85`. 

---

# 3. Rule 2: Guaranteed Access Rule

> *"Each and every datum (atomic value) in a relational data base is guaranteed to be logically accessible by resorting to a combination of table name, primary key value and column name."*

### 🧠 Simple Meaning
**You can find ANY specific piece of data if you know 3 things:**
1. The Table Name (`students`)
2. The Primary Key (`student_id = 1`)
3. The Column Name (`first_name`)

If you have those 3 pieces of information, the database guarantees it can fetch exactly the one piece of data you want ("Rahul"). 

### 🎮 Interactive Question 2

Ask the students:
> "If I only give the database the Table Name (`students`) and the Column Name (`marks`), why is that not enough to guarantee I get a specific piece of data?"

Expected answer:
> "Because there are many students! You didn't specify WHICH student's marks you want!"

**Teacher responds:**
"Exactly! Without the Primary Key (like `student_id = 2`), the database doesn't know whose marks you are asking for. That's why Rule 2 requires all three!"

---

# 4. Rule 3: Systematic Treatment of Null Values

> *"Null values (distinct from the empty character string or a string of blank characters and distinct from zero or any other number) are supported in fully relational DBMS for representing missing information and inapplicable information in a systematic way, independent of data type."*

### 🧠 Simple Meaning
**NULL is special. It means "Unknown" or "Missing".**

If a new student joins but hasn't taken their exam yet, their `marks` should be `NULL`. 
- `NULL` is **not** equal to `0`. (0 means they took the test and failed completely).
- `NULL` is **not** a blank space `' '`. 

A true RDBMS must understand that `NULL` is a completely unique concept meaning "We don't know yet".

---

# 5. Rule 4: Dynamic Online Catalog Based on the Relational Model

> *"The data base description is represented at the logical level in the same way as ordinary data, so that authorized users can apply the same relational language to its interrogation as they apply to the regular data."*

### 🧠 Simple Meaning
**The Database's own settings are also stored in Tables!**

How does the database remember that the `students` table exists? It stores that information in a special hidden table called the **Data Dictionary** (or Catalog). 

Because the dictionary is just another table, you can write SQL queries to ask the database about itself! 

*(For example, in MySQL, you can literally run `SELECT * FROM information_schema.tables;` to see a list of all your tables!)*

---

# 🎯 Summary for the Board

You don't need to memorize the exact academic quotes. Just remember the simple concepts:

```text
CODD'S RULES FOR A TRUE RDBMS:

Rule 0 (Foundation) : Must use relations (tables) to manage data.
Rule 1 (Information): EVERYTHING is stored in tables.
Rule 2 (Access)     : Table Name + Primary Key + Column = Guaranteed Data.
Rule 3 (NULLs)      : NULL means "Unknown", it does not mean Zero.
Rule 4 (Catalog)    : The database settings are also stored in tables!
```
