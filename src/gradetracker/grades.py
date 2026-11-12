"""Core grade calculations for the Grade Tracker."""

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
    total = 0
    for s in scores:
        total = total + s
    return total / len(scores)


def letter_grade(score):
    """Convert a 0-100 score to a letter grade, or INVALID if out of range."""
    if score is None or score < 0 or score > 100:
        return INVALID_GRADE
    for minimum, letter in GRADE_BOUNDARIES:
        if score >= minimum:
            return letter
    return "F"


def is_passing(score):
    if score >= PASSING_GRADE:
        return True
    else:
        return False


def is_perfect(scores):
    avg = average(scores)
    if avg == 100.0:
        return True
    return False
