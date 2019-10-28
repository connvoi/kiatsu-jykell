import urllib.parse
import requests

class Api:

    #クエリを組み立てる
    def url(cityid):
        domain="https://api.openweathermap.org/data/2.5/forecast"
        query = {
                'id': cityid,
                'mode': 'json',
                'units': 'metric',
                'lang': 'ja',
                'APPID': 'adc240180d6c352135ef91540c488134',
                }
        return domain + '?' + urllib.parse.urlencode(query)
          
    def get(cityid):
        url=self.url(cityid)
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