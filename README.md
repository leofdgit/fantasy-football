# fantasy-football

To use: download all files and place in single directory.

The two .txt files are data dumps from the official website's APIs.
###To Python files, ensure that the two .txt files are in the same directory as Python files.


correlations_practice.py looks at stats whose values are numerical and tests which ones most strongly correlate to a high points per game value.

ppg_swing_by_team.py computes how points hauls are affected by opponent. The script takes the form of a function, whose arguments decide which positions are taken into account in the analysis.


database_grabber.py scrapes the relevant API for info on players' previous games. (Run this once per gameweek to ensure predictive information is up-to-date).

Captain_chooser.py and team_selector.py can be run in the command line (in same directory as data dumps) to get optimal team selections and captaincy choices based on model's analysis.


####################
TO-DO LIST
####################

o Update graphs on correlations_practice

o Have captain_chooser and team_selector take into account player injuries and bans (problem: data not always available)

o Test effectiveness of prediction model and improve the model

o Transfer suggestions: use points predictions to inform players how they can best use their transfers



