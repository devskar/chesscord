from PIL import Image
from pystray import Menu, MenuItem, Icon

from src.objects import states
from src.utils import utils
from src.utils.static import RESOURCES_DIR


class TrayIcon:

    def start(self):
        def on_clicked(icon, _):
            print('[APP] Closed by tray icon')
            print('[APP] Closing...')
            states.running = False
            icon.stop()

        def clicked_display(_, item):
            states.displayed = item.checked

        tray_icon = Icon('chesscord',
                         title='chesscord',
                         icon=Image.open(RESOURCES_DIR / 'logo.png'))
        tray_icon.menu = Menu(
            MenuItem(
                'update config',
                utils.open_webpage
            ),
            MenuItem(
                'hide',
                clicked_display,
                checked=lambda item: not states.displayed
            ),
            MenuItem(
                'Exit',
                on_clicked
            )
        )

        tray_icon.run()
