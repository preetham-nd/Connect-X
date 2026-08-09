# Task 15 — Content Moderation

## What is content moderation

**Content moderation** is how administrators **review and act** on user-generated content and accounts: removing harmful posts or comments, **restricting** abusive users, and working through a **reports queue**.

In ConnectX, Task 15 uses a **naive** style: moderation **SQL and rules** live in Flask **route handlers** under the admin blueprint (for example `routes/admin.py`), alongside Task 14’s read-only dashboard paths. There is **no** separate service/repository layer for delete, block, or report listing actions in this task.

---

## Why moderation matters

Without moderation tools, harmful content can spread, users lose trust, and operators cannot respond quickly to abuse. Even basic **delete**, **block/unblock**, and **reports** views establish a foundation for safer communities and complement Task 14’s **read-only monitoring**.

This task focuses on **actions** (mutations and enforcement), not on ranking, appeals, or full audit trails.

---

## Objectives

The objective of this task is to:

- Let **admins** **hard-delete** any **post** via a dedicated POST route.
- Let **admins** **hard-delete** any **comment** via a dedicated POST route.
- Let **admins** **block** and **unblock** normal users using **`user.is_blocked`**, with guards so admins **cannot block themselves** or **another admin** (in this app’s rules).
- Expose **`GET /admin/reports`** listing rows from **`reported_content`** (`content_type`, `content_id`, `reason`, timestamps).
- **Restrict blocked users** at **login** and when creating **posts** or **comments** so suspended accounts cannot keep engaging.
- Enforce **admin-only** access to all Task 15 moderation routes using the same **session + database** admin checks as the rest of **`/admin/*`**.

---

## How moderation is built (routes and database)

Data and control flow for Task 15:

- **Routes** (`routes/admin.py`) — after **`_admin_guard()`** passes, handlers run **`text()`** SQL via SQLAlchemy’s session (`DELETE`, `UPDATE`, `SELECT` for reports).
- **`reported_content`** — a table used for the reports queue; it may exist in **`database/db_schema.sql`** without a full ORM model in tests (SQLite fixtures can create it explicitly).
- **`user.is_blocked`** — persisted flag checked in **auth** and **content-creation** paths so blocked users cannot obtain a normal session or add new posts/comments.

This is intentionally different from Task 14’s **service → repository** pattern for dashboard **reads**; moderation **writes** stay in the route layer for learning purposes.

---

## Route behaviour

**`POST /admin/delete/post/<post_id>`** (admin only):

- Deletes the post row (`DELETE FROM posts WHERE id = ?`).
- Flashes success and redirects (for example back toward the **dashboard** experience).

**`POST /admin/delete/comment/<comment_id>`** (admin only):

- Deletes the comment row (`DELETE FROM comments WHERE id = ?`).
- Flashes success and redirects (for example toward **admin comments** listing).

**`POST /admin/block/user/<user_id>`** (admin only):

- Rejects blocking the **current admin** (`user_id == session user`).
- Rejects blocking a user whose **`role`** is **`admin`**.
- Otherwise sets **`is_blocked = 1`** for the target user and redirects back to **users** admin UI.

**`POST /admin/unblock/user/<user_id>`** (admin only):

- Sets **`is_blocked = 0`** for the target user.

**`GET /admin/reports`** (admin only):

- Lists **`reported_content`** rows for triage (type, id, reason, created time).

**Blocked users (not a single HTTP route, but product behaviour):**

- **Login** — blocked accounts do not complete a normal login session; the UI should surface a **blocked** style message.
- **Posts / comments** — creation paths must check **`is_blocked`** and refuse new content from blocked users.

---

## Access rules

The platform should enforce:

- **Anonymous** requests to Task 15 admin actions (for example **`POST /admin/delete/post/<id>`**) → **302** to **`/auth/login`** when no session exists.
- **Logged-in non-admins** must **not** successfully invoke moderation endpoints; they should be turned away (for example to **public home** with an error flash), same spirit as Task 14’s admin guard.
- **Admins** — users recognised as **`admin`** after **`_admin_guard()`** (session role synced from **`user.role`** when needed) — may run delete, block/unblock, and open **reports**.

---

## Admin UI expectations

Templates and chrome should:

- Reuse the **admin layout** and navigation used for Task 14 so **Reports**, **Users**, **Posts**, and **Comments** feel like one **Admin** area.
- Surface **delete** and **block/unblock** controls where appropriate (for example on admin listings or user rows), with clear **success/error** flashes after POST actions.
- Present **`/admin/reports`** as a **read-only queue** table (or list) until a later task adds resolve/dismiss workflows.

---

## Dashboard vs moderation

- **Task 14 (dashboard):** **Read-only** insight — counts and listings via **`AdminDashboardService`** and repositories.
- **Task 15 (moderation):** **Write** operations — deletes, **`is_blocked`** updates, and the **reports** queue. These belong in **separate** route handlers and documentation from pure monitoring, even when they share **`/admin`** URLs and templates.

---

## Validation and automated tests

The following behaviours are checked by the Task 15 pytest coverage in **`testing_config/py_tests/task.py`** and should match the product:

- **Anonymous delete post** — `POST /admin/delete/post/<id>` without a session returns **302** and the **`Location`** includes **`/auth/login`**.
- **Non-admin cannot delete** — A logged-in **`role="user"`** account posting to **`/admin/delete/post/<id>`** does **not** remove the post; the response should reflect **public** access (for example home content with **“Welcome to ConnectX”** when following redirects).
- **Admin delete post** — Admin POST removes the **post** row; response **302** includes the **dashboard** path in **`Location`** (or equivalent redirect target used in the app).
- **Admin delete comment** — Admin POST removes the **comment** row; **302** targets the **admin comments** experience (path includes **`/admin/comments`**).
- **Block / unblock** — Block sets **`is_blocked`** for a normal user; unblock clears it (verified via SQL or ORM reload).
- **Cannot block self** — Admin posting block for **own** `user_id` leaves **`is_blocked`** unset for that admin.
- **Cannot block another admin** — Blocking a user with **`role="admin"`** does not set **`is_blocked`** on that user.
- **Blocked user login** — Login with valid credentials for a blocked user returns **200** with **“blocked”** messaging (case-insensitive check) and **does not** set **`user_id`** in session.
- **Reports page** — Admin **`GET /admin/reports`** returns **200** and the body includes seeded or inserted report data (for example **reason** text and **content** identifiers).

---

## Expected outcome

At the end of this task:

- Admins can **delete posts and comments**, **block and unblock** users, and **review** **`reported_content`** from the admin UI.
- **Blocked** users are stopped at **login** and cannot add **posts** or **comments**.
- Moderation **writes** remain **explicit and traceable** in route code, establishing a base for richer moderation and audit features later.

This layers **operational control** on top of Task 14’s **visibility** without mixing the two concerns in the same abstraction.
