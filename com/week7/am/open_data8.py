# 업종별 상가업소 조회
import urllib.request
from urllib.parse import unquote, urlencode, quote_plus
from bs4 import BeautifulSoup

key = 'EY%2BsdFRIuhsttul39THTv2eMbtfMflErFo4wTqZKy8%2FhdsTrQtUBlohL0jaSaBy6h1cAEeiPqqq0%2F7AR%2BLPGdQ%3D%3D'


def get_store_list():
    url = 'http://apis.data.go.kr/B553077/api/open/sdsc/storeListInUpjong'
    query_params = '?' + urlencode({quote_plus('ServiceKey'): unquote(key),
                                    quote_plus('divId'): 'indsLclsCd',
                                    quote_plus('key'): 'Q',
                                    quote_plus('numOfRow'): '10',
                                    quote_plus('type'): 'xml'})

    request = urllib.request.Request(url + query_params)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if (rescode == 200):
        response_body = response.read()
        # print(response_body.decode('utf-8'))
        result = response_body.decode('utf-8')
        soup = BeautifulSoup(result, 'xml')
        return soup.find_all('item')
    else:
        print("Error Code:" + rescode)
        return None

store_list = get_store_list()
for store in store_list:
    #print(type(store))
    biz_name = store.find('bizesNm').text # 상호명
    address = store.find('rdnmAdr').text # 도로명 주소
    zipcode = store.find('newZipcd').text # 우편번호
    print(biz_name, address, zipcode)