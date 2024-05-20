
# import game modes



def start_quiz(countries, player):
   # randomly choose game mode
        print()
        modes = ["flags", "capitals", "population", "borders", "area"]
        # mode = random.choice(modes)
        mode = "flags"

        # Guess which country belongs to flag
        if mode == "flags":
            from quizzes.flags import flags
            flags(countries, player)

        # # Guess population of a country
        # elif mode == "population":
        #     population(countries, player)

        # # Guess the capital of a country
        # elif mode == "capitals":
        #     capitals(countries, player)

        # # Guess which country is not a neighbor of a country
        # elif mode == "borders":
        #     borders(countries, player)

        # # Guess which country is biggest (area)
        # elif mode == "area":
        #     area(countries, player)

        # print(player)
        # print() 