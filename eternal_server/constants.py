import enum
import logging


BUF_SIZE=131072
ZEROES=bytearray(BUF_SIZE)
NEWLINES=bytearray(0xA for _ in range(BUF_SIZE))


@enum.unique
class OperationMode(enum.Enum):
    clock = 1
    newline = 2
    urandom = 3
    null = 4

    def __str__(self):
        return self.name

    def __contains__(self, e):
        return e in self.__members__


class LogLevel(enum.IntEnum):
    debug = logging.DEBUG
    info = logging.INFO
    warn = logging.WARN
    error = logging.ERROR
    fatal = logging.FATAL
    crit = logging.CRITICAL

    def __str__(self):
        return self.name

    def __contains__(self, e):
        return e in self.__members__
