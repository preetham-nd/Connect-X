# Task 13 — Comment System

## What is a Comment

A **comment** is a text reply attached to a post so readers can discuss the content, ask questions, or react in more depth than a like allows.  
In ConnectX, each comment is stored as **one row** linking a **user** to a **post** with a **content** field and a timestamp.

This task implements comments in a **naive** way: logic and SQL live in route handlers, not in a separate service layer.

---

## Why comments matter

Comments deepen engagement on a feed:

- They turn posts into **conversations** and surface clarifying questions.
- They give authors **qualitative feedback** beyond counts.
- They are still simple to model: one table, foreign keys to `user` and `posts`.

This task focuses on **add** and **delete (own only)**, not on threading, edits, or moderation workflows.

---

## Objectives

The objective of this task is to:

- Let a **logged-in** user **add** a non-empty comment to an existing post.
- **Reject** empty or whitespace-only comment submissions without inserting a row.
- Let a user **delete their own** comment via a dedicated route.
- **Block** deletion when the logged-in user is not the comment author.
- Ensure **anonymous** users cannot add comments (redirect to login).
- Show **comments on the feed** (or equivalent view) with a way to add new comments.

---

## Comments data model (user ↔ post ↔ comment)

Comments model a **one-to-many** relationship from posts (and from users) to comments:

- One **user** can write many comments.
- One **post** can have many comments.
- Each **comment** belongs to exactly one user and one post.

ConnectX uses a **`comments`** table, typically with:

- `id` — primary key  
- `user_id` — who wrote the comment  
- `post_id` — which post it belongs to  
- `content` — comment body  
- `created_at` — when the comment was created  

Foreign keys reference `user.id` and `posts.id` so comments cannot hang off deleted users or posts (behaviour depends on your schema’s `ON DELETE` rules).

---

## Validating comment input

Empty or whitespace-only comments should not be stored.

The app should:

- **Trim** `content` from the form before validation.
- **Reject** submissions where the trimmed text is empty (flash or message + redirect without `INSERT`).
- Optionally treat very long content consistently with your post limits (this task keeps validation minimal).

---

## Add and delete comment behaviour

**Add comment** (for example `POST /comments/add/<post_id>`):

- Require a **logged-in** user.
- Confirm the **post exists**.
- Read **`content`** from form data, trim it, and ensure it is **non-empty**.
- **Insert** into `comments (user_id, post_id, content)` for the session user.
- Redirect back to the **feed** (or the same view) with a simple flash message.

**Delete comment** (for example `POST /comments/delete/<comment_id>`):

- Require a **logged-in** user.
- Load the comment by **`comment_id`**.
- If `comment.user_id` matches **`session["user_id"]`**, **delete** the row.
- If it does **not** match, **do not** delete (show error flash); redirect to feed.
- No admin override is required for this task.

---

## Comments in the UI

For each post shown in the feed (or equivalent):

- **List** existing comments (author and text, and optionally time).
- Provide an **Add comment** form posting to `/comments/add/<post_id>` with a `content` field.
- When there are no comments, show a clear **empty state** (for example “No comments yet.”).
- For comments owned by the **current user**, expose **delete** (form POST to `/comments/delete/<comment_id>`). Other users must not see a working delete for rows they do not own.

After add or delete, a normal redirect or refresh should show updated comments.

---

## Access rules

The platform should enforce:

- **Only logged-in users** can add comments (anonymous users are redirected to login or see an error).
- Users may add comments on **any post** that exists (unless you add extra rules later).
- Users may **delete only their own** comments; attempts on others’ comments are blocked in application logic.

---

## Validation and automated tests

The following behaviours are checked by the Task 13 pytest suite and should match the product:

- **Add comment requires login** — `POST /comments/add/<post_id>` without a session returns **302** and the response targets **`/auth/login`**.
- **Add comment creates row** — A logged-in user posting valid `content` gets **302** to **`/feed`**, and exactly **one** matching row exists in **`comments`** for that user, post, and content.
- **Empty comment not stored** — Posting only whitespace yields **302** (or your chosen response) and **no** new row for that user and post.
- **Delete own comment** — Owner posts to **`/comments/delete/<comment_id>`**; comment row count for that id becomes **zero**; redirect includes **`/feed`**.
- **Delete other user’s comment blocked** — Non-owner receives **302** to **`/feed`** (or equivalent) and the comment row **still exists**.
- **Feed shows comments UI** — **`GET /feed`** returns **200** and the body includes comments section labels, the empty-state line when applicable, and the **add-comment** form action for the post.

---

## Expected outcome

At the end of this task:

- A **`comments`** table exists with **`user_id`** and **`post_id`** tied to **`user`** and **`posts`**.
- Logged-in users can **add** comments and see them in context on the feed.
- **Empty** comments are **not** persisted.
- Users can **delete only their own** comments; others’ comments stay intact.

This adds **discussion** on top of the feed so users can engage beyond likes alone.
