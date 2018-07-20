"""The hello command."""


from json import dumps
from .base import Base
from .utils import *

class Hello(Base):
    """Say hello, world!"""

    def run(self):
        print('This adds a file or directory to jagger config')
        print('You supplied the following options:', dumps(self.options, indent=2, sort_keys=True))
        target = self.options['<path>']
        target = os.path.abspath(target)

        if not os.path.exists(target):
            print("The <path> provided does not exist")
            exit(-1)

        config = safeLoadConfig()

        if os.path.isdir(target):
            if not JAGGER_DIRS in config: config[JAGGER_DIRS] = dict()
            config[JAGGER_DIRS][target] = None
        elif os.path.isfile(target):
            # TODO check if File is a md File
            if not JAGGER_FILES in config: config[JAGGER_FILES] = dict()
            config[JAGGER_FILES][target] = None

        saveConfig(config)

        print("config has been updated")
        print(safeLoadConfig())