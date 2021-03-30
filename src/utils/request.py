import requests


def get(url, **kwargs):
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    response = requests.get(url, headers=headers, **kwargs)

    if response.status_code == 200:
        return response.json()

    print('Request to', url, 'failed with status code:', response.status_code)

    return None
