import requests
import json
import re
import time

page=1

while True:
    now = time.time()
    timeStamp = (int(round(now * 1000)))
    print(timeStamp)

    headers={
'Accept': '* / *',
'Accept - Encoding': 'gzip, deflate',
'Accept - Language': 'zh - CN, zh;q = 0.9',
'Connection': 'keep - alive',
'Host': 'apps.game.qq.com',
'Referer': 'http: // daoju.qq.com / lol / list / shoppinglist.shtml?ADTAG = innercop.lol.SY.shoppinglist_new',
'User - Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 70.0.3538.77Safari / 537.36'
    }

    request=requests.get('http://apps.game.qq.com/daoju/v3/api/hx/goods/api/list/v54/GoodsListApp.php?view=biz_portal&page={0}&pageSize=8&orderby=dtShowBegin&ordertype=desc&appSource=pc&appSourceDetail=pc_lol_revison&channel=1001&storagetype=6501&plat=0&output_format=jsonp&biz=lol&_={1}'.format(page,timeStamp),headers=headers)
    str=request.text+'aaaaaaaaaaa'
    pategood = re.compile(r'var ogoods_list_api =(.*?)aaaaaaaaaaa')
    try:
        jsongood = json.loads(pategood.findall(str)[0])
        for good in jsongood['data']['goods']:
            requestimg=requests.get(good['propImg'])
            with open('goodimg/{0}.jpg'.format(good['propName'].replace('/','')),'wb') as file:
                file.write(requestimg.content)
            time.sleep(1)
        if jsongood['data']['totalPage'] == page:
            break
        page += 1
        time.sleep(2)
    except:
        pass