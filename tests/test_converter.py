import re

import pytest

from src.toolkit.converter import convertation
from src.toolkit.validator import initial_convertation_validation


@pytest.mark.parametrize(
    "value, from_unit, to_unit, expected",
    [
        # length
        (10, "cm", "mm", 100.0),
        (10, "m", "km", 0.01),
        (100, "cm", "m", 1.0),
        (5, "km", "m", 5000.0),
        (1200, "mm", "m", 1.2),

        # weight
        (500, "g", "KG", 0.5),
        (3.42, "kg", "g", 3420.0),
        (1234, "g", "kg", 1.234),

        # temperature
        (20, "C", "K", 293.15),
        (286, "k", "f", 55.13),
        (50, "f", "k", 283.15),
        (-25, "c", "f", -13.0),
    ]
)
def test_valid_convertation(value, from_unit, to_unit, expected):
    assert convertation(value, from_unit, to_unit) == pytest.approx(expected)


@pytest.mark.parametrize(
    "value, from_unit, to_unit, error",
    [
        # unknown_unit
        (100, 'kg', 'lb', 'Unknown Unit'),
        (25, 'm', 'inch', 'Unknown Unit'),

        # wrong_convertation_units
        (1000, 'g', 'km', 'Different type of Units'),
        (25, 'cm', 'c', 'Different type of Units'),

        # temperature_below_absolute_zero
        (-274, 'c', 'f', 'Below absolute zero'),
        (-1, 'k', 'c', 'Below absolute zero'),

        # empty_sequence
        ('', 'g', 'km', 'Empty sequence'),

        # wrong_value
        ('abc', 'g', 'kg', 'Incorrect value')
    ]
)
def test_invalid_convertation(value, from_unit, to_unit, error):
    with pytest.raises(ValueError, match=re.escape(error)):
        initial_convertation_validation(value, from_unit, to_unit)
