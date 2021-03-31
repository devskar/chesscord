import logging

import requests


def get(url, **kwargs):
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    response = requests.get(url, headers=headers, **kwargs)

    if response.status_code == 200:
        return response.json()

    logging.warning(f'Request to {url} failed.\n Status code: {response.status_code}')

    return None
