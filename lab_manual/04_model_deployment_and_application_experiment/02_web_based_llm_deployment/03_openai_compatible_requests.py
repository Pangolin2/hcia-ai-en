import json

import requests


def get_completion(prompt):
    headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer no-key'}
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {
                "role": "user",
                "content": prompt,
            }
        ],
    }
    response = requests.post(
        url='http://localhost:8080/v1/chat/completions',
        headers=headers,
        data=json.dumps(data),
    )
    return response.json()['choices']


print(get_completion('Hello'))
