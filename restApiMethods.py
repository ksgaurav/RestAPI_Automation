from json.decoder import JSONObject, JSONArray

import requests
import json
import jsonpath


class GetMethods_Demo():
    # API URL
    global url
    url = "http://samples.openweathermap.org/data/2.5/weather?zip=07110,us&appid=b1b15e88fa797225412429c1c50c122a1"

    def i_send_get_request_api_endpoint(self):
        response = requests.get(url)

    def test_fetch_node_value(self, key, value):
        self.key = key  # key = "name"
        self.value = value  # value = "Mountain View"
        response = self.i_send_get_request_api_endpoint()
        abc = response.json()
        x = abc[self.key]
        assert x == self.value

    def test_value_present(self, value):
        self.value = value
        response = self.i_send_get_request_api_endpoint()
        data = json.loads(response.text)
        # for key in data:
        # key, '->', data[key]
        a_list = data['weather'][0];
        for i in a_list:
            assert i == value

    def isJsonValid(self):
        response = self.i_send_get_request_api_endpoint()
        json_file = json.loads(response.text)
        print(json_file)
        try:
            JSONObject(json_file)
            # return True
        except Exception:
            try:
                JSONArray(json_file)
            except Exception:
                return False
        return True

    def test_isJSONValid(self):
        actual_value = self.isJsonValid()
        assert actual_value == True
