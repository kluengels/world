### leaderboard

import os
import json
from tabulate import tabulate  # pretty print table
from termcolor import colored, cprint  # color text


def get_scores():
    """read scores.json, load date into memory"""
    # create leaderboard file if it does not exit
    if not os.path.isfile("scores.json"):
        open("scores.json", "x")

    # read high score file
    with open("scores.json", "r") as file:
        try:
            file_data = json.load(file)
            file_data = sorted(
                file_data, key=lambda item: item["_points"], reverse=True
            )
        except:
            file_data = []
        return file_data


def write_score(player):
    """Append player object to file"""
    scores = get_scores()
    scores.append(player)

    # write to high scores file
    with open("scores.json", "w") as file:
        json.dump(scores, file, default=vars, indent=2)


def get_board(player):
    """creates top 10 in table, player will be green if he reached top10"""
    # get scores
    scores = get_scores()
    top_scores = []

    # helper: i keeps track of index, n keeps track of rank
    n = 1
    i = 0

    # leaderboard shall be Top 10 only
    if len(scores) > 10:
        r = 10
    else:
        r = len(scores)

    # create top 10 list of objects
    for _ in range(r):
        try:
            if top_scores[i - 1]["Points"] == scores[i]["_points"]:
                rank = n
            else:
                n += 1
                rank = n

        except IndexError:
            rank = n

        # mark acutual player in top 10
        if scores[i]["_id"] == player.id:
            name = colored(f"{scores[i]['_name']}", "green")
        else:
            name = scores[i]["_name"]

        item = {"Rank": rank, "Name": name, "Points": scores[i]["_points"]}
        top_scores.append(item)
        i += 1

    # create table out of top 10
    return tabulate(top_scores, headers="keys", tablefmt="outline")
