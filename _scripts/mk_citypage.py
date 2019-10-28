import pandas as pd

fh= open('template.md', 'r')

org=fh.read()
df = pd.read_csv('../_data/citylist.csv')

for i,row in df.iterrows():
    txt=org
    with open('../city/'+row['nameid']+'.html', mode='w') as f:
        txt=txt.replace("###cityname###", row['name'])
        f.write(txt.replace('###cityid###', row['nameid']))
 
       

