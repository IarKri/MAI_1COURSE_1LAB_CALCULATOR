import sys

import pytest
from toolkit.__main__ import main

def test_calc_simpliest_tests(capsys):

    main(["calc", "1+3"])
    captured = capsys.readouterr()
    assert captured.out.strip() == '4.0'


def test_calc_order_of_operations(capsys):
    main(["calc", "2+3*4"])
    captured = capsys.readouterr()
    assert captured.out.strip() == "14.0"


def test_calc_spaces(capsys):
    main(["calc", "2  +3- 4"])
    captured = capsys.readouterr()
    assert captured.out.strip() == "1.0"


def test_calc_float(capsys):
    main(["calc", "1.4 + 3.5"])
    captured = capsys.readouterr()
    assert captured.out.strip() == "4.9"


def test_calc_int_division(capsys):
    main(["calc", "5 // 2"])
    captured = capsys.readouterr()
    assert captured.out.strip() == "2.0"


def test_calc_remainder(capsys):
    main(["calc", "5 % 2"])
    captured = capsys.readouterr()
    assert captured.out.strip() == "1.0"


def test_calc_unary_minus(capsys):
    main(["calc", "-5 + 3"])
    captured = capsys.readouterr()
    assert captured.out.strip() == "-2.0"


def test_convert_length(capsys):
    main(["convert", "150", "--from", "cm", "--to", "m"])
    captured = capsys.readouterr()
    assert captured.out.strip() == "1.5"

def test_convert_weight(capsys):
    main(["convert", "1000", "--from", "g", "--to", "kg"])
    captured = capsys.readouterr()
    assert captured.out.strip() == "1.0"


def test_convert_temperature(capsys):
    main(["convert", "25", "--from", "c", "--to", "k"])
    captured = capsys.readouterr()
    assert captured.out.strip() == "298.15"






