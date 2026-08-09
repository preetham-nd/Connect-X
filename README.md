# ConnectX

A full-stack social media web application built with **Python, Flask, SQLAlchemy, MySQL, HTML, CSS, and JavaScript**.

ConnectX provides a complete social-media-style workflow where users can register, authenticate, create posts, interact with posts, manage their profiles, report content, and browse other users. The application also includes an **admin dashboard** for monitoring users, posts, comments, and reported content.

---

## Features

### User Authentication

* User registration with username, email, password, and password confirmation
* Login using email and password
* Secure password hashing using Werkzeug's `scrypt`
* Session-based authentication
* Logout functionality
* Duplicate username and email validation
* Blocked-user validation during login

Passwords are never stored as plain text; the application hashes passwords before storing them in the database.

### Posts

Authenticated users can:

* Create posts
* View posts through the main feed
* Edit their own posts
* Delete their own posts
* View post authors
* Report posts

Posts are limited to **1000 characters** and are displayed in reverse chronological order.

### Likes

Users can:

* Like posts
* Unlike posts
* See the number of likes on posts
* Prevent duplicate likes on the same post

The like system maintains a relationship between users and posts in the database.

### Comments

Users can:

* Add comments to posts
* View comments associated with posts
* Delete their own comments
* Prevent empty comments

Comments are associated with both the user who created them and the post they belong to.

### User Profiles

Each user can have a profile containing:

* Display name
* Bio
* Profile image
* Account information

Users can view their own profile or another user's profile and can edit only their own profile.

Supported profile image formats:

* PNG
* JPG
* JPEG
* GIF
* WebP

Profile uploads are limited to **5 MB**.

### User Directory

Authenticated users can browse a list of registered users and access their profiles.

### Content Reporting

Users can report posts that they believe require administrator review.

Reports contain:

* Content type
* Content ID
* Reason
* Creation timestamp

Users cannot report their own posts.

---

# Admin Dashboard

ConnectX includes a separate administration section protected by role-based access control.

Administrators can:

* View dashboard statistics
* View all users
* View all posts
* View all comments
* Review reported content
* Delete posts
* Delete comments
* Block users
* Unblock users

The dashboard provides counts for:

* Total users
* Total posts
* Total comments

The admin dashboard uses a service/repository structure to separate data access from dashboard logic.

---

# Technology Stack

| Layer             | Technology            |
| ----------------- | --------------------- |
| Backend           | Python                |
| Web Framework     | Flask                 |
| ORM               | Flask-SQLAlchemy      |
| Database          | MySQL                 |
| Database Driver   | PyMySQL               |
| Frontend          | HTML, CSS, JavaScript |
| Template Engine   | Jinja2                |
| Authentication    | Flask Sessions        |
| Password Security | Werkzeug Scrypt       |
| Configuration     | python-dotenv         |
| Testing           | pytest                |

The current dependency list is defined in `requirements.txt`.

---

# Architecture

ConnectX follows a modular Flask application structure.

```text
                    ┌─────────────────────┐
                    │      Browser        │
                    │ HTML/CSS/JavaScript │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │       Flask         │
                    │     Application     │
                    └──────────┬──────────┘
                               │
              ┌────────────────┼────────────────┐
              │                │                │
              ▼                ▼                ▼
        ┌───────────┐    ┌────────────┐   ┌────────────┐
        │  Routes   │    │  Services  │   │   Utils    │
        │ Blueprints│    │            │   │            │
        └─────┬─────┘    └──────┬─────┘   └────────────┘
              │                 │
              ▼                 ▼
        ┌───────────┐    ┌────────────┐
        │   Models  │    │Repositories│
        └─────┬─────┘    └──────┬─────┘
              │                 │
              └────────┬────────┘
                       ▼
                ┌──────────────┐
                │    MySQL     │
                │   Database   │
                └──────────────┘
```

The Flask application factory initializes SQLAlchemy and registers separate blueprints for authentication, posts, profiles, likes, comments, the main application, and administration.

---

# Project Structure

