from app.roman_numerals import parse
from pytest import mark


def test_roman_numeral_parser():
    result = parse('IX')
    assert result == 9


def test_roman_numeral_parser():
    result = parse('MCMLXXII')
    assert result == 1972

def test_roman_numeral_parser():
    result = parse("CCCXXXIII")
    assert result == 333

@mark.parametrize("s,expected", [("XXXIV", 34), ("XLI", 41), ("XIX", 19)])
def test_roman_numeral_parametrize(s, expected):
    result = parse(s)

    assert result == expected
