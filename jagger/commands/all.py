"""The hello command."""


from json import dumps

from .base import Base
from .utils import *

class All(Base):
    """Say hello, world!"""

    def run(self):
        print('Hell, world!')
        print('You supplied the following options:', dumps(self.options, indent=2, sort_keys=True))
        config = safeLoadConfig()

        print(config[JAGGER_FILES].keys())

        files_to_jagger = list()

        # check if there are files saved in config
        if JAGGER_FILES in config:
            files_to_jagger += config[JAGGER_FILES].keys()

        # check if the files in config have been changed
        if JAGGER_DIRS in config:
            for jagger_dir in config[JAGGER_DIRS]:
                files_to_jagger += [f for f in os.listdir(jagger_dir) if assertMdFile(f)]

        if not files_to_jagger:
            print("No files added to config yet: {}".format(config))
            exit(-1)

        # jagger all changed files
        for file_path in files_to_jagger:
            jaggerFile(file_path)