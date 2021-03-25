import requests


def get(url, **kwargs):
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    response = requests.get(url, headers=headers, **kwargs)

    return response.json()
