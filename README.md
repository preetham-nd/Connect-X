# ConnectX — Social Media Platform

## Project Overview

**ConnectX** is a simplified social media platform built as an internship learning project. The goal of this project is to help developers understand how real-world web applications are structured and implemented by building a small but complete platform from scratch.

The application allows users to:

* Create an account and log in
* Create and manage posts
* View posts in a feed
* Like posts
* Comment on posts
* Maintain a personal profile

The platform also includes **administrator capabilities** that allow monitoring of activity and moderation of inappropriate content.

The project follows a **monolithic architecture**, where both the backend and frontend exist within a single Flask application. This approach keeps the system easier to understand for learning purposes while still reflecting the structure used in real backend applications.

The system is built using the following technologies:

* **Python** — backend programming language
* **Flask** — web framework
* **Jinja2** — template rendering engine
* **MySQL** — database system
* **HTML / CSS / JavaScript** — frontend interface

---

# High-Level System Idea

ConnectX simulates how a basic social media platform operates.

A typical interaction flow looks like this:

1. A user registers on the platform.
2. The user logs into the system.
3. The user creates a post.
4. Other users see the post in their feed.
5. Users can interact with the post by liking or commenting.
6. Administrators monitor platform activity and moderate content if necessary.

The platform contains two main roles:

### User

Regular users interact with the platform by creating posts, viewing the feed, liking posts, commenting, and managing their profile.

### Admin

Admins monitor the platform, review activity, manage users, and remove inappropriate posts or comments.

---

# Project Structure

The project follows a modular Flask structure where different responsibilities are separated into different directories.

```
project_root
│
├── docs
│   └── connectX.md
│
├── exskilence_project
│   ├── errors
│   ├── models
│   ├── routes
│   ├── static
│   │   ├── css
│   │   └── js
│   ├── templates
│   │   ├── admin
│   │   ├── auth
│   │   ├── base.html
│   │   ├── navbar.html
│   │   └── footer.html
│   └── utils
│
├── .env
├── .gitignore
├── app.py
├── config.py
├── extensions.py
├── requirements.txt
└── README.md
```

### Key Directories

**docs**

Contains project documentation explaining the system and development tasks.

**errors**

Handles centralized error management and custom exception handling.

**models**

Contains the application's data layer and manages how data is stored and retrieved.

**routes**

Defines all application endpoints and request handlers.

**static**

Stores frontend assets such as stylesheets and JavaScript files.

**templates**

Contains HTML templates rendered using Jinja2. Shared layout components such as the navigation bar and footer are also defined here.

**utils**

Includes reusable helper functions used across the application.

---

# How to Set Up the Project

Follow the steps below to run the project locally.

## 1. Clone the Repository

```
git clone <repository_url>
cd connectx
```

---

## 2. Create a Virtual Environment

Create a Python virtual environment to isolate project dependencies.

```
python -m venv venv
```

Activate the environment:

**Mac / Linux**

```
source venv/bin/activate
```

**Windows**

```
venv\Scripts\activate
```

---

## 3. Install Project Dependencies

Install all required packages listed in the requirements file.

```
pip install -r requirements.txt
```

---

## 4. Configure Environment Variables

Create or update the `.env` file with required configuration values such as:

* database credentials
* application secret key
* environment settings

Example variables may include:

```
FLASK_ENV=development
SECRET_KEY=your_secret_key
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=connectx
```

---

## 5. Configure the Database

Ensure that MySQL is installed and running on your system.

Create the required database for the project. The application will connect to this database using the configuration provided in the `.env` file.

---

## 6. Run the Application

Start the Flask server using the main application file.

```
python app.py
```

Once the server starts, open a browser and navigate to:

```
http://localhost:5000
```

---

# Development Goals

This project helps developers learn important backend development concepts such as:

* Flask project structure
* authentication and session handling
* role-based access control
* modular application design
* content management systems
* feed-based applications
* moderation workflows

---

# Final Outcome

By completing the ConnectX project, developers will build a working **mini social media platform** that demonstrates how modern web applications manage users, content, and interactions.

The project acts as a strong foundation for understanding larger systems such as production-scale social media platforms.
