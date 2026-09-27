from src.toolkit.tokenizer import tokenize

def division_by_zero(chars):
    if '/0' in chars or '//0' in chars:
        return True
    return False

def no_number_after_operator(chars):
    if chars[-1] in ['-','+','*','/','//','%']:
        return True
    return False

def incorrect_float(chars):
    if any(f' .{char}' in chars or f'{char}. ' in chars for char in '0123456789'):
        return True
    return False

def several_operators(chars):
    for char in range(len(chars)-1):
        if chars[char] in ['-','+','*','/','//','%'] and chars[char+1] in ['-','+','*','/','//','%'] :
            return True
    return False

def no_operator_between_numbers(chars):
    for char in range(len(chars)-2):
        if (chars[char] in '0123456789' and chars[char+1] == ' ' and \
            chars[char+2] in '0123456789'):
            return True
    return False

def first_char_is_operator(chars):
    if chars[0] in ['*', '/', '//', '%']:
        return True
    return False

def unknown_unit(from_unit, to_unit):
    if from_unit not in ['cm', 'mm', 'm', 'km', 'c', 'f', 'k', 'kg', 'g'] or \
    to_unit not in ['cm', 'mm', 'm', 'km', 'c', 'f', 'k', 'kg', 'g']:
        return True
    return False

def wrong_convertation_units(from_unit, to_unit):
    if from_unit in ['cm', 'mm', 'm', 'km'] and to_unit not in ['cm', 'mm', 'm', 'km']:
        return True
    if from_unit in ['c', 'f', 'k'] and to_unit not in ['c', 'f', 'k']:
        return True
    if from_unit in ['kg', 'g'] and to_unit not in ['kg', 'g']:
        return True
    return False

def temperature_below_absolute_zero(value, from_unit):
    if from_unit == 'c' and value < -273.15:
        return True
    if from_unit == 'f' and value < -459.67:
        return True
    if from_unit == 'k' and value < 0:
        return True
    return False

def space_cleaner(chars):
    while '  ' in chars:
        chars=chars.replace('  ', ' ')
    return chars

def operators_formatter(chars):
    while "++" in chars or "--" in chars:
        chars=chars.replace("++", "+").replace("--", "-")
    return chars


def initial_calculation_validation(expression):
    if no_operator_between_numbers(expression):
        raise ValueError("No operator between numbers")
    if first_char_is_operator(expression):
        raise ValueError("Expression cant start with * / % //")
    if no_number_after_operator(expression):
        raise ValueError("Expression cant end with + - * / % // ")
    if several_operators(expression):
        raise ValueError("Incorrect operation")
    if division_by_zero(expression):
        raise ZeroDivisionError("Division by zero")
    return False

def initial_convertation_validation(from_unit, to_unit):
    from_unit=from_unit.lower()
    to_unit=to_unit.lower()
    if unknown_unit(from_unit, to_unit):
        raise ValueError("Unknown Unit")
    if wrong_convertation_units(from_unit, to_unit):
        raise ValueError("Different type of Units")
    if temperature_below_absolute_zero(from_unit, to_unit):
        raise ValueError("Below absolute zero")
    return False
    

# s="/1*+2"
# print(initial_calculator_validation(s))
##программа моежт некорректно работать с пробелами и двойным минусом/плюсом - составить алгоритм по корректной поэтапной зачистке/проверке выражения
##Проверить типы ошибок

