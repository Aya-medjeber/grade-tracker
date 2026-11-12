"""Independent risk test: what happens when a student has no scores yet?

SonarQube Cloud does not flag this, because division by len(scores) is only
a problem at runtime when the list is empty.
"""

import pytest

from gradetracker.grades import average


def test_average_of_empty_list_raises_clear_error():
    with pytest.raises(ValueError):
        average([])
