import requests,urllib
from bs4 import BeautifulSoup

url='https://www.52pojie.cn/'
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}


def jingpin():
    a=[]
    for i in range(1,20):
        url1='https://www.52pojie.cn/forum.php?mod=forumdisplay&fid=16&page={}'.format(i)
        wb=requests.get(url1,headers=headers)
        soup=BeautifulSoup(wb.text,'lxml')
        t=soup.select('.s.xst')
        for x in t:
            a.append(x.get_text())
            a.append(url+x['href'])
    print(*a,sep='\n')


def sousuo(q):
    q=urllib.parse.quote(q)
    for p in range(11):
        url2='http://zhannei.baidu.com/cse/site?q={}&p={}&cc=52pojie.cn'.format(q,p)
        wb=requests.get(url2,headers=headers)
        wb.encoding=wb.apparent_encoding
        soup=BeautifulSoup(wb.text,'lxml')

        links=soup.select('.result.f h3 a')
        for i in links:
            print(i.get_text(),i['href'])
jingpin()
# sousuo('fdm')