
# Task 4 — Database Setup

## Context

Most modern web applications require a database to store and retrieve information.
In this project, the application will use **MySQL** as the primary database and **SQLAlchemy** as the ORM (Object Relational Mapper) for interacting with the database from Python.

Before implementing application features such as users, posts, or comments, the backend must be able to **connect to the database and execute queries successfully**.

This task focuses on configuring the database connection and verifying that the Flask application can communicate with the database.

No application-specific tables such as users, posts, comments, likes, or profiles should be created yet.

---

# Objectives

The objective of this task is to:

* Configure MySQL connection settings.
* Integrate SQLAlchemy with the Flask application.
* Verify database connectivity.
* Prepare database schema files for future tasks.
* Create a simple test table and model to confirm database operations work.

---

# Database Technology

The project uses the following technologies:

Python
Flask
MySQL
SQLAlchemy

SQLAlchemy acts as a bridge between the Python application and the MySQL database.

This allows developers to interact with the database using **Python models and objects instead of writing raw SQL queries everywhere**.

---

# Environment Configuration

Database credentials should **not be hardcoded inside the source code**.

Instead, they must be stored inside the environment configuration file:

`.env`

Example variables that should be defined:

DATABASE_URL
MYSQL_HOST
MYSQL_PORT
MYSQL_USER
MYSQL_PASSWORD
MYSQL_DB

The Flask application will read these values through the configuration system.

---

# Configuration Setup

## config.py

The configuration file should be updated to include database configuration.

The application must read the database connection string from the environment variable:

DATABASE_URL

Example structure of a connection string:

```
mysql+pymysql://username:password@host:port/database_name
```

The configuration file should expose this setting so it can be used when initializing SQLAlchemy.

---

# Extensions Initialization

## extensions.py

This file is responsible for initializing Flask extensions.

In this task, **SQLAlchemy should be initialized here**.

Responsibilities include:

* creating the SQLAlchemy instance
* linking the extension with the Flask application
* ensuring the database is ready when the application starts

Keeping extensions inside a separate file keeps the project structure clean and modular.

---

# Database Folder

To organize database-related resources, a new folder should be created:

```
exskilence_project/database/
```

This folder will contain SQL scripts related to database structure and initial data.

---

## db_schema.sql

This file contains SQL statements used to create initial database tables.

For this task, only a **simple test table** should be created.

The purpose of this table is to:

* verify insert operations
* verify read operations
* confirm that the database connection is working

No application-specific tables should be created yet.

---

## seed_data.sql

This file contains **sample records used for testing**.

Seed data allows developers to quickly populate the database with test records during development.

For this task, a few records should be inserted into the test table created in `db_schema.sql`.

---

# Test Model

A simple SQLAlchemy model should be created inside the **models folder**.

The model will represent the test table created in the schema file.

The model should contain:

* a primary key
* one or two basic fields

This model is used only to verify that SQLAlchemy can interact with the database.

---

# Database Test Route

To confirm the database connection works correctly, a simple route should be created.

This route should:

1. Insert a test record into the test table.
2. Retrieve the record from the database.
3. Return the result in the response.

This confirms that:

* the database connection is working
* SQLAlchemy is correctly configured
* the application can perform database operations.

---

# Expected Outcome

At the end of this task:

* The Flask application successfully connects to the MySQL database.
* SQLAlchemy is integrated with the Flask application.
* The database folder and SQL files exist.
* A test table and test model are created.
* The application can insert and retrieve records from the database.

This confirms that the backend is ready for future tasks that require persistent data storage.
