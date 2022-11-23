from constants import PLAYERS
from constants import TEAMS
from statistics import mean
import random

cleaned_players_data = []
player_list_of_tuple = []

shorty_and_funny_list = []
tall_and_handsome_list = []
people_who_went_to_university_of_life = []
good_luck_finding_a_job_without_two_billion_years_experience = []

team_A = []
team_B = []
team_C = []
random_generated_team = []

def PLAYERS_data_redo():
    for player_dict in PLAYERS:
        looped_dict = {}
        looped_dict["name"] = player_dict["name"]
        if " and " in player_dict["guardians"]:
            guardians_tuple = tuple(player_dict["guardians"].split(" and "))
            looped_dict["guardians"] = guardians_tuple
        else:
            looped_dict["guardians"] = player_dict["guardians"]
        if player_dict["experience"] == "NO":
            looped_dict["experience"] = False
        else:
            looped_dict["experience"] = True
        digits = int(player_dict["height"][0:2])
        looped_dict["height"] = digits
        cleaned_players_data.append(looped_dict)
    return cleaned_players_data

def tuple_player_info():
    for player_info in cleaned_players_data:
        player_tuple = (player_info["name"], player_info["height"], player_info["experience"])
        player_list_of_tuple.append(player_tuple)
    return player_list_of_tuple

def average_height(list_of_players_to_collect_height_from):
    list_of_height = []
    for player in list_of_players_to_collect_height_from:
        list_of_height.append(player["height"])
    avg_height = float(mean(list_of_height))
    return avg_height

def separating_people_by_height():
    for player in cleaned_players_data:
        if player["height"] <= 42:
            shorty_and_funny_list.append(player)
        else:
            tall_and_handsome_list.append(player)
    return shorty_and_funny_list, tall_and_handsome_list

def experienced_or_not_you_are_hired():
    for player in cleaned_players_data:
        if player["experience"] == True:
            people_who_went_to_university_of_life.append(player)
        else:    
            good_luck_finding_a_job_without_two_billion_years_experience.append(player)
    return people_who_went_to_university_of_life, good_luck_finding_a_job_without_two_billion_years_experience

def create_the_three_teams():
    list_of_numbers = []
    while len(list_of_numbers) < 9:
        random_number = random.randrange(0,9)
        if random_number not in list_of_numbers:
            list_of_numbers.append(random_number)
    for number in list_of_numbers:
        if len(team_A)<3:
            team_A.append(people_who_went_to_university_of_life[number])
        elif len(team_B)<3:
            team_B.append(people_who_went_to_university_of_life[number])
        else:
            team_C.append(people_who_went_to_university_of_life[number])
    for number in list_of_numbers:
        if len(team_A)<6:
            team_A.append(good_luck_finding_a_job_without_two_billion_years_experience[number])
        elif len(team_B)<6:
            team_B.append(good_luck_finding_a_job_without_two_billion_years_experience[number])
        else:
            team_C.append(good_luck_finding_a_job_without_two_billion_years_experience[number])       
    return team_A, team_B, team_C

def reset_teams():
    global team_A
    global team_B
    global team_C
    team_A = []
    team_B = []
    team_C = []
    return team_A, team_B, team_C

def print_stats(chosen_team_name, team_list_of_players):
    experienced_count = 0
    not_experienced_count = 0
    list_of_names = []
    list_of_not_galaxy_guardians = []
    for player in sorted(team_list_of_players, key=lambda x: x["height"]):
        if player["experience"] == True:
            experienced_count += 1
        else:
            not_experienced_count += 1
        list_of_names.append(player["name"])
        if type(player["guardians"]) == tuple:
            if player["guardians"][0] not in list_of_not_galaxy_guardians:
                list_of_not_galaxy_guardians.append(player["guardians"][0])
            if player["guardians"][1] not in list_of_not_galaxy_guardians:
                list_of_not_galaxy_guardians.append(player["guardians"][1])
        elif player["guardians"] not in list_of_not_galaxy_guardians:
            list_of_not_galaxy_guardians.append(player["guardians"])
    print(f"Team: {chosen_team_name}")
    print(f"Total players: {len(team_list_of_players)}")
    print(f"Experienced ones count: {experienced_count}")
    print(f"Not experienced ones count: {not_experienced_count}")
    print(f"Average height: {int(average_height(team_list_of_players))}")
    players_for_print = ", ".join(list_of_names)
    print(f"\nPlayers: {players_for_print}")
    guardians_for_print = ", ".join(list_of_not_galaxy_guardians)
    print(f"\nGuardians: {guardians_for_print}\n")

