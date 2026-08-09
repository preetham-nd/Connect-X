# Task 9 — Profile Management

## Context

In social media platforms, a **user profile represents the identity of a user**.
Profiles allow users to present information about themselves and provide a way for others on the platform to recognize and interact with them.

A profile typically contains basic details such as the user’s name, profile picture, and other optional information. It acts as the central place where a user’s identity is displayed.

This task focuses on creating the **profile system** for the ConnectX platform.
Users should be able to view their own profile, update certain profile details, and view the profiles of other users.

Some important fields used for authentication, such as email and password, must **not be editable from the profile editing interface**.

---

# Objectives

The objective of this task is to:

* Design the database structure for user profiles.
* Create a profile page where users can view their information.
* Allow users to update certain profile details.
* Support uploading a profile picture.
* Allow users to view the profiles of other users.

---

# Profile Data Storage

A profile table should be created to store additional user information that is not part of the core user account.

The profile table should be linked to the user table using a relationship.

Typical profile information may include:

* user reference (foreign key to the user table)
* display name
* bio or description
* profile picture
* account creation details

Separating profile information from the main user table helps keep authentication data and user profile data organized.

---

# View Profile Page

Users should be able to view their own profile page.

The profile page should display information such as:

* display name
* profile picture
* bio
* other profile details

This page should follow the layout created in the navigation and layout task to maintain UI consistency.

---

# Edit Profile

Users should be able to update certain profile details.

Editable fields may include:

* display name
* bio
* profile picture

These updates allow users to personalize their presence on the platform.

However, some fields should **not be editable** from the profile page.

---

# Restricted Fields

Certain fields are used for authentication and must remain unchanged during profile updates.

These fields include:

* Email address
* Password

These values are provided during registration and are used as login credentials.
For this reason, they should **not appear in the profile editing form**.

---

# Profile Picture Upload

Users should be able to upload a profile picture.

The system should allow image uploads and store the file location so that the image can be displayed on the profile page.

The upload feature should ensure that:

* files are stored in an appropriate static folder
* the profile record stores the path to the uploaded image

Proper validation should be applied to ensure only appropriate file types are accepted.

---

# View Other User Profiles

Users should also be able to view the profiles of other users.

This allows interaction between users and helps create a sense of community within the platform.

When viewing another user's profile:

* the information should be displayed
* editing options should not be available

Only the profile owner should be able to modify their profile details.

---

# Expected Outcome

At the end of this task:

* A profile table exists in the database.
* Users can view their own profile.
* Users can edit certain profile details.
* Users can upload and display a profile picture.
* Users can view the profiles of other users.

This feature establishes the **user identity system** that will later support posts, comments, and interactions on the platform.
