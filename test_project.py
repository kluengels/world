from player.Player import Player
from player.leaderboard import get_scores, write_score
from project import (
    load_countries,
    use_joker,
    get_random,
    filter_countries,
    create_answer_options,
    check_answer,
)
from random import randint


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
class TestCountries:
    # sample date for testing
    countries = [
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
            "cca3": "MDA",
            "capital": ["Chi\u0219in\u0103u"],
            "region": "Europe",
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
            "cca3": "USA",
            "capital": ["Washington, D.C."],
            "region": "Americas",
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
            "cca3": "MYT",
            "capital": ["Mamoudzou"],
            "region": "Africa",
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
            "cca3": "NRU",
            "capital": ["Yaren"],
            "region": "Oceania",
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
            "cca3": "MOZ",
            "capital": ["Maputo"],
            "region": "Africa",
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
            "cca3": "BRA",
            "capital": ["Bras\u00edlia"],
            "region": "Americas",
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
            "cca3": "CPV",
            "capital": ["Praia"],
            "region": "Africa",
            "borders": [],
            "area": 4033.0,
            "population": 555988,
        },
        {
            "flags": {
                "png": "https://flagcdn.com/w320/gq.png",
                "svg": "https://flagcdn.com/gq.svg",
                "alt": "The flag of Equatorial Guinea is composed of three equal horizontal bands of green, white and red with the national coat of arms centered in the white band and an isosceles triangle superimposed on the hoist side of the field. The triangle is light blue, has its base on the hoist end and spans about one-fifth the width of the field.",
            },
            "name": {
                "common": "Equatorial Guinea",
                "official": "Republic of Equatorial Guinea",
                "nativeName": {
                    "fra": {
                        "official": "R\u00e9publique de la Guin\u00e9e \u00c9quatoriale",
                        "common": "Guin\u00e9e \u00e9quatoriale",
                    },
                    "por": {
                        "official": "Rep\u00fablica da Guin\u00e9 Equatorial",
                        "common": "Guin\u00e9 Equatorial",
                    },
                    "spa": {
                        "official": "Rep\u00fablica de Guinea Ecuatorial",
                        "common": "Guinea Ecuatorial",
                    },
                },
            },
            "cca3": "GNQ",
            "capital": ["Malabo"],
            "region": "Africa",
            "borders": ["CMR", "GAB"],
            "area": 28051.0,
            "population": 1402985,
        },
        {
            "flags": {
                "png": "https://flagcdn.com/w320/al.png",
                "svg": "https://flagcdn.com/al.svg",
                "alt": "The flag of Albania features a silhouetted double-headed black eagle at the center of a red field.",
            },
            "name": {
                "common": "Albania",
                "official": "Republic of Albania",
                "nativeName": {
                    "sqi": {
                        "official": "Republika e Shqip\u00ebris\u00eb",
                        "common": "Shqip\u00ebria",
                    }
                },
            },
            "cca3": "ALB",
            "capital": ["Tirana"],
            "region": "Europe",
            "borders": ["MNE", "GRC", "MKD", "UNK"],
            "area": 28748.0,
            "population": 2837743,
        },
        {
            "flags": {
                "png": "https://flagcdn.com/w320/vi.png",
                "svg": "https://flagcdn.com/vi.svg",
                "alt": "",
            },
            "name": {
                "common": "United States Virgin Islands",
                "official": "Virgin Islands of the United States",
                "nativeName": {
                    "eng": {
                        "official": "Virgin Islands of the United States",
                        "common": "United States Virgin Islands",
                    }
                },
            },
            "cca3": "VIR",
            "capital": ["Charlotte Amalie"],
            "region": "Americas",
            "borders": [],
            "area": 347.0,
            "population": 106290,
        },
        {
            "flags": {
                "png": "https://flagcdn.com/w320/hm.png",
                "svg": "https://flagcdn.com/hm.svg",
                "alt": "",
            },
            "name": {
                "common": "Heard Island and McDonald Islands",
                "official": "Heard Island and McDonald Islands",
                "nativeName": {
                    "eng": {
                        "official": "Heard Island and McDonald Islands",
                        "common": "Heard Island and McDonald Islands",
                    }
                },
            },
            "cca3": "HMD",
            "capital": [],
            "region": "Antarctic",
            "borders": [],
            "area": 412.0,
            "population": 0,
        },
    ]

    # mock random selection of indexes and right_index
    indexes = [1, 4, 5, 8]  # USA, Mozambique, Brazil, Albania
    right_index = 1  # USA

    def test_filter_countries(self):
        player = Player("player")
        # mode "borders": 5 countries without borders should be excluded
        filtered = filter_countries(self.countries, "borders", player)
        assert len(filtered) == len(self.countries) - 5

        # mode "capitals": 1 country without capital should be excluded
        filtered = filter_countries(self.countries, "capitals", player)
        assert len(filtered) == len(self.countries) - 1

        # if player has received a question about a specific country in the same mode before
        # that should be filtered as well
        player.add_exclude(
            "MDA", "capitals"
        )  # MDA should be excluded though it has a value for capital
        filtered = filter_countries(self.countries, "capitals", player)
        assert len(filtered) == len(self.countries) - 2
        assert len([c for c in filtered if c["cca3"] == "MDA"]) == 0

    def test_get_random(self):
        # function should return 4 indexes and 1 "right_index", which is in indexes
        indexes, right_index = get_random(self.countries)
        assert len(indexes) == 4
        assert type(right_index) is int
        assert right_index in indexes

    def test_create_answer_options(self):
        ### mode "flags":
        options = create_answer_options(
            self.countries, self.indexes, self.right_index, "flags"
        )
        # should return 4 answers
        assert len(options) == 4
        # "United States", Mozambique, Brazil, Albania should be in options
        countries = ["United States", "Mozambique", "Brazil", "Albania"]
        for c in countries:
            assert c in str(options)
        # only 1 answer should be right
        assert len([o for o in options if o["right"] == True]) == 1
        # right answer should be USA
        assert [o for o in options if o["right"] == True][0]["name"] == "United States"

        ### mode "capitals"
        options = create_answer_options(
            self.countries, self.indexes, self.right_index, "capitals"
        )
        # should return 4 answers
        assert len(options) == 4
        # capital names of "United States", Mozambique, Brazil, Albania should be in options
        countries = ["Washington, D.C.", "Maputo", "Brasília", "Tirana"]
        for c in countries:
            assert c in str(options)
        # only 1 answer should be right
        assert len([o for o in options if o["right"] == True]) == 1
        # right answer should be Washington, D.C.
        assert [o for o in options if o["right"] == True][0][
            "name"
        ] == "Washington, D.C."

        ### mode "population"
        options = create_answer_options(
            self.countries, self.indexes, self.right_index, "population"
        )
        # should return 4 answers
        assert len(options) == 4
        # only 1 answer should be right
        assert len([o for o in options if o["right"] == True]) == 1
        # right answer should be 329.48 million (population of USA)
        assert [o for o in options if o["right"] == True][0]["name"] == "329.48 million"

        ### mode "area"
        options = create_answer_options(
            self.countries, self.indexes, self.right_index, "area"
        )
        # should return 4 answers
        assert len(options) == 4
        # "United States", Mozambique, Brazil, Albania should be in options
        countries = ["United States", "Mozambique", "Brazil", "Albania"]
        for c in countries:
            assert c in str(options)
        # only 1 answer should be right
        assert len([o for o in options if o["right"] == True]) == 1
        # right answer should be USA
        assert [o for o in options if o["right"] == True][0]["name"] == "United States"

        ### mode "borders" not tested here as logic is more complex


def test_check_answer():
    """Test if wrong answer will withdraw life from player, while right answer adds point"""
    player1 = Player("Player 1")  # initial lifes: 3, points: 0
    answer_options = [
        {"index": 1, "name": "Armenia", "right": False},
        {"index": 2, "name": "India", "right": False},
        {"index": 3, "name": "Norway", "right": False},
        {"index": 4, "name": "Åland Islands", "right": True},
    ]

    # player gives wrong answer
    player_answer = randint(1, 3)
    check_answer(answer_options, player_answer, "right_answer", player1)
    # player should loose one life
    assert player1.lifes == 2

    # player gives right answer
    player_answer = 4
    check_answer(answer_options, player_answer, "right_answer", player1)
    assert player1.points == 1


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
