import os
import copy
import json
import requests

default_url = os.getenv('URL', 'https://nvision-api.nipa.cloud/v1/')
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

    def predict(self,
                image,
                confidence_threshold=0.1,
                output_cropped_image=False):
        """
        docstring: Make a RESTful request for model inference
            :param image: base64 encoded string
            :param confidence_threshold: float
                - value options: [0,1]
                - default: 0.1
            :param output_cropped_image: Boolean
                - value options: True or False,
                - default: False
        """

        data = {
            "raw_data": image,
            "configurations": [
                {
                    "parameter": "ConfidenceThreshold",
                    "value": str(confidence_threshold)
                },
                {
                    "parameter": "OutputCroppedImage",
                    "value": str(output_cropped_image).lower()
                }
            ]
        }

        response = requests.post(url=self.endpoint,
                                 headers=self.headers,
                                 data=json.dumps(data))

        return response