import os
import psutil
import threading
import logging

import src.objects.server as server
import src.objects.app as app
from src.objects.tray import TrayIcon

import src.utils.config as config


if __name__ == '__main__':

    logging.getLogger().setLevel(logging.INFO)

    thread = threading.Thread(target=server.run)
    thread.start()
    logging.info('Server thread started...')

    tray = TrayIcon()
    thread = threading.Thread(target=tray.start)
    thread.start()
    logging.info('Tray thread started...')

    logging.info('Loading config...')
    config.update_data()

    logging.info('Starting mainloop...')
    app.start_mainloop()
    print('ended')

    # kills the system process
    psutil.Process(os.getpid()).terminate()
