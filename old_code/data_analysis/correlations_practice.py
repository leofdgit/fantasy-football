import json
import os
import requests
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import scipy.stats as st
import math


with open("player_infos.txt", "r") as f:
    dbase = json.load(f) #data dump


with open("player_fixtures.txt", "r") as h:
    other_db = json.load(h) #second data dump




key_list = [] ### Create a list of keys - the values associated with keys will be used to get correlations
              ### The keys we choose must have values that are numerical in order to compute correlations (later: correlation but with discrete variables, e.g. logistic regression)
for key in dbase['elements'][0].keys():
    if (key == 'points_per_game' or key == 'squad_number' or key == 'chance_of_playing_this_round' or key == 'chance_of_playing_next_round'
    or key == 'loans_in' or key == 'loans_out' or key == 'loaned_out' or key == 'loaned_in' or key == 'ea_index'): #troublesome keys with 'bad' data
        continue
    if (type(dbase['elements'][0]['{}'.format(key)]) == bool):
        continue
    try:
        float(dbase['elements'][0]['{}'.format(key)])
        key_list.append(key)
    except ValueError:
        pass



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


just_vals = []
just_labs = []
for label,value in ordered_corrs:
    if value > 0.7:
        just_vals.append(value)
        just_labs.append(label)



val = 0 # this is the value where you want the data to appear on the y-axis.
plt.plot(np.zeros_like(just_vals) + val, just_vals,  'ro')
plt.xticks([-1,0,1])
plt.yticks(np.arange(round(min(just_vals),1)-0.05, round(max(just_vals)+0.5), 0.2))
plt.ylabel('Correlations to PPG - Top Indicators of Success')
plt.title('Correlations of PPG to Other Data')
#next, annotating the points

alternating_annos = [0.3*(-1)**i for i in range(len(just_vals))] #so that labels do not overlap
for i in range(len(just_vals)):
    plt.annotate(just_labs[i], xy = (alternating_annos[i], just_vals[i]))

plt.show()
#interesting: influence is a better predictor of total core than ict index? but maybe this doesn't take into account different types of player
#how would results change with restrictions on players included? for example those who play regularly

#idea: create list of lists, one for every key of the dict.
#store keys in a separate list
#for each element, check if the value associated with each key is a numerical value.
#   If yes, then append this to the appropriate list
#   If no, then skip this.
#For all non-empty lists, plot the numbers against ppg/check correlation.
#return the best indicators of high ppg.
