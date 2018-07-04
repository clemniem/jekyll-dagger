import os
import yaml

CONFIG_FILE_PATH = "{}/.config/{}/config.yml".format(os.environ['HOME'],"jagger")

def assertConfig():
    return os.path.exists(CONFIG_FILE_PATH)

def safeLoadConfig():
    content = None
    if assertConfig():
        with open(CONFIG_FILE_PATH,'r') as config_stream:
            content = yaml.safe_load(config_stream)
    if content is None:
        print("Could not find config-file, please run 'jagger init' first.")
        exit(-1)
    else:
        return content

def saveConfig(config):
    with open(CONFIG_FILE_PATH, 'w') as config_file:
        yaml.dump(config, config_file, default_flow_style=False)