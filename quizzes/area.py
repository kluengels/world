### area quiz: Which contries is biggest?

import random


def create_area_answers(countries, indexes):
    answers_options = []
    for i in indexes:
        country_object = {
            "name": countries[i]["name"]["common"],
            "area": int(countries[i]["area"]),
            "right": False,
        }

        answers_options.append(country_object)

    # sort them by area (biggest in index 0)
    answers_options.sort(key=lambda x: x["area"], reverse=True)

    # set country in index 0 as right answer
    answers_options[0]["right"] = True

    # shuffle answer options, add index number
    random.shuffle(answers_options)

    n = 0
    for a in answers_options:
        n += 1
        a["index"] = n
    return answers_options
