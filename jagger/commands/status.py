"""The hello command."""


from json import dumps

from .base import Base
from .utils import safeLoadConfig, printDict

class Status(Base):
    """Say hello, world!"""

    def run(self):
        print('Hell, world!')
        print('You supplied the following options:', printDict(self.options))

        printDict(safeLoadConfig())
