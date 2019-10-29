import time
from datetime import datetime, timezone, timedelta

class Parse:

    def icon(self, d):
        w={}
        for i,v in d[0].items():
            w[i] = v

        w['icon']='http://openweathermap.org/img/wn/' + str(w['icon']) +'@2x.png'
        return w


    def parse(self, data):
        result=[]
        JST = timezone(timedelta(hours=+9), 'JST')

        for i in data['list']:
            res={}
            res['main']=i['main']
            res['weather'] = self.icon(i['weather'])

            jst = datetime.fromtimestamp(i['dt'], JST)
            res['time'] = jst.strftime("%m/%d %H")

            #array.pushに変更する。
            result.append(res)

        return json.dump(result, f, ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ': '))
