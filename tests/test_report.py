"""Unit tests for gradetracker.report."""

from gradetracker.report import class_report, honours_report, top_student, top_students

STUDENTS = [
    {"name": "Alice", "scores": [90, 95, 100]},
    {"name": "Bob", "scores": [60, 65, 70]},
]


def test_class_report_lists_every_student():
    report = class_report(STUDENTS)
    assert "CLASS REPORT" in report
    assert "Alice" in report
    assert "Bob" in report
    assert "Students: 2" in report


def test_honours_report_only_lists_students_at_80_or_more():
    report = honours_report(STUDENTS)
    assert "HONOURS REPORT" in report
    assert "Alice" in report
    assert "Bob" not in report


def test_top_student():
    assert top_student(STUDENTS) == "Alice"


def test_top_students_handles_ties():
    tied = STUDENTS + [{"name": "Cara", "scores": [95, 95, 95]}]
    assert top_students(tied) == ["Alice", "Cara"]


def test_top_student_of_empty_class_is_none():
    assert top_student([]) is None
    assert top_students([]) == []
