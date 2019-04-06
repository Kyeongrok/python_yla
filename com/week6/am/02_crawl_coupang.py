# 쿠팡에서 특정 키워드로 검색한 결과를 파싱하기
import requests
from bs4 import BeautifulSoup

def crawl(url):
    data = requests.get(url)
    print(data, url)
    return data.content

def getProductInfo(li):
    name = li.find("div", {"class":"name"})
    priceValue = li.find("strong", {"class":"price-value"})
    return {"name":name.text, "price":priceValue.text}

def parse(pageString):
    bsObj = BeautifulSoup(pageString, "html.parser")
    ul = bsObj.find("ul", {"id":"productList"})
    lis = ul.findAll("li")
    print("상품개수:", len(lis))
    products = []
    for li in lis:
        productInfo = getProductInfo(li)
        products.append(productInfo)
    return products

keywordResult = []
for page in range(1, 17):
    url = "https://www.coupang.com/np/search?component=&q={}&page={}&channel=user".format("에어컨",page)
    pageString = crawl(url)
    products = parse(pageString)
    keywordResult = keywordResult + products

print(len(keywordResult))
import json
file = open("./에어컨.json", "w+")
file.write(json.dumps(keywordResult))
