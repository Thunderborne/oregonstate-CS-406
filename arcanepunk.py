# Author: Alfred Nguyen
# Date: 04/27/2024
# Version: 0.0
# Course: CS 406 - Professor Van Londen
# Description: Arcane Punk is a text-rpg where the user go through a
# series of obstacles set in a futuristic-fantasy world. This file
# houses the infinite loop that runs the main program.

# Import functions

# Ascii Art

# Messages
goodbye_text = "Goodbye! Thank you for playing."

# Error Messages
name_error = "Name must be between 1-20 characters."
class_select_error = "Please enter a number corresponding to the three classes."

# Help Menus
class_help_menu = """
1. Hunter - A hunter starts with +2 Attack and +20 Health
2. Operative - An operative has +2 to all evasive options
3. Arcanist - An arcanist has +2 to all spell casting
"""

# Initial Options
# Level One
lvl_one_option1 = """
1. Attack
2. Run
3. Use offensive magic
4. Sneak closer
"""

lvl_one_option2 = """
1. Attack
2. Escape
3. Use healing magic
4. 
"""


# Main Loop
while True:

    # Turn counter
    total_turns = 0

    # Loop boolean to terminate loops
    name_loop = True
    user_class_loop = True
    level_one_loop = True
    level_two_loop = True
    level_three_loop = True
    level_four_loop = True
    level_five_loop = True

    # Store user stats
    user_stats = {
        'char_name': "",
        'char_classname': "",
        'char_class': 0,
        'char_health': 100,
        'char_attack': 10,
        'char_evade': 0,
        'char_magic': 0}

    # Store options
    option_stats = {
        'attack': 1,
        'sneak': 1,
        'o-magic': 1,
        'heal': 1,
        'talk': 1
    }


    # Prompts username
    while name_loop is True:
        player_name = input("Enter your name (1-20 characters): ")
        if len(player_name) < 1 or len(player_name) > 20:
            print(name_error)
            continue
        elif player_name.upper() == "QUIT" or player_name.upper() == "EXIT":
            print(goodbye_text)
            quit()
        else:
            user_stats['char_name'] = player_name
            print('Welcome to Arcane Punk, ' + user_stats['char_name'])
            name_loop = False

    # Prompts user class
    while user_class_loop is True:
        player_class_selection = input("Select your class (enter number or type HELP): \n"
                                       "1. Hunter \n"
                                       "2. Operative \n"
                                       "3. Arcanist \n"
                                       + user_stats['char_name'] + " selects: ")
        if player_class_selection.upper() == "HELP":
            print(class_help_menu)
            continue
        elif player_class_selection.upper() == "QUIT" or player_class_selection.upper() == "EXIT":
            print(goodbye_text)
            quit()
        elif player_class_selection.isnumeric() is False:
            print(class_select_error)
            continue
        elif int(player_class_selection) < 1 or int(player_class_selection) > 3:
            print(class_select_error)
            continue
        else:
            user_stats['char_class'] = int(player_class_selection)
            # Initialize the class stats
            if user_stats['char_class'] == 1:
                user_stats['char_classname'] = "Hunter"
                user_stats['char_health'] = 120
                user_stats['char_attack'] = 12
            if user_stats['char_class'] == 2:
                user_stats['char_classname'] = "Operative"
                user_stats['char_evade'] = 2
            if user_stats['char_class'] == 3:
                user_stats['char_classname'] = "Arcanist"
                user_stats['char_magic'] = 2
            print(user_stats['char_name'] + " has chosen the " + user_stats['char_classname'] + ".")
            print(user_stats['char_name'] + "'s stats are: \n")
            print(user_stats)
            user_class_loop = False

    # Level One of Tower Loop
    """
    TODO: Fill in the story scenario in UI phase
    TODO: Call the pipe for stats and dice roll
    """
    level_one_turns = 0
    level_one_win = 0
    while level_one_loop is True:
        print("Scenario 1: You see a dragon. \n")
        print("What do you do? \n")
        lvl_one_select = input("1. Attack \n"
                               "2. Run \n"
                               "3. Use offensive magic \n"
                               "4. Sneak closer \n" +
                               user_stats['char_name'] + " selects: ")
        if lvl_one_select.upper() == "QUIT" or player_class_selection.upper() == "EXIT":
            print(goodbye_text)
            quit()

        elif level_one_win == 1:
            level_one_loop = False



