### presents quiz options without the ones excluded by joker

def display_options(answers: list, exclude=[]):
    for a in answers:
        if a["index"] not in exclude:
            print(f"{a['index']}) {a['name']}")
        else:
            print()