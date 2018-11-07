import requests
import re
import json

page=1

while True:
    request=requests.get('http://bbs.lol.qq.com/forum.php?mod=forumdisplay&fid=196&page={0}'.format(page))
    str=request.text.replace(' style="font-weight: bold;color: #EE5023"','')
    #print(str)
    patforum=re.compile(r'</em> <a href="(.*?)" onclick="atarget\(this\)" class="xst" >(.*?)</a>')
    for a in patforum.findall(str):
        with open('forum.txt','a+',encoding='utf-8') as file:
            file.write(a[1]+'      '+a[0]+'\n')
    page+=1
    if page>100:
        break