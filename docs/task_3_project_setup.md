# Task 3 — Flask Project Setup

## Context

Before implementing any application features, the backend project must be properly structured.
A well-organized project structure helps maintain code readability, simplifies development, and makes it easier to scale the system as more features are added.

In this task, the goal is to initialize the **Flask application**, define the **core project structure**, and ensure the application can run successfully.

No business logic, database integration, or authentication should be implemented yet.

This task only focuses on **preparing the foundation of the application**.

---

## Objectives

The objective of this task is to:

* Initialize the Flask application.
* Prepare the main project directory structure.
* Configure basic application settings.
* Prepare reusable template layout files.
* Prepare the static file structure.
* Ensure the application starts successfully.

---

## Project Structure

The Flask application should follow this structure:

exskilence_project/

models/
routes/
utils/
errors/
static/
templates/

config.py
extensions.py
app.py

The root project directory should also contain:

.env
requirements.txt
README.md

---

## Folder Responsibilities

### models

This folder will contain all **database models** used by the system.
Each model represents a database table and defines how data is stored and accessed.

In this task, the folder is created but **no models are implemented yet**.

---

### routes

This folder will contain the **Flask route handlers**.
Each module inside this folder will define endpoints that respond to HTTP requests.

Examples in later tasks will include:

* authentication routes
* admin routes
* user routes
* post routes

For now, only a **simple test route** should exist to verify the application runs.

---

### utils

This folder will contain **utility functions** used across the application.

Examples include:

* helper functions
* validation logic
* reusable service functions

No utilities are required in this task yet.

---

### errors

This folder will contain **custom error handling logic**.

Examples include:

* validation errors
* authorization errors
* resource not found errors

These will be implemented in later tasks.

---

### static

This folder stores **frontend assets** such as:

* CSS files
* JavaScript files
* images

Inside the static folder, the following directories should be created:

css
js

These folders will store styling and client-side scripts.

---

### templates

This folder stores **HTML templates used by Flask with Jinja2**.

To support reusable layouts, the following files should be created:

base.html
navbar.html
footer.html

These templates will act as the **foundation for all future pages**.

---

## UI Theme Requirement

The visual style of the application should follow a layout similar to **X (formerly Twitter)**.

The UI should follow these design principles:

* clean and minimal interface
* easy readability
* simple navigation
* modular layout components

Future pages should reuse the base layout created in this task.

---

## Configuration Setup

The project must include a **configuration file**.

### config.py

This file is responsible for storing application configuration.

It should:

* load environment variables
* define base configuration values
* provide default Flask settings

Common configuration variables include:

SECRET_KEY
DEBUG

Database configuration will be added in **Task 4**.

---

## Extensions Initialization

The project should include a file called:

extensions.py

This file will act as the **central location for initializing Flask extensions**.

Examples of extensions that will be initialized in later tasks:

* SQLAlchemy
* authentication helpers
* other Flask extensions

For now, the file should only contain placeholder initialization logic.

---

## Application Setup

The main Flask application must be created in:

app.py

Responsibilities include:

* creating the Flask application instance
* loading configuration from config.py
* initializing extensions
* registering routes
* configuring template and static folders

The application must start successfully without errors.

---

## Test Route

To confirm the application works correctly, a simple route should be created.

Example:

GET /

This route should return a simple response such as a message or a rendered template.

This ensures the Flask server is working properly.

---

## Expected Outcome

At the end of this task:

* The Flask application structure is ready.
* The application can start successfully.
* The template and static folder structure exists.
* A simple test route confirms the server is running.

No application features are implemented yet.

---