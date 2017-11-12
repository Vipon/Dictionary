from threading import Timer

class xTimer():
    DEF_PERIOD = 1.0
    ONE_SHOT = int(0)
    PERIODICAL = int(1)

    __time = DEF_PERIOD
    __func = None
    __mod = ONE_SHOT
    __timer = None
    def __init__(self, time = DEF_PERIOD, func = None, mod = ONE_SHOT):
        self.__time = time
        self.__func = func
        self.__mod = mod
        if func is None:
            raise Exception("Func is None")

        if mod == xTimer.ONE_SHOT:
            self.__timer = Timer(time, func)
        elif mod == xTimer.PERIODICAL:
            self.__timer = Timer(time, lambda: self.__repeat())


    def __repeat(self):
        if self.__func is None:
            raise Exception("Func is None")

        if self.__timer is None:
            raise Exception("Timer is uninitialized")

        self.__func()
        self.__timer = Timer(self.__time, lambda: self.__repeat())
        self.__timer.start()


    def start(self):
        if self.__timer is None:
            raise Exception("Timer is uninitialized")

        self.__timer.start()


    def cancel(self):
        self.__timer.cancel()
