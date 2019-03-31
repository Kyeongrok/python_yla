import requests
from bs4 import BeautifulSoup

def crawl():
    url = "https://finance.naver.com/item/main.nhn?code=068270"
    data = requests.get(url)
    print(data)
    return data.content

def parse(pageString):
    print(pageString)
    soup = BeautifulSoup(pageString, "html.parser")
    noToday = soup.find("p", {"class":"no_today"})
    print(noToday)
    return {}

# 크롤(crawl)-긁어오는거 f5, 파스(parse)-데이터를 뽑는 것
pageString = crawl()
companyInfo = parse(pageString)
print(companyInfo)