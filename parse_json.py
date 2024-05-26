import json
main={}
data=json.load(open('airports_filtered.json'))
for airport in data:
        main[airport['iata']]= {"name":airport['name'],"city":airport['city'],"state":airport['state']}
with open('airports_shortened.json','w') as f:
    json.dump(main,f,indent=4)