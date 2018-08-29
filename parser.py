#!/usr/local/bin/python
# coding: utf8

import json
import re
import unicodedata


PARSER_FILE = 'fr.json'

class Parser:

    def __init__(self, raw_input):

        self.stopwords = json.load(open(PARSER_FILE, 'r'))
        self.raw_input = raw_input

    def list_convert(self):
        """convert the string in list and delete the words we don't want in the answer"""
        string = self.remove_symbols()
        list = string.split()

        for word in list:
            if word in self.stopwords:#ignore words in stopwords list
                list.remove(word)
        return list

    def string_convert(self):
        """convert list in string"""
        list = self.list_convert()
        return " ".join(list)

    def remove_symbols(self):
        """remove anything that is not a letter or number"""
        removed_string = re.sub(r'[\W_]+', ' ', self.raw_input)
        return removed_string

    def convert_ascii(self):
        """remove accents in words"""
        string = unicodedata.normalize('NFKD', self.string_convert()).encode('ascii', 'ignore').decode()
        return string

if __name__ == "__main__":
    parser = Parser("bonjour  beaucoup #  bonjour émile ?")
    print(parser.list_convert())
    print(parser.string_convert())
    print(parser.remove_symbols())
    print(parser.convert_ascii())
