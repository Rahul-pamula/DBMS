# Unit 2 Part 5: SQL Built-in Functions

Welcome to Part 5! Until now, we have been retrieving data exactly as it was stored in the database. But what if we need to analyze that data? What if we want to calculate the average marks of a class, convert all student names to uppercase, or find out how many days are left until an exam?

Instead of downloading all the data and doing the math in Python or Java, SQL provides powerful **Built-in Functions** that do the calculations directly inside the database at lightning speed.

---

## What are SQL Functions?

A function in SQL is a predefined formula that takes one or more inputs (arguments), performs an operation, and returns an output.

**Types of Built-in Functions:**
1. **Aggregate Functions:** Operate on a group of rows and return a single summary value.
2. **Scalar Functions:** Operate on a single value and return a single value. These are further divided into:
   - **Numeric Functions** (Math)
   - **String Functions** (Text manipulation)
   - **Date Functions** (Time manipulation)

---

## 1. Aggregate Functions

Aggregate functions take a whole column of data and "aggregate" or squish it down into one single output. 

### A. COUNT()
**Purpose:** Returns the total number of rows that match a specified criterion.
**Syntax:** `SELECT COUNT(column_name) FROM table_name;`

**Examples 1-5: COUNT()**
```sql
-- Ex 1: Count total number of students in the university
SELECT COUNT(*) FROM students;

-- Ex 2: Count how many students have a phone number (ignores NULLs)
SELECT COUNT(phone_number) FROM students;

-- Ex 3: Business Example - Find the total number of computer science faculty (assuming dept 1)
SELECT COUNT(*) FROM faculty WHERE dept_id = 1;

-- Ex 4: Count the number of unique departments in the students table
SELECT COUNT(DISTINCT dept_id) FROM students;

-- Ex 5: Count how many exams have been graded (score is not null)
SELECT COUNT(score) FROM marks;
```
**Sample Output for Ex 1:**
| COUNT(*) |
| :--- |
| 5000 |

### B. SUM()
**Purpose:** Returns the total sum of a numeric column.
**Syntax:** `SELECT SUM(column_name) FROM table_name;`

**Examples 6-10: SUM()**
```sql
-- Ex 6: Find the total credits offered by the university
SELECT SUM(credits) FROM courses;

-- Ex 7: Find the total marks scored by student ID 101 across all subjects
SELECT SUM(score) FROM marks WHERE student_id = 101;

-- Ex 8: Business Example - Total years of experience of all faculty combined
SELECT SUM(experience_years) FROM faculty;

-- Ex 9: Total credits of courses taught by faculty 5
SELECT SUM(credits) FROM courses WHERE faculty_id = 5;

-- Ex 10: Sum of positive scores only
SELECT SUM(score) FROM marks WHERE score > 0;
```

### C. AVG()
**Purpose:** Returns the average value of a numeric column.
**Syntax:** `SELECT AVG(column_name) FROM table_name;`

**Examples 11-15: AVG()**
```sql
-- Ex 11: Find the average score of all students in the university
SELECT AVG(score) FROM marks;

-- Ex 12: Business Example - Find the average experience of Mechanical dept faculty (dept 2)
SELECT AVG(experience_years) FROM faculty WHERE dept_id = 2;

-- Ex 13: Average credits per course
SELECT AVG(credits) FROM courses;

-- Ex 14: Average score for a specific exam (e.g., Midterms)
SELECT AVG(score) FROM marks WHERE exam_type = 'Midterm';

-- Ex 15: Find the average score of student 105
SELECT AVG(score) FROM marks WHERE student_id = 105;
```

### D. MAX()
**Purpose:** Returns the largest value in a column.
**Syntax:** `SELECT MAX(column_name) FROM table_name;`

**Examples 16-20: MAX()**
```sql
-- Ex 16: Find the highest score achieved in the university
SELECT MAX(score) FROM marks;

-- Ex 17: Business Example - Find the most experienced faculty member's years of experience
SELECT MAX(experience_years) FROM faculty;

-- Ex 18: Find the alphabetically last student name
SELECT MAX(last_name) FROM students;

-- Ex 19: Find the most credits offered by a single course
SELECT MAX(credits) FROM courses;

-- Ex 20: Find the latest date of birth (the youngest student)
SELECT MAX(dob) FROM students;
```

