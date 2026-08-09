# Task 5 — User Registration

## Context

User registration is the entry point for people who want to use the platform.
Before users can create posts, interact with content, or manage profiles, they must first create an account in the system.

This task introduces the process of **collecting user information through a registration form and storing it securely in the database**.

It also introduces an important security concept: **password hashing**.
Passwords should never be stored in plain text. Instead, they must be securely hashed before being stored.

This task focuses only on **creating user accounts and storing them correctly**. Login functionality will be implemented in a later task.

---

# Objectives

The objective of this task is to:

* Create a database table for storing user accounts.
* Build a registration form using HTML and Jinja templates.
* Validate user input before saving it to the database.
* Securely hash user passwords before storing them.
* Store user information in the database.

---

# User Table

A database table should be created to store user account information.

The table should include fields such as:

* Unique user identifier
* Username
* Email address
* Password hash
* Role (admin or user)
* Account creation timestamp

The email address and password will be used later for login authentication.

Passwords **must not be stored in plain text**.

---

# Registration Form

A registration form should be created to collect user information.

The form should be implemented using **HTML templates with Jinja2** and should contain fields such as:

* Username
* Email address
* Password
* Confirm password

The form should send the data to the Flask backend using a POST request.

---

# Input Validation

Before saving the data, the system should validate user input.

Examples of validation include:

* Required fields must not be empty.
* Email must follow a valid format.
* Password and confirm password must match.
* Duplicate email addresses should not be allowed.

If validation fails, the system should show a clear error message to the user.

---

# Password Hashing

Passwords must be securely hashed before storing them in the database.

Hashing ensures that even if the database is compromised, raw passwords cannot be easily retrieved.

A password hashing utility should be used to convert the password into a secure hashed value before saving it.

Only the hashed version should be stored in the database.

---

# Saving User Data

Once validation is successful and the password is hashed, the system should:

1. Create a new user record.
2. Store the data in the user table.
3. Confirm that the user account was successfully created.

The system may display a success message after registration.

---

# Default Role Assignment

When a new user registers, the system should automatically assign a default role.

For this project:

* Regular users should be assigned the **user role** by default.
* Admin accounts will be managed separately.

This ensures the system can distinguish between administrators and normal users in later tasks.

---

# Expected Outcome

At the end of this task:

* The user table exists in the database.
* Users can register using a form.
* Input validation prevents invalid data.
* Passwords are securely hashed before storage.
* New user accounts are successfully saved in the database.

This prepares the system for the next task, where users will be able to **log in and start interacting with the platform**.
