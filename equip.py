import requests
import re
import json
import os

request = requests.get('https://lol.qq.com/biz/hero/item.js')
request.encoding='utf-8'
str = request.text
patequip = re.compile(r',"data":(.*?),"tree":')
jsonequip = json.loads(patequip.findall(str)[0])
for equip in jsonequip:
    requestimg=requests.get('https://ossweb-img.qq.com/images/lol/img/item/{0}.png'.format(equip))
    with open('equipimg/{0}.png'.format(jsonequip[equip]['name']),'wb') as file:
        file.write(requestimg.content)
