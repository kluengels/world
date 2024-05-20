
### Area (size) quiz
def area(countries, player):
    # filter countries list of dict to make sure every country object has a key for "area"
    countries = [c for c in countries if "capital" in c]
    indexes, _ = get_random(countries)

    print("Which of the following countries has the biggest area?")

    # create answer options
    answers = []
    for i in indexes:
        country_object = {
            "name": countries[i]['name']['common'],
            "area": int(countries[i]['area']),
            "right": False
        }
        answers.append(country_object)

    # sort them by area (biggest in index 0)
    answers.sort(key=lambda x: x["area"], reverse=True)
    # set country in index 0 as right answer
    answers[0]["right"] = True
    right_answer = f"{answers[0]['name']} with {answers[0]['area']:,} square kilometres"

    # shuffle answer options, create number
    random.shuffle(answers)
    n = 0
    for a in answers:
        n += 1
        a["index"] = n

    # dispay the shuffled answer options
    display_options(answers)

    # ask user for input and check answer
    wants_joker = check_answer(answers, right_answer, player)

    # if user wants joker re-display 2 options
    if wants_joker:
        player.joker50 -= 1
        exclude = use_joker(answers)
        display_options(answers, exclude)
        check_answer(answers, right_answer, player, joker=True)