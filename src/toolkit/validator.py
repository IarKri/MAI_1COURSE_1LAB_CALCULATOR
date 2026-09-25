from src.toolkit.tokenizer import tokenize
from src.toolkit.errors import several_operators
from src.toolkit.errors import no_operator_between_numbers
from src.toolkit.errors import first_char_is_operator
from src.toolkit.errors import no_number_after_operator
from src.toolkit.errors import division_by_zero
from src.toolkit.errors import incorrect_float
from src.toolkit.errors import temperature_below_absolute_zero
from src.toolkit.errors import unknown_unit
from src.toolkit.errors import wrong_convertation_units

def space_cleaning(chars):
    while '  ' in chars:
        chars=chars.replace('  ',' ')
    return chars

def initial_calculator_validation(expression):
    if no_operator_between_numbers(expression):
        raise ValueError("No operator between numbers")
    if first_char_is_operator(expression):
        raise ValueError("Expression cant start with * / % //")
    if no_number_after_operator(expression):
        raise ValueError("Expression cant end with + - * / % // ")
    if several_operators(expression):
        raise ValueError("Incorrect operation")
    if division_by_zero(expression):
        raise ZeroDivisionError("Division by 0")
    return False

def initial_converter_validation(expression):
    if unknown_unit(expression):
        raise ValueError("Unknown Unit")
    if wrong_convertation_units(expression):
        raise ValueError("Different type of Units")
    if temperature_below_absolute_zero(expression):
        raise ValueError("Below absolute zero")
    return False
    

# s="/1*+2"
# print(initial_calculator_validation(s))
##программа моежт некорректно работать с пробелами и двойным минусом/плюсом - составить алгоритм по корректной поэтапной зачистке/проверке выражения
##Проверить типы ошибок

