import configparser

REQUIRED_KEYS = ['LichessUsername', 'ChesscomUsername']
ADDITIONAL_KEYS = ['LichessApiToken']


class Config:
    def __init__(self, file_path):
        self.config = configparser.ConfigParser()

        self.config.read(file_path)

        self.required = self.config['REQUIRED']
        self.additional = self.config['ADDITIONAL']

        self.dictionary = dict()

        self._check_keys()

    def _check_keys(self):
        self._check_required_keys()
        self._check_additional_keys()

    def _check_required_keys(self):

        print('[REQUIRED KEYS]')

        for key in REQUIRED_KEYS:

            value = self.required.get(key)

            if value == '' or value is None:
                print('[KEY] MISSING REQUIRED KEY: ' + key)
                exit(1)
            else:
                print(f'[KEY] {key}\t\t{value}')
                self.dictionary[key] = value

        print()

    def _check_additional_keys(self):

        print('[ADDITIONAL KEYS]')

        for key in ADDITIONAL_KEYS:

            value = self.additional.get(key)

            if value == '' or value is None:
                print(f'[KEY] {key}\t\tnone')
            else:
                print(f'[KEY] {key}\t\t{value}')
                self.dictionary[key] = value

        print()

    def get_lichess_username(self):
        return self.dictionary[REQUIRED_KEYS[0]]

    def get_chesscom_username(self):
        return self.dictionary[REQUIRED_KEYS[1]]
