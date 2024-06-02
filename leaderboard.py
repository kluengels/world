### leaderboard

from tabulate import tabulate  # pretty print table
from termcolor import colored  # color text
from cs50 import SQL
from datetime import datetime

# set up database
db = SQL("sqlite:///leaderboard.db")


def write_score(player):
    """Append player  to leaderboard"""
     # insert player into leaderboard and get id identifier back
    id = db.execute(
        "INSERT INTO leaderboard (name, score, date) VALUES(?, ?, ?)",
        player.name,
        player.points,
        datetime.now(),
    )
    return id 


def get_board(id):
    """creates top 10 in table, player will be green if he reached top10"""
    # get top ten from database
    results = db.execute(
        "SELECT id, name, score, date FROM leaderboard ORDER BY score DESC LIMIT 10"
    )

    # check if player is in top ten and mark his name 
    player_object = [obj for obj in results if obj["id"] == id]
    if (len(player_object)) == 1:
        print("true")
        index_of_player_object = results.index(player_object[0])
        name = results[index_of_player_object]["name"]
        # mark player in green
        results[index_of_player_object]["name"] = colored(f"{name}", "green")

    # add rank to objects
    results_with_rank = []
    rank = 0
    for i in range(len(results)):
        # if first in list -> rank 1
        if i == 0:
            rank = 1

        # if same score then player above -> rank does not change
        elif results[i - 1]["score"] == results[i]["score"]:
            rank = rank

        # if score is lower -> increment rank
        else:
            rank += 1

        # append new item with rank to results list
        item = {"Rank": rank, "Name": results[i]["name"], "Score": results[i]["score"], "Date": results[i]["date"]}
        results_with_rank.append(item)

    # create table
    table = f'{tabulate(results_with_rank, headers="keys", tablefmt="outline")}'

    return table

