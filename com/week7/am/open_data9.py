# 업종별 상가업소 조회
import urllib.request
from urllib.parse import unquote, urlencode, quote_plus
from bs4 import BeautifulSoup
from pandas import DataFrame

key = 'EY%2BsdFRIuhsttul39THTv2eMbtfMflErFo4wTqZKy8%2FhdsTrQtUBlohL0jaSaBy6h1cAEeiPqqq0%2F7AR%2BLPGdQ%3D%3D'


def get_stores():
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
        return soup
    else:
        print("Error Code:" + rescode)
        return None


stores = get_stores()
bizesNm_list = []
for bizesNm in stores.find_all('bizesNm'):
    # print(bizesNm.text)
    bizesNm_list.append(bizesNm.text)
    # print(type(bizesNm.text))
print(bizesNm_list)

rdnmAdr_list = []
for rdnmAdr in stores.find_all('rdnmAdr'):
    # print(rdnmAdr.text)
    rdnmAdr_list.append(rdnmAdr.text)
    # print(type(rdnmAdr.text))
print(rdnmAdr_list)

newZipcd_list = []
for newZipcd in stores.find_all('newZipcd'):
    # print(newZipcd.text)
    newZipcd_list.append(newZipcd.text)
    # print(type(newZipcd.text))
print(newZipcd_list)

data = {'bizesNm': bizesNm_list,
        'rdnmAdr': rdnmAdr_list,
        'newZipcd': newZipcd_list}
biz_frame = DataFrame(data)

print(biz_frame)
