import json
from json.decoder import JSONObject, JSONArray

import requests

# API URL
global url
url = "http://samples.openweathermap.org/data/2.5/weather?zip=07110,us&appid=b1b15e88fa797225412429c1c50c122a1"

response = requests.get(url)
data = json.loads(response.text)
for key in data:
    print(key, '->', data[key])
print("___________weather__________________")
print(data['weather'])
print(type(data['weather']))
a_list = data['weather']
print(type(a_list))
print("___________________Result______________________")

a_list = data['weather'][0];
for i in a_list:
    if i == "id":
        print("Hello")
