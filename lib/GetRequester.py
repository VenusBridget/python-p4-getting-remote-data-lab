import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        # pass
        url = self.url
        response = requests.get(url)
        return response.content

    def load_json(self):
        # pass
        response_body = self.get_response_body()
        json_data = json.loads(response_body)
        return json_data