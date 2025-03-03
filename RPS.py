import random

def player(prev_play, opponent_history=[]):
    """Function that plays Rock, Paper, Scissors intelligently"""
    if prev_play:
        opponent_history.append(prev_play)

    if len(opponent_history) < 3:
        return random.choice(["R", "P", "S"])  # Initial random choices

    # Frequency analysis to counter most common move
    counts = {move: opponent_history.count(move) for move in "RPS"}
    most_common = max(counts, key=counts.get)

    # Counter strategy
    counter = {"R": "P", "P": "S", "S": "R"}
    return counter[most_common]
