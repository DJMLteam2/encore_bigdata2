from src.encore_bigdata2.app_jiug import play_card_game

def test_play_card_game():
    result = play_card_game(5)
    assert isinstance(result, list)
    assert all(isinstance(i, int) for i in result)
    assert all(0 <= i <= 26 for i in result)