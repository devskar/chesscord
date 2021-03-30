import threading
import time
from src import server, app
from src.objects.tray import TrayIcon

import src.utils.config as config

thread = threading.Thread(target=server.run)
thread.start()

tray = TrayIcon()
thread = threading.Thread(target=tray.start)
thread.start()

print('Loading config...\n')
config.update_data()

app.start_mainloop()
