import requests
import time
from bs4 import BeautifulSoup

url='https://www.zhihu.com/api/v4/questions/347035787/answers?include=data%5B%2A%5D.is_normal' \
    '%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail' \
    '%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent' \
    '%2Ceditable_content%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cis_labeled%2Cis_recognized%2Cpaid_info%2Cpaid_info_content%3Bdata%5B%2A%5D.mark_infos%5B%2A%5D.url%3Bdata%5B%2A%5D.author.follower_count%2Cbadge%5B%2A%5D.topics&limit=5&offset={}&platform=desktop&sort_by=default'
headers={ 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}


def content(page):
    wb = requests.get(url.format(page),headers=headers)
    data_json = wb.json()
    content_list = data_json['data']
    for i in content_list:
        comment = i['content']
        author = i['author']['name']
        soup = BeautifulSoup(comment,'lxml')
        text = soup.get_text()
        print(author+': '+text)
    time.sleep(0.5)
    if data_json['paging']['is_end'] == True :
        return True

if __name__ == '__main__':
    for page in range(0,500,5):
        if  content(page):
            break