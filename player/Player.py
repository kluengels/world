### Player class
import sys
from player.leaderboard  import get_scores
class Player:
    # initialize object
    def __init__(self, name, id = 1, lifes = 3, points = 0):
        # define instance variables
        self.name = name
        self.id = id
        self.points = points
        self.lifes = lifes
        self.joker50 = 1

    # define print method
    def __str__(self):
        if self.joker50 == 1:
            joker_str = "joker"
        else:
            joker_str = "jokers"
        return f"You have {self.lifes} lifes and {self.joker50} {joker_str} left."
    

    #method to create new instance of Player
    @classmethod
    def get(cls):
        while True:
            try:
                name = input("Enter your name (Ctr+C to exit): ")
                return cls(name)
            except ValueError as e:
                print(e)
            except KeyboardInterrupt:
                print()
                sys.exit("See you next time")

    # getter for name
    @property
    def name(self):
        return self._name

    # setter for name
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Please enter a name")
        self._name = name

    # getter for id
    @property
    def id(self):
        return self._id

    # setter for id
    @id.setter
    def id(self, id):
        file_data = get_scores()
        self._id = len(file_data) + 1

    # getter for points
    @property
    def points(self):
        return self._points

    # setter for point
    @points.setter
    def points(self, points):
        self._points = points


    def add_point(self):
        self._points += 1

    # getter for lifes
    @property
    def lifes(self):
        return self._lifes
    
    # setter for lifes
    @lifes.setter
    def lifes(self, lifes):
        self._lifes = lifes

   
    def withdraw_life(self):
        self._lifes -= 1
        

