Author: Tom Zheng U98418371 


To Compile the java files:

Do:
javac *.java

To run the program:
Do:

java P1



The following are the commands:

add_coach ID SEASON FIRST_NAME LAST_NAME SEASON_WIN SEASON_LOSS PLAYOFF_WIN PLAYOFF_LOSS TEAM - add new coach data

add_team ID LOCATION NAME LEAGUE - add a new team

print_coaches - print a listing of all coaches

print_teams - print a listing of all teams

remove_coach coach_ID - remove an existing record in coaches by ID

remove_team team_ID - remove an existing record in teams by ID

coaches_by_name NAME - list info of coaches with the specified FIRST NAME

teams_by_city_league CITY - list the teams in the specified CITY and specific LEAGUE

load_coach FILENAME - bulk load of coach info from a file

load_team FILENAME - bulk load of team info from a file

best_coach SEASON - print the name of the coach with the most netwins in a specified SEASON

search_coaches field=VALUE - print the name of the coach satisfying the specified conditions

exit - quit the program
