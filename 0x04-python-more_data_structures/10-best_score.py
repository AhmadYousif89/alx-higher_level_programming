#!/usr/bin/python3
def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or not a_dictionary:
        return None

    best_score = float('-inf')  # Case of negative scores
    winner = None

    for name, score in a_dictionary.items():
        if score is not None and score > best_score:
            best_score = score
            winner = name

    return winner
