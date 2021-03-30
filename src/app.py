import time

from pypresence import Presence

from src.objects import states
from src.objects.platforms.chesscom import Chesscom
from src.objects.platforms.lichess import Lichess
from src.utils import config, utils
from src.utils.static import OFFLINE, PLAYING, ONLINE, CLIENT_ID


def start_mainloop():
    print('Starting Mainloop')

    count = 0

    rpc = Presence(CLIENT_ID)
    rpc.connect()

    while states.running:
        platforms = []

        updated = False

        if config.get_lichess_username():
            platforms.append(Lichess(config.get_lichess_username()))

        if config.get_chesscom_username():
            platforms.append(Chesscom(config.get_chesscom_username()))

        if len(platforms) == 0:

            utils.open_webpage()

            while config.get_temp_data() == {} or all(config.get_temp_data()[key] is None for key in config.get_temp_data()):
                print('sleep')
                time.sleep(1)
            else:
                continue

        count += 1
        print('[PRESENCE] updated presence', count, 'times')

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

        time.sleep(15)

    rpc.clear()
    print('[APP] Successfully closed')
