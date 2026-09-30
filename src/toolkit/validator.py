from .tokenizer import tokenize


def space_cleaner(chars):
    '''
    функция по очистке выражения от лишних пробелов

    Args:
        chars: математическое выражение для подчсета

    Returns:
        chars: очищенное от лишних пробелов математическое выражение
    '''
    while '  ' in chars:
        chars = chars.replace('  ', ' ')
    return chars


def operators_formatter(chars):
    '''
    функция по форматированию идущих подряд унарных минусов и плюсов

    Args:
        chars: математическое выражение для подсчета

    Returns:
        chars: отформатированное математическое выражение
    '''
    while "++" in chars or "--" in chars:
        chars = chars.replace("++", "+").replace("--", "+")
    return chars


def division_by_zero(chars):
    '''
    Проверка ошибки деления на ноль

    Args:
        chars: математическое выражение для подсчета

    Returns: True/False
    '''
    chars = tokenize(chars)
    for char in range(len(chars)-1):
        if (chars[char][0] == '/' or chars[char][0] == '//' or chars[char][0] == '%') and \
                chars[char+1][0] == "0":
            return True
    return False


def no_number_after_operator(chars):
    '''
    Проверка ошибки завершения выражения на оператор

    Args:
        chars: математическое выражение для подсчета

    Returns: True/False
    '''
    if chars[-1] in ['-', '+', '*', '/', '//', '%']:
        return True
    return False


def incorrect_float(chars):
    '''
    Проверка ошибки некорректного введения числа типа float

    Args:
        chars: математическое выражение для подсчета

    Returns: True/False
    '''
    if any(f' .{char}' in chars or f'{char}. ' in chars for char in '0123456789'):
        return True
    return False


def several_operators(chars):
    '''
    Проверка ошибки введения нескольких операторов подряд

    Args:
        chars: математическое выражение для подсчета

    Returns: True/False
    '''
    chars = tokenize(chars)
    for char in range(len(chars)-1):
        if (chars[char][1] in "OPERATOR" and chars[char+1][1] in "OPERATOR") and\
                (chars[char][0] not in ['-', '+'] or chars[char+1][0] not in ['-', '+']):
            return True
    return False


def no_operator_between_numbers(chars):
    '''
    Проверка ошибки отсутствия оператора между операндами

    Args:
        chars: математическое выражение для подсчета

    Returns: True/False
    '''
    for char in range(len(chars)-2):
        if (chars[char] in '0123456789' and chars[char+1] == ' ' and
                chars[char+2] in '0123456789'):
            return True
    return False


def first_char_is_operator(chars):
    '''
    Проверка ошибки начала строки с неверного оператора

    Args:
        chars: математическое выражение для подсчета

    Returns: True/False
    '''
    if chars[0] in ['*', '/', '//', '%']:
        return True
    return False


def unknown_unit(from_unit, to_unit):
    '''
    Проверка ошибки ввода неизвестной единицы измерения

    Args:
        from_unit: единица измерения значения
        to_unit: единица измерения, в которую переводится значение

    Returns: True/False
    '''
    if from_unit not in ['cm', 'mm', 'm', 'km', 'c', 'f', 'k', 'kg', 'g'] or \
            to_unit not in ['cm', 'mm', 'm', 'km', 'c', 'f', 'k', 'kg', 'g']:
        return True
    return False


def wrong_convertation_units(from_unit, to_unit):
    '''
    Проверка ошибки ввода разных типов единиц измерения

    Args:
        from_unit: единица измерения значения
        to_unit: единица измерения, в которую переводится значение

    Returns: True/False
    '''
    if from_unit in ['cm', 'mm', 'm', 'km'] and to_unit not in ['cm', 'mm', 'm', 'km']:
        return True
    if from_unit in ['c', 'f', 'k'] and to_unit not in ['c', 'f', 'k']:
        return True
    if from_unit in ['kg', 'g'] and to_unit not in ['kg', 'g']:
        return True
    return False


def temperature_below_absolute_zero(value, from_unit):
    '''
    Проверка ошибки ввода температуры ниже абсолютного нуля

    Args:
        value: значение для перевода
        from_unit: единица измерения значения

    Returns: True/False
    '''
    if from_unit == 'c' and value < -273.15:
        return True
    if from_unit == 'f' and value < -459.67:
        return True
    if from_unit == 'k' and value < 0:
        return True
    return False


def value_validation(value):
    '''
    Проверка ошибки ввода некорректного значения 

    Args:
        value: значение для конвертации

    Returns: True/False
    '''
    if not isinstance(value, int) and not isinstance(value, float):
        return True
    return False


def empty_sequence(sequence):
    '''
    Проверка ошибки ввода пустой строки для обработки

    Args:
        sequence: выражение для обработки калькулятором/конвертером

    Returns: True/False
    '''
    if sequence == '':
        return True
    return False


def initial_calculation_validation(expression):
    '''
    Валидатор математичского выражения, поступивешего на вход калькулятору

    Args:
        expression: математическое выражение

    Returns:
        Ошибку, возникнувшую при валидации, или False, если ошибки не были найдены

    Raises:
        ValueError: один из типов проверяемых при валидации ошибок
        ZeroDivisionError: ошибка деления на ноль
    '''
    if empty_sequence(expression):
        raise ValueError("Empty sequence")
    if first_char_is_operator(expression):
        raise ValueError("Expression cant start with * / % //")
    if no_operator_between_numbers(expression):
        raise ValueError("No operator between numbers")
    if several_operators(expression):
        raise ValueError("Incorrect operation")
    if division_by_zero(expression):
        raise ZeroDivisionError("Division by zero")
    if no_number_after_operator(expression):
        raise ValueError("Expression cant end with + - * / % // ")
    return False


def initial_convertation_validation(value, from_unit, to_unit):
    '''
    Валидатор данных, поступивших на вход конвертеру

    Args:
        value: значение для конвертации
        from_unit: единица измерения значения
        to_unit: единица измерения, в которую переводится значение

    Returns:
        Ошибку, возникнувшую при валидации, или False, если ошибки не были найдены

    Raises:
        ValueError: один из типов проверяемых при валидации ошибок
    '''
    if empty_sequence(value):
        raise ValueError("Empty sequence")
    if value_validation(value):
        raise ValueError("Incorrect value")
    if unknown_unit(from_unit, to_unit):
        raise ValueError("Unknown Unit")
    if wrong_convertation_units(from_unit, to_unit):
        raise ValueError("Different type of Units")
    if temperature_below_absolute_zero(value, from_unit):
        raise ValueError("Below absolute zero")
    return False
