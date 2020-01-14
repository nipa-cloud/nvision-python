import os
import copy
import json
import requests

default_url = os.getenv('URL', 'https://nvision.nipa.cloud/api/')
default_headers = {
    'Content-Type': 'application/json; charset=utf-8',
}


def scrub_dict(d):
    new_dict = {}
    for k, v in d.items():
        if isinstance(v, dict):
            v = scrub_dict(v)
        if v not in (u'', None, {}):
            new_dict[k] = v
    return new_dict


class ObjectDetection:
    def __init__(self, api_key):
        service_name = 'object-detection'
        self.endpoint = default_url + service_name
        self.headers = copy.copy(default_headers)
        self.headers['Authorization'] = 'ApiKey {}'.format(api_key)

    def predict(self, image):
        data = json.dumps({"raw_data": image})
        response = requests.post(url=self.endpoint,
                                 headers=self.headers,
                                 data=data)

        return response