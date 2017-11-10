from DictionaryEntry import *
import os

class Dictionary:
    # __dict contains dictionaries by types of words
    __dict = dict()
    __file = None

    TMPSTR = 'tmp_'
    def __init__(self, file = ''):
        # Check previous session.
        tmp = self.TMPSTR + file
        if os.path.exists(tmp):
            # We could not perform all actions to save the dictionary.
            if os.path.exists(file):
                # We saved part of dictionary, but not all.
                self.__tryRecover(file, tmp)
            else:
                # Optimization. We couldn't to perform only rename.
                os.rename(tmp, file)

        # Create new dictionary, after check.
        if os.path.exists(file):
            self.__file = open(file, 'r+', encoding='utf8')
        else:
            self.__file = open(file, 'w+', encoding='utf8')

        for line in self.__file:
            entry = DictionaryEntry(line)
            Type = entry.getType()
            Word = entry.getWord()
            if Type not in self.__dict:
                self.__dict[Type] = []

            self.__dict[Type].append(entry)

        # Sort new dictionary.
        self.sort()


    def __tryRecover(self, file, tmp):
        '''
        !TODO: Need make function more clever. Currently, there is a very
        stupid recover. We will save only the biggest dictionary.
        '''
        if os.path.getsize(tmp) > os.path.getsize(file):
            os.remove(file)
            os.rename(tmp, file)
        else:
            os.remove(tmp)


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
        newFile = open(self.TMPSTR + oldFileName, 'w+', encoding='utf8')
        newFile.write(str)
        newFile.close()
        os.remove(oldFileName)
        os.rename(newFile.name, oldFileName)
        self.__file = open(oldFileName, 'r+', encoding='utf8')


    def close(self):
        self.save()
        self.__file.close()


    def createNewEntry(self, Word = '', Type = '', Def = '', Tran = ''):
        if Type not in self.__dict:
            self.__dict[Type] = []

        str = Word + ': ' + Type+ ': ' + Def+ ': ' + Tran + ';'
        self.__dict[Type].append(DictionaryEntry(str.lower()))
        self.sort(Type)


    def findEntries(self, Word = ''):
        Word = Word.strip().lower()
        entries = []
        for Type in self.__dict:
            for entry in self.__dict[Type]:
                if entry.getWord() == Word:
                    entries.append(entry)

        return entries


    def changeEntry(self, Entry = DictionaryEntry(), newWord = None, \
                        newType = None, newDef = None, newTran = None):
        if newWord != None:
            Entry.setWord(newWord)
        if newType != None:
            Entry.setTran(newType)
        if newDef  != None:
            Entry.setDef(newDef)
        if newTran != None:
            Entry.setTran(newTran)
