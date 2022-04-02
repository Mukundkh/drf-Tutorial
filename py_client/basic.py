import requests


endpoint = "http://httpbin.org/status/200"
endpoint = "http://httpbin.org/anything"

get_response = requests.get(endpoint, data={"query" : "hello world"}) #HTTP Request
print(get_response.text) #Print raw text response

"""
    HTTP REQUEST -> HTML,
    WHEREAS REST API HTTP REQUEST -> JSON, XML
"""
print(get_response.json())