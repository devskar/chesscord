from PIL import Image
from pystray import Menu, MenuItem, Icon


class TrayIcon:

    def __init__(self, states):
        self.states = states

    def start(self):
        def on_clicked(icon, _):
            print('[APP] Closed by tray icon')
            print('[APP] Closing...')
            self.states.running = False
            icon.stop()

        def clicked_display(_, item):
            self.states.displayed = item.checked

        tray_icon = Icon('chesscord',
                         title='chesscord',
                         icon=Image.open('resources/logo.png'))
        tray_icon.menu = Menu(
                             MenuItem(
                                 'hide',
                                 clicked_display,
                                 checked=lambda item: not self.states.displayed
                             ),
                             MenuItem(
                                 'Exit',
                                 on_clicked
                             ))
        tray_icon.run()
