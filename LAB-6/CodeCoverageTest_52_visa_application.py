"""Line/code coverage tests for visa_application.py.

These tests execute every executable line at least once. They deliberately
focus on statement coverage; branch alternatives are completed in the
separate BranchCoverageTest_52_visa_application.py suite.
"""
import pytest

from visa_application import visa_fee, documents_complete, application_status


def test_visa_fee_unknown_type_raises():
    with pytest.raises(ValueError, match="unknown visa type"):
        visa_fee("work", 2, "normal", "B")


def test_visa_fee_negative_entries_raises():
    with pytest.raises(ValueError, match="invalid entries"):
        visa_fee("tourist", -1, "normal", "B")


def test_visa_fee_included_entries_return_zero():
    assert visa_fee("tourist", 1, "normal", "B") == 0


def test_visa_fee_nationality_a_adds_included_entry():
    assert visa_fee("tourist", 3, "normal", "A") == 40


def test_visa_fee_express_rate():
    assert visa_fee("student", 4, "express", "B") == 200


def test_visa_fee_large_extra_count_uses_rate_increase():
    assert visa_fee("business", 9, "normal", "B") == 360


def test_visa_fee_large_extra_count_express_adds_extra_surcharge():
    assert visa_fee("business", 9, "express", "B") == 780


def test_documents_complete_new_application():
    assert documents_complete(3, 2, False) is True


def test_documents_incomplete_new_application_due_to_insufficient_forms():
    assert documents_complete(2, 2, False) is False


def test_documents_incomplete_new_application_due_to_insufficient_photos():
    assert documents_complete(3, 1, False) is False


def test_documents_complete_renewal():
    assert documents_complete(1, 0, True) is True


def test_application_status_express_peak_open():
    assert application_status(25, True, True) == "open"


def test_application_status_normal_non_peak_closing():
    assert application_status(20, False, False) == "closing"


def test_application_status_normal_peak_closed():
    assert application_status(20, False, True) == "closed"
