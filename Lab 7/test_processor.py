
from hypothesis import given, strategies as st
from processor import parse_application, processing_average, payable_fee


# Test 1: Fuzz parse_application
@given(st.text() | st.none())
def test_parse_application_no_crash(s):
    parse_application(s)


# Test 2: Fuzz processing_average
@given(st.text() | st.none())
def test_processing_average_no_crash(s):
    processing_average(s)


# Test 3: Fuzz payable_fee
@given(st.text() | st.none())
def test_payable_fee_no_crash(s):
    payable_fee(s)


import pytest


@pytest.mark.parametrize("input_data, expected", [
    ("tourist:2", ("Tourist", 2)),
    ("business:5", ("Business", 5)),
    ("tourist:", None),
    (":2", None),
    ("tourist:-1", None),
])
def test_parse_application_correctness(input_data, expected):
    assert parse_application(input_data) == expected


@pytest.mark.parametrize("input_data, expected", [
    ("5,10,21", 12),
    ("10,20", 15),
    ("5,,10", None),
    ("", None),
    ("-5,10", None),
])
def test_processing_average_correctness(input_data, expected):
    assert processing_average(input_data) == expected


@pytest.mark.parametrize("input_data, expected", [
    ("6000|500", 6580.0),
    ("1000|200", 980.0),
    ("abc|500", None),
    ("|", None),
    ("-100|0", None),
])
def test_payable_fee_correctness(input_data, expected):
    assert payable_fee(input_data) == expected
