from tkinter import *
from Dictionary import *
from DictionaryEntry import *

class DictionaryFrame:
    __frame = None
    __text  = None
    __word  = None
    __type  = None
    __def   = None
    __tran  = None

    Dict    = None
    def __init__(self, file):
        self.Dict = Dictionary(file)

        appFrame = Tk()
        appFrame.title("Dictionary")
        appFrame.geometry('1600x900')
        appFrame.protocol('WM_DELETE_WINDOW', self.__close)

        topFrame = Frame(appFrame, bd = 1, relief = GROOVE)
        rowWord = Frame(topFrame)
        DictionaryFrame.makeLabel(rowWord, 'Word:').pack(side = LEFT)
        self.__word = DictionaryFrame.makeEntry(rowWord)
        self.__word.pack(side = RIGHT,  expand = YES, fill = X)
        rowWord.pack(side = TOP, fill = X)

        rowType = Frame(topFrame)
        DictionaryFrame.makeLabel(rowType, 'Type:').pack(side = LEFT)
        self.__type = DictionaryFrame.makeEntry(rowType)
        self.__type.pack(side = RIGHT,  expand = YES, fill = X)
        rowType.pack(side = TOP, fill = X)

        rowTran = Frame(topFrame)
        DictionaryFrame.makeLabel(rowTran, 'Translation:').pack(side = LEFT)
        self.__tran = DictionaryFrame.makeEntry(rowTran)
        self.__tran.pack(side = RIGHT,  expand = YES, fill = X)
        rowTran.pack(side = TOP, fill = X)

        rowDef = Frame(topFrame)
        DictionaryFrame.makeLabel(rowDef, 'Definition:').pack(side = LEFT)
        self.__def  = DictionaryFrame.makeEntry(rowDef)
        self.__def.pack(side = RIGHT,  expand = YES, fill = X)
        rowDef.pack(side = TOP, fill = X)

        rowAdd = Frame(topFrame)
        Button(rowAdd, text = 'Add Word',   \
                        font = 'Menlo 24',  \
                        command = (lambda: self.addWord())).pack(side = RIGHT)
        rowAdd.pack(side = TOP, fill = X)
        topFrame.pack(side = TOP, fill = X)

        botFrame = Frame(appFrame, bd = 1, relief = GROOVE)
        searchRow = Frame(botFrame)
        DictionaryFrame.makeLabel(searchRow, 'Search:').pack(side = LEFT)
        searchEntry = DictionaryFrame.makeEntry(searchRow)
        searchEntry.focus()
        searchEntry.bind('<Return>', (lambda event: self.doSearch(searchEntry)))
        searchEntry.pack(side = RIGHT,  expand = YES, fill = X)
        searchRow.config(bd = 1, relief = GROOVE)
        searchRow.pack(side = TOP, fill = X)

        self.__text = Text(botFrame, bd = 1, relief = GROOVE, font=('Menlo', 24))
        sBar = Scrollbar(self.__text)
        sBar.config(command = self.__text.yview)
        self.__text.config(yscrollcommand = sBar.set)
        self.__text.pack(side = LEFT, expand = YES, fill = BOTH)
        sBar.pack(side = RIGHT, fill = Y)
        botFrame.pack(side = TOP, expand = YES, fill = BOTH)

        self.__frame = appFrame

    def showText(self, text):
        self.__text.delete('1.0', END)
        self.__text.insert('1.0', text)

    def doSearch(self, ent):
        word = ent.get()
        if word != '':
            # Get all entries in a dictionary for a target word
            entries = self.Dict.findEntries(word)
            if not entries:
                # If there is no entries, write about ir and return
                self.showText("There is no entry: " + word)
                return

            # If there is at least one entry, write.
            entries_str = entries[0].getWord() + ':\n'
            for entry in entries:
                entries_str += '\t[' + entry.getType() + '] - ' \
                            + entry.getTran() + '.\n'           \
                            + '\tDefinition: ' + entry.getDef() + '\n\n'

            self.showText(entries_str)

    def makeLabel(rootFrame, txt):
        return Label(rootFrame, text = txt, height = 1, \
                                width = 12, font = 'Menlo 24')

    def makeEntry(rootFrame, fnt = 'Menlo 24'):
        return Entry(rootFrame, font = fnt)

    def makeInputRow(rootFrame, text):
        row = Frame(rootFrame)
        Label(row, text = text, height = 1, width = 12, font = 'Menlo 24').pack(side = LEFT)
        Entry(row).pack(side = RIGHT, expand = YES, fill = X)
        return row

    def addWord(self):
        Word = self.__word.get()
        Type = self.__type.get()
        Def = self.__def.get()
        Tran = self.__tran.get()

        self.Dict.createNewEntry(Word, Type, Def, Tran)

    def start(self):
        self.__frame.mainloop()

    def __close(self):
        self.Dict.close()
        self.__frame.destroy()
        self.__frame.quit()
