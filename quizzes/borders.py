##### Borders quiz
def borders(countries, player):
    # # filter countries list of dict: only include countries with 3 or more neighbours
    countries = [c for c in countries if ("borders" in c and len(c["borders"]) >= N - 1)]
    indexes, object_index = get_random(countries)

    # get the country the question is about
    q = countries[object_index]["name"]["common"]

    # get code of countries with borders to that country
    neighbor_list = countries[object_index]["borders"]

    # prepare lists with full names and indexes of neighbor countries
    neighbor_list_full = []
    indexes = []

    # populate these lists (n options)
    for neighbor in neighbor_list:
        country = [c for c in countries if "cca3" in c and c["cca3"] == neighbor]
        if len(country) > 0:
            # generate answer object (will be "wrong" answer)
            answer_object = {
                "name": country[0]["name"]["common"],
                "right": False
            }
            neighbor_list_full.append(answer_object)

    ## add an answer option with the name  of a country that is no neighbor (this will be "right answer")
    # get region of country the quesition is about
    region = countries[object_index]["region"]

    # get list of other countries in that region
    countries_in_region_objects = [c for c in countries if c["region"] == region]

    # exclude countries in that region that are in neighbours list
    countries_in_region = []
    neighbor_list_full_names = []
    for nb in neighbor_list_full:
        neighbor_list_full_names.append(nb["name"])
    # print("All neighbors:", neighbor_list_full_names)
    for co in countries_in_region_objects:
        if co["name"]["common"] not in neighbor_list_full_names:
            # generate answer object
            answer_object = {
                "name": co["name"]["common"],
                "right": True
            }
            countries_in_region.append(answer_object)
            # countries_in_region.append(c["name"]["common"] )

    # restart quiz if no country remains or user has less than N answer option
    if len(countries_in_region) == 0 or len(neighbor_list_full) < N - 1:
        return borders(countries, player)

    else:
        # shorten neighbors_list_full to N-1
        for x in range(0, len(neighbor_list_full) - (N - 1)):
            neighbor_list_full.pop()

        answers = neighbor_list_full
        # choose one from list randomly and assign as "right answer"
        right_answer_object = random.choice(countries_in_region)
        right_answer = right_answer_object["name"]
        # append to answers list
        answers.append(right_answer_object)
        # shuffle list
        random.shuffle(answers)
        # create indexex
        i = 0
        for a in answers:
            i += 1
            a["index"] = i

        # print options
        print(f"Which country has no border with {q}?")
        display_options(answers)

        # ask user for input and check answer
        wants_joker = check_answer(answers, right_answer, player)
        if wants_joker:
            player.joker50 -= 1
            exclude = use_joker(answers)
            display_options(answers, exclude)
            check_answer(answers, right_answer, player, joker=True)
