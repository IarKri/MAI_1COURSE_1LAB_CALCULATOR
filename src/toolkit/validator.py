from tokenizer import tokenize
from errors import double_operator
from errors import no_operator_between_numbers
from errors import first_char_is_operator
from errors import no_number_after_operator
from errors import division_by_zero
from errors import incorrect_float
from errors import temperature_below_absolute_zero
from errors import unknown_unit
from errors import wrong_convertation_units

def space_cleaning(chars):
    for char in chars:
        if char == ' ':
            chars=chars.replace(char, '')
    return chars

def initial_calculator_validation(expression):
    if no_operator_between_numbers(expression):
        raise ValueError("Между операндами нет оператора")
    if first_char_is_operator(expression):
        raise ValueError("Выражение не может начинаться на * / % //")
    if no_number_after_operator(expression):
        raise ValueError("Выражение не может заканчиваться оператором")
    if double_operator(expression):
        raise ValueError("Некорректная арифметическая операция")
    if division_by_zero(expression):
        raise ZeroDivisionError("Деление на 0")
    if incorrect_float(expression):
        raise ValueError("Число типа float введено некорректно")

def initial_converter_validation(expression):
    if unknown_unit(expression):
        raise ValueError("Неизвестная единица измерения")
    if wrong_convertation_units(expression):
        raise ValueError("Разные типы единиц измерения")
    if temperature_below_absolute_zero(expression):
        raise ValueError("Температура ниже абсолютного нуля")

    

# s="/1*+2"
# print(initial_calculator_validation(s))
##программа моежт некорректно работать с пробелами и двойным минусом/плюсом - составить алгоритм по корректной поэтапной зачистке/проверке выражения
##Проверить типы ошибок

