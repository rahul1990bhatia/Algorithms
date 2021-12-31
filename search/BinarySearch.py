from TestSearch import *

def BinarySearch (deck: list, low: int, high:int, query: int) -> int:

    if high >= 1:
        mid = (high + low) // 2
        if deck[mid] == query:
            return mid
        elif deck[mid] > query:
            return BinarySearch(deck, mid+1, high, query)
        elif deck[mid] < query:
            return BinarySearch(deck, low, mid, query)
    else:
        return -1

def BinarySearchTop ( deck: list, query: int) -> int:

    high = len(deck)
    low = 0
    if high >= 0:
        return BinarySearch(deck,low, high, query)
    else:
        return -1

for test in test_list:
    if BinarySearchTop(**test['input']) == test['result']:
        print("PASS")
    else:
        print("FAIL")
