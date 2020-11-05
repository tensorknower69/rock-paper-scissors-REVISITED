#!/usr/bin/env python3

import numpy as np

rock, paper, scissors = np.identity(3)

def play(a, b):
    """
    returns whether the player playing 'a' wins or not:
        +1 means he/she wins.
        0 means its a draw.
        -1 means he/she loses.
    """
    return np.dot(np.cross(b, a), 1 - a - b)

def test_play(a, b, actual):
    pred = play(a, b)
    correct = pred == actual
    print(f"{a=} {b=} {pred=} {actual=} {correct=}")
    return correct

a = [
        test_play(rock, rock, 0),
        test_play(rock, paper, -1),
        test_play(rock, scissors, 1),
        test_play(paper, rock, 1),
        test_play(paper, paper, 0),
        test_play(paper, scissors, -1),
        test_play(scissors, rock, -1),
        test_play(scissors, paper, 1),
        test_play(scissors, scissors, 0),
    ]

if all(a):
    print("All tests passed")
