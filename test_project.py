from player.Player import Player
from player.leaderboard import get_scores, write_score, get_board
from project import load_countries, use_joker, get_random
from random import randint
from unittest import mock


### Tests for player class
def test_new_player():
    """New player should have 3 lifes, 1 joker and 0 points"""
    new_player = Player("kluengels")
    assert new_player.lifes == 3
    assert new_player.points == 0
    assert new_player.joker50 == 1


def test_player_str_method():
    """Check str output for new playder"""
    new_player = Player("Bob")
    assert str(new_player) == "You have 3 lifes and 1 joker left.\n"


def test_lifes():
    """Check if subtracting from lifes works"""
    new_player = Player("Player1")
    new_player.withdraw_life()
    assert new_player.lifes == 2

    new_player2 = Player("Player2")
    new_player2.withdraw_life()
    new_player2.withdraw_life()
    new_player2.withdraw_life()
    assert new_player2.lifes == 0


def test_add_points():
    """Check if addidng points works"""
    new_player = Player("xyz")
    for _ in range(10):
        new_player.add_point()
    new_player.points == 10


def test_id():
    """Id of a new player should be length of leaderboard + 1"""
    length = len(get_scores())
    player1 = Player("Player 1")
    assert player1.id == length + 1


### Test on countries.json data
def test_countries():
    """Checks if list of countries is properly loaded"""
    data = load_countries()

    # data should contain dicts for more than 190 countries
    assert len(data) > 190

    # Sample check if United States, Sweden, Germany and Ghana are in data
    countries_to_Test = ["United States", "Sweden", "Ghana", "Germany"]
    for c in countries_to_Test:
        assert any(country["name"]["common"] == c for country in data)

    # check if keys important for the quizzes exit within the data for a rondom country
    random_index = randint(0, 190)
    all_keys = list(data[random_index].keys())
    print(all_keys)
    keys_to_check = ["area", "population", "flags", "borders", "capital"]
    for k in keys_to_check:
        assert k in keys_to_check


### Tests on leaderboard
def test_write_score():
    """Check if player data is appended"""

    # create player for testing
    player1 = Player("player1")
    player1.add_point()  # player should now have 1 point

    # write to file
    write_score(player1)

    # get scores
    leaderboard = get_scores()

    # check if player dict is in data
    assert vars(player1) in leaderboard


### Tests on quiz functions
def test_use_joker():
    """Test if Joker will exclude two wrong answer options"""
    answers = [
        {"index": 1, "name": "Armenia", "right": False},
        {"index": 2, "name": "India", "right": False},
        {"index": 3, "name": "Norway", "right": False},
        {"index": 4, "name": "Åland Islands", "right": True},
    ]
    reduced_answers = use_joker(answers)
    assert len(reduced_answers) == 2
    assert any("right" in answer for answer in reduced_answers) == True


