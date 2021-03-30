from src.objects.platforms.chessplatform import ChessPlatform
from src.utils import request
from src.utils.static import CHESSCOM_API_URL, CHESSCOM_DETAILS, ONLINE_STATE, CHESSCOM_IMAGE


class Chesscom(ChessPlatform):

    def __int__(self, username):
        self.username = username

    def _get_data(self):
        data1 = request.get(f'{CHESSCOM_API_URL}/player/{self.username}/is-online')
        data2 = request.get(f'{CHESSCOM_API_URL}/player/{self.username}/games')

        if data1 is None or data2 is None:
            return {}

        return {**data1, **data2}

    def display_online(self, rpc):
        rpc.update(details=CHESSCOM_DETAILS,
                   state=ONLINE_STATE,
                   large_image=CHESSCOM_IMAGE)

    def display_playing(self, rpc):
        # Todo
        pass


if __name__ == "__main__":
    chesscom = Chesscom('oskar123123123123123')
