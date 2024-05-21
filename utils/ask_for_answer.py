### presents answer options (and joker option) to player 

import sys

def ask_for_answer(answer_options, player, joker=False) -> int:
    possible_answers = [item['index'] for item in answer_options]
    while True:
        try:
            # offer player to use a 50/50 joker if not already done and joker left
            if joker == False and player.joker50 > 0:
                answer = input("Your answer (or 'J' for Joker): ").strip().lower()
                if answer == "j" or answer == "'j'" or answer == "joker":
                    # return if user wants joker
                    return 0
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
                return answer
            else: 
                raise ValueError
        except (IndexError, ValueError):
            print(f"Please enter a valid number")
            continue
