import requests


endpoint = "http://httpbin.org/status/200"
endpoint = "http://httpbin.org/anything"

get_response = requests.get(endpoint) #HTTP Request
print(get_response.text) #Print raw text response

