from parser import Parser

def test_string_convert():
    parser = Parser("bonjour  beaucoup  bonjour")
    assert parser.string_convert() == "bonjour bonjour"

def test_remove_symbols():
    parser = Parser("bonjour  beaucoup#  bonjour?")
    assert parser.remove_symbols() == "bonjour beaucoup bonjour "
