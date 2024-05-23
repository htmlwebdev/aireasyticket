import json
main=[]
data=dict(json.load(open('airports.json')))
for key,value in data.items():
    if value['iata']!="":
        value['objectID']=value['iata']
        main.append(value)

with open('airports_filtered.json','w') as f:
    json.dump(main,f,indent=4)