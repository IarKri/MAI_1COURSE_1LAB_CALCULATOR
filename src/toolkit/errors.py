def division_by_zero(chars):
    if '/0' in chars:
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
        return((chars[char] in ['+', '-', '*', '/', '//', '%'] and \
            chars[char+1] in ['*', '/', '//', '%']) or \
                (chars[char] in ['*', '/', '//', '%'] and chars[char+1] in ['+', '-', '*', '/', '//', '%']))

def no_operator_between_numbers(chars):
    while ' ' in chars:
        chars=chars.replace(' ','')
    if all(chars[char] in '0123456789' and chars[char+1] == ' ' and \
           chars[char+2] in '0123456789' for char in range(len(chars) - 2)):
        return True
    return False

def first_char_is_operator(chars):
    if chars[0] in ['*', '/', '//', '%']:
        return True
    return False

def unknown_unit(from_unit_to_unit):
    tokens=[token for token in from_unit_to_unit.split()]
    if tokens[1] not in ['cm', 'mm', 'm', 'km', 'c', 'f', 'k', 'kg', 'g'] or \
    tokens[3] not in ['cm', 'mm', 'm', 'km', 'c', 'f', 'k', 'kg', 'g']:
        return True
    return False

def wrong_convertation_units(from_unit_to_unit):
    tokens=[token for token in from_unit_to_unit.split()]
    if tokens[1] in ['cm', 'mm', 'm', 'km'] and tokens[3] not in ['cm', 'mm', 'm', 'km']:
        return True
    if tokens[1] in ['c', 'f', 'k'] and tokens[3] not in ['c', 'f', 'k']:
        return True
    if tokens[1] in ['kg', 'g'] and tokens[3] not in ['kg', 'g']:
        return True
    return False

def temperature_below_absolute_zero(value, from_unit_to_unit):
    tokens=[token for token in from_unit_to_unit.split()]
    if tokens[1] == 'c' and value < -273.15:
        return True
    if tokens[1] == 'f' and value < -459.67:
        return True
    if tokens[1] == 'k' and value < 0:
        return True
    return False

# print(temperature_below_absolute_zero(-300, 'from c to f'))