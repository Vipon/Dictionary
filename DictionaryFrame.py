from tkinter import *
from Dictionary import *
from DictionaryEntry import *

class DictionaryFrame:
    __frame = None

    def __init__(self):
        frame = Tk()
        frame.title("Dictionary")
        frame.geometry('900x600')
        frame.protocol('WM_DELETE_WINDOW', self.__close)

        self.__frame = frame

    def start(self):
        self.__frame.mainloop()

    def __close(self):
        self.__frame.destroy()
        self.__frame.quit()