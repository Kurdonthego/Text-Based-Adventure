# Course: CS 30
# Period: 3
# Date created: September 21st, 2021
# Name: Zana Osman
# Description: Menu for Text-Based Adventure
import sys

# Starting of the menu, player_ choses username
print("Text-Based Adventure Menu")
print("Welcome user_")
Username_ = input("What shall I call you? ")
print("Ok " + Username_ + " what would you like to do?")
# Actions and directions possible
possible_actions = ["Attack", "Defend", "Explore", "Heal", "Quit"]
possible_directions = ["north", "east", "south", "west "]


def menu_():
    """Definition for the menu"""
    menu_c = str((input)(possible_actions))
    if menu_c == "Attack":
        print("Attacking!")
    elif menu_c == "Defend":
        print("Defending!")
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
