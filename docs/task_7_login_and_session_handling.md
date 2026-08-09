# Task 7 — Login & Session Handling

## Context

After users register on the platform, they must be able to **log in to access personalized features**.
Login allows the system to identify the user and provide access to features such as creating posts, interacting with content, and managing profiles.

This task introduces **authentication basics** and the concept of **sessions**.

A session allows the application to remember that a user is logged in while they navigate through different pages. Without sessions, the application would treat every request as coming from a new visitor.

This task focuses on implementing the login process and maintaining the logged-in state of the user.

---

# Objectives

The objective of this task is to:

* Create a login form for users.
* Verify user credentials using stored account information.
* Compare the entered password with the stored password hash.
* Create a session for authenticated users.
* Track the logged-in user across requests.
* Implement logout functionality.

---

# Login Form

A login form should be created to collect user credentials.

The form should include:

* Email address
* Password

The form will submit the data to the backend using a POST request.

The login page should use the base layout created in the previous task to maintain a consistent interface.

---

# Credential Verification

When a user submits the login form, the application must verify the provided credentials.

The verification process should include:

1. Searching the database for a user with the provided email address.
2. If the user exists, compare the entered password with the stored password hash.
3. If the password is correct, authenticate the user.
4. If the password is incorrect, display an error message.

This ensures that only valid users can access the system.

---

# Session Creation

Once the user is successfully authenticated, the application should create a session.

A session stores information about the logged-in user so that the application knows who is making requests.

Typical session data may include:

* user ID
* username
* user role

The session should remain active until the user logs out or the session expires.

---

# Logged-In User Tracking

After the session is created, the application should be able to identify the logged-in user on every request.

This allows the system to:

* display personalized navigation
* control access to certain pages
* show user-specific data

Future tasks will rely on this information to enforce permissions and personalize the user experience.

---

# Logout Functionality

Users must have the ability to log out of the system.

Logging out should:

* clear the session
* remove stored user information
* redirect the user to a public page such as the home page or login page

This ensures that the account is no longer active in the browser.

---

# Flash Messages

Flash messages should be used to inform users about login actions.

Examples include:

* Login successful
* Invalid email or password
* Logout successful

These messages help users understand the result of their actions.

---

# Security Considerations

When implementing login functionality, certain security practices should be followed:

* Passwords should never be stored or compared in plain text.
* Always compare passwords using the stored hash.
* Sessions should store minimal user information.
* Sensitive data should never be exposed in templates.

These practices help protect user accounts and maintain application security.

---

# Expected Outcome

At the end of this task:

* Users can log in using their email and password.
* The system verifies credentials using stored password hashes.
* A session is created when authentication is successful.
* The application can identify the logged-in user.
* Users can log out and terminate their session.

This prepares the application for the next tasks, where the system will begin to identify **user roles and restrict access to certain features**.
