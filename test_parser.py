from parser import Parser

def test_string_convert():
    parser = Parser("bonjour  beaucoup  bonjour")
    assert parser.string_convert() == "bonjour bonjour"

def test_remove_symbols():
    parser = Parser("bonjour  beaucoup#  bonjour?")
    assert parser.remove_symbols() == "bonjour beaucoup bonjour "

def test_convert_ascii():
    parser = Parser("bonjour  beaucoup#  bonjour? émile")
    assert parser.convert_ascii() == "bonjour bonjour emile"

def test_list_convert():
    result = ["openclassrooms", "Paris"]
    parser = Parser("openclassrooms Paris")
    assert parser.list_convert() == result
