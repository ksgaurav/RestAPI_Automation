import requests
import json
from restApiMethods import GetMethods_Demo
from pytest_bdd import scenarios, given, when, then, parsers


class MyStepDefinitions():

    @given("^I set REST API URL$")
    def i_set_rest_api_url(self):
        global url
        url = "http://samples.openweathermap.org/data/2.5/weather?zip=07110,us&appid=b1b15e88fa797225412429c1c50c122a1"
        
    @when("^I send Get Request api endpoint$")
    def i_send_get_request_api_endpoint(self):
        GetMethods_Demo.i_send_get_request_api_endpoint

    @then("^Response BODY should have correct format$")
    def response_body_should_have_correct_format(self):
        GetMethods_Demo.isJsonValid()
        print("_________Do at last__________")

    @then("^Response BODY should contain (.+) value$")
    def response_body_should_contain_value(self, value):
        GetMethods_Demo.test_value_present(self, value)

    @then("^(.+) should have (.+) value$")
    def should_have_value(self, key, value):
        GetMethods_Demo.test_fetch_node_value(self, key, value)
