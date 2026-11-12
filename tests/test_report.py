"""Unit tests for gradetracker.report (baseline)."""

from gradetracker.report import class_report, top_student

STUDENTS = [
    {"name": "Alice", "scores": [90, 95, 100]},
    {"name": "Bob", "scores": [60, 65, 70]},
]


def test_class_report_lists_every_student():
    report = class_report(STUDENTS)
    assert "Alice" in report
    assert "Bob" in report
    assert "Students: 2" in report


def test_top_student():
    assert top_student(STUDENTS) == "Alice"
