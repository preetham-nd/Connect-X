# Task 12 — Like Feature

## What is a Like

A **like** is a lightweight way to react to a post with one action—without writing a comment.  
In ConnectX, each like is stored as a **single row** linking one **user** to one **post**, so the platform can show counts and whether the current user already liked a post.

This task implements likes in a **naive** way: logic and SQL live in route handlers, not in a separate service layer.

---

## Why likes matter

Likes help a social feed feel interactive:

- They give **feedback** to authors (content resonated).
- They increase **engagement** with very little friction.
- They are easy to **aggregate** into a per-post count.

This task focuses on **like / unlike** and **preventing duplicate likes**, not on ranking algorithms or notifications.

---

## Objectives

The objective of this task is to:

- Let a logged-in user **like** a post they have not liked yet.
- Let the same user **unlike** (remove) their like.
- Ensure a user can like a given post **at most once** (enforced in the database and checked in code).
- Show a **like count** on each post in the feed (or equivalent view).
- Show the correct **Like** vs **Unlike** control for the current user.

---

## Likes data model (many-to-many)

Likes model a **many-to-many** relationship between users and posts:

- One user can like **many** posts.
- One post can receive likes from **many** users.

ConnectX uses a **`likes`** join table, typically with:

- `id` — primary key  
- `user_id` — who liked  
- `post_id` — which post  
- `created_at` — when the like was created  

A **unique constraint** on `(user_id, post_id)` stops duplicate likes at the database level.

---

## Preventing duplicate likes

If duplicates were allowed, one user could inflate popularity by liking the same post repeatedly.

The app should combine:

- **Database rule** — `UNIQUE (user_id, post_id)` on `likes`.  
- **Application check** — before insert, `SELECT` whether a row already exists for that pair; if it exists, skip insert or show a neutral message.

Together, these keep behaviour predictable even under race conditions.

---

## Like and unlike behaviour

**Like** (for example `POST /like/<post_id>`):

- Require a **logged-in** user.
- Confirm the **post exists**.
- If no like row exists for `(user_id, post_id)`, **insert** one.
- If a row already exists, **do not** insert again (optional user message).
- Redirect back to the **feed** (or the same view where the action started).

**Unlike** (for example `POST /unlike/<post_id>`):

- Require a **logged-in** user.
- **Delete** the `likes` row for that `(user_id, post_id)`.
- Redirect back to the **feed**.

---

## Like count in the UI

For each post shown in the feed:

- Compute how many likes exist — for example `SELECT COUNT(*) FROM likes WHERE post_id = ?`.
- Display that number next to the post.
- If the current user has a like row for that post, show **Unlike**; otherwise show **Like**.

Counts should update after like/unlike actions without requiring a full page redesign beyond normal refresh or redirect behaviour.

---

## Access rules

The platform should enforce:

- **Only logged-in users** can like or unlike (anonymous users get redirected to login or see an error).
- A user may create **at most one** like per post (unique constraint + pre-insert check).
- Users remove **only their own** like via unlike (delete by `user_id` + `post_id` for the session user).

---

## Expected outcome

At the end of this task:

- A **`likes`** table exists with a **unique** pair `(user_id, post_id)`.
- Users can **like** and **unlike** posts from the UI.
- Each post shows an accurate **like count**.
- Duplicate likes from the same user on the same post are **not** stored.

This adds **quick interaction** on top of the feed so users can engage without writing comments.

