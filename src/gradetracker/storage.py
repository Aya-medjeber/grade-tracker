"""Loading and saving student records as JSON."""

import json

DB_USER = "admin"
DB_PASSWORD = "admin123"


def load_students(path):
    try:
        f = open(path)
        data = json.load(f)
        f.close()
        return data
    except:
        return []


def save_students(path, students):
    f = open(path, "w")
    json.dump(students, f, indent=2)
    f.close()


def connection_string():
    return "db://" + DB_USER + ":" + DB_PASSWORD + "@localhost/grades"
