# 업종별 상가업소 조회
import urllib.request
from urllib.parse import unquote, urlencode, quote_plus

key = 'EY%2BsdFRIuhsttul39THTv2eMbtfMflErFo4wTqZKy8%2FhdsTrQtUBlohL0jaSaBy6h1cAEeiPqqq0%2F7AR%2BLPGdQ%3D%3D'

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
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)
