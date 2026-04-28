import json

import requests


def get_completion(prompt):
    headers = {'Content-Type': 'application/json'}
    data = {"prompt": prompt}
    response = requests.post(
        url='http://localhost:8080/completions',
        headers=headers,
        data=json.dumps(data),
    )
    return response.json()['content']


print(get_completion('<|User|>Hello<|Assistant|>'))
