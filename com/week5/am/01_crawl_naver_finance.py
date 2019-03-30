# crawl 크롤 크롤러 - requests
# parse 파스 파서 - bs4
import requests
from bs4 import BeautifulSoup

def crawl(url):
    response = requests.get(url)
    print(response, url)
    return response.content

def parse(pageString):
    soup = BeautifulSoup(pageString, "html.parser")
    noToday = soup.find("p", {"class":"no_today"})
    blind = noToday.find("span", {"class":"blind"})
    wrapCompany = soup.find("div", {"class":"wrap_company"})
    aTag =wrapCompany.find("a")
    img = wrapCompany.find("img")
    code = wrapCompany.find("span", {"class":"code"})
    return {"name":aTag.text, "price":blind.text, "category":img['alt'],
            "code":code.text
            }

codes = ['068270', '000660', '282330']

for code in codes:
    url = "https://finance.naver.com/item/main.nhn?code={}".format(code)
    pageString = crawl(url)
    companyInfo = parse(pageString)
    print(companyInfo)

