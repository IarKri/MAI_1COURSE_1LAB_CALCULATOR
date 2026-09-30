# Calculator-Converter

CLI-калькулятор-конвертер с валидацией выражений

## Описание

Проект состоит из двух инструментов:

- **Калькулятор** - вычисление математических выражений
    В работе калькулятора могут использоваться рациональные числа; 
    операторы:
    - `+`, `-`, `*`, `/`
    - `//`, `%` (поддерживают только `int`)
    - унарный минус и унарный плюс
    Поддерживается работа с выражениями, содержащими в своей записи пробелы

- **Конвертер** — переводит значения из одной системы единиц измерения в другую
    Конвертер поддерживает работу с единицами систем измерения:
    - веса(`g`, `kg`)
    - расстояния(`mm`, `cm`, `m`, `km`)
    - температуры(`c`, `f`, `k`)

## Основные команды

```bash
python -m toolkit calc "expression"
python -m toolkit convert value --from_Unit --to_Unit
python -m calc -help
python -m convert -help
python -m -help

```
**НО**
Для корректной работы калькулятора, ставьте перед выражением -- если оно начинается более чем с одного минуса
_Пример:_
```bash
python -m toolkit calc -- "--7+5"
```
## Ошибки калькулятора

- `Empty sequence` - Выражением является пустая строка
- `Expression cant start with * / % //` - Выражение начинается с `*, /, %, //`
- `No operator between numbers` - В выражении пропущена операция между операндами
- `Incorrect operation` - В выражение введено невозможное сочетание операций
- `Division by zero` - В выражении присутсвует деление на ноль
- `Expression cant end with + - * / % //` - Выражение заканчивается на `+, -, *, /, %, //`
- `Float type is incorrect` - Float число введено некорректно
- `Incorrect character` - В выражении есть символ, неподдерживающийся калькулятором
- `Incorrect value for operation with //` - Для операции `//` используется не `int` число
- `Incorrect value for operation with %` - Для операции `%` используется не `int` число

## Ошибки конвертера

- `Empty sequence` - Значением является пустая строка
- `Incorrect value` - Значение введено некорректно
- `Unknown Unit` - Введена неизвестная единица измерения
- `Different type of Units` - Запрошена конвертация разных типов единиц измерения
- `Below absolute zero` - Температура ниже абсолютного нуля

## Структура проекта

lab_01\
    requests_history\
        successful_requests.json
    src\
        toolkit\
            __init__.py
            __main__.py
            calculator.py
            classes.py
            converter.py
            json_dump.py
            tokenizer.py
            validator.py
    tests\
         __init__.py
        test_calculator.py
        test_CLI.py
        test_converter.py
    .gitignore
    pyproject.toml
    README.md

## Установка и создание виртуального окружения

```bash
git clone https://github.com/IarKri/MAI_1COURSE_1LAB_CALCULATOR
cd lab_01
python -m venv venv
venv/Scripts/activate
pip install -e.