### E. MIN()
**Purpose:** Returns the smallest value in a column.
**Syntax:** `SELECT MIN(column_name) FROM table_name;`

**Examples 21-25: MIN()**
```sql
-- Ex 21: Find the lowest score recorded
SELECT MIN(score) FROM marks;

-- Ex 22: Business Example - Find the minimum experience required among current faculty
SELECT MIN(experience_years) FROM faculty;

-- Ex 23: Find the alphabetically first course name
SELECT MIN(course_name) FROM courses;

-- Ex 24: Find the lowest passing score (Assuming > 35)
SELECT MIN(score) FROM marks WHERE score > 35;

-- Ex 25: Find the earliest date of birth (the oldest student)
SELECT MIN(dob) FROM students;
```
---

## 2. Numeric Functions

These functions perform mathematical operations on scalar (single) numeric values.

### A. ROUND()
**Purpose:** Rounds a number to a specified number of decimal places.
**Syntax:** `ROUND(number, decimals)`

**Examples 26-29: ROUND()**
```sql
-- Ex 26: Round average marks to 2 decimal places
SELECT ROUND(AVG(score), 2) FROM marks;

-- Ex 27: Round a faculty's calculated bonus to 0 decimal places (whole number)
SELECT ROUND(5432.789, 0); -- Output: 5433

-- Ex 28: Business Example - Rounding course fee discounts to 1 decimal place
SELECT ROUND(discount_amount, 1) FROM fees;

-- Ex 29: Round a negative decimal
SELECT ROUND(-4.56, 1); -- Output: -4.6
```

### B. MOD()
**Purpose:** Returns the remainder of a division.
**Syntax:** `MOD(dividend, divisor)`

**Examples 30-33: MOD()**
```sql
-- Ex 30: Find the remainder of 10 divided by 3
SELECT MOD(10, 3); -- Output: 1

-- Ex 31: Business Example - Grouping students into 2 teams based on even/odd student_id
SELECT student_id, MOD(student_id, 2) AS team FROM students;

-- Ex 32: Find if a credit value is perfectly divisible by 2
SELECT course_name, MOD(credits, 2) FROM courses;

-- Ex 33: Modulo with large numbers
SELECT MOD(2023, 100); -- Output: 23
```

### C. POWER()
**Purpose:** Returns the value of a number raised to the power of another number.
**Syntax:** `POWER(base, exponent)`

**Examples 34-37: POWER()**
```sql
-- Ex 34: 2 to the power of 3
SELECT POWER(2, 3); -- Output: 8

-- Ex 35: Business Example - Calculating compound interest for delayed fee payments
SELECT POWER(1.05, 3); -- Output: 1.157625

-- Ex 36: Squaring the score (for statistical variance calculations)
SELECT POWER(score, 2) FROM marks;

-- Ex 37: 10 squared
SELECT POWER(10, 2); -- Output: 100
```

### D. ABS()
**Purpose:** Returns the absolute (positive) value of a number.
**Syntax:** `ABS(number)`

**Examples 38-41: ABS()**
```sql
-- Ex 38: Absolute value of -15
SELECT ABS(-15); -- Output: 15

-- Ex 39: Business Example - Finding the score difference between two subjects (always positive)
SELECT ABS(score1 - score2) FROM exam_comparisons;

-- Ex 40: Finding distance in room numbers
SELECT ABS(room_1 - room_2) FROM hostels;

-- Ex 41: Absolute of a positive number (remains unchanged)
SELECT ABS(42); -- Output: 42
```

### E. CEIL()
**Purpose:** Returns the smallest integer value that is GREATER than or equal to a number (Rounds UP).
**Syntax:** `CEIL(number)`

