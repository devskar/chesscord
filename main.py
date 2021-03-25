import threading
import time
from pypresence import Presence

from objects.tray import TrayIcon
from objects.config import Config
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

    lichess = Lichess(config.get_lichess_username())
    chesscom = Chesscom(config.get_chesscom_username())

    while states.running:

        count += 1

        lichess.update_data()
        chesscom.update_data()

        if states.displayed:

            print('[PRESENCE] updated', count)

            if lichess.is_online():

                if lichess.is_playing():
                    lichess.display_playing(rpc)
                else:
                    lichess.display_online(rpc)
            elif chesscom.is_online():
                
                if chesscom.is_playing():
                    chesscom.display_playing(rpc)
                else:
                    chesscom.display_online(rpc)
            else:
                rpc.clear()
        else:
            rpc.clear()

        time.sleep(15)

    print('[APP] Successfully closed')


if __name__ == '__main__':
    run()
