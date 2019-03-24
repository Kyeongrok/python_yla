import requests
from bs4 import BeautifulSoup


def get_html(URL):
    response = requests.get(URL)
    return response.text


def get_up_price(html):
    soup = BeautifulSoup(html, 'html.parser')
    tables = soup.find_all('table', {'class', 'no_info'})
    # print(tables[0])

    span_tags = tables[0].find_all('span', {'class', 'blind'})
    # span_tags 안에 값을 확인해서 최고 값을 찾는다.
    # print(span_tags)
    # for span_tag in span_tags:
    #    print(span_tag)
    text_price = span_tags[5].text
    price = text_price.replace(",", "") # , 제거
    price = int(price) # 문자열을 숫자로
    return price

URL = 'https://finance.naver.com/item/main.nhn?code=068270' # 셀트리온
#URL = 'https://finance.naver.com/item/main.nhn?code=005930' # 삼성전자
#URL = 'https://finance.naver.com/item/main.nhn?code=000660' # SK
#URL = 'https://finance.naver.com/item/main.nhn?code=066570' # LG전자

html = get_html(URL)
up_price = get_up_price(html)
print(up_price)