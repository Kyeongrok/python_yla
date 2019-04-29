# 업종별 상가업소 조회
import urllib.request
from urllib.parse import unquote, urlencode, quote_plus
import json
import folium

key = 'EY%2BsdFRIuhsttul39THTv2eMbtfMflErFo4wTqZKy8%2FhdsTrQtUBlohL0jaSaBy6h1cAEeiPqqq0%2F7AR%2BLPGdQ%3D%3D'


def get_store_list():
    url = 'http://apis.data.go.kr/B553077/api/open/sdsc/storeListInUpjong'
    query_params = '?' + urlencode({quote_plus('ServiceKey'): unquote(key),
                                    quote_plus('divId'): 'indsLclsCd',
                                    quote_plus('key'): 'Q',
                                    quote_plus('numOfRows'): '100',
                                    quote_plus('type'): 'json'})

    request = urllib.request.Request(url + query_params)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()

    if (rescode == 200):
        response_body = response.read()
        # print(response_body.decode('utf-8'))
        result = response_body.decode('utf-8')
        # str -> json
        json_result = json.loads(result)
        # {'body':{ 'items': } }
        return json_result['body']['items']
    else:
        print("Error Code:" + rescode)
        return None


store_list = get_store_list()

map = folium.Map(location=[37.5665, 126.9780], tiles='Stamen Toner')

for store in store_list:
    # print(store)
    ctprvnNm = store['ctprvnNm']
    if ctprvnNm == '서울특별시':
        bizesNm = store['bizesNm']
        lat = store['lat']
        lon = store['lon']
        indsMclsNm = store['indsMclsNm']  # '한식' (blue) or '중식'(red) 나머지('green')
        # print(indsMclsNm)
        if indsMclsNm == '한식':
            color = 'blue'
        elif indsMclsNm == '중식':
            color = 'red'
        else:
            color = 'green'

        folium.Marker([lat, lon], popup=bizesNm,
                      icon=folium.Icon(color=color)).add_to(map)

map.save('bizes.html')