### get N random countries

import random

# Configuration: Number of options for each question
N = 4


def get_random(countries):
    # seclet N random countries by index
    indexes = []
    n = 0
    while n < N:
        i = random.randint(0, len(countries) - 1)
        if i not in indexes:
            indexes.append(i)
            n +=1

    # choose the country the question will be about
    right_index = indexes[random.randint(0, len(indexes) - 1)]

    return indexes, right_index