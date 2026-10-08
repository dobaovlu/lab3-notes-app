# Notes app — Lab 3 starting point (Python + FastAPI)

This is a minimal working result of Lab 2 and the Week 4 practice: a small web app,
a `Dockerfile`, a `.dockerignore`, and a `compose.yml` that starts the app with a
PostgreSQL database. Use it only if your team does not have a working Dockerfile.

It is the starting point for Lab 3, **not** a solution to it. Lab 3 Task A is still yours:
the port is hard-coded and there is no `/health` endpoint yet.

## 1. Put it in your team repository

1. Copy every file in this folder into your team repository folder — including the hidden
   files `.dockerignore`, `.gitignore` and `.env.example`, and the folders `app/` and `db/`.
2. Commit and push to `main` (through a pull request if your branch is protected):

       git add .
       git commit -m "Start Lab 3 from the starter"
       git push

## 2. Check it works on your machine (before the lab)

    podman build -t app:dev .
    podman run --rm -p 3000:8000 -e DATABASE_URL=postgresql://unused@localhost/none app:dev

Open http://localhost:3000 — you should see:

    {"app":"notes","status":"running","version":"1.0.0","env":"development"}

Press Ctrl+C to stop. (Everything also works with `docker` in place of `podman`.)

To run the full local stack with the database (the Week 4 way):

    cp .env.example .env          # works in PowerShell too
    # edit .env and set DB_PASSWORD to letters and digits only, e.g. labpass2026
    podman compose up --build

Then http://localhost:3000/health/db should show `{"db":"ok","notes":1}`.

## 3. Then follow the Lab 3 handout from Task A

| Handout says              | In this starter                                      |
|---------------------------|------------------------------------------------------|
| `app.main:app`            | the module is `app/main.py` — same name, nothing to change |
| "Add a health endpoint"   | the `TODO` at the bottom of `app/main.py`            |
| "Read the port from the environment" | the last line of the `Dockerfile`          |
| "A visible change" (Task E) | change `APP_VERSION` in `app/main.py`              |

Tip for Task A: inside `sh -c`, start the command with `exec`
(`"exec uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000}"`), so uvicorn — not the
shell — receives the stop signal when Render replaces the container.

## Environment variables on Render (Task C)

| Variable       | Value on Render                                        |
|----------------|--------------------------------------------------------|
| `DATABASE_URL` | Required, or the app stops at start-up with `KeyError: 'DATABASE_URL'`. Until Week 7, any placeholder works, e.g. `postgresql://app:unused@localhost:5432/appdb`. `/health/db` will answer 503 on Render until then — that is expected. |
| `APP_ENV`      | `production` — the home page shows it, so you can see your configuration arrived. |
| `PORT`         | Do **not** set it. Render sets it for you.             |

Never commit `.env`. It is already listed in `.gitignore` and `.dockerignore`.