def random_team_generator(chosen_team):
    print(f"\nTeam: {chosen_team}")
    while True:
        team = []
        list_of_heights = []
        list_of_names = []
        list_of_guardians = []
        experienced_count = 0
        not_experienced_count = 0
        while len(team)<3:
            random_picker = random.randrange(0,9)
            if shorty_and_funny_list[random_picker] not in team:
                team.append(shorty_and_funny_list[random_picker])
        while len(team)<6:
            random_picker = random.randrange(0,9)
            if tall_and_handsome_list[random_picker] not in team:
                team.append(tall_and_handsome_list[random_picker])
        for player in team:
            list_of_heights.append(player["height"])
        for player in team:
            if player["experience"] == True:
                experienced_count += 1
            else:
                not_experienced_count += 1
        for names in team:
            list_of_names.append(names["name"])
        for guardians in team:
            if type(guardians["guardians"]) == tuple:
                if guardians["guardians"][0] not in list_of_guardians:
                    list_of_guardians.append(guardians["guardians"][0])
                if guardians["guardians"][1] not in list_of_guardians:
                    list_of_guardians.append(guardians["guardians"][1])
            elif guardians["guardians"] not in list_of_guardians:
                list_of_guardians.append(guardians["guardians"])
        if experienced_count == not_experienced_count:
            break
        else:
            continue
    print(f"Total players: {len(team)}")
    print(f"Experienced: {experienced_count}")
    print(f"Not experienced: {not_experienced_count}")
    print(f"Average height: {int(mean(list_of_heights))}")
    players_for_print = ", ".join(list_of_names)
    print(f"\nPlayers: {players_for_print}")
    guardians_for_print = ", ".join(list_of_guardians)
    print(f"\nGuardians: {guardians_for_print}")
    return team

def console():
    print("\nWelcome!")
    while True:
        print("\nLet's generate some teams:\na)Random generator\nb)Select a team\nc)Exit\n")
        answer = input(" > ")
        if "c" in answer.lower() or "exit" in answer.lower():
            exit()
        elif "a" in answer.lower() or "random" in answer.lower():
            random_team_generator(TEAMS[random.randrange(0,3)])
        elif "b" in answer.lower() or "select" in answer.lower():
            create_the_three_teams()
            while True:
                print("\nChose a Team or press any other key to go back:\n1)Panthers\n2)Bandits\n3)Warriors\n4)Reset Teams\n")
                chosed_team = input(" > ")
                if "1" in chosed_team or chosed_team.lower() == "panthers":
                    print_stats(TEAMS[0], team_A)
                elif "2" in chosed_team or chosed_team.lower() == "bandits":
                    print_stats(TEAMS[1], team_B)
                elif "3" in chosed_team or chosed_team.lower() == "warriors":
                    print_stats(TEAMS[2], team_C)
                elif "4" in chosed_team or "reset" in chosed_team.lower():
                    reset_teams()
                    create_the_three_teams()
                else:
                    break
        else:
            print("Sorry, what?")
            continue

def app_loop():
    PLAYERS_data_redo()
    tuple_player_info()
    separating_people_by_height()
    experienced_or_not_you_are_hired()
    while True:
        console()

if __name__ == "__main__":
    app_loop()