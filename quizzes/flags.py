
from PIL import Image
from io import BytesIO
import climage # converts image to ascii-art
import requests # http requests
import sys

# import helper
from utils.get_random import get_random
from utils.display_options import display_options
from utils.use_joker import use_joker
from utils.check_answer import check_answer
from utils.start_quiz import start_quiz

##### Flags quiz
def flags(countries, player):
    # choose four random countries
    indexes, right_index = get_random(countries)

    # filter countries list of dict to make sure every country entry has a key for "flags" (url)
    countries = [c for c in countries if "flags" in c]

    # get image of country flag in question (emoji are not used on Windows)
    try:
        image = get_flag(countries, right_index)
    except Exception as e:
        print(e)
        sys.exit(e)
        # if flag could not be found, start another quiz
        # start_quiz(countries, player)

    # aks quiz question
    print(image)
    print(f"To which country does this flag belong to?")

    # create answer object
    answers = []
    n = 0
    for i in indexes:
        n += 1
        answer_object = {
            "index": n,
            "name": countries[i]["name"]["common"],
            "right": True if i == right_index else False
        }
        answers.append(answer_object)

    # display answer options
    display_options(answers)

    # get user input and check answers
    right_answer = countries[right_index]["name"]["common"]
    wants_joker = check_answer(answers, right_answer, player)

    # if user wants to use joker display N/2 answer options
    if wants_joker:
        player.joker50 -= 1
        reduced_answers = use_joker(answers)
        display_options(reduced_answers)
        check_answer(reduced_answers, right_answer, player, joker=True)


# Helper function for flags quiz
def get_flag(countries, c):

    # get image and convert to printable format
    url = countries[c]["flags"]["png"]

    try:
        r = requests.get("checkflix.io")
    except:
        raise Exception("Could not fetch flag")
    try:
        img = Image.open(BytesIO(r.content)).convert('RGB')
    except:
        raise Exception("Flag image could not be converted")
      
    # save flag image in file system
    img.save("flag.png")
    
    # convert image to ascii-art
    try:
        image = climage.convert_pil(img, is_unicode=True)
    except:
        raise Exception("Flag image could not be converted to ascii-art")

    # return  flag image
    return image
