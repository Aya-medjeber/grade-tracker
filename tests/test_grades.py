"""Unit tests for gradetracker.grades."""

import pytest

from gradetracker.grades import average, letter_grade, is_passing


def test_average_of_scores():
    assert average([80, 90, 100]) == 90


def test_average_single_score():
    assert average([72]) == 72


# Happy path: every grade band, including the exact boundary values
@pytest.mark.parametrize(
    "score, expected",
    [
        (100, "A+"), (90, "A+"),
        (89.9, "A"), (80, "A"),
        (79, "B"), (70, "B"),
        (69, "C"), (60, "C"),
        (59, "D"), (50, "D"),
        (49.9, "F"), (0, "F"),
    ],
)
def test_letter_grade_bands(score, expected):
    assert letter_grade(score) == expected


# Sad path: anything outside 0-100 (or missing) is rejected
@pytest.mark.parametrize("score", [None, -1, 100.1, 150])
def test_letter_grade_invalid(score):
    assert letter_grade(score) == "INVALID"


def test_is_passing():
    assert is_passing(50) is True
    assert is_passing(49) is False
