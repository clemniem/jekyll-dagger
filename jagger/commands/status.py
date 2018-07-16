"""The hello command."""


from json import dumps

from .base import Base
from .utils import safeLoadConfig


class Status(Base):
    """Say hello, world!"""

    def run(self):
        print('Hell, world!')
        print('You supplied the following options:', dumps(self.options, indent=2, sort_keys=True))

        print(safeLoadConfig())
