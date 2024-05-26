### Borders quiz: Which countries do not have a border with x?


import random


def create_border_answers(countries, right_index):
    """Create list of dicts with countries as possible answer for multiple choice question"""

    # get code of countries with borders to that country
    neighbor_list = countries[right_index]["borders"]
    # restart quiz if selected country has less than 3 neighbors:
    if len(neighbor_list) < 3:
        from project import get_random
        indexes, right_index = get_random(countries)
        return create_border_answers(countries, right_index)

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