**Examples 42-45: CEIL()**
```sql
-- Ex 42: Ceil of 4.2
SELECT CEIL(4.2); -- Output: 5

-- Ex 43: Business Example - Calculating the number of buses needed (if 45.2 buses are needed, we need 46)
SELECT CEIL(total_students / 50.0) FROM students;

-- Ex 44: Ceil of exactly 5.0
SELECT CEIL(5.0); -- Output: 5

-- Ex 45: Ceil of -4.2
SELECT CEIL(-4.2); -- Output: -4
```

### F. FLOOR()
**Purpose:** Returns the largest integer value that is LESS than or equal to a number (Rounds DOWN).
**Syntax:** `FLOOR(number)`

**Examples 46-50: FLOOR()**
```sql
-- Ex 46: Floor of 4.8
SELECT FLOOR(4.8); -- Output: 4

-- Ex 47: Business Example - Calculating completed full years of experience
SELECT FLOOR(10.9); -- Output: 10

-- Ex 48: Floor of exact integer
SELECT FLOOR(25); -- Output: 25

-- Ex 49: Calculating full hours spent from minutes
SELECT FLOOR(150 / 60); -- Output: 2

-- Ex 50: Floor of negative decimal
SELECT FLOOR(-4.2); -- Output: -5
```
---

## 3. String Functions

These functions manipulate text data.

### A. UPPER()
**Purpose:** Converts text to uppercase.
**Syntax:** `UPPER(string)`

**Examples 51-54: UPPER()**
```sql
-- Ex 51: Convert student name to upper case
SELECT UPPER(first_name) FROM students;

-- Ex 52: Business Example - Printing certificates in block letters
SELECT UPPER(course_name) AS certificate_title FROM courses;

-- Ex 53: Hardcoded string
SELECT UPPER('hello world'); -- Output: HELLO WORLD

-- Ex 54: Normalizing input for a search query
SELECT * FROM students WHERE UPPER(last_name) = 'SHARMA';
```

### B. LOWER()
**Purpose:** Converts text to lowercase.
**Syntax:** `LOWER(string)`

**Examples 55-58: LOWER()**
```sql
-- Ex 55: Convert faculty emails to lowercase
SELECT LOWER(email) FROM faculty;

-- Ex 56: Lowercase department names
SELECT LOWER(dept_name) FROM departments;

-- Ex 57: Normalizing email generation
SELECT LOWER(first_name) FROM students;

-- Ex 58: Hardcoded string
SELECT LOWER('DATABASE SYSTEMS'); -- Output: database systems
```

### C. LENGTH()
**Purpose:** Returns the length of a string (number of characters).
**Syntax:** `LENGTH(string)`

**Examples 59-62: LENGTH()**
```sql
-- Ex 59: Find the length of a student's first name
SELECT first_name, LENGTH(first_name) FROM students;

-- Ex 60: Business Example - Find students who provided an invalid short phone number
SELECT * FROM students WHERE LENGTH(phone_number) < 10;

-- Ex 61: Find the longest course name
SELECT MAX(LENGTH(course_name)) FROM courses;

-- Ex 62: Length of a sentence including spaces
SELECT LENGTH('SQL is fun'); -- Output: 10
```

### D. CONCAT()
**Purpose:** Adds two or more strings together.
**Syntax:** `CONCAT(string1, string2, ...)`

**Examples 63-66: CONCAT()**
```sql
-- Ex 63: Combine first and last name for a full name
SELECT CONCAT(first_name, ' ', last_name) AS full_name FROM students;

-- Ex 64: Business Example - Generate official university email addresses
SELECT CONCAT(LOWER(first_name), '.', LOWER(last_name), '@univ.edu') FROM students;

-- Ex 65: Creating descriptive sentences
SELECT CONCAT(full_name, ' has ', experience_years, ' years of experience.') FROM faculty;

-- Ex 66: Concatenating 3 strings
SELECT CONCAT('A', 'B', 'C'); -- Output: ABC
```

### E. SUBSTRING()
**Purpose:** Extracts a portion of a string.
**Syntax:** `SUBSTRING(string, start_position, length)` *(Note: SQL strings are usually 1-indexed)*

