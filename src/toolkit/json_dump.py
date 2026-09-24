import json
from datetime import datetime

def calculator_dump(expression, calculated_expression):

    data = {
        "type": "calculation",
        "expression": expression,
        "result": calculated_expression
        }

    with open("requests_history/successful_requests.json", "r", encoding="utf-8") as json_file:
        requests = json.load(json_file)

    requests.append(data)

    with open("requests_history/successful_requests.json", "w", encoding="utf-8") as json_file:
        json.dump(requests, json_file, indent=4)
