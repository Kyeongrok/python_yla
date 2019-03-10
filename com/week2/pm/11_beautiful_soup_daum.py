import requests
from bs4 import BeautifulSoup

URL = 'http://www.daum.net/'
# print(URL)

result = requests.get(URL)
# print(result.status_code)
# print(result.text)

soup = BeautifulSoup(result.text, 'html.parser')

# print(soup.find_all('a'))

# print(['http://naver.com', 'http://daum.net'])

# for link in ['http://naver.com', 'http://daum.net']:
#    print(link)

# 다음 -> 고아라 발목 부상이 링크
for link in soup.find_all('a'):
    print(link.get('class'))
    #if link.get_text() == '고아라 발목부상':
    #    print(link.get('href'))
    # print(link.get('href'))