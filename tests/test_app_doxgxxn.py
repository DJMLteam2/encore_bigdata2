from encore_bigdata2.app_doxgxxn import coin_game

## 인풋 값을 받기 때문에 pytest 작동안해서 pytest -s로 테스트 했습니다
def test_game():
    coin_game(3)
    assert True