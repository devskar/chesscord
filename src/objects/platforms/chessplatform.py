from src.utils.static import PLAYING, ONLINE, OFFLINE


class ChessPlatform:
    def __init__(self, username):
        self.username = username
        self.cache_data = {}

    def is_playing(self):
        pass

    def display_online(self, rpc):
        pass

    def display_playing(self, rpc):
        pass

    def is_online(self):
        return self.cache_data.get('online')

    def _get_data(self):
        pass

    def update_data(self):
        self.cache_data = self._get_data()

    def get_status(self):
        if self.is_online():
            if self.is_playing():
                return PLAYING
            else:
                return ONLINE
        else:
            return OFFLINE

    def update_username(self, username):
        self.username = username

    def is_available(self):
        return self.username != '' and self.username is not None
