import json

from utils.constants import CONFIG_FILE_PATH


def load_config():
    with open(CONFIG_FILE_PATH, 'r') as file:
        content = file.read()
        return json.loads(content)