**Examples 67-71: SUBSTRING()**
```sql
-- Ex 67: Extract the first 3 letters of a department name
SELECT SUBSTRING(dept_name, 1, 3) FROM departments;

-- Ex 68: Business Example - Extract the country code from a phone number (e.g., +919876543210)
SELECT SUBSTRING(phone_number, 1, 3) FROM students;

-- Ex 69: Extract initials of a student's first name
SELECT SUBSTRING(first_name, 1, 1) FROM students;

-- Ex 70: Extract characters starting from position 5 to the end
SELECT SUBSTRING('Database', 5); -- Output: base

-- Ex 71: Extract middle characters
SELECT SUBSTRING('University', 4, 4); -- Output: vers
```

### F. REPLACE()
**Purpose:** Replaces all occurrences of a substring within a string with a new substring.
**Syntax:** `REPLACE(string, old_substring, new_substring)`

**Examples 72-76: REPLACE()**
```sql
-- Ex 72: Replace 'Engg' with 'Engineering' in department names
SELECT REPLACE(dept_name, 'Engg', 'Engineering') FROM departments;

-- Ex 73: Business Example - Update old email domains to a new domain
SELECT REPLACE(email, '@olduniv.edu', '@newuniv.edu') FROM faculty;

-- Ex 74: Remove spaces from a string (Replace space with nothing)
SELECT REPLACE('123 456 789', ' ', ''); -- Output: 123456789

-- Ex 75: Censor a word
SELECT REPLACE('Badword here', 'Badword', '***'); -- Output: *** here

-- Ex 76: Replace hyphens in phone numbers
SELECT REPLACE('987-654-3210', '-', ''); -- Output: 9876543210
```

### G. TRIM()
**Purpose:** Removes leading and trailing spaces from a string.
**Syntax:** `TRIM(string)`

**Examples 77-80: TRIM()**
```sql
-- Ex 77: Remove accidental spaces users typed during registration
SELECT TRIM(first_name) FROM students;

-- Ex 78: Trim hardcoded spaces
SELECT TRIM('   Hello   '); -- Output: Hello

-- Ex 79: Update table to clean up dirty data
UPDATE students SET last_name = TRIM(last_name);

-- Ex 80: Combine TRIM with UPPER
SELECT UPPER(TRIM('   sql   ')); -- Output: SQL
```
---

## 4. Date and Time Functions

These functions handle dates, months, years, and calculate differences between them.

### A. NOW() and CURRENT_DATE()
**Purpose:** Retrieves the current date and time from the system.
**Syntax:** `NOW()` or `CURRENT_DATE`

**Examples 81-88: NOW() & CURRENT_DATE**
```sql
-- Ex 81: Get current date and time
SELECT NOW(); -- Output: 2026-08-04 10:30:00

-- Ex 82: Get only current date
SELECT CURRENT_DATE(); -- Output: 2026-08-04

-- Ex 83: Business Example - Automatically stamping enrollment date
INSERT INTO enrollments (student_id, course_id, enrollment_date) 
VALUES (101, 1001, CURRENT_DATE());

-- Ex 84: Stamping a log entry with exact time
INSERT INTO server_logs (log_msg, log_time) VALUES ('Server started', NOW());

-- Ex 85: Get current time only (MySQL)
SELECT CURRENT_TIME(); 

-- Ex 86: Select current year (using YEAR function on NOW)
SELECT YEAR(NOW());

-- Ex 87: Check if a student's dob is in the past (always true)
SELECT * FROM students WHERE dob < CURRENT_DATE();

-- Ex 88: Get current date in a where clause
SELECT * FROM attendance WHERE date = CURRENT_DATE();
```

### B. DATEDIFF()
**Purpose:** Returns the number of days between two dates.
**Syntax:** `DATEDIFF(date1, date2)`

