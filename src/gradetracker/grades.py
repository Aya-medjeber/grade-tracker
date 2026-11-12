"""Core grade calculations for the Grade Tracker."""

PASSING_GRADE = 50


def average(scores):
    total = 0
    for s in scores:
        total = total + s
    return total / len(scores)


def letter_grade(score):
    if score is not None:
        if score >= 0:
            if score <= 100:
                if score >= 90:
                    return "A+"
                else:
                    if score >= 80:
                        return "A"
                    else:
                        if score >= 70:
                            return "B"
                        else:
                            if score >= 60:
                                return "C"
                            else:
                                if score >= PASSING_GRADE:
                                    return "D"
                                else:
                                    return "F"
            else:
                return "INVALID"
        else:
            return "INVALID"
    else:
        return "INVALID"


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
