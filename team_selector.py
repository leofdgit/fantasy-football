import json
import requests
import numpy as np
import ppg_swing_by_team as ppg
import captain_chooser as cc

#Open the two data sources.
with open("player_infos.txt", "r") as f:
    dbase = json.load(f)

with open("player_fixtures.txt", "r") as h:
    other_db = json.load(h)

def team_points(team_id):
    '''
    Input team id and output player predicter to get most points following gameweek.
    '''
    team_info = requests.get(url='https://fantasy.premierleague.com/drf/entry/{}/event/14/picks'.format(team_id)).json()
    ids = np.array([i['element'] for i in team_info['picks']])
    pred_scores = [(cc.ppp_round(int(k)), int(k), dbase['elements'][k-1]['web_name'], dbase['elements'][k-1]['element_type']) for k in ids]
    total = np.round(sum([k[0] for k in pred_scores]),1)
    pred_scores.sort(key = lambda x: x[0], reverse = True)
    return pred_scores, total

def points_by_formation(team_id, formation):
    '''
    Formation should be a list, e.g. [1,4,4,2].
    Returns two arguments: 1) a list of tuples giving the expected points for the players to be picked
                           2) the sum of the points of the picks
    '''
    tm_pts = team_points(team_id)[0]
    filled_spots = np.array([0,0,0,0])
    picks = []
    for i in range(len(tm_pts)):
        posi=tm_pts[i][3]-1
        if (filled_spots[posi] == formation[posi]):
            continue
        picks.append(tm_pts[i])
        filled_spots[posi] += 1
    return picks, sum(x[0] for x in picks) #returns the picks to make, and total points expected doing this

def team_picker(team_id):
    '''
    Runs points_by_formation on each formation and outputs the optimal formation, picks with this
    formation and predicted points (in a 3-tuple).
    '''
    tm_pts = team_points(team_id)[0]
    validFormations = np.array([[1,3,5,2], [1,3,4,3], [1,4,5,1], [1,4,4,2], [1,5,4,1], [1,5,3,2], [1,5,2,3]])
    pts_prediction = [(points_by_formation(team_id, f)[0], f, points_by_formation(team_id, f)[1]) for f in validFormations]
    pts_prediction.sort(key=lambda x: x[2], reverse = True)
    return pts_prediction[0] #returns optimal picks, formation and points expteced in a list

if __name__ == '__main__':
    while True:
        try:
            team_id = int(input("Please enter your team id number: "))
        except ValueError:
            print("I didn't understand that. Try again.")
            print()
            continue
        else:
            break
    print("You should choose the following team for this week's matches:")
    picks = team_picker(team_id)
    for i in picks[0]:
        print(i[2], i[0])
        print()
    print('The total points expected from this team (neglecting captaincy choice) is:', round(picks[2],0))
