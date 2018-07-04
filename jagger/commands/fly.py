"""The hello command."""

import datetime
from json import dumps
from .base import Base
import os

class Fly(Base):
    """Jagging the scribble"""

    def fly(self,inputPath):
        # TODO Move to config file.
        # constants
        START_ICON = "<!-- @@"
        END_ICON = "<!-- $$"
        TITLE_ICON = "#"
        FILE_ENDING = ".md"

        baseFileName = datetime.datetime.today().strftime('%Y-%m-%d')
        TARGET_PATH = "/Users/cn/Documents/clemniem.github.io/_posts/"

        # define default structure
        DEFAULT_HEADER = """---
        layout: post
        title: {title}
        tags: {tags}
        category: blog
        ---
        """

        def checkIfHeading(line):
            if line.startswith(TITLE_ICON):
                return line.lstrip(TITLE_ICON).rstrip("\n")
            else:
                return None

        def writeToPost(contents, tags, mode='w'):
            # get Title
            title = None
            while title is None:
                title = checkIfHeading(contents.pop(0))

            # title = getTitleFromContent(contents)
            print("Writing {} ({}) to _posts".format(title, tags))
            # header
            header = DEFAULT_HEADER.format(title=title, tags=tags)

            filePath = os.path.join(TARGET_PATH, baseFileName + title.replace(" ", "-") + FILE_ENDING)

            if not os.path.exists(filePath):
                with open(filePath, mode) as pFile:
                    pFile.write(header)
                    pFile.writelines(contents)
            else:
                print("  --> Post <{}> already exists.".format(title))

        def getTitleFromContent(contents):
            for line in contents:
                if line.startswith(TITLE_ICON):
                    return line.lstrip(TITLE_ICON).rstrip("\n")

        # load scribble
        with open(inputPath, "r") as f:
            lines = f.readlines()

        is_section = False
        section_tmp = list()
        section_tags = ""
        section_mode = "w"

        for line in lines:
            # parse from start to end of block -@@-
            if is_section:
                if line.startswith(END_ICON):
                    is_section = False
                    writeToPost(section_tmp.copy(), section_tags, section_mode)
                    section_tmp = list()
                    section_tags = ""
                else:
                    section_tmp.append(line)
            elif line.startswith(START_ICON):
                is_section = True
                # get Tags
                section_tags = line.lstrip(START_ICON).rstrip("\n")

    def run(self):
        print('Hell, world!')
        print('You supplied the following options:', dumps(self.options, indent=2, sort_keys=True))


