from nose.tools import * 
import sys
import sys,os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../')
import parse
import api

class TestParse:
    def setup(self):
        pass


    def test_parse(self):
        data = api.Api().get('1850147')
        json = parse.Parse().parse(data)
        print(json)