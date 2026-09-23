import pytest
import re
from toolkit.calculator import calculator

@pytest.mark.parametrize(
        "expression,expected",
    [   
        #simpliest tests 
        ("2+2", 4.0),
        ("3-2", 1.0),
        ("5*7", 35.0),
        ("15/3", 5.0),
        ("14//3", 4.0),
        ("20%6", 2.0),

        #order of operations
        ("3+2*3", 9.0),
        ("7-6//4+2", 8.0),
        ("21//5%3", 1.0),

        #unary_minus|unary_plus
        ("-4/-2", 2.0),
        ("+7-+3", 4.0),
        ("--5*+7++3", 38.0),

        #spaces
        ('1 + 2', 3.0),
        ('  -12+ 2 ', -10.0),

        #rational numbers
        ("3.6-2.5", 1.1),
        ("2.5*6/7.5", 2.0),

        #critical_test
        ("-  - 12 *3++ 123//--12 + 8%4 + 0.000000001  -2.5", 43.500000001)
    ]
)
def test_valid_calculation(expression, expected):
    assert calculator(expression) == pytest.approx(expected)

#дописать тесты на запуски с ошибкой