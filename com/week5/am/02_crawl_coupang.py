import requests
from bs4 import BeautifulSoup

def crawl(url):
    response = requests.get(url)
    print(response, url)
    return response.content

def parse(pageString):
    soup = BeautifulSoup(pageString, "html.parser")
    ul = soup.find("ul", {"id":"productList"})
    lis = ul.findAll("li")

    products = []
    for li in lis:
        name = li.find("div", {"class":"name"})
        price = li.find("strong", {"class":"price-value"})
        product = {"name":name.text, "price":price.text}
        products.append(product)
    return products

pageString = crawl("https://www.coupang.com/np/search?component=&q=식빵&channel=user")
products = parse(pageString)
print(products)
print(len(products))

import json
file = open("./bread.json", "w+")
file.write(json.dumps(products))
