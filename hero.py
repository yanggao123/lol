import re
import requests
import json
import os

url='https://lol.qq.com/biz/hero/champion.js'
request=requests.get(url)
str=str(request.text)
#pat =re.compile(r'"([0-9]{1,4})":"([\w]*)",*')
#print(pat.findall(str))
pat =re.compile(r'"keys":{(.*?)}')
#pat1 =re.compile(r'},"data":{(.*?)}}}')
json1=json.loads('{'+pat.findall(str)[0]+'}')
#json2=json.loads('{'+pat1.findall(str)[0]+'}}}')

for value,name in json1.items():

    '''英雄头像'''
    #requestimg=requests.get('https://ossweb-img.qq.com/images/lol/img/champion/{0}.png'.format(name))
    #with open('heroimg/{0}.png'.format(name),'wb') as imgfile:
    #    imgfile.write(requestimg.content)

    request = requests.get('https://lol.qq.com/biz/hero/{0}.js'.format(name))
    str = request.text
    '''英雄名称'''
    patheroname = re.compile(r',"name":"(.*?)","title":')
    heroname = eval("u"+"\'"+patheroname.findall(str)[0]+"\'")

    '''皮肤'''
    #patskins = re.compile(r',"skins":(.*?),"info"')
    #jsonskins = json.loads(patskins.findall(str)[0])
    #for skin in jsonskins:
    #    requestskin = requests.get('https://ossweb-img.qq.com/images/lol/web201310/skin/big{0}.jpg'.format(skin['id']))
    #    path = 'skinimg/{0}'.format(name)
    #    if not os.path.exists(path):
    #        os.mkdir(path)
    #    with open('skinimg/{0}/{1}.jpg'.format(name, skin['name']), 'wb') as imgfile:
    #        imgfile.write(requestskin.content)

    '''技能'''
    #patspells = re.compile(r',"spells":(.*?),"passive":')
    #jsonspells = json.loads(patspells.findall(str)[0])
    #for spell in jsonspells:
    #    requestskin = requests.get('https://ossweb-img.qq.com/images/lol/img/spell/{0}.png'.format(spell['id']))
    #    path = 'spellimg/{0}'.format(name)
    #    if not os.path.exists(path):
    #        os.mkdir(path)
    #    with open('spellimg/{0}/{1}.png'.format(name, spell['name'].replace(' ', '').replace('/', '')), 'wb') as imgfile:
    #        imgfile.write(requestskin.content)

    '''推荐装备'''
    #try:
    #    patrecommendeds = re.compile(r'{"map":"1","mode":"CLASSIC","recommended":(.*?)}]},"version":')
    #    jsonrecommendeds = json.loads(patrecommendeds.findall(str)[0])
    #    for recommended in jsonrecommendeds:
    #        if recommended['type'] == 'starting':
    #            path = 'startingimg/{0}'.format(name)
    #            if not os.path.exists(path):
    #                os.mkdir(path)
    #            for item in recommended['items']:
    #                request = requests.get('https://ossweb-img.qq.com/images/lol/img/item/{0}.png'.format(item['id']))
    #                with open('startingimg/{0}/{1}.png'.format(name, item['id']), 'wb') as imgfile:
    #                    imgfile.write(request.content)
    #        if recommended['type'] == 'essential':
    #            path = 'essentialimg/{0}'.format(name)
    #            if not os.path.exists(path):
    #                os.mkdir(path)
    #            for item in recommended['items']:
    #                request = requests.get('https://ossweb-img.qq.com/images/lol/img/item/{0}.png'.format(item['id']))
    #                with open('essentialimg/{0}/{1}.png'.format(name, item['id']), 'wb') as imgfile:
    #                    imgfile.write(request.content)
    #        if recommended['type'] == 'offensive' and recommended['showIfSummonerSpell'] == '':
    #            path = 'offensiveimg/{0}'.format(name)
    #            if not os.path.exists(path):
    #                os.mkdir(path)
    #            for item in recommended['items']:
    #                request = requests.get('https://ossweb-img.qq.com/images/lol/img/item/{0}.png'.format(item['id']))
    #                with open('offensiveimg/{0}/{1}.png'.format(name, item['id']), 'wb') as imgfile:
    #                    imgfile.write(request.content)
    #        if recommended['type'] == 'defensive' and recommended['showIfSummonerSpell'] == '':
    #            path = 'defensiveimg/{0}'.format(name)
    #            if not os.path.exists(path):
    #                os.mkdir(path)
    #            for item in recommended['items']:
    #                request = requests.get('https://ossweb-img.qq.com/images/lol/img/item/{0}.png'.format(item['id']))
    #                with open('defensiveimg/{0}/{1}.png'.format(name, item['id']), 'wb') as imgfile:
    #                    imgfile.write(request.content)
    #except:
    #    pass

    '''攻略'''
    try:
        request = requests.get(
            'https://apps.game.qq.com/lol/LOLElasticSearch/SearchGuide.php?source=1&query={0}&category=&champion=&page=1&size=4000&var=searchObj&_=1541487882404'.format(
                heroname))
        request.encoding='utf-8'
        str = request.text
        patguide = re.compile(r',"data":(.*?)}};')
        jsonguides = json.loads(patguide.findall(str)[0])
        guidecontent=''
        for guide in jsonguides:
            guidecontent+=guide['title']+'\n'
        with open('guidelist/{0}.txt'.format(heroname),'w') as file:
            file.write(guidecontent)
    except:
        pass
