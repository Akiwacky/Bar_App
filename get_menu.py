import requests
import os

SHEETY_URL = os.environ.get("SHEETY_URL")
headers = {
    "Authorization": os.environ.get("headers")
}


class FetchItems:

    def __init__(self):
        self.items = []

    def get_items(self):
        response = requests.get(SHEETY_URL, headers=headers)
        response = response.json()['menuItems']
        items = [index for index in response]
        self.items = items

