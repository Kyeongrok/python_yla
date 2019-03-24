import requests
from bs4 import BeautifulSoup

# 네이버 금융에서 '삼성전자' 글씨 찾기
URL = 'https://finance.naver.com/'

# 1. 주어진 URL에서 html (page) 정보 가져오기
html = requests.get(URL)

# 2. html 정보를 text 정보로 변환
# Beautiful Soup에서 사용하기 위해서
html_text = html.text

# 3. BeautifulSoup 라이브러리를 통해 html 색인을 만드는 과정
soup = BeautifulSoup(html_text, 'html.parser')

# 4. html 문서내에서 tag가 a인 모든 정보를 가져옴
tags = soup.find_all('a')

print(tags)

for tag in tags:
    print(tag.text)
