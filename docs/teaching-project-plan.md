# DBMS Teaching & Open Source Contribution Plan

## 1. Core Philosophy: Teacher as Maintainer
In this project, you will act as the **Teacher and Open-Source Maintainer**, and your juniors will act as **Contributors**. This mirrors real-world software engineering:
* You teach a unit and then translate that unit into actionable **GitHub Issues**.
* Students claim an issue, write the SQL or code, and submit a **Pull Request (PR)**.
* You review their PR, request changes if necessary, and finally merge it into the `main` branch.
* This teaches them not only DBMS concepts but also essential industry skills: Git, GitHub collaboration, code reviews, and open-source contribution.

## 2. Infrastructure
* **Database Host:** Aiven (MySQL)
  * Use a single Aiven cloud cluster. Instruct each student to create their own logical database inside it (e.g., `ramya_db`, `yamini_db`). This gives everyone a safe sandbox in the cloud, completely bypassing local installation errors.
* **Backend:** Node.js (with Prisma ORM) or Python (with SQLAlchemy)
* **Version Control:** GitHub

---

## 3. The Mini-Project Idea
**Project Name:** College Management System Backend
*Aligns perfectly with the examples in your Unit notes.*

* **Core Entities:** Students, Departments, Faculty, Courses, Enrollments.
* **Goal:** Build the schema collaboratively unit-by-unit.

---

## 4. Step-by-Step Teaching Plan (Unit-wise Workflow)

### Phase 1: Pure SQL & Database Connection (Unit 2)
Before introducing ORMs or backend code, students must learn raw SQL. To give all 6 students equal practice without conflicts, use the "Classroom Sandbox" workflow:
1. **The Setup:** Provide the credentials to the central Aiven MySQL cluster. First, instruct each student to log in and create their *own* logical database (e.g., `ramya_db`, `yamini_db`).
2. **The Lesson:** Teach DDL (`CREATE TABLE`) and DML (`INSERT`, `SELECT`).
3. **The Issues:** You raise identical, individual GitHub Issues for all 6 students.
   * *Issue 1: @ramya - Create the `Students` table in your personal db.*
   * *Issue 2: @yamini - Create the `Students` table in your personal db.*
4. **The Contribution:** 
   * Each student creates a branch. To avoid merge conflicts, they name their SQL file after themselves (e.g., `unit-2/ramya_students.sql`).
   * They connect to their personal database via DBeaver, run and test their script, and then open a Pull Request.
5. **The Review:** You review all 6 PRs individually. You check their syntax and constraints, provide feedback, and merge all 6 into the main repository!

### Phase 2: Advanced SQL (Joins & Constraints)
1. **The Lesson:** Teach primary/foreign keys, joins, and aggregations.
2. **The Issue:** You raise an Issue: *"Add a Foreign Key linking `Students` to `Departments` and write a query to fetch all CSE students."*
3. **The Contribution & Review:** Students branch, write the `ALTER TABLE` and `SELECT JOIN` scripts, and submit a PR for your review.

### Phase 3: Introducing the Backend and ORM
Once they understand what SQL does under the hood, introduce the backend code.
1. **The Setup:** You initialize a basic Node.js + Prisma (or Python) backend on the `main` branch.
2. **The Lesson:** Show them how an ORM Model maps to the `CREATE TABLE` statements they wrote in Phase 1.
3. **The Issue:** *"Convert the `Faculty` SQL table into an ORM Model."*
4. **The Contribution:** Students write the ORM schema, generate the migration file, and send a PR.

### Phase 4: CI/CD & Automated Migrations (Advanced Collaboration)
This is where they see the full power of modern development.
1. **The Lesson:** Explain that we don't manually run `ALTER TABLE` in production; we use migration scripts.
2. **The Setup:** Set up a **GitHub Action** that runs the migration command (e.g., `npx prisma migrate deploy`) against the Aiven database whenever a PR is merged into `main`.
3. **The Workflow:** 
   * A junior picks up an issue: *"Add an `Email` column to Students."*
   * They create the migration, push the branch, and open a PR.
   * You review and merge.
   * **Magic:** The GitHub Action automatically applies their migration to the Aiven database in the cloud!

---

## 5. Why this approach is powerful
1. **Fundamentals First:** They learn raw MySQL first, so ORMs don't feel like "black magic."
2. **Open Source Experience:** By acting as a maintainer reviewing PRs, you are giving them genuine open-source contribution experience.
3. **Industry Standard:** They learn Git, Code Reviews, CI/CD, and Cloud Databases—skills that will make their resumes stand out for internships and jobs.
