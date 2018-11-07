#http://lol.qq.com/act/a20150326dqpd/index.htm
import requests
import re
import json

requestserverstatus=requests.get('http://apps.game.qq.com/lol/act/a20150325ServerStatus/getServerStatus.php')
strserverstatus = requestserverstatus.text+'aaaaaaaaa'
patserverstatus=re.compile(r'var RetObj =(.*?)aaaaaaaaa')
jsonserverstatus=json.loads(patserverstatus.findall(strserverstatus)[0])
serverstatusinfo=jsonserverstatus['msg'][0]

requestserverinfo=requests.get('http://gameact.qq.com/comm-htdocs/js/game_area/lol_server_select.js')
strserverinfo = requestserverinfo.text.replace('\n','').replace(' ','')
patserverinfo=re.compile(r'{t:"(.*?)",v:"(.*?)",status:"(.*?)"}')

serverinfo={}

for serverinfoitem in patserverinfo.findall(strserverinfo):
    serverinfo[serverinfoitem[1]]=serverinfoitem[0]

serverstatus={'G':'正常',
                'Y':'拥挤',
                'R':'满载',
                'S':'维护',
              }

for id,status in serverstatusinfo.items():
    print(serverinfo[id],serverstatus[status])


