from TestSearch import *

def LinearSearch (deck: list, query: int) -> int:
    for index,item in enumerate(deck):
        if item == query:
            return index
    return -1

for test in test_list:
    if LinearSearch(**test['input']) == test['result']:
        print("PASS")
    else:
        print("FAIL")

