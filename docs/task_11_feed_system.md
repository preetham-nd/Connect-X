# Task 11 — Feed System (View Posts)

## Context

In a social media platform, the **feed** is the central place where users discover content created by others.
Instead of manually visiting each user’s profile, the feed provides a unified stream of posts.

This task focuses on creating a **basic feed system** for the ConnectX application.
The feed will display posts created by users so that content can be easily discovered and consumed.

At this stage, the feed will show posts in a **chronological order**, typically displaying the newest posts first.

This task builds upon the post creation system implemented earlier and focuses on **content visibility and browsing**.

---

# Objectives

The objective of this task is to:

* Create a feed page where users can see posts.
* Display posts from multiple users.
* Order posts by creation time.
* Show basic information for each post.
* Allow users to navigate to the profile of the post author.

---

# Feed Page

The feed page acts as the **main content page** of the platform.

When a user logs into the system, they should be able to access the feed page where posts are displayed.

The feed should include posts created by users on the platform.

Each post displayed in the feed should show:

* Post content
* Author name
* Creation date and time

The layout should follow the previously defined application UI theme.

---

# Post Ordering

Posts should be displayed in **reverse chronological order**, meaning:

* Newer posts appear first.
* Older posts appear later in the list.

This ordering helps users quickly see the most recent content on the platform.

---

# Feed Display

Each post displayed in the feed should include:

* Post content
* Author name
* Author profile link
* Post creation time

The design should ensure that posts are clearly separated and easy to read.

The feed should support displaying multiple posts on the page.

---

# Author Profile Navigation

From each post in the feed, users should be able to navigate to the **profile page of the post author**.

This allows users to explore more information about the person who created the post.

When a user clicks the author's name:

* The system should open the author's profile page.
* The user should be able to view the profile details.

---

# Access Rules

The system should enforce the following rules:

* Only logged-in users should be able to view the feed.
* Posts shown in the feed should belong to registered users.
* Users should not be able to edit or delete posts directly from the feed unless they are the author.

---

# Expected Outcome

At the end of this task:

* A feed page exists in the application.
* The feed displays posts created by users.
* Posts are ordered by creation time.
* Each post shows author information and timestamp.
* Users can navigate to the author’s profile from the feed.

This task establishes the **core content discovery experience**, allowing users to view and interact with posts created by others on the platform.
