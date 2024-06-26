### A geo-quizz with 5 game modes

import json
import sys
import random
from art import *  # ascii-art
from termcolor import colored  # color text

# helper function specific to game modes
from quizzes import flags, borders, capitals, population, area

# player class and leaderboard
from Player import Player
from leaderboard import write_score, get_board

# do not print debug messages
import logging

logging.getLogger("requests").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)
logging.getLogger("PIL.PngImagePlugin").propagate = False


def main():
    # welcome screen
    print(welcome())

    # menu
    print(
        f'Type "start" to begin, "help" for a tutorial or "imprint" for the imprint, CTR+C to exit'
    )
    try:
        while True:
            command = input("Enter command: ").strip().lower()
            if command == "start":
                break
            if command == "help":
                print(
                    f"\nWorld Quiz will ask you randomly generated questions about countries. "
                    "You start with 3 lifes and 1 joker. The joker can be used one time to eliminate two answer options. "
                    "If your answer is wrong, you loose one life. "
                    "You will receive new questions as long as you have at least one life left.\n"
                )
                continue
            if command == "imprint":
                print(
                    f"\nWorld Quiz is a project made by:\n\n"
                    "Steffen Ermisch \n"
                    "Pressebüro JP4\nRichard-Wagner-Str. 10-12\n50674 Köln, Germany\n"
                    "https://steffen-ermisch.de\n\n"
                    "Props to https://restcountries.com/ for providing the countries database!\n"
                )
                continue
    except KeyboardInterrupt:
        sys.exit()

    print()

    # ask user for name, will create a player instance from Player class
    player = Player.get()
    print()
    print(f"Let's go, {player.name}! 🌍")
    print()

    # As long as player more than one life ask him randomly new questions
    while player.lifes > 0:
        # start a new radnomly chosen quiz
        start_quiz(player)

        # tell user how much liefes and jokers he has left
        print(player)

    # game over if player has no lifes left
    print(
        f"Game over. You got {player.points} points. You have reached the leaderboard if you find your name in green in the table."
    )

    # write to leaderboard
    player_id = write_score(player)

    # print leaderboard
    table = get_board(player_id)
    print(table)

    # aks user if he wants to play another round
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


#### functions related to all quizzes (will be imported by quiz files)
def start_quiz(player, mode="unknown"):
    """Logic that all quizzes share"""
    try:
        # (1) load countries data
        countries = load_countries()

        # (2) randomly select game mode
        if mode == "unknown":
            modes = ["flags", "capitals", "population", "borders", "area"]
            mode = random.choice(modes)

        # (3) filter countries
        countries = filter_countries(countries, mode, player)

        # (4) choose four random countries for questions
        indexes, right_index = get_random(countries)

        # exclude that country from future quizz questions in same mode
        # to avoid duplicate questions
        player.add_exclude(countries[right_index]["cca3"], mode)

        # Check if the selected country has less than three neighbors for the "borders" mode
        if mode == "borders" and len(countries[right_index]["borders"]) < 3:
            # print(colored("Restart quiz", "red"))
            return start_quiz(player, "borders")  # Restart the quiz

        # (5) create answer options
        answer_options = create_answer_options(countries, indexes, right_index, mode)

        # (6) construct and print the question
        question = construct_question(countries, right_index, mode)
        print(question)

        # (7) display answer option
        display_options(answer_options)

        # (8) get user input
        player_answer: int = ask_for_answer(answer_options, player)

        # (9) handle joker (player_answer == 0)
        if (player_answer) == 0:
            player.joker50 -= 1
            reduced_answer_options = use_joker(answer_options)
            display_options(reduced_answer_options)
            player_answer = ask_for_answer(reduced_answer_options, player, joker=True)

        # (10) prepare right answer text
        if mode == "capitals":
            right_answer = ", ".join(countries[right_index]["capital"])
        else:
            right_answer = [a for a in answer_options if a["right"] == True][0]["name"]

        # (11) check answer
        result_text, color = check_answer(
            answer_options, player_answer, right_answer, player
        )

        # (12) print result
        print(colored(result_text, color))

    # if anythings goes wrong, start a new quiz
    except (IndexError, ValueError):
        # print(colored("index error", "magenta"))
        start_quiz(player, mode)


### helper functions for all quizzes


def load_countries():
    """(1) Load countries data from local json file"""
    try:
        f = open("countries.json", "r")
        return json.load(f)
    except:
        sys.exit("Could not open the file countries.json")


def filter_countries(countries, mode, player):
    """(3) Filter countries list dependend on game mode"""
    # exclude countries that have been subject to a quiz question in same game mode
    exclude_list = player.exclude[mode]

    match mode:
        case "borders":
            # only include countries with borders
            return [
                c
                for c in countries
                if "borders" in c
                and len(c["borders"]) > 0
                and c["cca3"] not in exclude_list
            ]
        case "flags":
            #  make sure every country entry has a key for "flags" (url)
            return [
                c for c in countries if "flags" in c and c["cca3"] not in exclude_list
            ]
        case "capitals":
            # make sure every country entry has a key for "capital"
            return [
                c
                for c in countries
                if "capital" in c
                and len(c["capital"]) > 0
                and c["cca3"] not in exclude_list
            ]
        case "population":
            # make sure every country entry has a key for "population"
            return [
                c
                for c in countries
                if "population" in c and c["cca3"] not in exclude_list
            ]
        case "area":
            # make sure every country object has a key for "area"
            return [
                c for c in countries if "area" in c and c["cca3"] not in exclude_list
            ]


def get_random(countries):
    """get 4 random countries"""
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


def create_answer_options(countries, indexes, right_index, mode):
    """(5) prepare answer options"""
    match mode:
        case "flags":
            return flags.create_flags_answers(countries, indexes, right_index)

        case "borders":
            return borders.create_border_answers(countries, right_index)

        case "capitals":
            return capitals.create_capitals_answers(countries, indexes, right_index)

        case "population":
            return population.create_population_answers(countries, indexes, right_index)

        case "area":
            return area.create_area_answers(countries, indexes)


def construct_question(countries, right_index, mode):
    """(6) construct questions for different game modes"""
    # get the country the question is about
    q = countries[right_index]["name"]["common"]
    match mode:
        case "flags":
            # download flag and print it
            image = flags.get_flag(countries, right_index)
            print(image)
            return f"To which country does this flag belong to?"
        case "borders":
            return f"Which country has no border with {q}?"
        case "capitals":
            return f"What is the capital of {q}?"
        case "population":
            return f"How many people live in {q}?"
        case "area":
            return f"Which of the following countries has the biggest area?"


def display_options(answers, exclude=[]):
    """(7) and (9): presents quiz options without the ones excluded by joker"""
    for a in answers:

        if a["index"] not in exclude:
            print(f"{a['index']}) {a['name']}")
        else:
            print()


def ask_for_answer(answer_options, player, joker=False) -> int:
    """(8) presents answer options (and joker option) to player"""
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


def use_joker(answers):
    """(9) Use of joker elimnates two wrong answers from answers list"""
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


def check_answer(
    answer_options,
    player_answer,
    right_answer,
    player,
):
    """(11) check if answer given by user is correct"""
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


### other functions


def welcome():
    """generate ascii art welcome message"""
    txt = "-" * 80 + "\n"
    Art = text2art("Welcome to")  # Return ASCII text (default font)
    txt += Art
    Art = text2art("World Quiz")
    txt += Art
    txt += "-" * 80 + "\n\n"
    return txt


if __name__ == "__main__":
    main()
