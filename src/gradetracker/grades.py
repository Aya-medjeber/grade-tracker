"""Core grade calculations for the Grade Tracker."""

import math

PASSING_GRADE = 50
INVALID_GRADE = "INVALID"

# (minimum score, letter) checked from highest to lowest
GRADE_BOUNDARIES = (
    (90, "A+"),
    (80, "A"),
    (70, "B"),
    (60, "C"),
    (PASSING_GRADE, "D"),
)


def average(scores):
    """Mean of *scores*. Raises ValueError for an empty list instead of ZeroDivisionError."""
    if not scores:
        raise ValueError("cannot average an empty list of scores")
    return sum(scores) / len(scores)


def letter_grade(score):
    """Convert a 0-100 score to a letter grade, or INVALID if out of range."""
    if score is None or score < 0 or score > 100:
        return INVALID_GRADE
    for minimum, letter in GRADE_BOUNDARIES:
        if score >= minimum:
            return letter
    return "F"


def is_passing(score):
    return score >= PASSING_GRADE


def is_perfect(scores):
    return math.isclose(average(scores), 100.0)
