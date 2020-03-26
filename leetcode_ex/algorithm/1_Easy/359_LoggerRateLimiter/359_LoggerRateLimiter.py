class Logger:
    def __init__(self):
        self.d = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.d:
            self.d[message] = timestamp
            return True
        else:
            if timestamp - self.d[message] < 10:
                return False
            else:
                self.d[message] = timestamp
                return True

