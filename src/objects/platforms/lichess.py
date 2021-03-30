from src.objects.platforms.chessplatform import ChessPlatform
from src.utils import request
from src.utils.static import LICHESS_DETAILS, ONLINE_STATE, LICHESS_IMAGE, INGAME_STATE, LICHESS_API_URL


class Lichess(ChessPlatform):

    def __init__(self, username, token=None):
        super().__init__(username)
        self.token = token

    def is_playing(self):
        return 'playing' in self.cache_data

    def display_online(self, rpc):
        rpc.update(details=LICHESS_DETAILS,
                   state=ONLINE_STATE,
                   large_image=LICHESS_IMAGE)

    def display_playing(self, rpc):

        link = self.cache_data['playing']

        *_, color = link.split('/')

        buttons = [
            {
                'label': 'Spectate',
                'url': link
            }
        ]

        rpc.update(details=LICHESS_DETAILS,
                   state=INGAME_STATE,
                   large_image=LICHESS_IMAGE,
                   buttons=buttons)

    def _get_data(self):
        data = request.get(f'{LICHESS_API_URL}/user/{self.username}')

        if data is None:
            return {}

        return data
