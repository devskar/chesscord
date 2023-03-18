from time import time

from utils import request
from utils.constants import (INGAME_STATE, LICHESS_API_URL, LICHESS_DETAILS,
                             LICHESS_IMAGE, OFFLINE, ONLINE, ONLINE_STATE,
                             PLAYING)


class Lichess():

    def __init__(self, username, token=None):
        self.username = username
        self.last_request = {}
        self.token = token

    def is_online(self):
        return 'online' in self.last_request and self.last_request['online']

    def is_playing(self):
        return 'playing' in self.last_request

    def display_online(self, rpc):
        profile = self.last_request['url']

        buttons = [
            {
                'label': 'Profile',
                'url': profile,
            }
        ]

        rpc.update(details=LICHESS_DETAILS,
                   state=ONLINE_STATE,
                   large_image=LICHESS_IMAGE,
                   buttons=buttons)

    def display_playing(self, rpc):

        link = self.last_request['playing']
        profile = self.last_request['url']

        buttons = [
            {
                'label': 'Spectate',
                'url': link
            },
            {
                'label': 'Profile',
                'url': profile,
            }
        ]

        rpc.update(details=LICHESS_DETAILS,
                   state=INGAME_STATE,
                   large_image=LICHESS_IMAGE,
                   buttons=buttons)

    def get_status(self):
        if self.is_playing():
            return PLAYING
        if self.is_online():
            return ONLINE
        return OFFLINE

    def update_data(self):
        data1 = request.get(f'{LICHESS_API_URL}/user/{self.username}')
        data2 = request.get(
            f'{LICHESS_API_URL}/users/status?ids={self.username}')[0]

        if data1 is None or data2 is None:
            return {}
        self.last_request = {**data2, **data1}
