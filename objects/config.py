import configparser

SECTION_NAME = 'FILL IN YOUR INFORMATION'
KEYS = ['LichessUsername', 'ChesscomUsername']


class Config:
    def __init__(self, file_path):
        self.config = configparser.ConfigParser()

        self.config.read(file_path)
        self.section = self.config[SECTION_NAME]

        self.dictionary = dict()

        self._check_keys()

    def _check_keys(self):

        print('[KEYS]')

        for key in KEYS:

            value = self.section.get(key)

            if value == '' or value is None:
                print('[KEY] MISSING KEY: ' + key)
            else:
                print(f'[KEY] {key}\t\t{value}')
                self.dictionary[key] = value

        print()

    def get_lichess_username(self):
        return self.dictionary.get(KEYS[0])

    def get_chesscom_username(self):
        return self.dictionary.get(KEYS[1])
