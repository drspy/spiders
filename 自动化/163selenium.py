from selenium import webdriver
import time,urllib.parse
from selenium.webdriver.chrome.options import Options

option=Options()
option.add_argument('--headless')
song=input('歌曲名&歌手：')
url_list='https://music.163.com/?from=infinity#/search/m/?s=%s' % (urllib.parse.quote(song))
url_song='https://music.163.com/?#/{}'

driver=webdriver.Chrome(chrome_options=option)
driver.get(url_list)
driver.switch_to.frame(0)
id=driver.find_element_by_xpath('//div[@class="srchsongst"]/div[1]//div[@class="text"]/a')
id=id.get_attribute('href').split('/')[-1]

driver.get(url_song.format(id))
driver.switch_to.frame(0)
js='window.scrollBy(0,8000)'
driver.execute_script(js)

with open(r'C:\Users\dr\Desktop\WYY.txt','a',encoding='utf-8') as f:
    for i in range (50):
        contants=driver.find_elements_by_xpath('//div[@class="cmmts j-flag"]/div')
        for t in contants:
            texts=t.find_element_by_xpath('.//div[@class="cnt f-brk"]').text
            print(texts,file=f)

        next_page=driver.find_element_by_partial_link_text('下一页')
        next_page.click()
        time.sleep(0.1)
