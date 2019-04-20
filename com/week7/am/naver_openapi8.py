import urllib.request
import ssl
import json

ssl._create_default_https_context = ssl._create_unverified_context


def search(keyword):
    client_id = "BoqP7ttLY0wDhxvLzawS"
    client_secret = "ztLCPvpLyO"

    encText = urllib.parse.quote(keyword)

    url = "https://openapi.naver.com/v1/search/blog?query=" + encText

    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if (rescode == 200):
        response_body = response.read()
        result = response_body.decode('utf-8')
        result = json.loads(result)
        return result['items']
    else:
        print("Error Code:" + rescode)
        return None


result = search("라디오 스타")
print(result)