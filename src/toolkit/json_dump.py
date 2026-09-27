import json
from datetime import datetime

def calculator_dump(expression, calculated_expression):

    data = {
        "type": "calculation",
        "expression": expression,
        "result": calculated_expression,
        "time": datetime.now().isoformat()
        }

    with open("requests_history/successful_requests.json", "r", encoding="utf-8") as json_file:
        requests = json.load(json_file)

    requests.append(data)

    with open("requests_history/successful_requests.json", "w", encoding="utf-8") as json_file:
        json.dump(requests, json_file, indent=2)

def converter_dump(value, from_unit, to_unit, converted_value):

    data={
        "type": "convertation",
        "value": str(value)+from_unit,
        "converted_value": str(converted_value)+to_unit,
        "time": datetime.now().isoformat()
    }

    with open("requests_history/successful_requests.json", "r", encoding="utf-8") as json_file:
        requests = json.load(json_file)

    requests.append(data)

    with open("requests_history/successful_requests.json", "w", encoding="utf-8") as json_file:
        json.dump(requests, json_file, indent=2)

