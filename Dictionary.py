from DictionaryEntry import *

Dictionary = open("Dictionary.txt", 'r+', encoding="utf8")

Noun = dict()   # For nouns
Verb = dict()   # For verbs
Adj  = dict()   # For adjectives
Col  = dict()   # For collocations

for line in Dictionary:
    entry = DictionaryEntry(line)
    print(entry)

