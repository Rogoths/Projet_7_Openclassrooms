from parser import Parser

def test_string_convert():
    parser = Parser("bonjour  beaucoup  bonjour")
    result = parser.list_convert()
    assert parser.string_convert(result) == "bonjour bonjour"
