#### Flags quiz

from PIL import Image
from io import BytesIO
import climage  # converts image to ascii-art
import requests  # http requests
from termcolor import colored, cprint  # color text

# import helper
from project import (
    start_quiz,
    use_joker,
    display_options,
    get_random,
    check_answer,
    ask_for_answer,
)


def flags(countries, player):
    try:
        # filter countries list of dict to make sure every country entry has a key for "flags" (url)
        countries = [c for c in countries if "flags" in c]
        # choose four random countries
        indexes, right_index = get_random(countries)

        # get image of country flag in question

        image = get_flag(countries, right_index)
        # aks quiz question
        print(image)
        print(f"To which country does this flag belong to?")

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
        right_answer = countries[right_index]["name"]["common"]
        result_text, color = check_answer(
            answer_options, player_answer, right_answer, player
        )
        print(colored(result_text, color))

    # if anything goes wrong start another quiz
    except Exception as e:
        start_quiz(countries, player)


# Helper function for flags quiz
def create_answer_options(countries, indexes, right_index):
    """Create list of dicts with countries as possible answer for multiple choice question"""
    answer_options = []
    n = 0
    for i in indexes:
        n += 1
        answer_object = {
            "index": n,
            "name": countries[i]["name"]["common"],
            "right": True if i == right_index else False,
        }
        answer_options.append(answer_object)
    return answer_options


def get_flag(countries, c):
    """download flag image and convert into printable format"""
    url = countries[c]["flags"]["png"]
    r = requests.get(url)
    img = Image.open(BytesIO(r.content)).convert("RGB")

    # save flag image in file system
    img.save("flag.png")

    # convert image to ascii-art
    return climage.convert_pil(img, is_unicode=True)