@mock.patch("project.random.randint", return_value=[1, 2, 3, 4, 6])
def test_get_random(mocked_randint):
    countries_data = [
        {
            "flags": {
                "png": "https://flagcdn.com/w320/md.png",
                "svg": "https://flagcdn.com/md.svg",
                "alt": "The flag of Moldova is composed of three equal vertical bands of blue, yellow and red, with the national coat of arms centered in the yellow band.",
            },
            "name": {
                "common": "Moldova",
                "official": "Republic of Moldova",
                "nativeName": {
                    "ron": {"official": "Republica Moldova", "common": "Moldova"}
                },
            },
            "capital": ["Chi\u0219in\u0103u"],
            "borders": ["ROU", "UKR"],
            "area": 33846.0,
            "population": 2617820,
        },
        {
            "flags": {
                "png": "https://flagcdn.com/w320/us.png",
                "svg": "https://flagcdn.com/us.svg",
                "alt": "The flag of the United States of America is composed of thirteen equal horizontal bands of red alternating with white. A blue rectangle, bearing fifty small five-pointed white stars arranged in nine rows where rows of six stars alternate with rows of five stars, is superimposed in the canton.",
            },
            "name": {
                "common": "United States",
                "official": "United States of America",
                "nativeName": {
                    "eng": {
                        "official": "United States of America",
                        "common": "United States",
                    }
                },
            },
            "capital": ["Washington, D.C."],
            "borders": ["CAN", "MEX"],
            "area": 9372610.0,
            "population": 329484123,
        },
        {
            "flags": {
                "png": "https://flagcdn.com/w320/yt.png",
                "svg": "https://flagcdn.com/yt.svg",
                "alt": "",
            },
            "name": {
                "common": "Mayotte",
                "official": "Department of Mayotte",
                "nativeName": {
                    "fra": {
                        "official": "D\u00e9partement de Mayotte",
                        "common": "Mayotte",
                    }
                },
            },
            "capital": ["Mamoudzou"],
            "borders": [],
            "area": 374.0,
            "population": 226915,
        },
        {
            "flags": {
                "png": "https://flagcdn.com/w320/nr.png",
                "svg": "https://flagcdn.com/nr.svg",
                "alt": "The flag of Nauru has a dark blue field with a thin yellow horizontal band across the center and a large white twelve-pointed star beneath the horizontal band on the hoist side of the field.",
            },
            "name": {
                "common": "Nauru",
                "official": "Republic of Nauru",
                "nativeName": {
                    "eng": {"official": "Republic of Nauru", "common": "Nauru"},
                    "nau": {"official": "Republic of Nauru", "common": "Nauru"},
                },
            },
            "capital": ["Yaren"],
            "borders": [],
            "area": 21.0,
            "population": 10834,
        },
        {
            "flags": {
                "png": "https://flagcdn.com/w320/mz.png",
                "svg": "https://flagcdn.com/mz.svg",
                "alt": "The flag of Mozambique is composed of three equal horizontal bands of teal, black with white top and bottom edges, and yellow. A red isosceles triangle spanning about two-fifth the width of the field is superimposed on the hoist side with its base on the hoist end. This triangle bears a crossed rifle and hoe in black superimposed on an open white book which is superimposed on a five-pointed yellow star.",
            },
            "name": {
                "common": "Mozambique",
                "official": "Republic of Mozambique",
                "nativeName": {
                    "por": {
                        "official": "Rep\u00fablica de Mo\u00e7ambique",
                        "common": "Mo\u00e7ambique",
                    }
                },
            },
            "capital": ["Maputo"],
            "borders": ["MWI", "ZAF", "SWZ", "TZA", "ZMB", "ZWE"],
            "area": 801590.0,
            "population": 31255435,
        },
        {
            "flags": {
                "png": "https://flagcdn.com/w320/br.png",
                "svg": "https://flagcdn.com/br.svg",
                "alt": "The flag of Brazil has a green field with a large yellow rhombus in the center. Within the rhombus is a dark blue globe with twenty-seven small five-pointed white stars depicting a starry sky and a thin white convex horizontal band inscribed with the national motto 'Ordem e Progresso' across its center.",
            },
            "name": {
                "common": "Brazil",
                "official": "Federative Republic of Brazil",
                "nativeName": {
                    "por": {
                        "official": "Rep\u00fablica Federativa do Brasil",
                        "common": "Brasil",
                    }
                },
            },
            "capital": ["Bras\u00edlia"],
            "borders": [
                "ARG",
                "BOL",
                "COL",
                "GUF",
                "GUY",
                "PRY",
                "PER",
                "SUR",
                "URY",
                "VEN",
            ],
            "area": 8515767.0,
            "population": 212559409,
        },
        {
            "flags": {
                "png": "https://flagcdn.com/w320/cv.png",
                "svg": "https://flagcdn.com/cv.svg",
                "alt": "The flag of Cape Verde is composed of five horizontal bands of blue, white, red, white and blue in the ratio of 6:1:1:1:3. A ring of ten five-pointed yellow stars is centered at three-eighth of the height from the bottom edge and three-eighth of the width from the hoist end of the field.",
            },
            "name": {
                "common": "Cape Verde",
                "official": "Republic of Cabo Verde",
                "nativeName": {
                    "por": {
                        "official": "Rep\u00fablica de Cabo Verde",
                        "common": "Cabo Verde",
                    }
                },
            },
            "capital": ["Praia"],
            "borders": [],
            "area": 4033.0,
            "population": 555988,
        },
    ]
    assert get_random(countries_data) == ([1,2,3,4], 6)
