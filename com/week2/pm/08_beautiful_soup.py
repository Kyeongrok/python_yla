import requests
from bs4 import BeautifulSoup

# Pycharm -> Preferences -> Project
# Create virtual environment
# Install request package

url = "https://finance.naver.com/item/main.nhn?code=005930"
response = requests.get(url)
print(response.text)

soup = BeautifulSoup(response.text, 'html.parser')

# print(soup.prettify())

# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# print(soup.title.parent.name)
# print(soup.p)
# print(soup.a)
# print(soup.find_all('a'))