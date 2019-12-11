import requests
import time
import re

url_top = 'https://weread.qq.com/web/bookListInCategory/{}?maxIndex={}'
url = 'https://weread.qq.com/web/category'


def book_kinds():
    response = requests.get(url)
    pattern = re.compile(r'<a href="/web/category/(.*?)"')
    kinds_list = re.findall(pattern,response.text)
    return kinds_list


def book_print(kind,page):
    response = requests.get(url_top.format(kind,page))
    books_data = response.json()
    if books_data['books'] != []:
        books_list = books_data['books']
        for book_dict in books_list:
            title = book_dict['bookInfo']['title']
            author = book_dict['bookInfo']['author']
            star = book_dict['bookInfo']['star']
            star = int(star)/10
            price = book_dict['bookInfo']['price']
            print({'title':title,'author':author,'star':star,'price':price})
            time.sleep(0.5)
    else:
        return False



if __name__ == '__main__':
    for kind in book_kinds():
        for page in range(0,1000,20):
            if not book_print(kind,page):
                break
