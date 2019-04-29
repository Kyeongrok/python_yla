# 업종별 상가업소 조회
import urllib.request
from urllib.parse import unquote, urlencode, quote_plus
import json
import folium

map = folium.Map(location=[37.5665, 126.9780])

key = 'EY%2BsdFRIuhsttul39THTv2eMbtfMflErFo4wTqZKy8%2FhdsTrQtUBlohL0jaSaBy6h1cAEeiPqqq0%2F7AR%2BLPGdQ%3D%3D'

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
    result = response_body.decode('utf-8')
    json_result = json.loads(result)
    #print(json_result['body'])
    #print(json_result['body'].keys())
    #print("items : ", json_result['body']['items'])
    print("numOfRows : ", json_result['body']['numOfRows'])
    print("pageNo : ", json_result['body']['pageNo'])
    print("totalCount : ", json_result['body']['totalCount'])

    items = json_result['body']['items']
    for item in items:
        print(item)
        # 상가명, 경도, 위도
        #print(item['bizesNm'], item['lon'], item['lat'])
        # print(type(item['bizesNm']), type(item['lon']), type(item['lat']))
        #bizesNm = item['bizesNm']
        #lat = item['lat']
        #lon = item['lon']
        #folium.Marker([lat, lon], popup=bizesNm, icon=folium.Icon(icon='red')).add_to(map)
        #folium.Marker([item['lat'], item['lon']], popup=item['bizesNm'],
        #              icon=folium.Icon(icon='red')).add_to(map)
else:
    print("Error Code:" + rescode)

map.save('bizes.html')