### Borders quiz: Which countries do not have a border with x?

# import helper
from project import (
    start_quiz,
    use_joker,
    display_options,
    get_random,
    check_answer,
    ask_for_answer,
)
import random
import sys

from termcolor import colored


def borders(countries, player):
    try:
        # filter countries list of dict: only include countries with 3 or more neighbours
        countries = [
            c for c in countries if ("borders" in c and len(c["borders"]) >= 4 - 1)
        ]
        # choose four random countries
        indexes, right_index = get_random(countries)

        # get the country the question is about
        q = countries[right_index]["name"]["common"]

        # create answers_option object

        answer_options = create_answer_options(countries, indexes, right_index, player)

        # aks quiz question
        print(f"Which country has no border with {q}?")

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

        right_answer = [a for a in answer_options if a["right"] == True][0]["name"]

        result_text, color = check_answer(
            answer_options, player_answer, right_answer, player
        )
        print(colored(result_text, color))

    # if anythings goes wrong, start another quiz
    except Exception as e:
        start_quiz(countries, player)


def create_answer_options(countries, indexes, right_index, player):
    """Create list of dicts with countries as possible answer for multiple choice question"""

    # get code of countries with borders to that country
    neighbor_list = countries[right_index]["borders"]
    # restart quiz if selected country has less than 3 neighbors:
    if len(neighbor_list) < 3:
        raise IndexError("Selected country has not enough neighbors")

    # randomly select 3 countries out of neighbor list
    selected_neighbors = random.sample(neighbor_list, 3)

    # add these selection to answers list with value "False" ( will be "false" answers)
    answer_options = []

    for s in selected_neighbors:

        # look up country
        neighbor = [c for c in countries if c["cca3"] == s][0]
        # keep only common name and a indicator that answer is wrong
        neighbor_reduced = {"name": neighbor["name"]["common"], "right": False}
        # append to answer options
        answer_options.append(neighbor_reduced)

    # get countries in the same region as the country which is subject of quiz, which do not have a shared border
    # also exclude the selected country
    countries_in_same_region = [
        c
        for c in countries
        if c["region"] == countries[right_index]["region"]
        and countries[right_index]["cca3"] not in c["borders"]
        and countries[right_index]["cca3"] != c["cca3"]
    ]
    # randomly choose one
    selected_country_in_same_region = random.choice(countries_in_same_region)

    # add to answer options as "right answer"
    answer_options.append(
        {"name": selected_country_in_same_region["name"]["common"], "right": True}
    )
    # shuffle answers
    random.shuffle(answer_options)
    # add index values
    n = 0
    for a in answer_options:
        n += 1
        a["index"] = n

    return answer_options
