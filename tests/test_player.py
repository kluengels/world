from player.Player import Player
from player.leaderboard import get_scores


def test_new_player():
    """New player should have 3 lifes, 1 joker and 0 points"""
    new_player = Player("kluengels")
    assert new_player.lifes == 3
    assert new_player.points == 0
    assert new_player.joker50 == 1


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
    
