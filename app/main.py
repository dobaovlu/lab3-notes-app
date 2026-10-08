# app/main.py — Lab 3 starting point (FastAPI)
#
# This is the end state of the Week 4 practice: the app reads DATABASE_URL
# from the environment and proves the database connection at /health/db.
#
# Lab 3, Task A asks you to:
#   1. read the port from the environment (that change is in the Dockerfile);
#   2. add a /health endpoint below (see the TODO).
import os

import psycopg
from fastapi import FastAPI
from fastapi.responses import JSONResponse

APP_VERSION = "1.0.1"  # Lab 3, Task E: change this, merge, and watch it go live
APP_ENV = os.environ.get("APP_ENV", "development")
DATABASE_URL = os.environ["DATABASE_URL"]  # crash at start if it is missing
MISSING = os.environ["DEFINITELY_NOT_SET"]  # Lab 3, Task F: deliberate start-up failure

app = FastAPI(title="notes")


@app.get("/")
def home():
    return {"app": "notes", "status": "running", "version": APP_VERSION, "env": APP_ENV}


@app.get("/health/db")
def health_db():
    # Week 4: proves the database works. Not the platform health check —
    # on Render it reports an error until Week 7 connects Supabase.
    try:
        with psycopg.connect(DATABASE_URL, connect_timeout=3) as conn:
            n = conn.execute("SELECT count(*) FROM notes").fetchone()[0]
        return {"db": "ok", "notes": n}
    except Exception as err:
        print("health/db failed:", err)  # the detail goes to the logs, not to the browser
        return JSONResponse(status_code=503, content={"db": "error"})


@app.get("/health")
def health():
    # Fast, no auth, touches nothing — this is the platform health check.
    return {"status": "ok"}
