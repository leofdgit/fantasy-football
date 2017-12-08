import json
import os
import requests
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st
import math



with open("player_infos.txt", "r") as f:
    dbase = json.load(f)


with open("player_fixtures.txt", "r") as h:
    other_db = json.load(h)

###########################################################

#cycle through each player and note their ppg.
#create list of tuples, one for each team.
#for each player's past matches, add tuple of ppg and score against opponent to appropriate list of tuples
#compute average swing in ppg using all tuples

###########################################################


#id-to-team-name conversion - used later
#id-to-team-name conversion - used later
def converter():
    return ({'1':'Arsenal', '2':'Bournemouth', '3': 'Brighton', '4':'Burnley',
'5':'Chelsea', '6':'Crystal Palace', '7':'Everton', '8':'Huddersfield',
'9': 'Leicester', '10':'Liverpool', '11':'Manchester City', '12':'Manchester United',
'13':'Newcastle', '14':'Southampton','15':'Spurs','16':'Stoke','17':'Swansea',
'18':'Watford','19':'West Brom','20':'West Ham'})

###########################################################



def point_swings(*args):  #optional arguments are the positions that will be included in the analysis. If no args given then consider all players.
    '''
    accepts optional args 1,2,3 and 4, where:
    1 corresponds to goalkeepers.
    2 corresponds to defenders.
    3 corresponds to midfielders.
    4 corresponds to attackers.
    Returns a list of tuples (team, point swing).
    '''
    if args:
        arglist = list(args)
    else:
        arglist = [1,2,3,4]
    #create 20 lists of tuples, one for each team. The tuples will contain players' ppg and score against said team.
    score_tuples = [ [] for i in range(20)]

    for i in range(1, len(dbase['elements'])+1):
        ppg = dbase['elements'][i-1]['points_per_game']
        for j in range(len(other_db['{}'.format(i)]['history'])):
            if (other_db['{}'.format(i)]['history'][j]['minutes'] and  dbase['elements'][i-1]['element_type'] in arglist)> 0:
                opponent_id = other_db['{}'.format(i)]['history'][j]['opponent_team']
                points_against_opponent = other_db['{}'.format(i)]['history'][j]['total_points']
                tup = (float(ppg), points_against_opponent)
                score_tuples[opponent_id-1].append(tup)
    #score_tuples now contains lists of tuples so that:
    #       if a player played at least 1 minute against an opponent then the associated tuple is in the correct list

    average_swing = []
    for k in range(len(score_tuples)):
        swings_list = []
        for m in range(len(score_tuples[k])):
            swing = score_tuples[k][m][1] - score_tuples[k][m][0]
            swings_list.append(swing)
        avg_swg = np.mean(swings_list)
        average_swing.append(avg_swg)
    co = converter()
    average_swing_with_ids = [(co['{}'.format(i+1)], average_swing[i]) for i in range(len(average_swing))]
    average_swing_with_ids.sort(key=lambda x: x[1])

    #    WHAT IS HAPPENING HERE?
    # create a list of tuples for average swing, so that we can more clearly see results
    # positive average swing implies the team is easy to play against
    # list sorted from hardest to easiest opponents
    return average_swing_with_ids


def graph_pswings(*args):
    '''
    accepts optional args 1,2,3 and 4, where:
    1 corresponds to goalkeepers.
    2 corresponds to defenders.
    3 corresponds to midfielders.
    4 corresponds to attackers.
    Prints a graph of point swings.
    '''
    if args:
        arglist = [arg for arg in args]
    else:
        arglist = [1,2,3,4]
    tuples = point_swings(*args)
    average_swing = [i[1] for i in tuples]
    #plotting the swings on an easy-to-interpret axis.
    val = 0 # this is the value where you want the data to appear on the y-axis.
    plt.plot(np.zeros_like(average_swing) + val, average_swing,  'ro')
    plt.xticks([-1,0,1])
    plt.yticks(np.arange(round(min(average_swing),1)-0.3, round(max(average_swing)+0.35), 0.2))
    plt.ylabel('Average Points Swing')
    plt.title('Average Points Swing by Opponent - Position(s) {}'.format(arglist))
    #next, annotating the points
    alternating_annos = [0.3*(-1)**i for i in range(20)] #so that labels do not overlap
    for i in range(20):
        plt.annotate(tuples[i][0], xy = (alternating_annos[i], tuples[i][1]))
    plt.show()

###TO-DO: FIX GRAPH LABELS OVERLAPPING
