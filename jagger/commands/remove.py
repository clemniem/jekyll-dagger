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

        config = safeLoadConfig()
        changed_config = False

        if os.path.isdir(target):
            if JAGGER_DIRS in config and target in config[JAGGER_DIRS]:
                print("Removed {}".format(target))
                del config[JAGGER_DIRS][target]
                changed_config = True
        elif os.path.isfile(target):
            if JAGGER_FILES in config and target in config[JAGGER_FILES]:
                print("Removed {}".format(target))
                del config[JAGGER_FILES][target]
                changed_config = True

        if changed_config:
            saveConfig(config)
            print("config has been updated")
            printDict(safeLoadConfig())
        else:
            print("Nothing to remove.")