```text
Connect-X/
│
├── database/
│   ├── db_schema.sql
│   └── seed_data.sql
│
├── docs/
│   └── connectX.md
│
├── errors/
│
├── models/
│   ├── __init__.py
│   ├── comment.py
│   ├── connection_test.py
│   ├── post.py
│   ├── profile.py
│   └── user.py
│
├── repositories/
│   ├── __init__.py
│   ├── comment_repository.py
│   ├── post_repository.py
│   └── user_repository.py
│
├── routes/
│   ├── __init__.py
│   ├── admin.py
│   ├── auth.py
│   ├── comments.py
│   ├── likes.py
│   ├── main.py
│   ├── posts.py
│   └── profile.py
│
├── services/
│   ├── __init__.py
│   └── admin_dashboard_service.py
│
├── static/
│   ├── css/
│   ├── js/
│   └── uploads/
│       └── profiles/
│
├── templates/
│   ├── admin/
│   │   ├── base_admin.html
│   │   ├── comments.html
│   │   ├── dashboard.html
│   │   ├── posts.html
│   │   ├── reports.html
│   │   └── users.html
│   │
│   ├── auth/
│   ├── posts/
│   │   ├── create.html
│   │   └── edit.html
│   │
│   ├── profile/
│   ├── base.html
│   ├── feed.html
│   ├── footer.html
│   ├── index.html
│   ├── login.html
│   ├── navbar.html
│   ├── register.html
│   └── users_list.html
│
├── utils/
│   ├── __init__.py
│   ├── decorators.py
│   └── password.py
│
├── .env
├── .gitignore
├── app.py
├── config.py
├── extensions.py
└── requirements.txt
```

The repository separates routes, database models, repositories, services, utilities, templates, static resources, and database scripts.

---

# Database Design

The application uses MySQL through SQLAlchemy.

The main entities include:

```text
User
 │
 ├────────────── Profile
 │
 ├────────────── Posts
 │                  │
 │                  ├──────── Likes
 │                  │
 │                  └──────── Comments
 │
 └────────────── Comments
```

### User

Stores authentication and account information.

Important fields:

* `id`
* `username`
* `email`
* `password_hash`
* `role`
* `is_blocked`
* `created_at`

### Profile

Stores additional user information.

Important fields:

* `id`
* `user_id`
* `display_name`
* `bio`
* `profile_image`
* `created_at`
* `updated_at`

Each user has at most one profile.

### Posts

Stores user-generated posts.

Important fields:

* `id`
* `user_id`
* `content`
* `created_at`
* `updated_at`

Each post belongs to a user.

### Comments

Stores comments made on posts.

Important fields:

* `id`
* `user_id`
* `post_id`
* `content`
* `created_at`

Comments have foreign-key relationships with both users and posts.

### Likes

The application stores user-post relationships for likes.

A user can like a particular post once and can later remove the like.

### Reports

Reported content is stored for administrator review.

The application currently uses the `reported_content` table for post reports and admin review.

---

# Application Flow

## Registration

```text
User
  │
  ▼
Registration Form
  │
  ▼
Validate username/email/password
  │
  ▼
Hash password
  │
  ▼
Create User
  │
  ▼
Store in MySQL
```

Passwords are hashed using Werkzeug before being stored.

## Login

```text
User
  │
  ▼
Login
  │
  ▼
Find user by email
  │
  ▼
Verify password
  │
  ▼
Check blocked status
  │
  ├── Admin ─────► Admin Dashboard
  │
  └── User ──────► Main Feed
```

The user's ID, username, and role are stored in the Flask session after successful authentication.

## Post Interaction

```text
Create Post
     │
     ▼
   Feed
     │
 ┌───┼───────────────┐
 ▼   ▼               ▼
Like Comment       Report
     │
     ▼
  Database
```

---

# Flask Blueprints

The application separates functionality into multiple blueprints.

| Blueprint  | Responsibility                           |
| ---------- | ---------------------------------------- |
| `main`     | Home page, feed, users, reports, DB test |
| `auth`     | Registration, login, logout              |
| `posts`    | Create, edit, delete posts               |
| `likes`    | Like and unlike posts                    |
| `comments` | Add and delete comments                  |
| `profile`  | View and edit profiles                   |
| `admin`    | Dashboard and moderation                 |

These blueprints are registered centrally inside the application factory.

---

# Authentication & Authorization

ConnectX uses two main roles:

### User

Regular users can:

* Create posts
* Edit their own posts
* Delete their own posts
* Like posts
* Comment on posts
* Manage their profile
* Report posts
* View other users

### Admin

Administrators can additionally:

* Access the admin dashboard
* View users
* View posts
* View comments
* Review reports
* Delete posts
* Delete comments
* Block users
* Unblock users

Access control is implemented using Flask sessions and route-level checks.

---

# Environment Configuration

Create a `.env` file in the project root.

```env
SECRET_KEY=your_secret_key
DEBUG=true

MYSQL_HOST=localhost
MYSQL_PORT=3306
MYSQL_USER=root
MYSQL_PASSWORD=your_mysql_password
MYSQL_DATABASE=ConnectX
```

Alternatively, the application supports providing a complete SQLAlchemy connection string through:

```env
DATABASE_URL=mysql+pymysql://username:password@localhost:3306/ConnectX
```

The configuration module loads environment variables using `python-dotenv` and builds the SQLAlchemy database URL.

> **Security:** Never commit your real `.env` file, database password, or production secret key to GitHub.

---

# Installation

## 1. Clone the repository

