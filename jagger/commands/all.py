"""The hello command."""


from json import dumps

from .base import Base


class All(Base):
    """Say hello, world!"""

    def run(self):
        print('Hell, world!')
        print('You supplied the following options:', dumps(self.options, indent=2, sort_keys=True))