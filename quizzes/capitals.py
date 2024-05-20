##### Capitals quiz
def capitals(countries, player):
    # filter countries list of dict to make sure every country entry has a key for "capital"
    countries = [c for c in countries if "capital" in c]
    indexes, right_index = get_random(countries)

    try:
        c = countries[right_index]["name"]["common"]
        print(f"What is the capital of {c}?")

        # generate answer options, get right answer string
        answers = []
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
            answers.append(answer_object)

        right_answer = countries[right_index]["capital"]
        if len(right_answer) == 1:
            right_answer = right_answer[0]
        else:
            right_answer = " ".join(str(e) for e in right_answer[0])

        # display answer options
        display_options(answers)

        # ask user for input and check answer
        wants_joker = check_answer(answers, right_answer, player)
        if wants_joker:
            player.joker50 -= 1
            exclude = use_joker(answers)
            display_options(answers, exclude)
            check_answer(answers, right_answer, player, joker=True)

    # if one of the countries has no data for capital generate new index numbers and re-run
    except KeyError:
        return capitals(countries, player)
