import logging
import time

from pypresence import Presence

import config
from platforms.lichess import Lichess
from utils.constants import (CONFIG_LICHESS_USER_KEY, DISCORD_CLIENT_ID,
                             DISCORD_RPC_INTERVAL, ONLINE, PLAYING)

if __name__ == '__main__':
    logging.getLogger().setLevel(logging.INFO)
    logging.info('Starting chesscord ...')

    logging.info('Loading config ...')
    configuration = config.load_config()

    if configuration == None:
        logging.error('No config found -> aborting')
        exit(1)

    if configuration.get(CONFIG_LICHESS_USER_KEY) is None:
        logging.error('No lichess user specified -> aborting')
        exit(1)
    lichess = Lichess(configuration.get(CONFIG_LICHESS_USER_KEY))

    logging.info(f'Successfully loaded lichess!')

    logging.info('Connecting to Discord ...')
    rpc = Presence(DISCORD_CLIENT_ID)
    rpc.connect()
    logging.info('Connected to Discord!')
    while True:
        updated = False

        lichess.update_data()
        status = lichess.get_status()
        if status is PLAYING:
            lichess.display_playing(rpc)
            updated = True

        if status is ONLINE:
            lichess.display_online(rpc)
            updated = True

        if not updated:
            rpc.clear()

        time.sleep(DISCORD_RPC_INTERVAL)
