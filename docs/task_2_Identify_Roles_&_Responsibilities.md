# Task 2 — Identify Roles & Responsibilities

## Context

In most applications, different users interact with the system in different ways. Some users manage the platform, while others use the platform to create and interact with content.

This task helps students understand **how permissions work in a system** and how responsibilities are divided between different types of users.

In the ConnectX platform, there are **two types of users**:

Admin
User

Admins manage and monitor the platform, while users create content and interact with other users.

Understanding these roles helps developers design features that ensure users only access the parts of the system relevant to them.

---

# Admin Responsibilities

Admins are responsible for **managing and maintaining the platform**.

Their primary goal is to ensure that the platform remains safe and that users follow platform rules.

Admin responsibilities include:

* Monitoring platform activity
* Viewing all users registered on the platform
* Viewing all posts created by users
* Viewing all comments on posts
* Removing inappropriate posts
* Removing abusive comments
* Blocking users who violate platform rules
* Unblocking users if necessary
* Reviewing reported content

Admins are responsible for moderation and overall platform management.

---

# User Responsibilities

Users are the main participants of the platform.

They use the platform to share content and interact with other users.

User responsibilities include:

* Creating posts
* Viewing posts in the feed
* Liking posts
* Commenting on posts
* Viewing profiles
* Managing their own profile information
* Deleting their own posts
* Deleting their own comments

Users interact with the social features of the platform but do not manage the system.

---

# Data Each Role Can See

Different roles can view different types of data within the platform.

## Admin Can See

Admins can view system-wide information, including:

* All registered users
* All posts created on the platform
* All comments made on posts
* Reported content
* Platform activity information

This visibility allows admins to monitor the platform effectively.

---

## Users Can See

Users can view content that is part of normal platform interaction.

Users can see:

* Posts created by other users
* Comments on posts
* Like counts on posts
* Their own profile information
* Profiles of other users

Users primarily interact with content rather than managing the system.

---

# Data Each Role Cannot See

To protect system security and privacy, some data is restricted.

## Admin Cannot See

Admins generally should not modify or access sensitive information such as:

* User passwords
* Private system configuration settings
* Internal server details

Admins mainly focus on content moderation.

---

## Users Cannot See

Users cannot access administrative or system-level information.

Users cannot access:

* Admin dashboard
* User management pages
* Platform moderation tools
* Other users' private account details
* Internal system configuration

These restrictions prevent misuse of the platform.

---

# Content Ownership Rules

Content ownership is an important rule in social media systems.

Ownership determines **who is allowed to modify or delete content**.

---

## Post Ownership

When a user creates a post:

* The post belongs to that user.
* Only the post creator can edit or delete the post.

However, administrators can remove posts if they violate platform guidelines.

Once a post is deleted, it cannot be restored.

---

## Comment Ownership

When a user writes a comment:

* The comment belongs to that user.
* Only the comment creator can delete the comment.

Admins can also remove comments if they contain abusive or inappropriate content.

Once a comment is deleted, it cannot be restored.

---

# Expected Learning Outcome

After completing this task, students should understand:

* the different types of users in the system
* the responsibilities of each role
* what information each role can access
* what information each role cannot access
* how content ownership works in a social media platform

This understanding will help students implement **role-based behavior and access restrictions** in later development tasks.

---

# Deliverables

For this task, students should prepare:

* Notes describing Admin responsibilities
* Notes describing User responsibilities
* A list of data that each role can see
* A list of restricted data for each role
* Defined rules for post and comment ownership

These notes will guide the implementation of access rules in the upcoming tasks.

---

# MCQs

### 1. What is the main responsibility of an Admin in the platform?

A. Creating posts
B. Managing and moderating the platform
C. Writing comments only
D. Browsing products

Correct Answer: **B**

---

### 2. Which of the following actions can a normal user perform?

A. Block other users
B. Delete platform database
C. Create posts and comments
D. Access admin dashboard

Correct Answer: **C**

---

### 3. Who can delete a post created by a user?

A. Any user on the platform
B. Only the system server
C. The post owner and the admin
D. Only the database administrator

Correct Answer: **C**

---

### 4. Which of the following information can a normal user view?

A. Admin dashboard
B. Posts created by other users
C. System configuration
D. Server settings

Correct Answer: **B**

---

### 5. What does content ownership mean?

A. Content belongs to the server
B. Content belongs to the user who created it
C. All users can edit any content
D. Content cannot be deleted

Correct Answer: **B**

---
