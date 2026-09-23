import pytest
from toolkit.converter import converter

@pytest.mark.parametrize(
    "value, from_unit_to_unit, expected",
    [
        #length
        (10, "from cm to mm", 100.0),
        (10, "from m to km", 0.01),
        (100, "from cm to m", 1.0),
        (5, "from km to m", 5000.0),
        (1200, "from mm to m", 1.2),

        #weight
        (500, "from g to kg", 0.5),
        (3.42, "from kg to g", 3420.0),
        (1234, "from g to kg", 1.234),

        #temperature
        (20, "from c to k", 293.15),
        (286, "from k to f", 55.13),
        (56, "from f to k", 286.48),
        (-25, "from c to f", -13.0),
    ]
)

def test_valid_converter(value, from_unit_to_unit, expected):
    assert converter(value, from_unit_to_unit) == pytest.approx(expected, abs = 0.005)

#дописать тесты на запуски с ошибкой