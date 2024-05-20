### Prompt user for his answer to quiz question, offer joker

import sys
from termcolor import colored, cprint # color text

def check_answer(answers, right_answer, player, joker=False):
    possible_answers = [item['index'] for item in answers]
    
    while True:
        try:
            # offer player to use a 50/50 joker if not already done and joker left
            if joker == False and player.joker50 > 0:
                answer = input("Your answer (or 'J' for Joker): ").strip().lower()
                if answer == "j" or answer == "'j'" or answer == "joker":
                    # return if user wants joker
                    return True
            else:
                answer = input("Your answer: ").strip().lower()   
        except KeyboardInterrupt:
            print()
            sys.exit("See you next time!")

        try:
            # make sure answer is not empty and an integer
            answer = int(answer[0])
            # stop asking for an answer if user typed a valid int
            if answer in possible_answers:
                break
            else: 
                raise ValueError
        except (IndexError, ValueError):
            print(f"Please enter a valid number")
            continue

    # check if answer is correct
    for a in answers:
        if a["index"] == answer:
            selected = a

    if selected["right"]:
        # player scores
        player.add_point()
        print( colored("That's correct. Congratulations", "green"))
        
    else:
        # player looses one life
        player.withdraw_life()
        print(colored(f"That's wrong. The right answer would have been {right_answer}.", "red"))

    # exit with false (means: user did not ask for a joker)
    return False # means: no joker used
