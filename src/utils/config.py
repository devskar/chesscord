import json
import logging

from src.utils.static import KEYS, DATA_FILE_DIR

temp_data = {}


def update_data():
    global temp_data
    temp_data = get_data()


def get_temp_data():
    return temp_data


def get_data():
    with open(DATA_FILE_DIR, 'r') as file:
        content = file.read()

        if content == '':
            return {}
        return json.loads(content)


def update_keys(dictionary):
    data = get_data()

    for key in dictionary:
        data[key] = dictionary[key]
    with open(DATA_FILE_DIR, 'w') as file:
        logging.info(f'Updated config to: {data}')
        json.dump(data, file)

    update_data()


def get_lichess_username():
    global temp_data
    return temp_data.get(KEYS[0])


def get_chesscom_username():
    global temp_data
    return temp_data.get(KEYS[1])
