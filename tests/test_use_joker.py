from utils.use_joker import use_joker


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
