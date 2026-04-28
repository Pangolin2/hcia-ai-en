import requests


def get_completion():
    response = requests.get(url='http://localhost:8080/health')
    return response


print(get_completion())
