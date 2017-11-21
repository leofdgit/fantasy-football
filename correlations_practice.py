import json
import os
import requests
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st
import math

dbase = {} #one data dump
###
###
# Only download data once per week
###
###
'''
other_db = requests.get(url='https://fantasy.premierleague.com/drf/bootstrap-static').json()

with open("player_infos.txt", "w") as g:
    g.write(json.dumps(other_db))
'''
with open("player_infos.txt", "r") as f:
    dbase = json.load(f)

db_keys = [x for x in dbase.keys()]
#keys are next-event, last-entry-event, stats, elements, teams, next_event_fixtures, current-event, game-settings, element-types, phases, events, stats_options, total-players

###############
###############
###############
###############
###
###
# Only download data once per week
###
###
'''
other_db = requests.get(url='https://fantasy.premierleague.com/drf/element-summary/{}'.format(12)).json() #here 12 is the player number

with open("player_fixtures.txt", "w") as g:
    g.write(json.dumps(other_db))
'''

with open("player_fixtures.txt", "r") as h:
    other_db = json.load(h)
other_db_keys = [x for x in other_db.keys()]
#has keys explain, fixtures, history_summary, fixtures_summary, history, history_past

###############
###############
###############
###############





key_list = [] ### Create a list of keys - the values associated with keys will be used to get correlations
for key in dbase['elements'][0].keys():
    if (key == 'points_per_game'):
        continue
    if (type(dbase['elements'][0]['{}'.format(key)]) == bool):
        print(key)
        continue
    try:
        float(dbase['elements'][0]['{}'.format(key)])
        key_list.append(key)
    except ValueError:
        pass



print(key_list)

numerical_stats = [ [] for i in range(len(key_list)) ] #each list contains values of stat for each player, in correct order

for i in range(len(key_list)):
    for element in dbase['elements']:
        if element[key_list[i]] is None:
            element[key_list[i]] = 0.0
        numerical_stats[i].append(float(element[key_list[i]]))

#create PPG list:
player_ppgs = []
for i in range(len(dbase['elements'])):
#    if dbase['elements'][i]['minutes'] < 360:
#        continue                           #only include players who have played at least 30 mins per week. 360 = 12*30
    player_ppgs.append(float(dbase['elements'][i]['points_per_game']))


#create corr list:
corr_list = []
for stat_list in numerical_stats:
    corr, p = st.pearsonr(player_ppgs, stat_list)
    corr_list.append(corr)


corr_by_key = {}
for i in range(len(key_list)):
    if math.isnan(corr_list[i]): #remove troublesome entries
        continue
    corr_by_key['{}'.format(key_list[i])] = corr_list[i]

ordered_corrs = sorted(corr_by_key.items(), key=lambda x: x[1])

for name,value in ordered_corrs:
    print(name, value)
    print('')
#interesting: influence is a better predictor of total core than ict index? but maybe this doesn't take into account different types of player
#how would results change with restrictions on players included? for example those who play regularly

#idea: create list of lists, one for every key of the dict.
#store keys in a separate list
#for each element, check if the value associated with each key is a numerical value.
#   If yes, then append this to the appropriate list
#   If no, then skip this.
#For all non-empty lists, plot the numbers against ppg/check correlation.
#return the best indicators of high ppg.
