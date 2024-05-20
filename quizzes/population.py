##### Population quiz

import sys
from utils.get_random import get_random

def population(countries, player):
    # filter countries list of dict to make sure every country entry has a key for "population"
    countries = [c for c in countries if "population" in c]
    indexes, right_index = get_random(countries)

    # aks quiz question
    print(f"How many people live in {countries[right_index]['name']['common']}?")

    # generate answer options, get right answer string
    answers = []
    n = 0
    for i in indexes:
        n += 1
        # transform millions
        inhabitants = countries[i]["population"]
        if int(inhabitants) >= 1000000:
            inhabitants = round(inhabitants / 1000000, 2)
            inhabitants = str(inhabitants) + " million"
        elif 10000 <= int(inhabitants) < 1000000:
            inhabitants = round(inhabitants / 1000)
            inhabitants = str(inhabitants) + ",000"
        answer_object = {
            "index": n,
            "name": inhabitants,
            "right": True if i == right_index else False
        }
        answers.append(answer_object)

    right_answer = countries[right_index]["population"]
    if int(right_answer) >= 1000000:
            right_answer = round(right_answer / 1000000, 2)
            right_answer = str(right_answer) + " million"
    elif 10000 <= int(right_answer) < 1000000:
        right_answer = round(right_answer / 1000)
        right_answer = str(right_answer) + ",000"

    # print options
    display_options(answers)

    # ask user for input and check answer
    wants_joker = check(answers, right_answer, player)

    # if user wants to use joker display N/2 answer options
    if wants_joker:
        player.joker50 -= 1
        exclude = joker(answers)
        display_options(answers, exclude)
        check(answers, right_answer, player, joker=True)

