import constants
import copy

def print_pleasantries():
    print("BASKETBALL TEAM STATS TOOL\n")
    print("---- MENU----\n")
    print("Here are your choices:")
    print("\t1) Display Team Stats")
    print("\t2) Quit\n")

def start_tool(teams,team_info):
    print_pleasantries()
    try:
        option = int(input("Enter an option from the above 1 or 2"))
        if option != 1 and option != 2:
            raise ValueError("Options should be 1 or 2")
        
        if option == 2:
            return
        elif option == 1:
            for i,v in enumerate(teams):
                print("{}) {}".format(i+1,v))
            option = int(input("Enter an option from the above as numbers"))
            if option < 1 or option > len(teams):
                raise ValueError("Options shoudl between the options")
            
            title = "Team: {} Stats".format(teams[option-1])
            print(title)
            print("-"*len(title))

            print("Total Players: {}".format(len(team_info[teams[option-1]])))
            print("\n")

            print("Players on Team:")
            print("\t{}".format(",".join([i['name'] for i in team_info[teams[option-1]]])))
            print("\n")

            guardians = []
            for team in team_info[teams[option-1]]:
                guardians.extend(team['guardians'])
            print("Guardians of the Team:")
            print("\t{}".format(",".join(guardians)))
            print("\n")

            # Average height of the team.
            heights = [int(i['height'].split(" ")[0]) for i in team_info[teams[option-1]]]
            avg_height = sum(heights) / len(team_info[teams[option-1]])
            print("The average height of the team is  : {}".format(avg_height))

            # inexperinced  players on the team :
            inexp = 0
            exp = 0
            for team in team_info[teams[option-1]]:
                if  team['experience'] == "NO":
                    inexp += 1
                else:
                    exp  += 1
            print("The number of experienced players are: {}".format(exp))
            print("The number of inexperienced players are: {}".format(inexp))
            # return
    except ValueError as err:
        print("Invalid input")
        if err:
            print(err)
        start_tool(teams,team_info)
    option = input("Do you want to see the stats again?? y or n")
    if option.lower() == 'y':
        start_tool(teams,team_info)
    elif option.lower() == 'n':
        print("Adios!!")
        return
    else:
        print("NeverMind!!!")
        return
if __name__ == "__main__":
    # do something
    teams = copy.copy(constants.TEAMS)
    players = copy.copy(constants.PLAYERS)
    yes_index = 0
    no_index = 0
    team_info = {}

    # creating a dictionary of teams.
    for team in teams:
        team_info[team] = []
    # balancing the team with experince
    for player in players:
        player['guardians'] = player['guardians'].split(" and ")
        if yes_index == len(teams):
            yes_index = 0
        if no_index == len(teams):
            no_index = 0
        if player['experience'] == "NO":
            team_info[teams[no_index]].append(player)
            no_index += 1
        if player['experience'] == "YES":
            team_info[teams[yes_index]].append(player)
            yes_index += 1
    start_tool(teams,team_info)