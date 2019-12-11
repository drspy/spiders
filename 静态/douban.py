import requests,time,pickle
from bs4 import BeautifulSoup

url = 'https://movie.douban.com/top250?start={}'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}


def response(url):
    wb = requests.get(url,headers=headers)
    soup = BeautifulSoup(wb.text,'lxml')

    titles = []
    title_link = soup.select('.hd a ')
    for i in title_link:
        titles.append(i.get_text(strip=True))

    directors = []
    director_link = soup.select('.info .bd p:nth-of-type(1)')
    for i in director_link:
        directors.append(i.get_text().split('\n')[1].strip())

    times = []
    time_link = soup.select('.info .bd p:nth-of-type(1)')
    for i in time_link:
        times.append(i.get_text().split('\n')[2].strip())

    scores = []
    score_link = soup.select('.rating_num')
    for i in score_link:
        scores.append(i.get_text())

    appraises = []
    appraise_link = soup.select('.star span:nth-of-type(4)')
    for i in appraise_link:
        appraises.append(i.get_text())

    results = []
    for x in range (25):
        results.append(titles[x]+'\n'+directors[x]+'\n'+times[x]+'\n'+scores[x]+'\t'+appraises[x])

    print(*results,sep='\n\n')




if __name__=='__main__':
    for i in range(0, 225, 25):
        response(url.format(i))
        time.sleep(0.5)


