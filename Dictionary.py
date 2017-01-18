from DictionaryEntry import *
import os

class Dictionary:
    # __dict contains dictionaries by types of words
    __dict = dict()
    __file = None

    def __init__(self, file = ''):
        self.__file = open(file, 'r+', encoding='utf8')
        for line in self.__file:
            entry = DictionaryEntry(line)
            Type = entry.getType()
            Word = entry.getWord()
            if Type not in self.__dict:
                self.__dict[Type] = []

            self.__dict[Type].append(entry)

        self.sort()

    def __str__(self):
        str = ''
        for Type in self.__dict:
            str += Type + ':\n'
            for entry in self.__dict[Type]:
                str += entry.__str__() + '\n'

            str += '\n'

        return str

    def sort(self, t = None):
        for Type in self.__dict:
            if (Type == t) or (t == None):
                self.__dict[Type].sort()

    def save(self):
        str = ''
        for Type in self.__dict:
            for entry in self.__dict[Type]:
                str += entry.getWord() + ': ' \
                    +  entry.getType() + ': ' \
                    +  entry.getDef()  + ': ' \
                    +  entry.getTran() + ';\n'

        '''
        For safety, create tmp file, save in tmp file and rename tmp
        into oldFileName. This way prevents data loss in bad situations.
        '''
        oldFileName = self.__file.name
        self.__file.close()
        newFile = open('tmp_' + oldFileName, 'w+', encoding='utf8')
        newFile.write(str)
        os.remove(oldFileName)
        os.rename(newFile.name, oldFileName)
        self.__file = newFile

    def close(self):
        self.save()
        self.__file.close()

    def createNewEntry(self, Word = '', Type = '', Def = '', Tran = ''):
        if Type not in self.__dict:
            self.__dict[Type] = []

        str = Word + ': ' + Type+ ': ' + Def+ ': ' + Tran + ';'
        self.__dict[Type].append(DictionaryEntry(str))
        self.sort(Type)

    def findEntry(self, Word = ''):
        for Type in self.__dict:
            for entry in self.__dict[Type]:
                if entry.getWord() == Word:
                    return entry

    def changeEntry(self, Entry = DictionaryEntry(), newWord = None, \
                        newType = None, newDef = None, newTran = None):
        if newWord != None:
            Entry.setWord(newWord)
        if newType != None:
            Entry.setTran(newType)
        if newDef != None:
            Entry.setDef(newDef)
        if newTran != None:
            Entry.setTran(newTran)

Dict = Dictionary('Dictionary.txt')
print(Dict)
Dict.createNewEntry('t')
entry = Dict.findEntry('t')
print(entry)
Dict.changeEntry(entry, 'yyy')

Dict.close()