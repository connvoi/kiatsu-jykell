import urllib.parse
import requests
import time
import pandas as pd
import json


#クエリを組み立てる
def url(query, server, start,  rows):
    domain='http://'+ server +'/api/search.php?'
    query = {
            'kw': query,
            'fq_publishpossiblepc': '-0',
            'fq_adultpc': '00',
            'wt': 'json',
            'start': start,
            'rows': rows,
            'cli': 'yodobashi',
            }
    return domain + urllib.parse.urlencode(query)
      
def get(url):
    header={"User-Agent": "uk-crawl"}

    try: 
        r=requests.get(url, timeout=10, headers=header)
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
    
def doc(d, code, name):
    sep="\t"
    for i in d:
        print(code + sep + name + sep + i['itemcode'] + sep + i['prodname'] + sep + i['categorypc'] )



#diffがあったらTrue, なければFalse
def diffcheck(itema, itemb):
    anum = itema['response']['numFound']
    bnum = itemb['response']['numFound']
    #print(itemb)
    if anum != bnum:
        return True
    else :
        return False

#firstdiffpoint
def firstdiff(itema, itemb):
    lista=[]
    listb=[]
    for i in itema['response']['docs']:
        lista.append(i['itemcode'])

    for i in itemb['response']['docs']:
        listb.append(i['itemcode'])
    a=''.join(lista)
    b=''.join(listb)

    if a != b:
        return 1
    
    return 0


sep='\t'


df=pd.read_csv('../data/yodobashi/taglog_searchRanking4SEM.txt',sep="\t", dtype= { 0:int, 1:str}, names=['uu', 'query'])
c=0

for i,row in df[df['uu']>3].iterrows():
    query=row['query']
    uu=row['uu']
    aurl=url(row['query'], '172.22.205.4', '0', '48')
    burl=url(row['query'], '172.22.205.7', '0', '48')
    #print(aurl)
    #print(burl)
    itema=get(aurl)
    itemb=get(burl)    
    #diff=diffcheck(itema,itemb)
    fdiff=firstdiff(itema,itemb)
    # クエリ url1, url2 numfound1 numfound2のかたちにする
    if fdiff > 0:
        print(str(query)+sep + str(uu) + sep + str(aurl) + sep + str(burl)+ sep + str(itema['response']['numFound']) + sep + str(itemb['response']['numFound']) + sep + str(fdiff))

    if c % 4 == 0:
        time.sleep(1)
    c+=1
