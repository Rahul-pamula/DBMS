# Assignment 5: Constraints & Referential Integrity

**Student Name:** Yamini

Please write the SQL queries for the following questions below each question.

### Questions:

**1. Create a table named `patients` with a primary key `patient_id` and a `NOT NULL` constraint on `first_name`.**
```sql

```

**2. Add a `UNIQUE` constraint to the `email` column in the `patients` table.**
```sql

```

**3. Create a table `appointments` with a `DEFAULT` constraint setting the `status` to 'Scheduled'.**
```sql

```

**4. Add a `CHECK` constraint to the `patients` table to ensure `age` is greater than or equal to 0.**
```sql

```

**5. Create a table `doctors` with a primary key `doctor_id`. Then add a `FOREIGN KEY` in `appointments` that references `doctor_id` in `doctors`.**
```sql

```

**6. Write a query to drop the `FOREIGN KEY` constraint from the `appointments` table.**
```sql

```

**7. Re-add the `FOREIGN KEY` constraint to `appointments` with `ON DELETE CASCADE`.**
```sql

```

**8. Attempt to insert a patient without a `first_name`. (Write the query that would cause this error).**
```sql

```

**9. Create a table with a Composite Primary Key using `patient_id` and `doctor_id`.**
```sql

```

**10. What happens if you try to delete a doctor who has existing appointments (without CASCADE)? (Write the DELETE query that would fail).**
```sql

```

---

### Proof of Work
*(Replace the image link below with your actual screenshot from the `images` folder)*

![Constraints Execution Screenshot](./images/yamini_constraints.png)
