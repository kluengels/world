## todo: testing, styling, unit tests, input options when joker is used
# joker should remove 4 options when N = 6
# crt c  oder ctr d for exit

### Imports
import json  # work with json data
import sys
import os  # access file system

import random  # generate random numbers
from art import *  # ascii-art
from termcolor import colored, cprint  # color text


# image handling
from PIL import Image
from io import BytesIO
import climage  # converts imag to ascii-art


# everything related to Player
from player.Player import Player
from player.leaderboard import write_score, get_board

# Configuration: Number of options for each question
N = 4


def main():
    # welcome screen
    print(welcome())
    print()

    # ask user for name, will create a player instance from Player class
    player = Player.get()
    print()

    # load countries json data, needed to generate quizzes
    countries = load_countries()

    # As long as player more than one life ask him randomly new questions
    while player.lifes > 0:
        # start a new quiz
        start_quiz(countries, player)
        # tell user how much liefes and jokers he has left
        print(player)

    # game over if player has no lifes left
    print(
        "Game over. You have reached the leaderboard if you find your name in green in the table."
    )

    # write to leaderboard
    write_score(player)

    # print leaderboard
    table = get_board(player)
    print(table)

    # aks user if he wants to play another round
    again()


#### functions related to all quizzes (will be imported by quiz files)
def start_quiz(countries, player):
    """Randomy chouse a game mode"""

    modes = ["flags", "capitals", "population", "borders", "area"]
    # mode = random.choice(modes)
    mode = "borders"

    # Guess which country belongs to flag
    if mode == "flags":
        from quizzes.flags import flags

        flags(countries, player)

    # Guess population of a country
    elif mode == "population":
        from quizzes.population import population

        population(countries, player)

    # Guess the capital of a country
    elif mode == "capitals":
        from quizzes.capitals import capitals

        capitals(countries, player)

    # Guess which country is not a neighbor of a country
    elif mode == "borders":
        from quizzes.borders import borders

        borders(countries, player)

    # # Guess which country is biggest (area)
    # elif mode == "area":
    #     area(countries, player)

    # print()


def use_joker(answers):
    """Use of joker elimnates two wrong answers from answers list"""
    indexes_wrong_answers = []
    for a in answers:
        if not a["right"]:
            indexes_wrong_answers.append(a["index"])
    indices_to_remove = random.sample(indexes_wrong_answers, 2)

    # Filtering the list to remove the two randomly selected wrong answers
    reduced_answers = [
        answer for answer in answers if answer["index"] not in indices_to_remove
    ]

    return reduced_answers


def display_options(answers, exclude=[]):
    """presents quiz options without the ones excluded by joker"""

    for a in answers:

        if a["index"] not in exclude:
            print(f"{a['index']}) {a['name']}")
        else:
            print()


def get_random(countries):
    """get N random countries"""
    # select N random countries by index
    indexes = []
    n = 0
    while n < 4:
        i = random.randint(0, len(countries) - 1)
        if i not in indexes:
            indexes.append(i)
            n += 1

    # choose the country the question will be about
    right_index = indexes[random.randint(0, len(indexes) - 1)]

    return indexes, right_index


def check_answer(
    answer_options,
    player_answer,
    right_answer,
    player,
):
    """check if answer given by user is correct"""
    # check if answer is correct
    for a in answer_options:
        if a["index"] == player_answer:
            selected = a

    if selected["right"]:
        # player scores
        player.add_point()
        return (f"That's correct. Congratulations!", "green")

    else:
        # player looses one life
        player.withdraw_life()
        return (
            f"That's wrong. The right answer would have been {right_answer}.",
            "red",
        )


def ask_for_answer(answer_options, player, joker=False) -> int:
    """presents answer options (and joker option) to player"""
    possible_answers = [item["index"] for item in answer_options]
    while True:
        try:
            # offer player to use a 50/50 joker if not already done and joker left
            if joker == False and player.joker50 > 0:
                answer = input("Your answer (or 'J' for Joker): ").strip().lower()
                if answer == "j" or answer == "'j'" or answer == "joker":
                    # return if user wants joker
                    return 0
            else:
                answer = input("Your answer: ").strip().lower()
        except KeyboardInterrupt:
            print()
            sys.exit("See you next time!")

        try:
            # make sure answer is not empty and an integer
            answer = int(answer[0])
            # stop asking for an answer if user typed a valid int
            if answer in possible_answers:
                return answer
            else:
                raise ValueError
        except (IndexError, ValueError):
            print(f"Please enter a valid number")
            continue


##### other functions
def load_countries():
    """Load countries data from local json file"""
    try:
        f = open("countries.json", "r")
        return json.load(f)
    except:
        sys.exit("Could not open the file countries.json")


def welcome():
    """generate ascii art welcome message"""
    txt = "-" * 80 + "\n"
    Art = text2art("Welcome to")  # Return ASCII text (default font)
    txt += Art
    Art = text2art("world quiz")
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
