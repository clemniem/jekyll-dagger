"""The init command."""


from json import dumps
import os
import yaml

from .base import Base
from .utils import *

TARGET = "target"


class Init(Base):
    """Initialise the jagger"""

    def run(self):
        print('This is the initialisation of jagger.')
        print('You supplied the following options:', dumps(self.options, indent=2, sort_keys=True))


        try:
            HOME = os.environ['HOME']
        except OSError:
            print("Your $HOME environment variable isn't set. Please set it to your Home directory")
            return

        CONFIG_PATH = '{}/.config/jagger'.format(HOME)

        if not os.path.exists(CONFIG_PATH):
            print("Creating directory for the configuration: {}".format(CONFIG_PATH))
            os.makedirs(CONFIG_PATH, exist_ok=True)

        CONFIG_FILE_PATH = CONFIG_PATH + "/" + "config.yml"

        # Where is the target directory ?
        config = {
            TARGET: None
        }

        # TODO get an autocomplete eg completer
        while config[TARGET] is None:
            config[TARGET] = input("Where is the _posts folder of your jekyll project (absolute path): ")
            if not os.path.isdir(config[TARGET]):
                config[TARGET] = None
                print("The provided path is not a directory.")

        # TODO make sense with config and utils
        saveConfig(config)

        print("Your config-file has been saved:")
        with open(CONFIG_FILE_PATH,'r') as config_stream:
            loaded_config = yaml.safe_load(config_stream)
            print(loaded_config)


        # Do you want to add a source directory ?



