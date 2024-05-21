# Joker eliminates two answers
import random

def use_joker(answers):
    indexes_wrong_answers = []
    for a in answers:
        if not a["right"]:
             indexes_wrong_answers.append(a["index"])
    indices_to_remove = random.sample(indexes_wrong_answers, 2)
    print("exclude", indices_to_remove)

    # Filtering the list to remove the tow randomly selected wrong answers
    reduced_answers = [answer for answer in answers if answer['index'] not in indices_to_remove]
   
    print("reduced", reduced_answers)
    return reduced_answers
