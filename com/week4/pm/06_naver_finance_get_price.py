import requests
from bs4 import BeautifulSoup


def get_html(URL):
    # response = requests.get(URL)
    data = requests.get(URL)
    # return response.text
    return data.text


def get_price(html):
    soup = BeautifulSoup(html, 'html.parser')
    today = soup.find('div', {'class', 'today'})
    blind = today.find('span', {'class', 'blind'})
    text_price = blind.text
    price = text_price.replace(",", "") # , 제거
    price = int(price) # 문자열을 숫자로
    return price


URLS = [
    'https://finance.naver.com/item/main.nhn?code=068270',
    'https://finance.naver.com/item/main.nhn?code=005930',
    'https://finance.naver.com/item/main.nhn?code=000660',
    'https://finance.naver.com/item/main.nhn?code=066570',
]

for URL in URLS:
    html = get_html(URL)
    price = get_price(html)
    print(price)
