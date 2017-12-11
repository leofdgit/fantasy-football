# Fantasy Football Project


####################

DESCRIPTION


This repository contains a collection of Python scripts which analyse data from Fantasy Premier League APIs. The aim of the project is to present interesting trends in the data and to use the data to create predictive tools that aid players of fantasy football accumulate more points.


####################

TABLE OF CONTENTS


1. Installation
2. User Guide
3. Improvements and Goals
4. Collaboration
5. License


####################

INSTALLATION


Download each of the Python files in the repository and place in the same directory. It is not necessary to download the text files, as running database_grabber.py will produce up-to-date versions of these files in directory from which it is run.


####################

USER GUIDE

o database_grabber.py scrapes the relevant APIs. Run this once per gameweek to ensure predictive information is up-to-date.

o ppg_swing_by_team.py computes how the points a player earns are affected by the opponent the player faces. The script takes the form of a function, whose arguments decide which positions are taken into account in the analysis. By default, running this script produces a graph showing points swings when players of each position are included in the analysis - script can be changed only include certain types of players. See in-script function descriptions.

o Captain_chooser.py and team_selector.py can be run in the command line (in same directory as data dumps) to get optimal team selections and captaincy choices. The input required is the ID of a team, which can be found in the address bar when viewing the team in a browser: .....https://fantasy.premierleague.com/a/team/'ID'/event/.....

o correlations_practice.py is a script that looks at player statistics, whose values are numerical, and tests which stat types most strongly correlate to a high points-per-game value. This is a tool that is only partially developed; correlation is just one method of judging similarity, and no work has yet been done to visualise the results.

####################

TO-DO AND GOALS

o Clean up correlations_practice code and do deeper analysis.

o Have captain_chooser and team_selector take into account player injuries and bans (problem: data not always available).

o Test effectiveness of prediction model and improve the model.

o Transfer suggestions: use points predictions to inform players how they can best use their transfers

o Long-term: create a Pandas DataFrame containing pre-computed information. This way, multiple program runs will take less time.


####################

COLLABORATION

If you find this project interesting and are interested in contributing then let me know - I am keen to work with others on this project.


####################

LICENSE

MIT.
