### Capitals quiz: Which is the capital of x?



def create_capitals_answers(countries, indexes, right_index):
    """Create list of dicts with countries as possible answer for multiple choice question"""
    answer_options  = []
    n = 0
    for i in indexes:
        n += 1
        capital = countries[i]["capital"]
        if len(capital) == 1:
            capital = capital[0]
        else:
            capital = ", ".join(str(e) for e in capital)
        answer_object = {
            "index": n,
            "name": capital,
            "right": True if i == right_index else False
        }
        answer_options.append(answer_object)
    return answer_options
