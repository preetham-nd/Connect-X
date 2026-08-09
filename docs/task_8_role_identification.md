# Task 8 — Role Identification

## Context

After users can successfully log in to the system, the application must be able to **identify what type of user is accessing the platform**.

In this project, there are two types of users:

Admin
User

Each role has different responsibilities and access permissions within the system.

For example:

* Admins manage platform activity.
* Users create posts and interact with content.

The system must be able to identify the role of the logged-in user and respond accordingly.

This task focuses on **storing the user role, identifying the role after login, and controlling access to certain routes**.

---

# Objectives

The objective of this task is to:

* Store the role information in the user table.
* Identify the role of the logged-in user.
* Redirect users to appropriate pages based on their role.
* Restrict access to admin-only routes.
* Prevent unauthorized access to protected pages.

---

# Role Storage

The user table must include a **role field** that identifies the type of user.

Typical role values may include:

admin
user

When a new account is created, the default role should be **user**.

Admin accounts can be created manually or configured separately.

This role value will later determine which features and pages a user can access.

---

# Role Identification

When a user logs in, the system should retrieve the user's role from the database.

This role information should be stored in the session along with other user details.

For example, the session may store:

* user_id
* username
* role

By storing this information in the session, the system can quickly determine the user's role for every request.

---

# Role-Based Redirection

After a user logs in successfully, the application should redirect them to the appropriate page based on their role.

For example:

* Admin users may be redirected to an admin dashboard.
* Regular users may be redirected to the main feed or home page.

This ensures that users land on pages relevant to their role.

---

# Route Access Restrictions

Some parts of the system should only be accessible to specific roles.

For example:

* Admin pages should only be accessible to admin users.
* Regular users should not be able to access admin functionality.

The application should verify the role stored in the session before allowing access to protected routes.

If a user attempts to access a restricted page without proper permissions, the system should block access and redirect them to an appropriate page.

---

# Unauthorized Access Handling

If an unauthorized user tries to access a restricted page, the application should:

* prevent access to the resource
* display a message explaining the restriction
* redirect the user to a safe page

This ensures that system functionality remains secure and protected.

---

# Navigation Adjustments

The navigation bar created earlier should be capable of adjusting its menu items based on the logged-in user's role.

For example:

Admins may see options such as:

* Admin Dashboard
* Manage Users
* Manage Posts

Regular users may see options such as:

* Home
* Profile
* Create Post

This dynamic navigation helps users quickly access relevant features.

---

# Expected Outcome

At the end of this task:

* The user table stores role information.
* The system identifies the role of the logged-in user.
* Sessions contain role data.
* Users are redirected to role-appropriate pages after login.
* Admin routes are protected from unauthorized access.

This prepares the system for future tasks where **admin features and user-specific functionality** will be implemented.
