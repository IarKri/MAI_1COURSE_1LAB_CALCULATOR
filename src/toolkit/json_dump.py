import json
from datetime import datetime

def calculator_dump(expression, calculated_expression):
    """
    Функция записи математичских выражений в файл с историей запросов

    Args:
        expression: математическое выражение

        calculated_expression: результат математического выражения
    
    """

    data = {
        "type": "calculation",
        "expression": expression,
        "result": calculated_expression,
        "time": datetime.now().isoformat()
        }

    #read
    with open("requests_history/successful_requests.json", "r", encoding="utf-8") as json_file:
        requests = json.load(json_file)

    requests.append(data)
    #write
    with open("requests_history/successful_requests.json", "w", encoding="utf-8") as json_file:
        json.dump(requests, json_file, indent=2)

def converter_dump(value, from_unit, to_unit, converted_value):
    """
    Функция записи конвертаций в файл с историей запросов

    Args:
        expression: математическое выражение

        calculated_expression: результат математического выражения
    
    """

    data={
        "type": "convertation",
        "value": str(value)+from_unit,
        "converted_value": str(converted_value)+to_unit,
        "time": datetime.now().isoformat()
    }

    #read
    with open("requests_history/successful_requests.json", "r", encoding="utf-8") as json_file:
        requests = json.load(json_file)

    requests.append(data)
    #write
    with open("requests_history/successful_requests.json", "w", encoding="utf-8") as json_file:
        json.dump(requests, json_file, indent=2)

