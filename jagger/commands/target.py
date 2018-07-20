"""The target command."""

from json import dumps

from .base import Base
import os
from .utils import *
import os

class Target(Base):
    """Write target to .config file"""

    def run(self):
        target = self.options['<target-dir>']

        config = safeLoadConfig()

        if not os.path.isdir(target):
            print("The provided path is not a directory.")
        else:
            config[TARGET] = target
            config[IS_TARGET_GIT] = isGitRepo(target)
            saveConfig(config)

            print("Config has been updated")
            printDict(safeLoadConfig())