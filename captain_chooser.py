import numpy as np
import requests
import json
import ppg_swing_by_team as ppg


#Open the two data sources.
with open("player_infos.txt", "r") as f:
    dbase = json.load(f)

with open("player_fixtures.txt", "r") as h:
    other_db = json.load(h)

def ppp_round(id_no): #player points predictor for next round's matches
    id_no = id_no -1
    player_ppg = float(dbase['elements'][id_no]['points_per_game'])
    #add swing value: first look at player's type, get opponent id and add corresponding swing value
    p_type = dbase['elements'][id_no]['element_type']
    swings = dict(ppg.point_swings(p_type))

    if other_db['282']['fixtures_summary'][0]['is_home']:
        opp_team_id = other_db['282']['fixtures_summary'][0]['team_a']
    else:
        opp_team_id = other_db['282']['fixtures_summary'][0]['team_h']
    co = ppg.converter()
    opponent_team_name = co['{}'.format(opp_team_id)]
    swing_val = swings[opponent_team_name]
    player_ppg += swing_val
    return (player_ppg)

def cap_chooser(team_id):
    '''
    Input team id and output player predicter to get most points following gameweek.
    '''
    team_info = requests.get(url='https://fantasy.premierleague.com/drf/entry/{}/event/14/picks'.format(team_id)).json() #change 14 to last gw
    ids = np.array([i['element'] for i in team_info['picks']])
    pred_scores = np.array([ppp_round(k) for k in ids])
    cap_choice = ids[np.argmax(pred_scores)]

    return cap_choice

if __name__ == "__main__":
    while True:
        try:
            team_id = int(input("Please enter your team id number: "))
        except ValueError:
            print("I didn't understand that. Try again.")
            print()
            continue
        else:
            break
    print("You should choose", dbase['elements'][cap_chooser(team_id)-1]['web_name'], "to be your captain.")
