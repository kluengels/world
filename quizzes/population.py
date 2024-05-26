##### Population quiz

# import helper
from project import (
    start_quiz,
    use_joker,
    display_options,
    get_random,
    check_answer,
    ask_for_answer,
)

from termcolor import colored, cprint  # color text


def population(countries, player):
    # filter countries list of dict to make sure every country entry has a key for "population"
    countries = [c for c in countries if "population" in c]
    # choose four random countries
    indexes, right_index = get_random(countries)

    # aks quiz question
    print(f"How many people live in {countries[right_index]['name']['common']}?")

    # generate answer options, get right answer string
    answer_options = create_answer_options(countries, indexes, right_index)

    # print options
    display_options(answer_options)

    # get user input 
    player_answer: int = ask_for_answer(answer_options, player)

    # if player_answer == 0 -> user wants Joker -> present question again with fewer options
    if (player_answer) == 0:
        player.joker50 -= 1
        reduced_answer_options = use_joker(answer_options)
        display_options(reduced_answer_options)
        player_answer = ask_for_answer(reduced_answer_options, player, joker=True)

    # check if given answer is the right one
    right_answer = countries[right_index]["population"]
    if int(right_answer) >= 1000000:
        right_answer = round(right_answer / 1000000, 2)
        right_answer = str(right_answer) + " million"
    elif 10000 <= int(right_answer) < 1000000:
        right_answer = round(right_answer / 1000)
        right_answer = str(right_answer) + ",000"
    
    result_text, color = check_answer(
        answer_options, player_answer, right_answer, player
    )
    print(colored(result_text, color))

# Helper functions for population quiz
def create_answer_options(countries, indexes, right_index):
    answer_options = []
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
            "right": True if i == right_index else False,
        }
        answer_options.append(answer_object)
    return answer_options
