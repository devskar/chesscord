import logging
import time

from pypresence import Presence

from src.objects import states
from src.objects.platforms.chesscom import Chesscom
from src.objects.platforms.lichess import Lichess
from src.utils import config, utils
from src.utils.static import OFFLINE, PLAYING, ONLINE, CLIENT_ID


def start_mainloop():
    logging.info('Mainloop started')

    count = 0

    rpc = Presence(CLIENT_ID)
    rpc.connect()

    lichess = Lichess(config.get_lichess_username())
    chesscom = Chesscom(config.get_chesscom_username())

    platforms = []

    while states.running:

        updated = False

        lichess.update_username(config.get_lichess_username())
        chesscom.update_username(config.get_chesscom_username())

        if lichess.is_available():
            platforms.append(lichess)

        if chesscom.is_available():
            print('available', chesscom.username)
            platforms.append(chesscom)

        print(platforms)

        if len(platforms) == 0:
            logging.warning('Missing information -> update config')
            rpc.clear()
            utils.open_webpage()

            while config.get_temp_data() == {} or all(config.get_temp_data()[key] is None for key in config.get_temp_data()):
                time.sleep(1)
            else:
                continue

        count += 1
        logging.info(f'Presence updated ({count})')

        for platform in platforms:

            platform.update_data()

            status = platform.get_status()

            if status is OFFLINE:
                continue

            if status is PLAYING:
                platform.display_playing(rpc)
                updated = True
                break

            if status is ONLINE:
                platform.display_online(rpc)
                updated = True
                break

        if not updated:
            rpc.clear()

        platforms.clear()
        time.sleep(15)

    rpc.clear()
    logging.info('Mainloop ended')
