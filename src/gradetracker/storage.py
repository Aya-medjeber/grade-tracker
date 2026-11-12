"""Loading and saving student records as JSON."""

import json
import os


def load_students(path):
    """Return the list of students in *path*, or [] if the file is missing or unreadable."""
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_students(path, students):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(students, f, indent=2)


def connection_string():
    """Build the DB URL from environment variables - credentials are never stored in code."""
    user = os.environ.get("GRADES_DB_USER", "")
    password = os.environ.get("GRADES_DB_PASSWORD", "")
    host = os.environ.get("GRADES_DB_HOST", "localhost")
    return f"db://{user}:{password}@{host}/grades"
