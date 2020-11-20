"""
Python Web Development Techdegree
Project 2 - Basketball Stats Tool
--------------------------------
"""

import constants
import copy
import sys


teams = copy.deepcopy(constants.TEAMS)
players = copy.deepcopy(constants.PLAYERS)
player_info = []
bandits = []
panthers = []
warriors = []
team_count = [bandits, panthers, warriors]



# Data cleaning function does the following:
# converts height to an integer
# converts experience Yes/No to True/False
def clean_data():
    for player in players:
        height = player['height'].split(" ")
        player['height'] = int(height[0])
        if player['experience'] == 'YES':
            player['experience'] = True
        else:
            player['experience'] = False
        player_info.append(player)



# Team balancing function does the following:
# balances total players across the three available teams
def balance_teams():
    num_players_team = len(players)/len(teams)
    for team in team_count:
        while len(team) < num_players_team:
            team.append(player_info.pop())


# The main function prompts the user for action to navigate the tool
def main():
    print("\nBASKETBALL TEAM STATS TOOL")
    print("\n---- MENU----")
    print("\nHere are your choices:")
    print("1) Display Team Stats")
    print("2) Quit")
    while True:
        try:
            menu_option = int(input("\nEnter an option > "))
        except ValueError:
            print("That is not an option. Please try again.")
        else:

            if menu_option == 1:
                for index, team in enumerate(teams, 1):
                    print(f'{index}) {team}')
                while True:
                    try:
                        team_num = int(input("\nEnter an option > "))
                    except ValueError:
                        print("That is not an option. Please try again.")
                    else:
                        if team_num == 1 or team_num == 2 or team_num == 3:
                            team_name = str(teams[team_num - 1])
                            selected_team = team_count[team_num - 1]
                            name_list = [player['name'] for player in selected_team]
                            print("\nTeam: " + team_name + " Stats")
                            print("--------------------")
                            print("Total players: ", len(selected_team))
                            print("\nPlayers on Team:")
                            print(', '.join(name_list))
                            continue_option = input("\nPress ENTER to return to Main Menu ")
                            if continue_option == '':
                                main()
                            else:
                                print("Thank you, come again!\n")
            elif menu_option == 2:
                print("Thank you, come again!\n")
                sys.exit()
            else:
                print("That is not an option. Please try again.")




if __name__ == '__main__':
    clean_data()
    balance_teams()
    main()