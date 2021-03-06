# Course: CS 30
# Period: 3
# Date created: September 21st, 2021
# Date modified: October 13th, 2021
# Name: Zana Osman
# Description: Menu for Text-Based Adventure
import sys
from time import sleep

# Starting function to create username for player
print("Text-Based Adventure Menu")
print("Welcome user_")
Username_ = input("What shall I call you? ")
print("Ok " + Username_ + " what would you like to do?")

# Actions and directions possible
possible_actions = ["Attack [1]", "Inventory [2]", "Explore [3]", "Heal[4]", "Quit[5]"]
possible_directions = ["North [1]", "East [2]", "South [3]", "West [4]"]
possible_characters = ["Wonder boy, Beef"]
# Inventory of character
inventory_s = {"Small Knife":
                        {"Description": "Provides small damage and can be used for utilities", "Damage": 5, "Protection": 0},
                "Axe":
                        {"Description": "Can cut down wooden and metal doors",
                        "Damage": 15, "Protection": 0},
                "Shield":
                        {"Description": "Provides protection against arrows, swords and bullets",
                        "Damage": 0, "Protection": 20}
                        }


def start_inventory_fnct():
    for weapon in inventory_s:
        print(f"{weapon}")


def inventory_description():
    for weapon in inventory_s:
        print(f"\n{weapon}:")
        for item in inventory_s[weapon]:
            print(f"{item} - {inventory_s[weapon][item]}")


def slow(text):
    """Prints title of game in a typewriter style"""
    words = str(text)

    for char in words:
        sleep(0.25)
        print(char, end="", flush=True)


# While loop for menu to stay active, will not close unless 'quit' is chosen
while True:
    """Definition for the menu"""
    for action in possible_actions:
        print(f" {action}")
    menu_c = str(input("What action would u like to choose? "))
    if menu_c == "1":
        print("Attacking!")
    elif menu_c == "2":
        print("\nInventory:")
        start_inventory_fnct()
        inv_desc = input("\nShow descriptions? ")
        if inv_desc == "yes":
            inventory_description()
        else:
            print("No problemo")
    elif menu_c == "3":
        # How the program will take your input for direction
        for direction in possible_directions:
                print(f" {direction}")
        directions_chosen = str(input("What direction would you like to go? "))
        if directions_chosen == [1,2,3,4]:
            print(f"Going {directions_chosen}!")
        else:
            print("Invalid direction, choose a direction!")
    elif menu_c == "4":
            print("Healing!")
    # Quit function will work with the sys.exit command
    elif menu_c == "5":
        if menu_c == "5":
            choice_s = input("Are you sure you would like to exit? (yes) ")
            if choice_s.lower() == "yes":
                print("Exiting, Goodbye " + Username_)
                sys.exit()
        else:
            print("Countinue!")
    else:
        print("Sorry that does not work, Choose a different option ")
