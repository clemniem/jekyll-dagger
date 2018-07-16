import os
import yaml
from datetime import datetime

TARGET = "target"

# define default structure
DEFAULT_HEADER = """---
layout: post
title: {title}
tags: {tags}
category: blog
---
"""

H1 = '# '
H2 = '## '
H3 = '### '
COMMENT = '> '


def assertConfig():
    return os.path.exists(getConfigFilePath())

def assertMdFile(path):
    if path.endswith("md") or path.endswith(".markdown"):
        return os.path.isfile(path)
    else:
        return False

def getOutputDir():
    config = safeLoadConfig()
    if TARGET in config:
        return config[TARGET]

def getConfigPath():
    try:
        HOME = os.environ['HOME']
    except OSError:
        print("Your $HOME environment variable isn't set. Please set it to your Home directory")
        return

    return '{}/.config/jagger'.format(HOME)

def getConfigFilePath():
    config_path = getConfigPath()

    if not os.path.exists(config_path):
        print("Creating directory for the configuration: {}".format(config_path))
        os.makedirs(config_path, exist_ok=True)

    return config_path + "/" + "config.yml"

def safeLoadConfig():
    content = None
    if assertConfig():
        with open(getConfigFilePath(),'r') as config_stream:
            content = yaml.safe_load(config_stream)
    if content is None:
        print("Could not find config-file, please run 'jagger init' first.")
        exit(-1)
    else:
        return content

def saveConfig(config):
    with open(getConfigFilePath(), 'w') as config_file:
        yaml.dump(config, config_file, default_flow_style=False)

def writeSection(title, lines, pTags, sTags):
    OUTPUT_DIR = getOutputDir()
    print("OutputDir={}".format(OUTPUT_DIR))
    post_filename = "{}-{}.md".format(datetime.today().date(), title.replace(" ", "-"))
    print(post_filename)
    post_path = os.path.join(OUTPUT_DIR, post_filename)
    print(post_path)
    tagString = ' '.join(set(pTags + sTags))

    # check if file Exists
    #     if(os.path.isfile(filePath)):
    #         if(file_len(filePath) >= len(lines)):
    #             print("early return")
    #             return

    with open(post_path, 'w') as post:
        post.write(DEFAULT_HEADER.format(title=title, tags=tagString))
        post.writelines(lines[1:])


def file_len(file_name):
    i = 0
    with open(file_name) as f:
        for i, l in enumerate(f):
            pass
    return i + 1


def jaggerFile(filePath):
    is_comment = False
    wasH1 = False
    wasH3 = False
    section_tmp = list()
    page_tags = list()
    section_tags = list()
    section_title = ""
    is_section = False

    with open(filePath, 'r') as mdFile:
        for line in mdFile:
            # TODO check for indented Comment Sections
            if line.startswith('```'):
                is_comment = not is_comment

            if is_comment:
                section_tmp.append(line)
                continue

            if wasH1:
                wasH1 = False
                if line.startswith(COMMENT):
                    # save page tags
                    for tag in line[len(COMMENT):-1:].split(" "):
                        page_tags.append(tag)
                    continue

            if wasH3:
                wasH3 = False
                if line.startswith(COMMENT):
                    # save section tags
                    for tag in line[len(COMMENT):-1:].split(" "):
                        section_tags.append(tag)
                    continue

            if line.startswith(H1):
                # new Page starts
                if section_tmp:
                    # write tmp out
                    print(section_tmp)
                    print(section_tags)
                    writeSection(section_title, section_tmp, page_tags, section_tags)
                    # reset values
                    section_tmp = list()
                    section_tags = list()
                    page_tags = list()
                    is_section = False
                # start new page
                page_tags.append(line[2::].strip())
                wasH1 = True
            elif line.startswith(H3):
                # new section starts
                if section_tmp:
                    # write tmp to output
                    print(section_tmp)
                    print(section_tags)
                    writeSection(section_title, section_tmp, page_tags, section_tags)
                    section_tmp = list()
                    section_tags = list()
                wasH3 = True
                is_section = True
                section_title = line[len(H3):-1]
                section_tmp.append(line)
            elif is_section:
                # add line to section
                section_tmp.append(line)
    # write last section if there is one
    if section_tmp:
        writeSection(section_title, section_tmp, page_tags, section_tags)

