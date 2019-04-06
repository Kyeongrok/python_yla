# 네이버 웹소설 - 베스트 리그 - 중에 특정 카테고리(저는 역사&전쟁)
# 에 있는 첫번째 웹소설의 제목을 콘솔에 출력 해보세요.
# 크롤러 - 크롤링 - url로 string불러오기
# 파서 - 파싱
# careercollege_9F / careercollege
import requests
from bs4 import BeautifulSoup

def crawl(url):
    data = requests.get(url)
    print(data, url)
    return data.content

def getNovelInfo(li):
    img = li.find("img")
    title = img['alt']
    span = li.find("span", {"class":"ellipsis"})
    aTag = li.find("a")
    link = "https://novel.naver.com{}".format(aTag['href'])

    result  = {"title":title, "writer":span.text, "link":link}
    return result

def parse(page_string):
    bsObj = BeautifulSoup(page_string, "html.parser")
    ul = bsObj.find("ul", {"class":"list_type1"})
    lis = ul.findAll("li")

    novelInfos = []
    for li in lis:
        novelInfos.append(getNovelInfo(li))
    return novelInfos

for page in range(1, 6)[:1]:
    url = "https://novel.naver.com/best/genre.nhn?genre=105&page={}".format(page)
    page_string = crawl(url)
    novels = parse(page_string)

    for novel in novels:
        print(novel)