import requests

# Pycharm -> Preferences -> Project
# Create virtual environment
# Install request package


URL = 'http://www.naver.com/'
print(URL)

response = requests.get(URL)

#print(response.status_code)

print(response.text)