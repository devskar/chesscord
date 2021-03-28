import threading
import time
from pypresence import Presence

from objects.tray import TrayIcon
from objects.config import Config

from utils.static import OFFLINE, ONLINE, PLAYING

from platforms.chesscom import Chesscom
from platforms.lichess import Lichess

CLIENT_ID = '823557044983693393'

print('Loading config...\n')
config = Config('config.config')


def run():
    class States:
        def __init__(self):
            self.running = True
            self.displayed = True

    rpc = Presence(CLIENT_ID)
    rpc.connect()

    states = States()

    tray = TrayIcon(states)

    thread = threading.Thread(target=tray.start)
    thread.start()

    count = 0

    platforms = []

    if config.get_lichess_username():
        platforms.append(Lichess(config.get_lichess_username()))

    if config.get_chesscom_username():
        platforms.append(Chesscom(config.get_chesscom_username()))

    if len(platforms) == 0:
        print('FILL IN CONFIG')
        exit(0)

    while states.running:

        print(f'update presence ({count})')

        updated = False

        count += 1
        if states.displayed:

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

    print('[APP] Successfully closed')


if __name__ == '__main__':
    run()
