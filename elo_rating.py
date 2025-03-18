def calculate_elo(player_rating, opponent_rating, result, k=32):
    """
    Calculates the new Elo rating for a player.

    :param player_rating: Current rating of the player
    :param opponent_rating: Current rating of the opponent
    :param result: 1 if player wins, 0 if player loses, 0.5 for a draw
    :param k: K-factor (default is 32)
    :return: New Elo rating
    """
    expected_score = 1 / (1 + 10 ** ((opponent_rating - player_rating) / 400))
    new_rating = player_rating + k * (result - expected_score)
    return round(new_rating)

# Example usage
if __name__ == "__main__":
    player1_rating = 1000
    player2_rating = 1100
    result = 1  # 1 if player1 wins, 0 if player1 loses, 0.5 for a draw

    new_player1_rating = calculate_elo(player1_rating, player2_rating, result)
    new_player2_rating = calculate_elo(player2_rating, player1_rating, 1 - result)

    print(f"New ratings -> Player 1: {new_player1_rating}, Player 2: {new_player2_rating}")
