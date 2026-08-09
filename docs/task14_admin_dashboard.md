# Task 14 — Admin Dashboard

## What is an Admin Dashboard

An **admin dashboard** is a **protected** area of the app where accounts with the **`admin`** role can see **high-level statistics** and **read-only listings** of users, posts, and comments. It answers “how big is the platform?” and “what was published recently?” without opening the database by hand.

In ConnectX, Task 14 implements this using a **small service layer** (`AdminDashboardService`) that calls **repositories** for counts and lists. **HTTP and access control** stay in Flask **route handlers** (for example the `admin_required` decorator on `/admin/*` routes).

---

## Why admin monitoring matters

A dashboard gives operators a **safe, UI-driven** way to observe the product:

- **Growth and health** — user, post, and comment counts summarize activity at a glance.
- **Investigation** — tabular views of users and content support triage before any moderation action (later tasks).
- **Separation of duties** — ordinary users never see admin-only pages; role checks keep listings and stats off non-admin sessions.

This task focuses on **monitoring** (read insight), not on deleting content or blocking accounts.

---

## Objectives

The objective of this task is to:

- Expose an **admin-only** section under **`/admin`** with a clear **home dashboard**.
- Show **aggregate statistics**: total **users**, **posts**, and **comments** on the dashboard.
- Provide **`GET /admin/users`** — a table of all registered users (id, username, email, role, joined).
- Provide **`GET /admin/posts`** — all posts **newest first**, with **author** and a **trimmed content preview** (long bodies truncated with an ellipsis).
- Provide **`GET /admin/comments`** — all comments **newest first**, with **post id**, **author**, and a **trimmed preview** of comment text.
- Enforce **role-based access**: only **`role == "admin"`** users reach these routes; anonymous users go to **login**; logged-in **non-admins** are sent back to the **public home** with an error flash.

---

## How the dashboard is built (routes → service → repositories)

Data flows in one direction for reads:

- **Routes** (`routes/admin.py`) — require an admin session, call the service, render templates.
- **`AdminDashboardService`** (`services/admin_dashboard_service.py`) — builds **stats** and **list-shaped dicts** for templates (including preview truncation lengths for posts and comments).
- **Repositories** (`repositories/user_repository.py`, `post_repository.py`, `comment_repository.py`) — run **ORM-backed** queries (counts, ordered lists, `joinedload` for authors where needed).

This is **not** the same “all SQL in the route” style as the naive comment/like tasks; it keeps **read paths** easier to test and extend.

---

## Route behaviour

**`GET /admin/`** (admin only):

- Redirects to **`/admin/dashboard`**.

**`GET /admin/dashboard`** (admin only):

- Renders the dashboard template with **`user_count`**, **`post_count`**, and **`comment_count`** from the service.
- Template should surface **quick links** to users, posts, and comments listing pages.

**`GET /admin/users`** (admin only):

- Lists **all users** for review (typically id, username, email, role, created).

**`GET /admin/posts`** (admin only):

- Lists **all posts**, **newest first**, each row with id, **author username**, **content preview** (trimmed), and created time.

**`GET /admin/comments`** (admin only):

- Lists **all comments**, **newest first**, each row with id, **post id**, **author username**, **content preview** (trimmed), and created time.

Preview rules (implementation detail, but useful for docs/tests):

- Post body preview is capped (for example **120** characters) with a trailing **ellipsis** when longer.
- Comment body preview uses a separate cap (for example **160** characters) with the same ellipsis convention.

---

## Access rules

The platform should enforce:

- **Anonymous** requests to any `/admin/*` page used in this task → **302** to **`/auth/login`** (with optional `next=` back to the requested URL).
- **Logged-in users who are not admins** → **302** (or follow to) the **main index** / home experience; they must **not** see admin statistics or tables.
- **Admins** — users whose stored **`role`** is **`admin`** — may open all Task 14 admin routes and see real data.

Access is implemented with **`@admin_required`** on the admin blueprint routes; the decorator resolves the current user from the session and **database** and compares **`user.role`**.

---

## Admin UI expectations

Templates under **`templates/admin/`** should:

- Extend a shared **admin layout** (for example `admin/base_admin.html`) for consistent nav and chrome.
- Present dashboard **stat cards** or lines for **users**, **posts**, and **comments** with clear labels.
- Use **tables** on users, posts, and comments pages that match the fields described above.
- Keep copy and structure appropriate for **read-only monitoring** (no delete/block buttons required in Task 14 itself).

---

## Monitoring vs moderation

- **Monitoring (Task 14):** **Read-only** insight — counts and listings. No requirement here to delete posts, delete comments, block users, or manage reports.
- **Moderation (later tasks):** **Actions** on content or accounts (hard delete, block/unblock, reports queue). Those belong in **separate** documentation and routes and must not be confused with the dashboard’s observational role.

---

## Validation and automated tests

The following behaviours are checked by the Task 14 pytest suite (`testing_config/py_tests/task.py`) and should match the product:

- **Anonymous dashboard** — `GET /admin/dashboard` without a session returns **302** and the **`Location`** includes **`/auth/login`**.
- **Anonymous users listing** — `GET /admin/users` without a session returns **302** and targets **`/auth/login`**.
- **Non-admin blocked** — A logged-in **`role="user"`** account opening **`/admin/dashboard`** (with redirects followed) lands on **public home** content (for example **“Welcome to ConnectX”**) and does **not** show **“Admin Dashboard”**.
- **Admin root redirect** — An admin `GET /admin/` returns **302** with **`/admin/dashboard`** in **`Location`**.
- **Dashboard statistics** — An admin `GET /admin/dashboard` returns **200**; the body includes **“Admin Dashboard”** and numeric **totals** matching seeded data (for example **2** users, **1** post, **1** comment in the test fixture) and **quick links** to users, posts, and comments.
- **Users page** — Admin `GET /admin/users` returns **200**; table includes another user’s **username**, **email**, **id**, and a **`<table>`** marker.
- **Posts preview** — Admin `GET /admin/posts` returns **200**; a very long post body appears **trimmed** to the configured preview length plus an **ellipsis** character.
- **Comments preview** — Admin `GET /admin/comments` returns **200**; a very long comment appears **trimmed** to the configured comment preview length plus an **ellipsis**, and the **author** username appears in the page.

---

## Expected outcome

At the end of this task:

- **`/admin`** exposes a **dashboard** and **read-only listings** for **users**, **posts**, and **comments**.
- **Only admins** can reach these pages; others are **redirected** appropriately.
- **Counts and previews** are driven by **`AdminDashboardService`** and **repositories**, keeping monitoring logic out of raw route SQL.

This establishes **operational visibility** over ConnectX before moderation and safety tooling are layered on top.
