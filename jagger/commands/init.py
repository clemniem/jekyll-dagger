"""The init command."""


from json import dumps

from .base import Base
from .utils import *




class Init(Base):
    """Initialise the jagger"""

    def run(self):
        print('This is the initialisation of jagger.')
        print('You supplied the following options:', dumps(self.options, indent=2, sort_keys=True))

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
        with open(getConfigFilePath(),'r') as config_stream:
            loaded_config = yaml.safe_load(config_stream)
            print(loaded_config)
