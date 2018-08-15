parser_file = 'fr.json'
query = #formulaire d'entrée page HTML

 with open(parser_file) as parser_words:
     stopwords = json.load(parser_words)

for stopword in stopwords:
            for word in query:
                if # word == stopword:
                    # ne pas prendre en compte les word
