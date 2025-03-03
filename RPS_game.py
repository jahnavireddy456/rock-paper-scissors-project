import random


def play(player1, player2, num_games, verbose=False):
    """Plays num_games of RPS between two players."""
    p1_history, p2_history = [], []
    p1_wins, p2_wins, ties = 0, 0, 0

    for _ in range(num_games):
        p1_move = player1(p2_history[-1] if p2_history else "")
        p2_move = player2(p1_history[-1] if p1_history else "")

        p1_history.append(p1_move)
        p2_history.append(p2_move)

        result = outcome(p1_move, p2_move)
        if result == 1:
            p1_wins += 1
        elif result == -1:
            p2_wins += 1
        else:
            ties += 1

        if verbose:
            print(f"Player 1: {p1_move} | Player 2: {p2_move} => Result: {result}")

    win_rate = (p1_wins / num_games) * 100
    print(f"Player 1 Wins: {p1_wins} ({win_rate:.2f}%) | Player 2 Wins: {p2_wins} | Ties: {ties}")
    return win_rate


def outcome(p1, p2):
    """Determines the outcome of a round"""
    if p1 == p2:
        return 0  # Tie
    elif (p1 == "R" and p2 == "S") or (p1 == "P" and p2 == "R") or (p1 == "S" and p2 == "P"):
        return 1  # Player 1 wins
    else:
        return -1  # Player 2 wins


# Bots
def quincy(prev_play, opponent_history=[]):
    sequence = ["R", "P", "S", "R", "P"]
    return sequence[len(opponent_history) % len(sequence)]


def abbey(prev_play, opponent_history=[]):
    if not prev_play:
        return "S"
    counter = {"R": "P", "P": "S", "S": "R"}
    return counter[prev_play]


def kris(prev_play, opponent_history=[]):
    return random.choice(["R", "P", "S"])


def mrugesh(prev_play, opponent_history=[]):
    if prev_play:
        opponent_history.append(prev_play)
    if len(opponent_history) < 3:
        return random.choice(["R", "P", "S"])

    most_common = max(set(opponent_history), key=opponent_history.count)
    counter = {"R": "P", "P": "S", "S": "R"}
    return counter[most_common]
