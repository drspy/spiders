import  requests
import os
import time
import re


headers = {'referer':'https://www.toutiao.com/search/?keyword=%E7%BE%8E%E5%A5%B3','cookie':
    'tt_webid=6766888897206322701; WEATHER_CITY=%E5%8C%97%E4%BA%AC; __tasessionId=ni5x8w4ao1575539117393; s_v_web_id=f4df9afe391350a29096f4899f221855; tt_webid=6766888897206322701; csrftoken=431997eb962fd48b3e3859a446363f6f','User-Agent': 'Mozilla/5.0 ('
                                                                                                'Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,like Gecko)Chrome/78.0.3904.108 Safari/537.36'}

url='https://www.toutiao.com/api/search/content/?aid=24&app_name=web_search&offset={}&format=json&keyword=%E7%BE%8E%E5%A5%B3&autoload=true&count=20&en_qc=1&cur_tab=1&from=search_tab&pd=synthesis'
article_url = []
if not os.path.exists(r'c:\users\dr\desktop\今日头条picture'):
    os.mkdir(r'c:\users\dr\desktop\今日头条picture')
for t in range(0,200,20):
    res = requests.get(url.format(t),headers=headers)
    data = res.json()
    if data['count'] != 0:
        for i in data['data']:
            if 'article_url' in i:
                article_url.append(i['article_url'])


        for i in article_url:
            response = requests.get(i,headers=headers)
            pattern = re.compile(r'(http:.*?)\&quot;')
            img_urls = pattern.findall(response.text)

            for x in img_urls:
                x = re.sub(r'\\u002F', '/', x)[:-1]
                file_name = x[-32:]
                with open(r'c:\users\dr\desktop\今日头条picture\{}.jpg'.format(file_name), 'wb')as f:
                    wb = requests.get(x,headers=headers)
                    time.sleep(0.5)
                    f.write(wb.content)
    time.sleep(0.5)
    if data['count'] < 20:
            break
    else:
        print('未请求到网页，请重试')





