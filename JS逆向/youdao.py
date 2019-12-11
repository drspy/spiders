import requests
from time import time
from random import randint
from hashlib import md5
from urllib.error import URLError,HTTPError


UA='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
url='http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
headers = {
     'Accept': 'application/json, text/javascript, */*; q=0.01',
     'Accept-Encoding': 'gzip, deflate',
     'Accept-Language':'zh-CN,zh;q=0.9,ko;q=0.8',
     'Cache-Control': 'no-cache',
     'Connection': 'keep-alive',
     'Content-Length': '264',
     'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
     'Cookie': 'OUTFOX_SEARCH_USER_ID=-1371095248@171.8.75.93; OUTFOX_SEARCH_USER_ID_NCOO=753417223.095676; UM_distinctid=16daeab8fc16a-0fb01eab3f5a42-67e1b3f-ea600-16daeab8fc2607; JSESSIONID=aaaHJKfz6TSl4-IXeeX6w; ___rl__test__cookies=1574928778312',
     'Host': 'fanyi.youdao.com',
     'Origin': 'http://fanyi.youdao.com',
     'Pragma': 'no-cache',
     'Referer': 'http://fanyi.youdao.com/',
     'User-Agent': UA}

print('-'*10+'*'*10+'有道词典'+'*'*10+'-'*10)

while True:
    i=input('（按`退出）输入你要翻译的词汇：')
    if i == '`':
        break

    salt=int((time())*1000)

    ts=str(salt)+str(randint(0,10))

    sign_hash=md5('fanyideskweb'.encode('utf-8')+i.encode('utf-8')+str(salt).encode('utf-8')+"n%A-rKaT5fb[Gy?;N5@Tj".encode('utf-8'))
    sign=sign_hash.hexdigest()

    bv=md5(UA.encode('utf-8')).hexdigest()

    data = {
      'i': i,
      'from': 'AUTO',
      'to': 'AUTO',
      'smartresult': 'dict',
      'client': 'fanyideskweb',
      'salt': salt,
      'sign': sign,
      'ts': ts,
      'bv': bv,
      'doctype': 'json',
      'version': '2.1',
      'keyfrom': 'fanyi.web',
      'action': 'FY_BY_CLICKBUTTION'}

    try:
        response=requests.post(url,headers=headers,data=data)

        answer=response.json()['smartResult']['entries'][1:]
        for i in answer:
            print(i.strip())
    except HTTPError as e:
        print(e.code,e.reason)
    except URLError as e:
        print(e.reason)
    except KeyError :
        answer=response.json()["translateResult"][0][0]["tgt"]
        print(answer)
