Nn  n
# Period: 3
# Date created: September 21st, 2021
# Date modified: September 28th, 2021
# Name: Zana Osman
# Description: Menu for Text-Based Adventure
import sys
from time import sleep

# Starting of the menu, player_ choses username
print("Text-Based Adventure Menu")
print("Welcome user_")
Username_ = input("What shall I call you? ")
print("Ok " + Username_ + " what would you like to do?")
# Actions and directions possible
possible_actions = ["Attack", "Inventory", "Explore", "Heal", "Quit"]
possible_directions = ["north", "east", "south", "west "]
possible_characters = [""]

inventory = {"": {"Small Knife":
                              {"description": "Provides small damage and can be used for utilities",
                               "damage": 5, "protection": 0},
                              "Axe":
                              {"description": "Can cut down wooden and metal doors",
                               "damage": 15, "protection": 0},
                              "Shield":
                              {"description": "Provides protection against arrows, swords and bullets "
                               "magically-empowered sword wielded",
                               "damage": 0, "protection": 20}},
                               "Shield": {"Batarang":
                        {"description": "Provides protection against arrows, swords and bullets ",
                         "damage": 10, "protection": 0},
                        "Grapple hook":
                        {"description": "pear-shooting spring-based device",
                         "damage": 5, "protection": 0},
                        "Sonic Bat Device":
                        {"description":
                         "high frequency emitter allowing the control of bats",
                         "damage": 15, "protection": 100}},
                        
             }

def slow(text):
    """Prints title of game in a typewriter style"""
    words = str(text)

    for char in words:
        sleep(0.25)
        print(char, end="", flush=True)


def menu_():
    """Definition for the menu"""
    for action in possible_actions:
        print(f" {action}")
    menu_c = str(input("What action would u like to choose? "))
    if menu_c == "Attack":
        print("Attacking!")
    elif menu_c == "Inventory":
        print(character_ + "s" + " Inventory ")
        for weapon in inventory:
            print(f"{weapon}: ")
        for item in weapon:
            print(f"{item} - {weapon[item]}")
    elif menu_c == "Explore":
        # How the program will take your input for direction
        for direction in possible_directions:
                print(f" {direction}")
        directions_chosen = input("What direction would you like to go? ")
        if directions_chosen.lower() in possible_directions:
            print(f"Going {directions_chosen}!")
        else:
            print("Invalid direction, choose a direction!")
    elif menu_c == "Heal":
            print("Healing!")
    # Quit function will work with the sys.exit command
    elif menu_c == "Quit":
        if menu_c == "Quit":
            choice_s = input("Are you sure you would like to exit? (yes) ")
            if choice_s.lower() == "yes":
                print("Exiting, Goodbye " + Username_)
                sys.exit()
        else:
            print("Countinue!")
    else:
        print("Sorry that does not work, maybe choose a different option ")


# While loop for menu to stay active, will not close unless 'quit' is chosen
while True:
    menu_()
