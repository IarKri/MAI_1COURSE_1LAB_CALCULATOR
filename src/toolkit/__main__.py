import argparse
import re
import sys

from src.toolkit.calculator import calculator
from src.toolkit.validator import initial_calculator_validation, initial_converter_validation
from src.toolkit.converter import converter
from src.toolkit.json_dump import  calculator_dump

def main():
    parser=argparse.ArgumentParser(
        prog="toolkit",
        description="Calculator-converter"
    )

    commands = parser.add_subparsers(dest="command")

    parse_calc = commands.add_parser(
        "calc",
        description="Calculator",
    )

    parse_calc.add_argument("expression")

    parse_convert = commands.add_parser(
        "convert",
        description= "Converter",
    )
    parse_convert.add_argument("value")
    parse_convert.add_argument("--from", required="True")
    parse_convert.add_argument("--to", dest="to_unit", required="True")


    args = parser.parse_args()

    if args.command == "calc":

        expr = args.expression


        compressed_expression = compress(expr)
        initial_validation_calc(compressed_expression)
        tokenized_expression = tokenize(compressed_expression)
        validation_calc(tokenized_expression)
        rpn_expression = shunting_yard(tokenized_expression)
        calculated_expression = calculate(rpn_expression)

        print(calculated_expression)
        calc_dump(expr, calculated_expression)
        sys.exit(0)
    elif args.command == "convert":
        
        try:
            value = float(args.value)
        except ValueError:
            raise InvalidValueError(args.value)
        from_unit = args.from_unit
        to_unit =  args.to_unit

        # Основной блок
        validation_convert(value, from_unit, to_unit)  # Валидация
        converted_value = convert(value, from_unit, to_unit)  # Перевод величин

        print(converted_value)  # Итоговый вывод
        convert_dump(value, converted_value, from_unit, to_unit)  # Выгрузка успешного запуска
        sys.exit(0)  # Успешное завершение программы

if __name__ == "__main__":
    try:
        main()
    except CalculatorError as error:
        print(f"Expected Error: {error}", file=sys.stderr)
        sys.exit(2)
    except ConverterError as error:
        print(f"Expected Error: {error}", file=sys.stderr)
        sys.exit(2)
    except Exception as error:
        print(f"UnexpectedError: {error}", file=sys.stderr)
        sys.exit(2)