
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
from utils.ask_for_answer import ask_for_answer

##### Flags quiz
def flags(countries, player):
    # choose four random countries
    indexes, right_index = get_random(countries)

    # filter countries list of dict to make sure every country entry has a key for "flags" (url)
    countries = [c for c in countries if "flags" in c]

    # get image of country flag in question
    try:
        image = get_flag(countries, right_index)
    except Exception as e:
        sys.exit(e)
        # if flag could not be found, start another quiz
        # start_quiz(countries, player)

    # aks quiz question
    print(image)
    print(f"To which country does this flag belong to?")

    # create answer_options object
    answer_options = []
    n = 0
    for i in indexes:
        n += 1
        answer_object = {
            "index": n,
            "name": countries[i]["name"]["common"],
            "right": True if i == right_index else False
        }
        answer_options.append(answer_object)

    # display answer options
    display_options(answer_options)

    # get user input and check answers
    
    player_answer: int = ask_for_answer(answer_options, player)

    # if player_answer == 0 -> user wants Joker -> present question again with fewer options
    if (player_answer) == 0:
        player.joker50 -= 1
        reduced_answer_options = use_joker(answer_options)
        display_options(reduced_answer_options)
        player_answer = ask_for_answer(reduced_answer_options, player, joker=True)

    
    # check if givven answer is the right one 
    right_answer = countries[right_index]["name"]["common"]
    check_answer(answer_options, player_answer, right_answer, player)
    
       


# Helper function for flags quiz
def get_flag(countries, c):

    # get image and convert to printable format
    url = countries[c]["flags"]["png"]

    try:
        r = requests.get(url)
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
