"""Unit tests for gradetracker.grades (baseline)."""

from gradetracker.grades import average, letter_grade, is_passing


def test_average_of_scores():
    assert average([80, 90, 100]) == 90


def test_average_single_score():
    assert average([72]) == 72


def test_letter_grade_a_plus():
    assert letter_grade(95) == "A+"


def test_letter_grade_b():
    assert letter_grade(74) == "B"


def test_letter_grade_fail():
    assert letter_grade(30) == "F"


def test_letter_grade_out_of_range():
    assert letter_grade(150) == "INVALID"


def test_is_passing():
    assert is_passing(50) is True
    assert is_passing(49) is False
