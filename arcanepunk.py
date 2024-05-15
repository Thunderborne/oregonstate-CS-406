# Author: Alfred Nguyen
# Date: 04/27/2024
# Version: 0.0
# Course: CS 406 - Professor Van Londen
# Description: Arcane Punk is a text-rpg where the user go through a
# series of obstacles set in a futuristic-fantasy world. This file
# houses the infinite loop that runs the main program.

# Import functions
import time
import random

# Ascii Art

# Messages
goodbye_text = "Goodbye! Thank you for playing."

# Error Messages
name_error = "Name must be between 1-20 characters."
class_select_error = "Please enter a number corresponding to the three classes."
selection_error = "Please select a number corresponding to the option."

# Help Menus
class_help_menu = """
1. Hunter - A hunter starts with +2 Attack and +20 Health
2. Operative - An operative has +2 to all sneak/evasive options
3. Arcanist - An arcanist has +2 to all spell casting
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
        'char_attack': 0,
        'char_evade': 0,
        'char_magic': 0
    }

    # Store options
    # Resets to 1 per level
    option_stats = {
        'attack': 1,
        'sneak': 1,
        'magic': 1,
        'heal': 1,
        'talk': 1
    }

    # Level One Data
    # -------------------------------------------------------------

    # Counters for Level One
    level_one_turns = 0
    level_one_win = 0
    enemy1_health = 100

    # Level One Dragon Attack
    def dragon_attack():
        """
        Function rolls dice for the dragon's attack on the user.
        :return: None.
        """
        # Sleep method used for text pauses
        time.sleep(2)
        print("The Dragon seethes with rage and attacks " + user_stats['char_name'] + "!")
        enemy_attack_value = random.randint(0, 10)
        time.sleep(2)
        enemy_attack_txt = f" takes {enemy_attack_value} damage."
        print(user_stats['char_name'] + enemy_attack_txt)
        user_stats['char_health'] -= enemy_attack_value
        return

    # Level One switch based on user selection
    def level_one_cases(user_selection, enemy1_health):
        """
        Function acts a switch statement for the level one encounter. This function
        is called in a loop, which terminates when enemy1_health reaches below 1.
        :param user_selection: User choice
        :param enemy1_health: value of current Dragon's health
        :return: enemy1_health
        """
        # User selects Attack
        if user_selection == 1:
            print(user_stats['char_name'] + " attacks the Dragon!")
            attack_value = random.randint(0, 16)
            time.sleep(2)  # Added sleep method for a dramatic pause
            if attack_value == 0:
                print(user_stats['char_name'] + " misses!")
            else:
                attack_value += user_stats['char_attack']
                attack_txt = f" attacks the Dragon for {attack_value}!"
                print(user_stats['char_name'] + attack_txt)
            enemy1_health -= attack_value
            if enemy1_health < 0:
                return enemy1_health
            # Call function so the dragon can return an attack
            dragon_attack()
            return enemy1_health
        # User selects Run
        elif user_selection == 2:
            print(user_stats['char_name'] + " attempts to run away.")
            run_attempt_value = random.randint(0, 20)
            run_attempt_value += user_stats['char_evade']
            time.sleep(2)
            if run_attempt_value >= 18:
                print(user_stats['char_name'] + " has successfully escaped the Dragon!")
                enemy1_health = 0
                return enemy1_health
            print(user_stats['char_name'] + " fails to flee the Dragon.")
            print(user_stats['char_name'] + " is vulnerable from exhaustion.")
            # Dragon attacks failed runners
            dragon_attack()
            return enemy1_health
        # User selects Magic
        elif user_selection == 3:
            # Check if user already used magic this round
            if option_stats['magic'] < 1:
                print(user_stats['char_name'] + " is unable to conjure another spell without rest.")
                return enemy1_health
            # Determines if spell is successful. Arcanist will always be successful.
            magic_chance = random.randint(0, 6) + user_stats['char_magic']
            if magic_chance < 1:
                print(user_stats['char_name'] + " hands begin to glow....")
                time.sleep(2)
                print("Dragon let's out a massive roar! " + user_stats['char_name'] +
                      "'s spell casting breaks and fizzles out.")
                # Set magic in option_stats to zero (prevents user from using magic again)
                option_stats['magic'] = 0
                return enemy1_health
            print(user_stats['char_name'] + "'s hands begin to glow...")
            time.sleep(2)
            print("A large prismatic fire of magenta, purple, green, and gold forms from thin air.")
            time.sleep(2)
            print(user_stats['char_name'] + " hurls the intensely glowing fireball towards the Dragon")
            time.sleep(1)
            print("The prismatic fireball pierces through the beast's iron scales.")
            time.sleep(1)
            # Magic damage minimum and maximum are increased if user is an Arcanist + a +2 bonus on top
            magic_attack_value = (random.randint(10 + user_stats['char_magic'], 20 + user_stats['char_magic'])
                                  + user_stats['char_magic'])
            enemy_magic_dmg_txt = f" takes {magic_attack_value} damage."
            print("Dragon " + enemy_magic_dmg_txt)
            # Set magic in option_stats to zero (prevents user from using magic again)
            option_stats['magic'] = 0
            enemy1_health -= magic_attack_value
            if enemy1_health < 0:
                return enemy1_health
            # Call enemy attack function
            dragon_attack()
            return enemy1_health
        # User selects Sneak Attack
        elif user_selection == 4:
            return enemy1_health
        # User selects Talk
        elif user_selection == 5:
            return enemy1_health
        else:
            print("Please enter the appropriate number corresponding to the options.")
            return enemy1_health



    # Begin Game Loop
    # -------------------------------------------------------------

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
                user_stats['char_attack'] = 2
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
    while level_one_loop is True:
        print("Scenario 1: You see a dragon. \n")
        print("What do you do? \n")
        lvl_one_select = input("1. Attack \n"
                               "2. Run (must roll 18+ (d20)) \n"
                               "3. Use offensive magic (must roll 1+ (d6)) \n"
                               "4. Sneak attack (must roll 10+ (d20) \n"
                               "5. Talk to the dragon (must roll 19+ (d20)) \n" +
                               user_stats['char_name'] + " selects: ")
        if lvl_one_select.upper() == "QUIT" or lvl_one_select.upper() == "EXIT":
            print(goodbye_text)
            quit()
        elif lvl_one_select.isnumeric() is False:
            print(selection_error)
            continue
        elif int(lvl_one_select) < 1 or int(lvl_one_select) > 5:
            print(selection_error)
            continue
        #else:
        # Call the level one switch function in a loop here. It terminates when the enemy health is 0
        #elif level_one_win == 1:
            #level_one_loop = False



