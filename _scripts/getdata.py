import urllib.parse
import requests
import time
import pandas as pd
import json
import time
from datetime import datetime, timezone, timedelta


#クエリを組み立てる
def url():
    domain="https://api.openweathermap.org/data/2.5/forecast"
    query = {
            'id': 'Tokyo,JP',
            'mode': 'json',
            'units': 'metric',
            'lang': 'ja',
            'APPID': 'adc240180d6c352135ef91540c488134',
            }
    return domain + '?' + urllib.parse.urlencode(query)
      
def get(url):
    try: 
        r=requests.get(url)
        if error_check(r):
            return r.json()
        else:
            return False
    except:
        return False


def error_check(r):
    if r.status_code != 200:
        return False
    else:
        return True

def weather_parse(d):
    w={}
    for i,v in d[0].items():
        w[i] = v
    w['icon']='http://openweathermap.org/img/wn/' + str(w['icon']) +'@2x.png'

    return w
    
url=url()
data=get(url)
result=[]

JST = timezone(timedelta(hours=+9), 'JST')


for i in data['list']:
    res={}
    res['main']=i['main']
    res['weather'] = weather_parse(i['weather'])
    weather_parse(i['weather'])

    jst = datetime.fromtimestamp(i['dt'], JST)
    res['time'] = jst.strftime("%m/%d %H")

    #array.pushに変更する。
    result.append(res)


f = open("../_data/weather.json", "w")
json.dump(result, f, ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ': '))