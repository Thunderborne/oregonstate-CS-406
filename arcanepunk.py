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

# Game win condition to terminate outer loop
win_game = 0

# Main Loop
while win_game < 1:

    # Turn counter
    turn_counter = {
        'total': 0,
        'level_1': 0,
        'level_2': 0,
        'level_3': 0
    }

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

    # NPC and Enemies
    npc_stats = {
        'dragon': 100,
        'enemy2': 100,
        'enemy3': 100
    }

    # Gear / Equipment
    char_gear = {
        'lightbrand': 1,
        'healbot': 1,
        'staff': 1,
        'shield': 1,
        'cyberblade': 1
    }

    # Level One Data
    # -------------------------------------------------------------

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
    def level_one_cases(user_selection):
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
                # Crit check, must roll a 20
                critical_strike_chance = random.randint(1, 20)
                if critical_strike_chance == 20:
                    print("Critical strike!")
                    critical_damage = random.randint(6, 12)
                    attack_value += critical_damage
                attack_value += user_stats['char_attack']
                attack_txt = f" attacks the Dragon for {attack_value}!"
                print(user_stats['char_name'] + attack_txt)
            npc_stats['dragon'] -= attack_value
            if npc_stats['dragon'] < 0:
                turn_counter['level_1'] += 1
                turn_counter['total'] += 1
                return
            # Call function so the dragon can return an attack
            dragon_attack()
            turn_counter['level_1'] += 1
            turn_counter['total'] += 1
            return
        # User selects Run
        elif user_selection == 2:
            print(user_stats['char_name'] + " attempts to run away.")
            run_attempt_value = random.randint(1, 20)
            print("---> " + user_stats['char_name'] + f" rolls a {run_attempt_value} "
                                                      f"out of 20 (+{user_stats['char_evade']} Evade).")
            run_attempt_value += user_stats['char_evade']
            time.sleep(2)
            if run_attempt_value >= 18:
                print(user_stats['char_name'] + " has successfully escaped the Dragon!")
                npc_stats['dragon'] = 0
                turn_counter['level_1'] += 1
                turn_counter['total'] += 1
                return
            print(user_stats['char_name'] + " fails to flee the Dragon.")
            print(user_stats['char_name'] + " is vulnerable from exhaustion.")
            # Dragon attacks failed runners
            dragon_attack()
            turn_counter['level_1'] += 1
            turn_counter['total'] += 1
            return
        # User selects Magic
        elif user_selection == 3:
            # Check if user already used magic this round
            if option_stats['magic'] < 1:
                print(user_stats['char_name'] + " is unable to conjure another spell without rest.")
                return
            # Determines if spell is successful. Arcanist will always be successful.
            magic_chance = random.randint(1, 6)
            print("---> " + user_stats['char_name'] + f" rolls a {magic_chance} out of "
                                                      f"6 (+{user_stats['char_magic']} Arcane).")
            magic_chance += user_stats['char_magic']
            if magic_chance < 2:
                print(user_stats['char_name'] + " hands begin to glow....")
                time.sleep(2)
                print("Dragon let's out a massive roar! " + user_stats['char_name'] +
                      "'s spell casting breaks and fizzles out.")
                # Set magic in option_stats to zero (prevents user from using magic again)
                option_stats['magic'] = 0
                turn_counter['level_1'] += 1
                turn_counter['total'] += 1
                return
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
            enemy_magic_dmg_txt = f"takes {magic_attack_value} damage."
            print("Dragon " + enemy_magic_dmg_txt)
            # Set magic in option_stats to zero (prevents user from using magic again)
            option_stats['magic'] = 0
            npc_stats['dragon'] -= magic_attack_value
            if npc_stats['dragon'] < 0:
                time.sleep(2)
                print("Dragon writhes and slowly collapses from the intense heat of the fire.")
                time.sleep(2)
                print("The Dragon huffs. And slowly...")
                time.sleep(3)
                print("it takes her last breath.")
                turn_counter['level_1'] += 1
                turn_counter['total'] += 1
                return
            # Call enemy attack function
            dragon_attack()
            turn_counter['level_1'] += 1
            turn_counter['total'] += 1
            return
        # User selects Sneak Attack
        elif user_selection == 4:
            # Checks if Sneak Attack has already been used in the fight
            if option_stats['sneak'] < 1 or turn_counter['level_1'] > 0:
                print(user_stats['char_name'] + " can no longer use a sneak attack in this fight.")
                return
            # Determines if sneak attack is successful. Operative has a +2 on top of the roll.
            sneak_chance = random.randint(1, 20)
            print("---> " + user_stats['char_name'] + f" rolls a {sneak_chance} "
                                                      f"out of 20 (+{user_stats['char_evade']} Evade).")
            sneak_chance += user_stats['char_evade']
            # Unsuccessful sneak attack
            if sneak_chance < 10:
                print(user_stats['char_name'] + " attempts to blend into the shadows...")
                time.sleep(2)
                print("Dragon spots " + user_stats['char_name'] + " stealth technique.")
                dragon_attack()
                # Set sneak in option_stats to zero (prevents user from using sneak again)
                option_stats['sneak'] = 0
                turn_counter['level_1'] += 1
                turn_counter['total'] += 1
                return
            print(user_stats['char_name'] + " attempts to blend into the shadows...")
            time.sleep(1)
            print("A shroud of darkness surrounds " + user_stats['char_name'] + ".")
            time.sleep(1)
            print(user_stats['char_name'] + " sneaks behind the Dragon and plunges a photon knife into "
                                            "the beast's belly.")
            time.sleep(1)
            # Sneak damage minimum and maximum are increased if user is an Operative + a +2 bonus on top
            sneak_attack_value = (random.randint(6 + user_stats['char_evade'], 12 + user_stats['char_evade'])
                                  + user_stats['char_evade'])
            enemy_sneak_dmg_txt = f" takes {sneak_attack_value} damage"
            print("Dragon" + enemy_sneak_dmg_txt + " and is momentarily stunned.")
            # Set sneak in option_stats to zero (prevents user from using sneak again)
            option_stats['sneak'] = 0
            npc_stats['dragon'] -= sneak_attack_value
            time.sleep(3)
            # Chance to double sneak stab. Must roll a 5+
            if user_stats['char_evade'] >= 1:
                double_sneak_chance = random.randint(1, 6)
                print(user_stats['char_name'] + " attempts to sneak attack the Dragon a second time...")
                time.sleep(2)
                if double_sneak_chance < 5:
                    print("But " + user_stats['char_name'] + " notices the Dragon begins to regain its "
                                                             "consciousness and wisely pulls back.")
                else:
                    double_sneak_value = random.randint(1, 12)
                    double_sneak_attack_txt = (f" causing {double_sneak_value} additional damage to "
                                               f"the stunned beast.")
                    print("There's still time...")
                    time.sleep(1)
                    print(user_stats['char_name'] + " quickly pulls out a photon blade and slashes "
                                                    "the Dragon's tail" + double_sneak_attack_txt)
                    npc_stats['dragon'] -= double_sneak_value
            turn_counter['level_1'] += 1
            turn_counter['total'] += 1
            return
        # User selects Talk
        elif user_selection == 5:
            if option_stats['talk'] < 1 or turn_counter['level_1'] > 0:
                print("The Dragon has no desire to speak. Choose another option.")
                return
            print(user_stats['char_name'] + " decides speaking to the beast is the best option.")
            time.sleep(2)
            print(user_stats['char_name'] + " slowly approaches the Dragon.")
            time.sleep(2)
            print("'I do not mean you any harm. I am just merely here to rescue a technohealer \n"
                  "held captive at the tower's top,' " + user_stats['char_name'] + " said.")
            time.sleep(5)
            print("The Dragon looks uninterested in " + user_stats['char_name'] + "'s words.")
            time.sleep(2)
            talk_success_chance = random.randint(1, 20)
            print("--> " + user_stats['char_name'] + f" rolls a {talk_success_chance} out of 20.")
            if talk_success_chance < 19:
                print("The Dragon seems insulted by " + user_stats['char_name'] +
                      "'s audacity to confront her without fear. She now wants to fight...")
                time.sleep(2)
                print("The Dragon quickly swipes her massive claws at " + user_stats['char_name'] + ".")
                time.sleep(2)
                print(user_stats['char_name'] + " reacts, dodging most of the impact, but sustains 5 damage.")
                user_stats['char_health'] -= 5
                option_stats['talk'] = 0
                turn_counter['level_1'] += 1
                turn_counter['total'] += 1
                return
            print("She bears her teeth, but decides to ignore " + user_stats['char_name'] + ".")
            time.sleep(2)
            print(user_stats['char_name'] + " quickly realizes that it's the only chance "
                                            "to walk by her unscathed.")
            # Successful talk allows user to bypass the encounter
            npc_stats['dragon'] = 0
            turn_counter['level_1'] += 1
            turn_counter['total'] += 1
            return
        else:
            print("Please enter the appropriate number corresponding to the options.")
            return


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
            print(user_stats['char_name'] + " has chosen the " + user_stats['char_classname'] + ".\n")
            time.sleep(1)
            print(user_stats['char_name'] + "'s stats are:")
            print(f"Class: {user_stats['char_classname']} \n"
                  f"Health: {user_stats['char_health']} \n"
                  f"Attack: +{user_stats['char_attack']}, Evade: +{user_stats['char_evade']}, "
                  f"Arcane: +{user_stats['char_magic']}")
            user_class_loop = False

    # Level One of Tower Loop
    """
    TODO: Fill in the story scenario in UI phase
    TODO: Call the pipe for stats and dice roll
    """
    time.sleep(3)
    print("\n")
    print("Scenario 1: You see a dragon. \n")
    print("What do you do? \n")

    while npc_stats['dragon'] > 0:
        # Check if the Dragon is dead
        if user_stats['char_health'] < 1:
            print(user_stats['char_name'] + "'s health has reached 0. Game over.")
            quit()
        time.sleep(3)
        print("-------------------------------------------------------")
        print(f"Turn Number: {turn_counter['total']}")
        print(user_stats['char_name'] + f"'s Health: {user_stats['char_health']}")
        print(f"Dragon's Health: {npc_stats['dragon']}")
        print("-------------------------------------------------------")
        time.sleep(2)
        # User selection
        print("Select number corresponding to your choice:")
        lvl_one_select = input("1. Attack \n"
                               "2. Run (must roll 18+ (d20)) \n"
                               "3. Use offensive magic (must roll 2+ (d6)) \n"
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
        else:
            user_select = int(lvl_one_select)
            level_one_cases(user_select)
            # Message player that they have completed level
            if npc_stats['dragon'] < 1:
                time.sleep(2)
                print("An light platform drops down from.")
                time.sleep(2)
                print("It appears to be a magical lift.")
                time.sleep(2)
                print(user_stats['char_name'] + " quickly hops on.")
                time.sleep(1)
                print("-------------------------------------------------------")
                print(user_stats['char_name'] + " has passed level one!")
                print(f"Health: {user_stats['char_health']}")
                print(f"Number of Turns in Level 1: {turn_counter['level_1']}")
                print("-------------------------------------------------------")


    # Placeholder win condition and message
    print("Congratulations")

    # Print summary of stats / number of turns

    # Terminates Outer loop
    win_game = 1



