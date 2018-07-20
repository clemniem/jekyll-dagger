"""The init command."""

from .base import Base
from .utils import *
import os

class Init(Base):
    """Initialise the jagger"""

    def run(self):
        print('This is the initialisation of jagger.')
        print('You supplied the following options:', dumps(self.options, indent=2, sort_keys=True))

        target_dir = self.options["<target-dir>"]

        # check if config already exists:
        if os.path.exists(getConfigFilePath()) and not self.options["--force"]:
            print("Config already exists:")
            print("  If you want to overwrite target run: jagger target <new-target-path>")
            print("  If you want to overwrite current config run: jagger init <target-path> -f")

        if not os.path.isdir(target_dir):
            print("The provided path is not a directory.")
        else:
            config = {
                TARGET: target_dir,
                IS_TARGET_GIT: isGitRepo(target_dir)
            }

            saveConfig(config)

            print("Your config-file has been saved:")
            printDict(safeLoadConfig())
