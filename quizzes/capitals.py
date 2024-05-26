##### Capitals quiz

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

def capitals(countries, player):
    # filter countries list of dict to make sure every country entry has a key for "capital"
    countries = [c for c in countries if "capital" in c]

    # choose four random countries
    indexes, right_index = get_random(countries)

    # aks quiz question
    c = countries[right_index]["name"]["common"]
    print(f"What is the capital of {c}?")

     # create answer_options object
    answer_options = create_answer_options(countries, indexes, right_index)

    # display answer options
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
    right_answer = countries[right_index]["capital"]
    if len(right_answer) == 1:
        right_answer = right_answer[0]
    else:
        right_answer = " ".join(str(e) for e in right_answer[0])
    result_text, color = check_answer(
        answer_options, player_answer, right_answer, player
    )
    print(colored(result_text, color))




def create_answer_options(countries, indexes, right_index):
    """Create list of dicts with countries as possible answer for multiple choice question"""
    answer_options  = []
    n = 0
    for i in indexes:
        n += 1
        capital = countries[i]["capital"]
        if len(capital) == 1:
            capital = capital[0]
        else:
            capital = " ".join(str(e) for e in capital)
        answer_object = {
            "index": n,
            "name": capital,
            "right": True if i == right_index else False
        }
        answer_options.append(answer_object)
    return answer_options