```bash
git clone https://github.com/preetham-nd/Connect-X.git
cd Connect-X
```

## 2. Create a virtual environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

The project currently requires Flask, Flask-SQLAlchemy, PyMySQL, python-dotenv, and pytest.

---

# Database Setup

Make sure MySQL is installed and running.

Create the database:

```sql
CREATE DATABASE ConnectX;
```

Then execute the database schema:

```bash
mysql -u root -p ConnectX < database/db_schema.sql
```

Optional seed data can be loaded using:

```bash
mysql -u root -p ConnectX < database/seed_data.sql
```

The repository contains both the schema and seed-data SQL files.

---

# Run the Application

Start the Flask application:

```bash
python app.py
```

The application runs on:

```text
http://localhost:5001
```

The port is configured directly in `app.py`.

---

# Main Routes

| Route                           | Description            | Access        |
| ------------------------------- | ---------------------- | ------------- |
| `/`                             | Home page              | Public        |
| `/auth/login`                   | Login                  | Public        |
| `/auth/register`                | Registration           | Public        |
| `/auth/logout`                  | Logout                 | Authenticated |
| `/feed`                         | Social feed            | Authenticated |
| `/users`                        | User directory         | Authenticated |
| `/profile/`                     | Current user's profile | Authenticated |
| `/profile/<user_id>`            | View user profile      | Authenticated |
| `/profile/<user_id>/edit`       | Edit profile           | Profile owner |
| `/posts/create`                 | Create post            | Authenticated |
| `/posts/<post_id>/edit`         | Edit post              | Post owner    |
| `/posts/<post_id>/delete`       | Delete post            | Post owner    |
| `/like/<post_id>`               | Like post              | Authenticated |
| `/unlike/<post_id>`             | Unlike post            | Authenticated |
| `/comments/add/<post_id>`       | Add comment            | Authenticated |
| `/comments/delete/<comment_id>` | Delete comment         | Comment owner |
| `/admin/dashboard`              | Admin dashboard        | Admin         |
| `/admin/users`                  | Manage users           | Admin         |
| `/admin/posts`                  | Manage posts           | Admin         |
| `/admin/comments`               | Manage comments        | Admin         |
| `/admin/reports`                | Review reports         | Admin         |

---

# Code Organization

The project uses several architectural patterns to keep responsibilities separated.

### Application Factory

`app.py` creates the Flask application and initializes the database extension and blueprints.

### Models

The `models/` package defines SQLAlchemy database models for users, profiles, posts, comments, and database connectivity testing.

### Repositories

The `repositories/` package provides database access for the admin dashboard.

Examples:

* `UserRepository`
* `PostRepository`
* `CommentRepository`

### Services

`AdminDashboardService` combines repository results and prepares data for the administration interface.

### Utilities

The `utils/` package contains reusable functionality such as:

* Password hashing
* Password verification
* Login-required decorators
* Admin authorization

---

# Testing

The project includes `pytest` as a development dependency.

```bash
pytest
```

Tests can be added under a dedicated test directory as the application evolves.

---

# Security Considerations

The application includes several basic security mechanisms:

* Password hashing instead of plaintext storage
* Session-based authentication
* Role-based authorization
* Blocked-user checks
* Owner-only post modification
* Owner-only comment deletion
* File-extension validation for profile images
* Maximum profile upload size
* Environment-based database configuration

For production deployment, additional security measures should be added, including CSRF protection, stronger production configuration, secure cookies, HTTPS, rate limiting, input sanitization, and production-grade secret management.

---

# Future Improvements

Potential improvements include:

* REST API layer
* Pagination for the feed
* Search functionality
* Follow/friend system
* Notifications
* Direct messaging
* Image attachments for posts
* Improved reporting workflow
* CSRF protection
* Automated tests for routes and services
* Database migrations using Flask-Migrate
* Production deployment configuration
* Docker support
* Improved query optimization for feed likes and comments

---

# Learning Outcomes

This project demonstrates practical implementation of:

* Python web development
* Flask application architecture
* Application factory pattern
* Flask Blueprints
* SQLAlchemy ORM
* MySQL database integration
* CRUD operations
* Authentication and sessions
* Password hashing
* Role-based access control
* Repository pattern
* Service-layer architecture
* File uploads
* Jinja2 templates
* HTML/CSS integration
* Database relationships
* Content moderation

---

# Project Purpose

ConnectX was developed as a practical full-stack web application to demonstrate how a social media platform can be designed and implemented using Python and Flask.

Rather than using a frontend framework and separate API backend, the current implementation uses **Flask with Jinja2 server-rendered templates**, allowing the backend, database layer, and frontend templates to work together within one application.

---

# Author

**Preetham ND**

GitHub: [@preetham-nd](https://github.com/preetham-nd)

---

# License

This project is intended for educational and development purposes.
