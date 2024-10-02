from singleton import Singleton
from datetime import datetime as dt
from queue import Queue
import threading

class Logger(metaclass=Singleton):
    __thread__ = None
    _queue = Queue()

    def __new__(self):
        if self.__thread__ is None:
            self.__thread__ = threading.Thread(target=self.process_log, args=(self,))
            self.__thread__.start()
        return super(Logger,self).__new__(self)

    def log(self, logmessage: str):
        now = dt.today()
        message = f"[{now}], {logmessage}"
        self._queue.put(message)

    def process_log(self):
        while True:
                entry = self._queue.get()
                print(entry)

tester1 = Logger()
tester2 = Logger()

for idx in range(1000):
    tester1.log(f"-{idx} pushed into queue by tester1")
    tester2.log(f"{idx} pushed into queue by tester2")

tester1.end()