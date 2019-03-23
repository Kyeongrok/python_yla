# 네이버 금융의 특정 종목(셀트리온)의 페이지를 불러오는
# crawl이라는 함수를 만들어 보세요.
import requests # crawl하는 라이브러리
from bs4 import BeautifulSoup

def crawl():
    url = "https://finance.naver.com/item/main.nhn?code=025980"
    data = requests.get(url)
    print(data, url)
    return data.content

def parse(pageString):
    soup = BeautifulSoup(pageString, "html.parser")
    noToday = soup.find("p", {"class":"no_today"})
    # noToday에서 span태그인데 class가 blind인 것을 찾아보세요 blind =
    blind = noToday.find("span", {"class":"blind"})
    price = blind.text
    wrapCompany = soup.find("div", {"class":"wrap_company"})
    aTag = wrapCompany.find("a")

    description = wrapCompany.find("div", {"class":"description"})
    code = description.find("span", {"class":"code"})

    def crawl():
        url = "https://finance.naver.com/item/main.nhn?code=025980"
        data = requests.get(url)
        print(data, url)
        return data.content

    def parse(pageString):
        soup = BeautifulSoup(pageString, "html.parser")
        noToday = soup.find("p", {"class": "no_today"})
        # noToday에서 span태그인데 class가 blind인 것을 찾아보세요 blind =
        blind = noToday.find("span", {"class": "blind"})
        price = blind.text
        return {"price": price}

    return {"price":price, "name": aTag.text, "code":code.text}


pageString = crawl()
companyInfo = parse(pageString)
print(companyInfo)