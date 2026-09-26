from src.toolkit.validator import initial_converter_validation
def converter(value, from_unit_to_unit):
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

    from_unit_to_unit = from_unit_to_unit.lower()
    if from_unit_to_unit in dict_of_units:
        return (value/float(dict_of_units[from_unit_to_unit][1])) \
            if dict_of_units[from_unit_to_unit][0] == '/' \
                else (value*float(dict_of_units[from_unit_to_unit][1]))
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



# print(converter(10,'from cm to mm'))