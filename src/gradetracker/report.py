"""Text reports for a class of students."""

from gradetracker.grades import average, letter_grade


def class_report(students):
    lines = []
    count = 0
    lines.append("=" * 40)
    lines.append("CLASS REPORT")
    lines.append("=" * 40)
    for student in students:
        name = student["name"]
        scores = student["scores"]
        avg = average(scores)
        grade = letter_grade(avg)
        lines.append(f"{name:<20} {avg:>6.1f}  {grade}")
    lines.append("-" * 40)
    lines.append(f"Students: {len(students)}")
    return "\n".join(lines)


def honours_report(students):
    lines = []
    lines.append("=" * 40)
    lines.append("HONOURS REPORT")
    lines.append("=" * 40)
    for student in students:
        name = student["name"]
        scores = student["scores"]
        avg = average(scores)
        grade = letter_grade(avg)
        if avg >= 80:
            lines.append(f"{name:<20} {avg:>6.1f}  {grade}")
    lines.append("-" * 40)
    lines.append(f"Students: {len(students)}")
    return "\n".join(lines)


def top_student(students):
    # TODO: handle ties between students
    best = None
    best_avg = -1
    for student in students:
        avg = average(student["scores"])
        if avg > best_avg:
            best_avg = avg
            best = student["name"]
    # print("best student is", best)
    # print("with average", best_avg)
    return best
