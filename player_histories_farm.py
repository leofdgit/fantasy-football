import json
import requests

other_db = requests.get(url='https://fantasy.premierleague.com/drf/bootstrap-static').json()
print(len(other_db['elements']))

fixtures_infos = {}
for i in range(1,len(other_db['elements'])+1):
    print(i)
    other_db1 = requests.get(url='https://fantasy.premierleague.com/drf/element-summary/{}'.format(i)).json()
    fixtures_infos['{}'.format(i)] = other_db1

with open("player_fixtures.txt", "w") as g:
    g.write(json.dumps(fixtures_infos))
