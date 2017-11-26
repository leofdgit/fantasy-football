import json
import os
import requests
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st
import math

###
###
# Only download data once per week
###
###

dbase = {}
'''
other_db = requests.get(url='https://fantasy.premierleague.com/drf/bootstrap-static').json()

with open("player_infos.txt", "w") as g:
    g.write(json.dumps(other_db))
'''
with open("player_infos.txt", "r") as f:
    dbase = json.load(f)

db_keys = [x for x in dbase.keys()]

with open("player_fixtures.txt", "r") as h:
    other_db = json.load(h)

###########################################################

#cycle through each player and note their ppg.
#create list of tuples, one for each team.
#for each player's past matches, add tuple of ppg and score against opponent to appropriate list of tuples
#compute average swing in ppg using all tuples

###########################################################

#print(other_db['2']['history'][7]['total_points']) #gives score in a particular round
#print(other_db['2']['history'][7]['minutes']) #minutes played in a round
#print(other_db['history'][2]['opponent_team']) #gives opponet's team id (1-20)
#print((other_db['4']['history']))
#print((dbase['elements'][0]))

#create 20 lists of tuples, one for each team. The tuples will contain players' ppg and score against said team.
score_tuples = [ [] for i in range(20)]

for i in range(1, len(dbase['elements'])+1):
    ppg = dbase['elements'][i-1]['points_per_game']
    for j in range(len(other_db['{}'.format(i)]['history'])):
        if other_db['{}'.format(i)]['history'][j]['minutes'] > 0:
            opponent_id = other_db['{}'.format(i)]['history'][j]['opponent_team']
            points_against_opponent = other_db['{}'.format(i)]['history'][j]['total_points']
            tup = (float(ppg), points_against_opponent)
            score_tuples[opponent_id-1].append(tup)
#score_tuples now contains lists of tuples so that:
#       if a player played at least 1 minute against an opponent then the associated tuple is in the correct list


#compute average swing for each team.
#the ith elements in the average_swing list corresponds to the ith team, by id

average_swing = []
for k in range(len(score_tuples)):
    swings_list = []
    for m in range(len(score_tuples[k])):
        swing = score_tuples[k][m][1] - score_tuples[k][m][0]
        swings_list.append(swing)
    avg_swg = np.mean(swings_list)
    average_swing.append(avg_swg)


#id-to-team-name conversion:
converter = {'1':'Arsenal', '2':'Bournemouth', '3': 'Brighton', '4':'Burnley',
'5':'Chelsea', '6':'Crystal_Palace', '7':'Everton', '8':'Huddersfield',
'9': 'Leicester', '10':'Liverpool', '11':'Manchester City', '12':'Manchester United',
'13':'Newcastle', '14':'Southampton','15':'Spurs','16':'Stoke','17':'Swansea',
'18':'Watford','19':'West Brom','20':'West Ham'}

#    WHAT IS HAPPENING HERE?
# create a list of tuples for average swing, so that we can more clearly see results
# positive average swing implies the team is easy to play against
# list sorted from hardest to easiest opponents

average_swing_with_ids = [(converter['{}'.format(i+1)], average_swing[i]) for i in range(len(average_swing))]
average_swing_with_ids.sort(key=lambda x: x[1])
print(average_swing_with_ids)


#plotting the swings on an easy-to-interpret axis.
val = 0 # this is the value where you want the data to appear on the y-axis.
plt.plot(np.zeros_like(average_swing) + val, average_swing,  'ro')
plt.xticks([-1,0,1])
plt.yticks(np.arange(-1.4, 1.2, 0.2))
plt.ylabel('Average Points Swing')
plt.title('Average Points Swing by Opponent')
#next, annotating the points
alternating_annos = [0.2*(-1)**i for i in range(20)] #so that labels do not overlap
for i in range(20):
    plt.annotate(average_swing_with_ids[i][0], xy = (alternating_annos[i], average_swing_with_ids[i][1]))
plt.show()
