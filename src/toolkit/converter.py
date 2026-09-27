def convertation(value, from_unit, to_unit):
    '''
    Конвертер величин

    Args:
        value: величина

        from_unit: единицы измерения величины

        to_unit: единицы измерения, в которые надо перевести величину
    
    Returns:
        result: результат конвертации выражения
    '''
    from_unit=from_unit.lower()
    to_unit=to_unit.lower()
    if from_unit == to_unit:
        return value
    from_unit_to_unit=f"from {from_unit} to {to_unit}"
    dict_of_units ={
                    #length
                    "from mm to cm": ('/',10),
                    "from cm to mm": ('*',10),
                    "from mm to m": ('/',1000),
                    "from m to mm": ('*',1000),
                    "from mm to km": ('/',1000000),
                    "from km to mm": ('*',1000000),
                    "from cm to m": ('/',100),
                    "from m to cm": ('*',100),
                    "from cm to km": ('/',100000),
                    "from km to cm": ('*',100000),
                    "from m to km": ('/',1000),
                    "from km to m": ('*',1000),

                    #weight
                    "from g to kg": ('/',1000),
                    "from kg to g": ('*',1000)
                    }
    
    if from_unit_to_unit in dict_of_units:
        return (value/(dict_of_units[from_unit_to_unit][1])) \
            if dict_of_units[from_unit_to_unit][0] == '/' \
                else (value*(dict_of_units[from_unit_to_unit][1]))
    else:
        #temperature
        if from_unit_to_unit == "from c to f":
            return value * 1.8 + 32
        if from_unit_to_unit == "from f to c":
            return (value - 32) / 1.8
        if from_unit_to_unit == "from c to k":
            return value + 273.15
        if from_unit_to_unit == "from k to c":
            return value - 273.15
        if from_unit_to_unit == "from k to f":
            return (value - 273.15)* 1.8 + 32
        if from_unit_to_unit == "from f to k":
            return (value - 32) / 1.8 + 273.15
