import requests

URL = 'http://www.daum.net'
#print(URL)

response = requests.get(URL)

#print(response.status_code)

print(response.text)