**Examples 89-93: DATEDIFF()**
```sql
-- Ex 89: Find how many days a student has been enrolled
SELECT DATEDIFF(CURRENT_DATE(), enrollment_date) FROM enrollments;

-- Ex 90: Business Example - Calculate exact age in days
SELECT DATEDIFF(CURRENT_DATE(), dob) AS age_in_days FROM students;

-- Ex 91: Find days remaining until an exam
SELECT DATEDIFF('2026-12-01', CURRENT_DATE());

-- Ex 92: Calculate the duration of a semester (Start to End date)
SELECT DATEDIFF('2026-12-15', '2026-08-01'); -- Output: 136

-- Ex 93: Negative difference (Date1 is older than Date2)
SELECT DATEDIFF('2020-01-01', '2020-01-10'); -- Output: -9
```

### C. DATE_ADD()
**Purpose:** Adds a specified time interval to a date.
**Syntax:** `DATE_ADD(date, INTERVAL value unit)`

**Examples 94-97: DATE_ADD()**
```sql
-- Ex 94: Add 10 days to the current date (e.g., assignment deadline)
SELECT DATE_ADD(CURRENT_DATE(), INTERVAL 10 DAY);

-- Ex 95: Business Example - Add 4 years to enrollment date to find expected graduation date
SELECT DATE_ADD(enrollment_date, INTERVAL 4 YEAR) FROM enrollments;

-- Ex 96: Add 3 months to an exam date
SELECT DATE_ADD('2026-01-01', INTERVAL 3 MONTH); -- Output: 2026-04-01

-- Ex 97: Subtract time (using negative interval) - finding date a week ago
SELECT DATE_ADD(CURRENT_DATE(), INTERVAL -1 WEEK);
```

### D. MONTH() and YEAR()
**Purpose:** Extracts the month or year from a date.
**Syntax:** `MONTH(date)`, `YEAR(date)`

**Examples 98-105: MONTH() & YEAR()**
```sql
-- Ex 98: Find the birth year of a student
SELECT YEAR(dob) FROM students;

-- Ex 99: Find the birth month of a student (Returns 1-12)
SELECT MONTH(dob) FROM students;

-- Ex 100: Business Example - Find all students born in the year 2005
SELECT * FROM students WHERE YEAR(dob) = 2005;

-- Ex 101: Find all enrollments that happened in August (Month 8)
SELECT * FROM enrollments WHERE MONTH(enrollment_date) = 8;

-- Ex 102: Extract year from current date
SELECT YEAR(CURRENT_DATE());

-- Ex 103: Using DAY() function to get the day of the month
SELECT DAY('2026-08-15'); -- Output: 15

-- Ex 104: Find all students who have a birthday this month
SELECT first_name FROM students WHERE MONTH(dob) = MONTH(CURRENT_DATE());

-- Ex 105: Calculate age in years approximately
SELECT YEAR(CURRENT_DATE()) - YEAR(dob) AS approx_age FROM students;
```

---

## Conclusion & Output Visualizations

By combining these functions, SQL transforms from a simple storage system into a powerful data analytics engine. 

**Visual Table Example: Calculating Final Grades**
Imagine a query combining String, Numeric, and Aggregate functions:
```sql
SELECT 
    CONCAT(first_name, ' ', last_name) AS full_name,
    ROUND(AVG(score), 1) AS average_score,
    UPPER(dept_name) AS department
FROM students
JOIN marks ... (we will learn Joins next!)
```
**Output Table:**
| full_name | average_score | department |
| :--- | :--- | :--- |
| Rahul Sharma | 88.5 | COMPUTER SCIENCE |
| Priya Singh | 92.0 | MECHANICAL |

---

## End of Unit Assignments

1. Write a query to find the length of the longest department name using `MAX()` and `LENGTH()`.
2. Write a query to generate an automatic password for students using the first 4 letters of their first name (in lowercase) concatenated with their birth year.
3. If an exam is scheduled for '2026-11-15', write a query using `DATEDIFF()` to show how many days are left from today.
4. An error caused all scores in the `marks` table to be negative. Write a query using `UPDATE` and `ABS()` to fix them all.
5. Create a view/query that calculates the exact age of all students in days, and rounds it to years using `FLOOR()`.
