# 측정소별 실시간 측정정보 조회

import urllib.request
import json

# http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty?serviceKey= &numOfRows=10&pageNo=1&stationName=%EC%A2%85%EB%A1%9C%EA%B5%AC&dataTerm=DAILY&ver=1.3
key = 'EY%2BsdFRIuhsttul39THTv2eMbtfMflErFo4wTqZKy8%2FhdsTrQtUBlohL0jaSaBy6h1cAEeiPqqq0%2F7AR%2BLPGdQ%3D%3D'
# python function
# getMsrstnAcctoRltmMesureDnsty(numOfRows, pageNo, stationName, ...)

# print(urllib.parse.quote('종로구'))
print(urllib.parse.quote('서초구'))
station = urllib.parse.quote('노원구')

url = 'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty' \
      + '?serviceKey=' + key + \
      '&numOfRows=10&pageNo=2' + \
      '&stationName=' + station + \
      '&dataTerm=DAILY&ver=1.3&_returnType=json'

# print(url)
# 측정소별 실시간 측정정보 조회
request = urllib.request.Request(url)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if (rescode == 200):
    response_body = response.read()
    result = response_body.decode('utf-8')
    print(result)
    print(type(result))
    #print(result['list'])

    # str -> dict
    json_result = json.loads(result)
    print(json_result)

    # {'key': value}
    print(json_result['list'])

    print("for loop")
    for item in json_result['list']:
        # print(item.keys())
        # print("key, value")
        # for key in item.keys():
        #     print(key, item[key])
        # print("\n")
        print(item['dataTime'], item['o3Value'])
else:
    print("Error Code:" + rescode)
