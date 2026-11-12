"""Independent risk test: what happens when a student has no scores yet?

SonarQube Cloud does not flag this, because division by len(scores) is only
a problem at runtime when the list is empty.
"""

import pytest

from gradetracker.grades import average, is_perfect


def test_average_of_empty_list_raises_clear_error():
    with pytest.raises(ValueError):
        average([])


def test_is_perfect_uses_tolerant_float_comparison():
    # 0.1 + 0.2 style rounding must not break a perfect score
    assert is_perfect([100.0, 100.0, 100.0]) is True
    assert is_perfect([33.3 * 3 + 0.1, 100.0]) is True
    assert is_perfect([99, 100]) is False
