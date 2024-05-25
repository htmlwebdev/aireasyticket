import json
main={}
data=json.load(open('airlines.json'))
for airline in data:
    if (airline['icao'] != 'N/A' and airline['iata'] != 'N/A'
            and airline['iata'] != '-' and airline['icao'] != '-'
            and airline['iata'] != '' and airline['icao'] != ''
            and airline['iata'] != '\\N' and airline['icao'] != '\\N'):
        main[airline['iata']]=airline['icao']

with open('airline_codes.json','w') as f:
    json.dump(main,f,indent=4)