### Population quiz: How big is the population of x?

def create_population_right_answer_str(countries, right_index):
    right_answer = countries[right_index]["population"]
    if int(right_answer) >= 1000000:
        right_answer = round(right_answer / 1000000, 2)
        right_answer = str(right_answer) + " million"
    elif 10000 <= int(right_answer) < 1000000:
        right_answer = round(right_answer / 1000)
        right_answer = str(right_answer) + ",000"



def create_population_answers(countries, indexes, right_index):
    answer_options = []
    n = 0
    for i in indexes:
        n += 1
        # transform millions
        inhabitants = countries[i]["population"]
        if int(inhabitants) >= 1000000:
            inhabitants = round(inhabitants / 1000000, 2)
            inhabitants = str(inhabitants) + " million"
        elif 10000 <= int(inhabitants) < 1000000:
            inhabitants = round(inhabitants / 1000)
            inhabitants = str(inhabitants) + ",000"
        answer_object = {
            "index": n,
            "name": inhabitants,
            "right": True if i == right_index else False,
        }
        answer_options.append(answer_object)
    return answer_options
