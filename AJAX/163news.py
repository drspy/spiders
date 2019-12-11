import requests
import json
import  time

url1='https://temp.163.com/special/00804KVA/cm_{}.js?callback=data_callback'
url='https://temp.163.com/special/00804KVA/cm_{}_0{}.js?callback=data_callback'
headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,'
                      'application/signed-exchange;v=b3', 'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,ko;q=0.8', 'Cache-Control': 'no-cache', 'Connection': 'keep-alive', 'Cookie': '_ntes_nnid=2b461147ca80634ee225a3ab99587c2d,1568565503673; _ntes_nuid=2b461147ca80634ee225a3ab99587c2d; s_n_f_l_n3=f7f1af0e3d0419e01575856316027; ne_analysis_trace_id=1575856478358; pgr_n_f_l_n3=f7f1af0e3d0419e015758564783611061; vinfo_n_f_l_n3=f7f1af0e3d0419e0.1.0.1575856316026.0.1575856673638; _antanalysis_s_id=1575856954115', 'Host': 'temp.163.com', 'Pragma': 'no-cache',
           'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-Site': 'none', 'Sec-Fetch-User': '?1', 'Upgrade-Insecure-Requests': '1',
           'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}

def get_kinds():
    return ['guoji','guonei','war']


def news_first_page(kind):
    response = requests.get(url1.format(kind),headers=headers)
    data_json = response.text[14:-1]
    news_list = json.loads(data_json)

    for news in news_list:
        title = news['title']
        link = news['docurl']
        tags = news['keywords']
        tag = []
        for i in tags:
            tag.append(i['keyname'])
        time = news['time']
        print({'title': title, 'link': link, 'time': time, 'tags': tag})


def news(kind,page):
    response = requests.get(url.format(kind,page),headers=headers)
    data_json = response.text[14:-1]
    news_list = json.loads(data_json)

    for news in news_list:
        title = news['title']
        link = news['docurl']
        tags = news['keywords']
        tag = []
        for i in tags:
            tag.append(i['keyname'])
        time = news['time']
        print({'title':title,'link':link,'time':time,'tags':tag})

if __name__ == '__main__':
    for kind in get_kinds():
        news_first_page(kind)
        for page in range(2,10):
            try:
                news(kind,page)
                time.sleep(1)
            except:
                break