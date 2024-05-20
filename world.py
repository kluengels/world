## todo: testing, styling, unit tests, input options when joker is used
# joker should remove 4 options when N = 6
# crt c  oder ctr d for exit

### Imports
import requests # http requests
import json # work with json data
import sys
import os # access file system
import random # generate random numbers
from art import * #ascii-art
from termcolor import colored, cprint # color text


# image handling
from PIL import Image
from io import BytesIO
import climage # converts imag to ascii-art

# get countries
from utils.get_countries import get_countries
# everything related to Player 
from player.Player import Player

# start a rondom quiz
from utils.start_quiz import start_quiz


# leaderboard
from player.leaderboard import write_score, get_board

def main():
    # welcome screen
    print(welcome())

   # ask user for name, will create a player instance from Player class
    player = Player.get()
    
    # load countries json data
    countries = get_countries()

    # As long as player more than one life ask him randomly new questions
    while player.lifes > 0:
        start_quiz(countries, player)
        

    # game over if player has no lifes left
    print("Game over. You have reached the leaderboard if you find your name in green in the table.")

    # write to leaderboard
    write_score(player)

    # print leaderboard
    table = get_board(player)
    print(table)

    # aks user if he wants to play another round
    again()






##### other functions
def welcome():
    txt = "-" * 80 + "\n"
    Art=text2art("Welcome to") # Return ASCII text (default font)
    txt += Art
    Art=text2art("world quiz")
    txt += Art
    txt += "-" * 80
    return txt









def again():
    while True:
        answer = input("Wanna play another round (y/n)? ").strip().lower()
        valid = ["y", "yes", "n", "no"]
        if answer not in valid:
            print("Please type y or n")
        else:
            if answer == "y" or answer == "yes":
                return main()
            else:
                print("Thank you for playing world quiz. See you next time!")
                break



if __name__ == "__main__":
    main()
