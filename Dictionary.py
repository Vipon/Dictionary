import re

Dictionary = open("Dictionary.txt", 'r+', encoding="utf8")

Noun = dict()   # For nouns
Verb = dict()   # For verbs
Adj  = dict()   # For adjectives
Col  = dict()   # For collocations
pattern = re.compile("(.*):(.*):(.*);")
for line in Dictionary:
    (enWord, wordType, ruWords) = pattern.search(line).groups()

    enWord = enWord.strip()
    wordType = wordType.strip()
    ruWords = ruWords.strip()
    if wordType == "noun":
        Noun[enWord] = ruWords
    elif wordType == "verb":
        Verb[enWord] = ruWords
    elif wordType == "adj":
        Adj[enWord] = ruWords
    elif wordType == "col":
        Col[enWord] = ruWords

print(Noun)
print(Verb)
print(Adj)
print(Col)