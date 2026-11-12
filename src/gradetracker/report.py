"""Text reports for a class of students."""

from gradetracker.grades import average, letter_grade

HONOURS_THRESHOLD = 80


def _build_report(title, students, include=lambda avg: True):
    """Shared report layout used by every report type (removes duplicated code)."""
    lines = ["=" * 40, title, "=" * 40]
    for student in students:
        avg = average(student["scores"])
        if include(avg):
            lines.append(f"{student['name']:<20} {avg:>6.1f}  {letter_grade(avg)}")
    lines.append("-" * 40)
    lines.append(f"Students: {len(students)}")
    return "\n".join(lines)


def class_report(students):
    return _build_report("CLASS REPORT", students)


def honours_report(students):
    return _build_report(
        "HONOURS REPORT", students, include=lambda avg: avg >= HONOURS_THRESHOLD
    )


def top_students(students):
    """Return every student sharing the highest average (handles ties)."""
    if not students:
        return []
    averages = {s["name"]: average(s["scores"]) for s in students}
    best = max(averages.values())
    return [name for name, avg in averages.items() if avg == best]


def top_student(students):
    """Return the first top student, or None for an empty class."""
    leaders = top_students(students)
    return leaders[0] if leaders else None
