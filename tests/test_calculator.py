import pytest
import re
from src.toolkit.calculator import calculator
from src.toolkit.validator import initial_calculator_validation
from src.toolkit.tokenizer import tokenize

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

@pytest.mark.parametrize(
        "expression, error",
    [
        #Several_Operators
        ("12/*3", "Incorrect operation"),
        ("34+5//*%3","Incorrect operation"),

        #incorrect_float
        ("5+.3", "Float type is incorrect"),
        ("7-5.", "Float type is incorrect"),

        #first_char_is_operator
        ("*5+3", "Expression cant start with * / % //"),
        ("/-7-3", "Expression cant start with * / % //"),

        #no_number_after_operator
        ("8*7-", "Expression cant end with + - * / % // "),
        ("3-5*", "Expression cant end with + - * / % // "),

        #no_operator_between_numbers
        ("10 3", "No operator between numbers"),
        ("13-4*3 5", "No operator between numbers"),
        ("2.5*4//2", "Incorrect value for operation with //")


        
    ]
)

def test_invalid_expression(expression, error):
    with pytest.raises(ValueError, match=re.escape(error)):
        initial_calculator_validation(expression)
        calculator(expression)

@pytest.mark.parametrize(
        "expression, error",
    [
        #ZeroDivisionError
        ("23/0", "Division by zero"),
        ("25*2/0", "Division by zero"),       
    ]                       
)

def test_invalid_expresion_zero_division_error(expression, error):
    with pytest.raises(ZeroDivisionError, match=re.escape(error)):
        initial_calculator_validation(expression)
        calculator(expression)
   
