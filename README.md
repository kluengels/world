# WORLD QUIZ

#### Video Demo:

not available yet
<URL HERE>

#### Web Version:

You will find a web version of World Quiz on [Python Anywhere](kluengels.pythonanywhere.com)

#### Description:

Word Quiz is a terminal based quiz game written in Python. It generate geographic quiz questions based on data pulled from [Rest Countries](https://restcountries.com/). Each question belongs to one of the following game modes, which is randomly chosen for each new question:

- "area": Which of the following countries has the biggest area?
- "borders": Which country has no border with X?
- "capitals": What is the capital of X?
- "flags": (displays a flag) To which country does this flag belong to?
- "population": How many people live in X?

A new player will start with 3 lifes and 1 50/50-joker. He will get new questions as long as he has a least one life left. For each question the program will generate four answer options, with only one answer beeing right. THe joker can be used once in the game to eleminate two wrong answers from the answer options.

When the player has lost all lifes his result will be written to a database. The game displays the leaderboard with Top-10-players and marks the player name in green if he has just reached the leaderboard. Afterwards the player is asked if he wants to play another round.

To start world quiz make sure your system meet all requirements (see below) and start project.py:

    python project.py

##### Structure:

Below are listed all files and folders and what they do.

###### Main folder:

- **project.py**: call this file to start world quiz. contains most of the game logic
- **player/Player.py**: Player class. When a user starts the game an instance of that class will be generated. Used to keep track of lifes, jokers and countries that have already been subject of a question in a specific game mode. This avoids duplicate questions.
- **player/leaderboard.py**: functions to write data to the leaderboard database file and read from it.
- **test_project.py**: contains unit tests, to be used with pytest. start with this command: `pytest test_project.py`
- **update_countries.py**: if this file is executed directly from the terminal it updates the file countries.json (see below)
- **requirments.txt**: lists all pip libraries that need to be installed before executing project.py
- **leaderboard.db**: database for the leaderboard with table "leaderboard" containing columns "id", "name", "score" and "date"
- **pytest.ini**: configuration for pytest - deprecation warnings are supressed
- **countries.json**: prefetched data from [Rest Countries](https://restcountries.com/), contains info about all independent countries
- **.gitnore**: lists file that do not need to be uploaded to github (e.g. cache)

###### Quizzes folder:

All game modes share most of the logic. However the answer options have some special logic for each mode to prepare the raw data. Also what is considered as "right answer" may differ from game mode to game mode. The mode "flags" also need a mechanism to fetch images of countries from the web with help of the link provided in the raw data. I chose to exclude these game mode specific functions from the main file to improve readability.

- **quizzes/area.py**: Special logic for "area" quiz mode
- **quizzes/borders.py**: Special logic for "borders" quiz mode
- **quizzes/capitals.py**: Special logic for "capitals" quiz mode
- **quizzes/flags.py**: Special logic for "flags" quiz mode
- **quizzes/population.py**: Special logic for "population" quiz mode
- **quizzes/**init**py**: Empty file that indicates to the interpreter that the whole folder can be seen as a module

##### Requirements:

To run World Quiz you will nedd python version 3.10 or above installed. You also need an internet connection as data from APIs is fetched. All required libraries are listed in the requirements.text. They can be installed using pip

    pip install -r requirements.txt

Find below a brief description what the libraries are used for:

- **cs50**: provides a module "SQL" that fascilitates writing to and reading from a SQLite database
- **colored /termcolor**: used to print colored text to the terminal
- **art**: used to print ASCII art to the terminal (used for opening screen)
- **climage**: converts image to ascii-art (used to display flags)
- **Pillow**: adds image processing capabilities to Python interpreter (used to display flags)
- **Requests**: used for http requests to fetch countries data and images of flags
- **tabulate**: pretty print tables (used for leaderboard)
- **pytest**: used for unit testing

##### Challenges during developement:

World Quiz is meant to be my final project for [Harvards CS50P](https://cs50.harvard.edu/python/2022/). I struggled a bit with the requirements, as they force students to put most of the logic in the main file. I would have liked to outsource more functions in seperate files to improve readability. It was also difficult to create useful unit tests as a lot of steps in the quiz involve random choices.

A general challenge was to make sure that in every game mode the right objects are fetched from the raw data. It is quite easy to mess up and accidentally show answer options that are all wrong.

##### Limitations / TODOs:

I wanted to create a terminal based game reflecting the charme of old-school computer games. However I think this World Quiz is not super-accessible as it requires a download and the installation of python and some libraries. This is why I created a web-based version on top, which can be found on [Python Anywhere](kluengels.pythonanywhere.com). This version emulates a terminal in the browser.

In general World Quiz heavily relies on the data provided by Restcountries. Though it is great piece of open source it can not be guaranteed that the data is accurate and up-to-date in all cases.

Future iterations of World Quiz could include more game modes and options to limit the quiz questions to certain regions. Furthermore a shared leaderboard would be nice and could be realized with a hosted SQL database.
