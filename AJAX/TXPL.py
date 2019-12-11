import requests,time,json
headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,'
                      'application/signed-exchange;v=b3', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'zh-CN,zh;q=0.9,ko;q=0.8', 'cache-control': 'no-cache', 'cookie': 'pgv_pvi=6259008512; RK=GHTdYFX5F5; ptcz=f8efcc424e57d278038cdb35ffc1700747a22c207efba176eacb648ea4bdd693; pgv_pvid=5333697070; eas_sid=418516o8P7V704e7a6p3D8g333; uin_cookie=o0905223752; ied_qq=o0905223752; LW_sid=71O5R6N9V0D4V8l4b2H2r0S6w2; LW_uid=e1a5A6T9X084K8v4D2E2h0R6k4; tvfe_boss_uuid=7bdd5e7e7f33cf82; o_cookie=905223752; pac_uid=1_905223752; _ga=amp-6TtZxSNCb0p5L5c2ALs3gA; pgv_flv=-; ptui_loginuin=905223752; uid=726358043; pgv_info=ssid=s2799180920; g_tk=a787987c8719131879c8e5ef00e0ebfea43454aa', 'pragma': 'no-cache', 'sec-fetch-mode': 'navigate', 'sec-fetch-site': 'none', 'sec-fetch-user': '?1', 'upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}

url='https://video.coral.qq.com/varticle/1093557636/comment/v2?callback=_varticle1093557636commentv2&orinum=10' \
    '&oriorder=o&pageflag=1&cursor={}&scorecursor=0&orirepnum=2&reporder=o&reppageflag=1&source=132'


def a(cursor=0):
    response = requests.get(url.format(cursor),headers=headers)
    data = json.loads(response.text[29:-1])

    contents = data['data']['oriCommList']
    for content in contents:
        content = content['content']
        print(content)
    time.sleep(0.5)
    if data['data']['hasnext'] == True :
        next = data['data']['last']

        return a(next)


a()
