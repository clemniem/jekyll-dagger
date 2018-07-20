"""The hello command."""

from json import dumps
from .base import Base
from .utils import *



class Fly(Base):
    """Jagging the scribble"""

    def run(self):
        print('This command takes an md file and jaggers it!')
        print('You supplied the following options:', dumps(self.options, indent=2, sort_keys=True))

        resource = self.options['<md-resource>']
        files_to_jagger = list()
        if os.path.isdir(resource):
            files_to_jagger = [f for f in os.listdir(resource) if assertMdFile(f)]
        elif assertMdFile(resource):
            files_to_jagger.append(resource)
        if not files_to_jagger:
            print("The path provided is not pointing to a valid md-File: {}".format(resource))
            exit(-1)
        print(files_to_jagger)

        for file_path in files_to_jagger:
            jaggerFile(file_path)


