"""Branch coverage tests for visa_application.py.

The cases exercise both outcomes of each decision, including threshold
boundaries and nested conditions, without changing the application code.
"""
import pytest

from visa_application import visa_fee, documents_complete, application_status


@pytest.mark.parametrize("visa_type,entries,speed,nationality,expected", [
    ("tourist", 1, "normal", "B", 0),
    ("tourist", 2, "normal", "B", 40),
    ("tourist", 2, "express", "B", 100),
    ("tourist", 3, "normal", "A", 40),
    ("student", 3, "normal", "A", 40),
    ("business", 9, "normal", "B", 360),
    ("business", 9, "express", "B", 780),
    ("business", 3, "normal", "B", 0),
])
def test_visa_fee_valid_decision_combinations(
    visa_type, entries, speed, nationality, expected
):
    assert visa_fee(visa_type, entries, speed, nationality) == expected


def test_visa_fee_unknown_type_branch():
    with pytest.raises(ValueError, match="unknown visa type"):
        visa_fee("other", 1, "normal", "B")


def test_visa_fee_negative_entries_branch():
    with pytest.raises(ValueError, match="invalid entries"):
        visa_fee("tourist", -1, "normal", "B")


@pytest.mark.parametrize("forms,photos,renewal,expected", [
    (1, 0, True, True),
    (0, 5, True, False),
    (3, 2, False, True),
    (2, 2, False, False),
    (3, 1, False, False),
])
def test_documents_complete_all_decision_outcomes(forms, photos, renewal, expected):
    assert documents_complete(forms, photos, renewal) is expected


@pytest.mark.parametrize("days,express,peak,expected", [
    (10, True, False, "open"),
    (9, True, False, "closing"),
    (-6, True, False, "closed"),
    (30, False, False, "open"),
    (15, False, False, "closing"),
    (14, False, False, "closed"),
    (45, False, True, "open"),
    (30, False, True, "closing"),
    (29, False, True, "closed"),
    (25, True, True, "open"),
    (10, True, True, "closing"),
    (9, True, True, "closed"),
])
def test_application_status_all_decision_outcomes(days, express, peak, expected):
    assert application_status(days, express, peak) == expected
