from TestSearch import *
import math

def JumpSearch (deck: list, query: int) -> int:

    deck_len = len(deck)
    step = int(math.floor(math.sqrt(deck_len)))
    prev = 0

    if deck_len == 0:
        return -1

    # Find step in which value exist
    while deck[min(step,deck_len)-1] > query:
        prev = step
        step = step + int(math.floor(math.sqrt(deck_len)))
        if prev >= deck_len:
            return -1


    while deck[prev] > query:
        prev = prev + 1
        if prev == min(step,deck_len):
            return -1

    if deck[prev] == query:
        return prev

    return -1

for test in test_list:
    if JumpSearch(**test['input']) == test['result']:
        print("PASS")
    else:
        print("FAIL")