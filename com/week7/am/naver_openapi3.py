import urllib.request
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
client_id = "BoqP7ttLY0wDhxvLzawS"
client_secret = "ztLCPvpLyO"
encText = urllib.parse.quote("나혼자 산다")
display_num = 20
url = "https://openapi.naver.com/v1/search/blog?query=" + encText + "&display=" + str(display_num)

request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id", client_id)
request.add_header("X-Naver-Client-Secret", client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()

if (rescode == 200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)
