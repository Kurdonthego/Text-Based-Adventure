# Course: CS 30
# Period: 3
# Date created: September 21st, 2021
# Date modified: o, 2021
# Name: Zana Osman
# Description: Menu for Text-Based Adventure
import sys
from time import sleep

# Starting of the menu, player_ choses username
print("Text-Based Adventure Menu")
print("Welcome user_")
Username_ = input("What shall I call you? ")
print("Ok " + Username_ + " what would you like to do?")
print("Choose a character")
# Actions and directions possible
possible_actions = ["Attack", "Inventory", "Explore", "Heal", "Quit"]
possible_directions = ["north", "east", "south", "west "]
possible_characters = ["Wonder boy, Beef"]


# defining the layout of the space ship
# EnemyTile is where the user must fight attackers
# SuppliesTile is where food, weapons, and first aid are stored
# EscapePod is the end of the game
# BoringTile is where nothing occurs
# StartTile is where the game begins
ship_map = [
     ["EnemyTile", "SuppliesTile", "BoringTile"],
     ["BoringTile", "BoringTile", "BoringTile"],
     ["EnemyTile", "StartTile", "EnemyTile"],
     ["EscapePod", "BoringTile", "BoringTile"]
 ]
ship_map[0][0] = "BoringTile"
ship_map[3][0] = "BoringTile"
ship_map[2][1] = "EscapePod"

inventory_s = {"Small Knife":
                                {"Description": "Provides small damage and can be used for utilities", "Damage": 5, "Protection": 0},
                "Axe":
                                {"Description": "Can cut down wooden and metal doors",
                                "Damage": 15, "Protection": 0},
                "Shield":
                                {"Description": "Provides protection against arrows, swords and bullets",
                                "Damage": 0, "Protection": 20}
             }

def inventory_fnct():
    for weapon in inventory_s:
        print(f"{weapon}: ")
        for item in inventory_s[weapon]:
            print(f"{item} - {inventory_s[weapon][item]}")


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
        print("Inventory:")
        inventory_fnct()
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
