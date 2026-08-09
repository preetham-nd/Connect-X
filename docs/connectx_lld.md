# ConnectX — Low-Level Design (Layered Monolith)

## Overview

ConnectX follows a **layered monolith** in Flask: dependencies flow inward.

`HTTP (routes) → services → repositories → models / database`

## Layers

### Routes (`routes/`)

- Handle requests and responses (templates, redirects, status).
- Enforce authentication and authorization (e.g. `admin_required`).
- Call **services** only for domain work.
- **No** SQL or ORM queries for business operations (keeps routes thin).

### Services (`services/`)

- Implement use cases (e.g. admin dashboard statistics and listings).
- Call one or more repositories.
- Shape data for templates (dicts / simple structures).

### Repositories (`repositories/`)

- Encapsulate data access (SQLAlchemy queries).
- Return models or raw query results.
- **No** HTTP, session, or authorization logic.

### Models (`models/`)

- SQLAlchemy mappings and relationships.

## Example: Admin dashboard

`GET /admin/dashboard` → route checks `admin_required` → `AdminDashboardService.get_dashboard_stats()` → `UserRepository` / `PostRepository` → template render.
