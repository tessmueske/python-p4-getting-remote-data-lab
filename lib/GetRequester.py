import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.content

        # The GetRequester class should have a get_response_body method that sends a GET request to the URL passed in on initialization. This method should return the body of the response.

    def load_json(self):
        response = requests.get(self.url)
        return response.json()

        # The GetRequester class should have a load_json method that should use get_response_body to send a request, then return a Python list or dictionary made up of data converted from the response of that request.