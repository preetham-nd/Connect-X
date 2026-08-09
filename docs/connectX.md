# ConnectX — Social Media Platform Project Specification

## Project Overview

This project is a simplified **Social Media Web Application** built using:

Python
Flask
Jinja2
MySQL

The application follows a **monolithic architecture**, where backend logic and frontend templates are implemented within the same project.

The system supports two primary user roles:

Admin
User

The goal of this project is to implement the **core workflow of a social media platform**, including post creation, feed interaction, likes, comments, profile management, and administrative moderation.

---

# System Workflow

The basic operational flow of the system is:

User → Create Post → Feed Display → Like / Comment → Platform Moderation

1. Users create accounts and log in.
2. Users create posts that appear on the platform.
3. Other users see posts in the feed.
4. Users interact with posts through likes and comments.
5. Administrators monitor platform activity and moderate content when necessary.

---

# System Roles

The system contains two types of users:

Admin
User

Each role has different responsibilities and system access permissions.

---

# Data Access Rules

## Admin Access

Admin can access:

* All users
* All posts
* All comments
* Platform activity
* Reported content
* Moderation controls

Admin can perform the following actions:

* Delete inappropriate posts
* Delete abusive comments
* Block users
* Unblock users
* Monitor platform statistics

Admin manages the overall safety and moderation of the platform.

---

## User Access

Users can access:

* Their own profile
* Posts created by other users
* Feed content
* Comments under posts
* Like interactions
* Their own posts and comments

Users cannot access:

* Admin dashboard
* User management features
* Moderation controls
* Other users’ private data

---

# Project Tasks

The project is divided into multiple implementation tasks.
Each task introduces a new part of the system.

---

# Task 1 — Understand Social Media Workflow

Define the operational workflow of a social media platform.

This task focuses on understanding how content flows through the platform and how users interact with each other.

The workflow includes:

* User registration
* User login
* Post creation
* Feed updates
* Likes
* Comments
* Platform moderation

The goal of this task is to understand how a social media system behaves before implementation begins.

---

# Task 2 — Identify Roles and Responsibilities

Define the roles used in the system and determine the responsibilities of each role.

The roles are:

Admin
User

For each role, define:

* Responsibilities
* Data they can access
* Data they cannot access

This task establishes the **access control model** for the platform.

---

# Task 3 — Flask Project Setup

Initialize the Flask application and prepare the project structure.

This task includes:

* Creating the Flask project structure
* Setting up the application entry point
* Configuring environment variables
* Preparing template and static directories
* Running the development server

The goal is to ensure the application starts successfully and is ready for development.

---

# Task 4 — Database Setup

Configure the MySQL database and connect it to the Flask application.

This task includes:

* Creating the project database
* Configuring database connection settings
* Establishing database connectivity
* Creating a test table
* Verifying database queries can be executed

This ensures the application can store and retrieve platform data.

---

# Task 5 — User Registration

Implement the registration system for new users.

This task includes:

* Creating the user data model
* Building the registration form
* Validating user inputs
* Implementing password hashing
* Saving user information securely

Users must provide:

* username
* email
* password
* confirm password

Email and password are used as login credentials.

---

# Task 6 — Navigation and Layout

Create shared layout components used throughout the application.

This task includes:

* Creating a base template
* Implementing a navigation bar
* Implementing a footer
* Displaying flash messages for user actions
* Showing role-based menu options

This ensures a consistent interface across the platform.

---

# Task 7 — Login and Session Handling

Implement user authentication and session management.

This task includes:

* Creating the login form
* Validating login credentials
* Creating user sessions
* Tracking logged-in users
* Implementing logout functionality

Sessions allow the system to recognize users while they navigate the platform.

---

# Task 8 — Role Identification

Implement role-based access control within the application.

This task includes:

* Storing the user role
* Identifying the role of the logged-in user
* Restricting admin-only routes
* Redirecting users to the appropriate pages

This ensures users only access features permitted for their role.

---

# Task 9 — Profile Management

Implement the user profile system.

This task includes:

* Creating profile pages
* Viewing personal profiles
* Editing profile details
* Uploading profile pictures
* Viewing other user profiles

During profile editing:

* Email and password should not be editable.
* Login credentials remain protected.

---

# Task 10 — Post Creation and Viewing

Implement the core feature of the platform: posts.

This task includes:

* Creating new posts
* Viewing posts created by users
* Displaying post author information
* Displaying post creation timestamps
* Deleting posts

Users can only modify or delete posts they created.

Once a post is deleted, it cannot be restored.

---

# Task 11 — Feed Page

Create the main feed where users view posts.

This task includes:

* Displaying posts from multiple users
* Sorting posts by latest first
* Displaying author details
* Showing post timestamps

Optional improvement:

* Implement feed pagination for large datasets.

---

# Task 12 — Like Feature

Implement the post like functionality.

This task includes:

* Liking a post
* Removing a like
* Preventing duplicate likes
* Displaying like counts

A user can like a post only once but can remove the like later.

---

# Task 13 — Comment Feature

Implement the comment system for posts.

This task includes:

* Adding comments to posts
* Displaying comments under posts
* Showing commenter information
* Deleting comments

Users can delete only their own comments.

Once a comment is deleted, it cannot be restored.

Admins may also remove inappropriate comments.

---

# Task 14 — Admin Dashboard

Create the administrative dashboard.

This task includes:

* Creating the admin home page
* Viewing all users
* Viewing all posts
* Monitoring platform activity

The dashboard provides administrators with an overview of system activity.

---

# Task 15 — Content Moderation

Implement moderation features for administrators.

This task includes:

* Deleting inappropriate posts
* Deleting abusive comments
* Blocking problematic users
* Unblocking users
* Viewing reported content

Admins can remove any post or comment regardless of ownership.

Once removed by an admin, content cannot be restored.

---

# Project Goal

The final system should support the following workflow:

1. Users register and log in to the platform.
2. Users create posts and interact with content through likes and comments.
3. Posts appear in a dynamic feed visible to other users.
4. Users maintain their personal profiles.
5. Administrators monitor platform activity and moderate inappropriate content.

The completed system demonstrates the **core functionality of a social media platform**, providing hands-on experience with authentication, content management, and moderation workflows.
