import nose
import sys
import sys,os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../')
import api

class TestApi:
    def setup(self):
        pass

    def test_url(self):
        url = api.url('11111')
        print(url)
