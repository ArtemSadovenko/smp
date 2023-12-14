import requests
import json
import csv
import re
from tabulate import tabulate

class JSONPlaceholderAPI:
    def __init__(self):
        self.base_url = "https://jsonplaceholder.typicode.com"

    def get_posts(self):
        endpoint = f"{self.base_url}/posts"
        response = requests.get(endpoint)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def get_post_details(self, post_id):
        endpoint = f"{self.base_url}/posts/{post_id}"
        response = requests.get(endpoint)
        if response.status_code == 200:
            return response.json()
        else:
            return None
