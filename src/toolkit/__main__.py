import argparse
import re
import sys

from .tokenizer import tokenize
from .calculator import calculation
from .validator import initial_calculation_validation, initial_convertation_validation, space_cleaner, operators_formatter
from .converter import convertation
from .json_dump import  calculator_dump, converter_dump




##################
def parser(argv=None):
    '''
        Формирует парсер аргументов

    Args:
        Argv: Аргументы, подающиеся на вход

    Returns:
        argparse.Namespace: объект с указанными полями 
    '''
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
    """
    Запускает функцию вычисления математического выражения 

    Математическое выражение, не содержащее ошибок, записывается в историю запросов

    Args:
        expression: математическое выражение
    
    Returns:
        result: результат математического выражения
    
    Raises:
        ValueError: Ошибка, встреченная при валидации
    
        ZeroDivisionError: Ошибка, встреченная при валидации

        Exception: Ошибка, встреченная при валидации
    """
    try:
        expression=space_cleaner(expression)
        expression=operators_formatter(expression)
        initial_calculation_validation(expression)
        result=calculation(expression)
        calculator_dump(expression, result)
        print(result)
    except ValueError as error:
        print(f"{error}", file = sys.stderr)
        sys.exit(2)
    except ZeroDivisionError as error:
        print(f"{error}", file = sys.stderr)
        sys.exit(2)
    except Exception as error:
        print(f"Error {error}", file = sys.stderr)
        sys.exit(2)

def converter(value, from_unit, to_unit):
    """
    Запускает функцию конвертации величины

    Выражение, поддерживаемое конвертером, записывается в историю запросов

    Args:
        value: величина

        from_unit: единицы измерения величины

        to_unit: единицы измерения, в которые надо перевести величину
    
    Returns:
        result: результат конвертации выражения
    
    Raises:
        ValueError: Ошибка, встреченная при валидации

        Exception: Ошибка, встреченная при валидации
    """
    try:
        initial_convertation_validation(value, from_unit,to_unit)
        result=convertation(value, from_unit, to_unit)
        print(result)
        converter_dump(value, from_unit, to_unit, result)
    except ValueError as error:
        print(f"ValueError {error}", file=sys.stderr)
        sys.exit(2)
    except Exception as error:
        print(f"Error {error}", file = sys.stderr)

def main(argv=None):
    """
    Запускает работу всей программы

    Args:
        argv: Аргументы, подающиеся на вход
    """
    args=parser(argv)
    if args.subcommand=="calc":
        calculator(args.expression)
    elif args.subcommand=="convert":
        converter(args.value, args.from_unit, args.to_unit)

if __name__=="__main__":
    main()
