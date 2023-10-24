import random

def play_card_game(n: int) -> list:
    """Play a card game n times. Returns a list of results."""
    results = []  # Store game results
    for _ in range(n):
        player_sum = random.randint(0,13) + random.randint(0,13)
        if player_sum == 21:
            print("Victory!")  # Player wins!
        elif player_sum > 21:
            print("Defeat!")   # Player loses.
        else:
            print(f"{player_sum}")
        results.append(player_sum)
    return results
