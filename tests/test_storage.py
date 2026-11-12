"""Unit tests for gradetracker.storage."""

from gradetracker.storage import connection_string, load_students, save_students

STUDENTS = [{"name": "Alice", "scores": [90, 95]}]


def test_save_then_load_round_trip(tmp_path):
    path = tmp_path / "students.json"
    save_students(path, STUDENTS)
    assert load_students(path) == STUDENTS


def test_load_missing_file_returns_empty_list(tmp_path):
    assert load_students(tmp_path / "does_not_exist.json") == []


def test_load_corrupt_file_returns_empty_list(tmp_path):
    path = tmp_path / "broken.json"
    path.write_text("{ not valid json", encoding="utf-8")
    assert load_students(path) == []


def test_connection_string_reads_environment(monkeypatch):
    monkeypatch.setenv("GRADES_DB_USER", "teacher")
    monkeypatch.setenv("GRADES_DB_PASSWORD", "from-env")
    monkeypatch.setenv("GRADES_DB_HOST", "db.example")
    assert connection_string() == "db://teacher:from-env@db.example/grades"
