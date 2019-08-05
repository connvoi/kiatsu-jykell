import urllib.parse
import requests

r=requests.get('https://www.yahoo.co.jp', timeout=10)
print(r.text)