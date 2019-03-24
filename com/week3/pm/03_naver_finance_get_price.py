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

URL = 'https://finance.naver.com/item/main.nhn?code=068270' # 셀트리온
#URL = 'https://finance.naver.com/item/main.nhn?code=005930' # 삼성전자
#URL = 'https://finance.naver.com/item/main.nhn?code=000660' # SK
#URL = 'https://finance.naver.com/item/main.nhn?code=066570' # LG전자

html = get_html(URL)
up_price = get_price(html)
print(up_price)