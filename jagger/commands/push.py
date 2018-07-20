"""The hello command."""


from json import dumps

from .base import Base
from .utils import safeLoadConfig

class Push(Base):
    """Say hello, world!"""

    def run(self):
        print('Hell, world!')
        print('You supplied the following options:', dumps(self.options, indent=2, sort_keys=True))

    config = safeLoadConfig()

