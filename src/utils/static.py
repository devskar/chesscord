import pathlib

import sys

# PRESENCE ID
CLIENT_ID = '823557044983693393'

# IMAGES
LICHESS_IMAGE = 'lichess-logo'
CHESSCOM_IMAGE = 'chesscom-logo'

# STATES
INGAME_STATE = 'currently in a match'
ONLINE_STATE = 'online'

# DETAILS
LICHESS_DETAILS = 'on lichess.org'
CHESSCOM_DETAILS = 'on chess.com'

# URLS
LICHESS_API_URL = 'https://lichess.org/api'
CHESSCOM_API_URL = 'https://api.chess.com/pub'

# KEYS
KEYS = ['LichessUsername', 'ChesscomUsername']

# GAME STATUS
OFFLINE = 0
ONLINE = 1
PLAYING = 2

# FILE NAME
DATA_FILE_NAME = 'data.json'
WEBPAGE_NAME = 'index.html'


def get_resource_path(relative_path, depth):
    rel_path = pathlib.Path(relative_path)
    dev_base_path = pathlib.Path(__file__).resolve().parents[depth]
    base_path = getattr(sys, '_MEIPASS', dev_base_path)
    return base_path / rel_path


# PATHS
BASE_DIR = pathlib.Path(__file__).resolve().parents[2]
RESOURCES_DIR = get_resource_path('resources', 1)
DATA_FILE_DIR = RESOURCES_DIR / DATA_FILE_NAME
INPUT_DIR = get_resource_path('input', 1)
WEBPAGE_DIR = INPUT_DIR / WEBPAGE_NAME
