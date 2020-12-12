#python3
#通用文字识别－高精版OCR文字识别（双11返场，2折）
#继续薅羊毛，阿里云的接口，似乎是一年内有效
import urllib.request
import urllib.parse
import json
import time
import base64
with open('E:\\00workspace\\99tools\\1.jpg', 'rb') as f:  # 以二进制读取本地图片
    data = f.read()
    encodestr = str(base64.b64encode(data),'utf-8')
#请求头
headers = {
         'Authorization': 'APPCODE c7bc6cbd30b14d7cb7a1ad90f2ad32ca',#这块有个坑，我以为是把APPCODE整个放上去就完了，没想到前面要加个APPCODE，导致一直401授权不通过
         'Content-Type': 'application/json; charset=UTF-8',
    }
def posturl(url,data={}):
  try:
    params=json.dumps(dict).encode(encoding='UTF8')
    req = urllib.request.Request(url, params, headers)
    r = urllib.request.urlopen(req)
    html =r.read()
    r.close();
    return html.decode("utf8")
  except urllib.error.HTTPError as e:
      print(e.code)
      print(e.read().decode("utf8"))
  time.sleep(1)
if __name__=="__main__":
    url_request="https://ocrapi-advanced.taobao.com/ocrservice/advanced"
    dict = {'img': encodestr}

    html = posturl(url_request, data=dict)
    print(html)