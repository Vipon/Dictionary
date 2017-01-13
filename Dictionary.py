from DictionaryEntry import *

class Dictionary:
    # __dict contains dictionaries by types of words
    __dict = dict()

    def __init__(self, file = ''):
        Dict = open(file, 'r+', encoding='utf8')
        for line in Dict:
            entry = DictionaryEntry(line)
            Type = entry.getType()
            Word = entry.getWord()
            if Type not in self.__dict:
                self.__dict[Type] = dict()

            self.__dict[Type][Word] = entry

    def print(self):
        for Type in self.__dict:
            print(Type, ':')
            for entry in self.__dict[Type]:
                print(self.__dict[Type][entry])

            print('')

Dict = Dictionary('Dictionary.txt')
Dict.print()