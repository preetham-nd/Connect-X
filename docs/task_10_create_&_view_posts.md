# Task 10 — Create & View Posts

## Context

Posts are the primary form of content on a social media platform.
Users create posts to share their thoughts, updates, or information with others on the platform.

This task introduces the **core content creation functionality** of the ConnectX application.
Users will be able to create posts, view posts, and manage their own content.

Each post must be associated with the user who created it. This allows the system to display the author of the post and enforce rules such as allowing users to modify or delete only their own posts.

The system should also track when the post was created so that posts can later be displayed in chronological order.

---

# Objectives

The objective of this task is to:

* Design the database structure for posts.
* Allow users to create new posts.
* Display posts created by users.
* Show the author and creation date for each post.
* Allow users to edit or delete only their own posts.

---

# Post Data Storage

A database table should be created to store post information.

Each post must be linked to the user who created it.

Typical fields in the post table may include:

* post identifier
* user reference (foreign key to the user table)
* post content
* creation timestamp
* last update timestamp

This relationship ensures that every post can be traced back to its author.

---

# Create Post

Users should be able to create new posts through a form.

The form should allow users to enter the content they want to share.

When the form is submitted:

1. The system should validate the input.
2. A new post record should be created in the database.
3. The post should be linked to the logged-in user.

The system should display a confirmation message after the post is successfully created.

---

# Display Posts

Posts should be displayed in a readable format on the platform.

Each post should show:

* the content of the post
* the author’s name
* the date and time the post was created

The display should follow the UI layout created earlier in the project.

This task focuses on basic post display. The feed functionality will be expanded in later tasks.

---

# Edit Post

Users should be able to edit posts they created.

When editing a post:

* The system should verify that the logged-in user is the author of the post.
* The user should be able to modify the post content.
* The system should update the post record in the database.

Users must **not be able to edit posts created by other users**.

---

# Delete Post

Users should also be able to delete their own posts.

Before deleting a post, the system should confirm that the logged-in user is the owner of the post.

Once a post is deleted:

* It should be permanently removed from the database.
* It should no longer appear in the system.

Deleted posts **cannot be restored**.

---

# Authorization Rules

The system must enforce the following rules:

* Users can create posts only when they are logged in.
* Users can edit only the posts they created.
* Users can delete only the posts they created.
* Users cannot modify content created by others.

These rules ensure that content ownership is respected.

---

# Expected Outcome

At the end of this task:

* A post table exists in the database.
* Users can create posts.
* Posts are stored and linked to the author.
* Posts display the author and creation time.
* Users can edit their own posts.
* Users can delete their own posts.

This task establishes the **core content creation system**, which will later support features such as feeds, likes, and comments.
