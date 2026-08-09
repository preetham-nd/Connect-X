# Task 6 — Navigation & Layout

## Context

A consistent layout is important for any web application.
Instead of creating a completely new structure for every page, applications typically use a **common layout template** that is shared across all pages.

This task focuses on creating the **main layout structure** of the ConnectX application. The layout will include reusable components such as the navigation bar, footer, and a central content area.

By creating a shared layout, developers can maintain a consistent user interface throughout the application and reduce duplication in template files.

The layout created in this task will be reused by all future pages such as registration, login, profiles, posts, and the admin dashboard.

---

# Objectives

The objective of this task is to:

* Create a reusable base template for the application.
* Implement a navigation bar that appears on all pages.
* Implement a footer section.
* Add support for displaying flash messages.
* Prepare the layout for role-based navigation in later tasks.

---

# Base Template

The application should use a **base template** that defines the overall page structure.

This template will act as the parent layout for all other templates.

The base template should include:

* Page header
* Navigation bar
* Main content section
* Footer

Other templates will extend this base layout using **Jinja template inheritance**.

This approach allows all pages to share the same structure while only defining the content that is unique to each page.

---

# Navigation Bar

The navigation bar should appear at the top of every page.

The navigation bar will provide quick access to important parts of the application.

Initially, the navigation bar may include items such as:

* Home
* Register
* Login

In later tasks, the navigation bar will change depending on whether a user is logged in and what role they have.

The navigation bar should be implemented as a separate template file so it can be reused easily.

---

# Footer

A footer section should be added to the bottom of the layout.

The footer may contain:

* Application name
* Copyright information
* Simple links or notes

Just like the navigation bar, the footer should be implemented as a reusable template component.

---

# Flash Messages

Web applications often need to display short messages to users after an action is performed.

Examples include:

* Registration successful
* Invalid input
* Action completed successfully

Flask provides a mechanism called **flash messages** to display these notifications.

The base template should include a section where flash messages can be displayed to the user.

This ensures that messages from any part of the application can appear consistently in the interface.

---

# Role-Based Navigation Preparation

In future tasks, the system will have different user roles such as:

* Admin
* User

Different roles will see different menu options in the navigation bar.

Although role logic is not implemented in this task yet, the navigation structure should be designed in a way that allows **conditional menu items** to be added later.

This preparation ensures that future features can be integrated without major layout changes.

---

# UI Theme Requirement

The user interface should follow a **clean and minimal design inspired by X (formerly Twitter)**.

The layout should prioritize:

* readability
* simplicity
* consistent spacing
* clear navigation

The structure should support future features such as feed pages, profile pages, and post interactions.

The base layout should be designed in a way that it can easily accommodate these features.

---

# Expected Outcome

At the end of this task:

* A base layout template exists.
* The navigation bar appears consistently across pages.
* A footer is included in the layout.
* Flash messages can be displayed to users.
* The layout supports template inheritance for future pages.

This provides a solid UI structure that future features will build upon.
