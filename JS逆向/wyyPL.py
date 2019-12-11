import requests,base64
from json import dumps
from random import sample
from Crypto.Cipher import AES
import binascii


headers={'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
 'accept-language': 'zh-CN,zh;q=0.9,ko;q=0.8',
 'cache-control': 'no-cache', 'content-length': '474',
 'content-type': 'application/x-www-form-urlencoded',
 'cookie': '_iuqxldmzr_=32; _ntes_nnid=2b461147ca80634ee225a3ab99587c2d,1568565503673; '
           '_ntes_nuid=2b461147ca80634ee225a3ab99587c2d; / '
           'WM_TID=6X%2BDpWYdoM5BBUQFRFZ55hsypJgM27T2; ntes_kaola_ad=1; '
           'WM_NI=eLP0oqWNlY3lTJBxxluxCGBFfxc4DpJ6Ay7P4lXn7zNSK2GLp8aczH6T'
           '%2B4fDSGAwkUDL8QydeNr5P01HWjkId '
           '%2FFYTcfHf6kZfKtF42YLRJnIWPoSKfW3KxfuTwAxKTfBR3g%3D; '
           'WM_NIKE=9ca17ae2e6ffcda170e2e6ee98d76192b3bab4e561949e8fa6d84b879b8eafb8218ab00095c66eaa939abadc2af0fea7c3b92aa794a0d1ee7b/'
           '9592a4bab26898968e99fb68b7a88da8c14ea6a8add5c77c8aea8f9ab65cf8b4988fb6728e8d85d3c648b4e8af84f944f68ce5d5e55091998f98ea5f88/'
           '94f8b2fc70a792bed6d33cf398998bea43a8f18abad769a698aad7ea52a695bca7b73a9b949eabed439590a1b4ca6e95ed8599e57f98a98f99ca60a69e9ed4e637e2a3; '
           'JSESSIONID-WYYY=Vz5oIDGyIkobm1XpTFvSZMkS%2BI8QP72y1hYTzl%2FbfxZkGNQC95Cin9D%2Fv%5Cq8fvAotajeoHhy8w%2F%2BK10X%2Bf6qq12z7Hkhei2WylCEDevy3Y1d9m'
           '7M%2FiK%2B%2F8bvQyVr2wGWUl3aIPw3egXbNhY4o7sE9VuMm6eY%5CatA9xBnugJGyefImjlQ%3A1575014016906; playerid=90251314',
 'origin': 'https://music.163.com',
 'pragma': 'no-cache',
 'referer': 'https://music.163.com/',
 'sec-fetch-mode': 'cors',
 'sec-fetch-site': 'same-origin',
 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}


second_params = "010001"
third_params="00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"
forth_params='0CoJUm6Qyw8W8jud'


#返回16位随机字符串
def a(a):

    s = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    t=''.join(sample(s,a))

    return t

#模拟JS AES加密
def b(a,b):

    if type(a) is bytes:
        a=a.decode()
    padding = 16 - len(a) % 16
    a += padding * chr(padding)      #填充至16倍数长度的明文

    text = a.encode('utf-8')
    key = b.encode('utf-8')
    iv = b'0102030405060708'
    aes = AES.new(key, AES.MODE_CBC,iv)
    entext = aes.encrypt(text)
    entext = base64.b64encode(entext)

    return entext

#模拟JS RSA加密
def c(a,b,c):
    text = a[::-1]  # 明文处理，反序并hex编码,RSA的密文是对代表明文的数字的E次方求mod N 的结果
    rsa = int(binascii.hexlify(text.encode('utf-8')), 16) ** int(b, 16) % int(c, 16)

    return format(rsa,'x').zfill(256)

#加密后的结果
def get_params_encseckey(d,e,f,g):
    i=a(16)
    d=dumps(d)
    encText=b(d,g)
    params=b(encText,i)
    encseckey=c(i,e,f)

    return params.decode(),encseckey

#搜索歌曲，返回歌曲菜单和ID
def main():
    song = input('请输入你想查询评论的歌曲名:')
    first_params1 = {'csrf_token': "", 'hlposttag': "</span>", 'hlpretag': '<span class="s-fc7">', 'limit': "30",
                     'offset': "0", 's': song, 'total': "true", 'type': "1"}
    data={}
    data['params'], data['encSecKey'] = get_params_encseckey(first_params1, second_params, third_params,forth_params)
    url_search='https://music.163.com/weapi/cloudsearch/get/web?csrf_token='
    response=requests.post(url_search,headers=headers,data=data)
    data_json=response.json()
    songs=data_json['result']['songs']
    songs_id=[]
    for i,song in enumerate(songs):
        songs_id.append(song['id'])
        print(i,'   歌曲:'+song['name']+'     歌手：'+song['ar'][0]['name'])
    return songs_id

#返回第一页评论
def main2(id):
    url_song = 'https://music.163.com/weapi/v1/resource/comments/R_SO_4_{}?csrf_token='.format(id)
    data = {}
    first_params2 = {'rid': "R_SO_4_{}".format(bianhao[number]), 'offset': "0", 'total': "true", 'limit': "20",
                     'csrf_token': ''}
    data['params'], data['encSecKey'] = get_params_encseckey(first_params2, second_params, third_params,
                                                             forth_params)
    response = requests.post(url_song, data=data, headers=headers)
    data_json = response.json()
    if data_json['hotComments']:
        HotComments = data_json['hotComments']
        print('\n' + '     精彩评论:')

        num1 = 1
        for hotcomment in HotComments:
            hotcomment = hotcomment['content']
            print('%d' % num1 + '.', hotcomment)
            num1 += 1
    NormalComments = data_json['comments']
    print('\n' + '     最新评论：')

    num2 = 1
    for normalcomment in NormalComments:
        normalcomment = normalcomment['content']
        print('%d' % num2 + '.', normalcomment)
        num2 += 1

    # 翻页
    for offset in range(0, 1000, 20):
        data = {}
        first_params2 = {'rid': "R_SO_4_{}".format(bianhao[number]), 'offset': str(offset), 'total': "false",
                         'limit': "20", 'csrf_token': ''}
        data['params'], data['encSecKey'] = get_params_encseckey(first_params2, second_params, third_params,forth_params)
        response = requests.post(url_song.format(id), data=data, headers=headers)
        data_json = response.json()
        comments = data_json['comments']

        for comment in comments:
            comment = comment['content']
            print('%d' % num2 + '.', comment)
            num2 += 1

        if data_json['more'] == False:
            break


if __name__ == '__main__':
    while True:
        # try:
            bianhao=main()
            number = int(input('\n' + '请输入你想查询的歌曲编号（输入30重新查询）：'))

            while number == 30:
                bianhao=main()
                number = int(input('\n' + '请输入你想查询的歌曲编号（输入30重新查询）：'))

            main2(bianhao[number])

            Q=input('按任意键继续查询，退出请按空格')
            if Q == ' ':
                break

        # except :
            print('出错了请重新输入！~')


