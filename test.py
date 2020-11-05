#!/usr/bin/env python3

import numpy as np

rock, paper, scissors = np.identity(3)

def f(a, b):
    """
    a is your hand.
    b is the opponent's hand.
    f(a,b) = 1 means you win.
    f(a,b) = 0 means a draw.
    f(a,b) = -1 means you lose.
    """
    return np.dot(np.cross(b, a), 1 - a - b)

def test_play(a, b, actual):
    correct = f(a, b) == actual
    print(f"{a=} {b=} {f(a, b)=} {actual=} {correct=}")
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

