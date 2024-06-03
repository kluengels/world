#### Flags quiz: To which county belongs this flag?

from PIL import Image
from io import BytesIO
import climage  # converts image to ascii-art
import requests  # http requests
from termcolor import colored, cprint  # color text


def create_flags_answers(countries, indexes, right_index):
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
    img = Image.open(BytesIO(r.content)).convert("RGBA")

    # save flag image in file system
    img.save("flag.png")

    # convert image to ascii-art
    return climage.convert_pil(img, is_unicode=True)
