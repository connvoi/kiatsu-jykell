#%%
import pandas as pd 
df = pd.read_csv('citylist.jp.tsv',sep="\t")
#df.sort_values(by=['lat', 'lon'], ascending=True).to_csv('citylist.jp.sorted.tsv', sep="\t")

df = df[
    (df['name'].str.contains('-ken')) |
    (df['name'].str.contains('Hokkai')) |
    (df['name'].str.contains('Tokyo'))
].sort_values(by=['lat', 'lon'], ascending=False)

df.loc[:,['name']].to_csv('ken.namelist.tsv', sep="\t", index=False)


#%%
import json
raw = open('/Users/kyagi/Downloads/city.list.json', 'r') 
json = json.load(raw)

f=open('citylist.jp.tsv', 'w')
sep="\t"
f.write('name'+sep+'cityid'+sep+ 'lat' +sep+ 'lon' +sep +'google'+"\n")
for i in json:
    if i['country'] =='JP':
        f.write(i['name']+sep+str(i['id'])+sep+ str(i['coord']['lat'])+sep+ str(i['coord']['lon']) +sep +'https://www.google.co.jp/maps/@'+ str(i['coord']['lat'])+','+str(i['coord']['lon']) +',15z'+"\n")
f.close()