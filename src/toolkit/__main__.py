import argparse
import re
import sys

from src.toolkit.tokenizer import tokenize
from src.toolkit.calculator import calculation
from src.toolkit.validator import initial_calculation_validation, initial_convertation_validation, space_cleaner, operators_formatter
from src.toolkit.converter import convertation
from src.toolkit.json_dump import  calculator_dump, converter_dump




##################
def parser(argv=None):
    format = argparse.RawTextHelpFormatter
    parser=argparse.ArgumentParser(
        prog="toolkit",
        description="Calculator-Converter",
        epilog=(""
        ""
        ),
        formatter_class=format
    )

    subparser=parser.add_subparsers(
        dest="subcommand",
        required=True,
        title='',
        metavar=''
    )

    calculator=subparser.add_parser(
        "calc",
        description="",
        epilog=(""
        ""
        ),
        help="",
        formatter_class=format
    )

    converter=subparser.add_parser(
        "convert",
        description='',
        epilog=(""
        ""
        ),
        help="",
        formatter_class=format
    )

    calculator.add_argument(
        "expression",
        help=""
    )

    converter.add_argument(
        "value",
        help=""
    )

    converter.add_argument(
        "--from",
        dest="from_unit",
        required=True,
        help=""
    )

    converter.add_argument(
        "--to",
        dest="to_unit",
        required=True,
        help=""
    )

    return parser.parse_args(argv)

def calculator(expression):
    try:
        expression=space_cleaner(expression)
        expression=operators_formatter(expression)
        initial_calculation_validation(expression)
        result=calculation(expression)
        calculator_dump(expression, result)
        print(result)
    except ValueError as error:
        print(f"{error}", file=sys.stderr)
        sys.exit(2)
    except ZeroDivisionError as error:
        print(f"{error}", file=sys.stderr)
        sys.exit(2)
    except Exception as error:
        print(f"Unknown Error {error}", file=sys.stderr)
        sys.exit(2)

def converter(value, from_unit, to_unit):
    try:
        initial_convertation_validation(value, from_unit,to_unit)
        result=convertation(value, from_unit, to_unit)
        print(result)
        converter_dump(value, from_unit, to_unit, result)
    except ValueError as error:
        print("", file=sys.stderr)
        sys.exit(2)

def main(argv=None):
    args=parser(argv)
    if args.subcommand=="calc":
        calculator(args.expression)
    elif args.subcommand=="convert":
        converter(float(args.value), args.from_unit, args.to_unit)

if __name__=="__main__":
    main()
