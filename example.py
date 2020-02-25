import os
import json
import base64
from nvision import ObjectDetection

model = ObjectDetection(api_key=os.getenv('API_KEY'))

# base64 encoded string
with open(os.path.join('docs', 'street.jpg'), 'rb') as file:
    image = file.read()
    image = base64.b64encode(image).decode('utf-8')

# Make a RESTful call to the Nvision API
response = model.predict(image)

print(response)
print(json.dumps(response.json(), indent=4, sort_keys=True))
