### check if answer given by user is correct 

import sys
from termcolor import colored, cprint # color text

def check_answer(answer_options, player_answer, right_answer, player,):
    # check if answer is correct
    for a in answer_options:
        if a["index"] == player_answer:
            selected = a

    if selected["right"]:
        # player scores
        player.add_point()
     
        print( colored("That's correct. Congratulations", "green"))
        
    else:
        # player looses one life
        player.withdraw_life()
        
        print(colored(f"That's wrong. The right answer would have been {right_answer}.", "red"))

