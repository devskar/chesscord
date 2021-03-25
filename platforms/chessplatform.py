class ChessPlatform:
    def __init__(self, username):
        self.username = username
        self.cache_data = None

    def is_playing(self):
        pass

    def display_online(self, rpc):
        pass

    def display_playing(self, rpc):
        pass

    def is_online(self):
        return self.cache_data['online']

    def _get_data(self):
        pass

    def update_data(self):
        self.cache_data = self._get_data()
