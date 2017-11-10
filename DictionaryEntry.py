import re

class DictionaryEntry:
    __patternStrFromDict = re.compile("(.*):(.*):(.*):(.*);")

    def __init__(self, strFromDict = ''):
        if strFromDict == '':
            return

        (self.__word, self.__type, self.__def, self.__tran) = \
                      DictionaryEntry.__patternStrFromDict.search(strFromDict).groups()

        self.__word = self.__word.strip().lower()
        self.__type = self.__type.strip().lower()
        self.__def  = self.__def.strip().lower()
        self.__tran = self.__tran.strip().lower()


    def __str__(self):
        return '%s [%s] - %s.\n\tDefinition: %s\n' % (  self.__word, \
                                                        self.__type, \
                                                        self.__tran, \
                                                        self.__def)


    def __lt__(self, other):
        if self.getWord() < other.getWord():
            return True

        return False


    def getWord(self):
        return self.__word


    def getType(self):
        return self.__type


    def getDef(self):
        return self.__def


    def getTran(self):
        return self.__tran


    def setWord(self, Word = ''):
        self.__word = Word


    def setType(self, Type = ''):
        self.__type = Type


    def setDef(self, Def  = ''):
        self.__def = Def


    def setTran(self, Tran  = ''):
        self.__tran = Tran
