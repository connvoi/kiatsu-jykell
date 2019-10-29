from nose.tools import * 
import sys
import sys,os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../')
import api

class TestApi:
    def setup(self):
        pass

    def test_url(self):
        url = api.Api().url('11111')
        eq_(url, 'https://api.openweathermap.org/data/2.5/forecast?id=11111&mode=json&units=metric&lang=ja&APPID=adc240180d6c352135ef91540c488134')

    def test_get(self):
        data = api.Api().get('1850147')
        eq_(data['city']['name'], 'Tokyo')