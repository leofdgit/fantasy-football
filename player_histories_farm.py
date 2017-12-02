import json
import requests

other_db = requests.get(url='https://fantasy.premierleague.com/drf/bootstrap-static').json()

fixtures_infos = {}
for i in range(1,len(other_db['elements'])+1):
    other_db1 = requests.get(url='https://fantasy.premierleague.com/drf/element-summary/{}'.format(i)).json()
    fixtures_infos['{}'.format(i)] = other_db1

with open("player_fixtures.txt", "w") as g:
    g.write(json.dumps(fixtures_infos))


other_db1 = requests.get(url='https://fantasy.premierleague.com/drf/bootstrap-static').json()
with open("player_infos.txt", "w") as g:
    g.write(json.dumps(other_db1))
