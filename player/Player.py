### Player class
import sys


class Player:
    # initialize object
    def __init__(
        self,
        name,
        lifes=3,
        points=0,
        exclude={
            "flags": [],
            "borders": [],
            "capitals": [],
            "population": [],
            "area": [],
        },
    ):
        # define instance variables
        self.name = name
        self.points = points
        self.lifes = lifes
        self.joker50 = 1
        # remember countries that have been subject to quiz question already
        self.exclude = exclude

    # define print method
    def __str__(self):
        if self.joker50 == 1:
            joker_str = "joker"
        else:
            joker_str = "jokers"
        return f"You have {self.lifes} lifes and {self.joker50} {joker_str} left.\n"

    # method to create new instance of Player
    @classmethod
    def get(cls):
        while True:
            try:
                name = input("Enter your name (Ctr+C to exit): ").strip()
                # reprompt user if username not valid
                if name == "":
                    continue
                if len(name) > 8:
                    print("Your username must not have more than 8 characters")
                    continue
                if not name.isalnum():
                    print("Only alphanumeric characters allowed")
                    continue
                return cls(name)
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

    # getter for exclude
    @property
    def exclude(self):
        return self._exclude

    # setter for exclude
    @exclude.setter
    def exclude(self, exclude):
        if isinstance(exclude, dict):
            self._exclude = exclude
        else:
            raise ValueError("grades must be a dictionary")

    def add_exclude(self, country_code, mode):
        if mode not in ["flags", "capitals", "borders", "population", "area"]:
            raise ValueError(f"game mode {mode} does not exist")
        self._exclude[mode].append(country_code)
        # print(self.exclude[mode])
        # new_exclude_list = self._exclude[0][mode].append(index)
        # self._exclude = new_exclude_list
