from TestSearch import *

# Requirement for interpolation is values should be uniformly distributed.
# Binary Search always goes to the middle element to check.
# On the other hand, interpolation search may go to different locations
# according to the value of the key being searched. For example,
# if the value of the key is closer to the last element,
# interpolation search is likely to start search toward the end side.
# pos = lo + [ (x-arr[lo])*(hi-lo) / (arr[hi]-arr[Lo]) ]
# arr[] ==> Array where elements need to be searched
# x     ==> Element to be searched
# lo    ==> Starting index in arr[]
# hi    ==> Ending index in arr[]

def interpolation_search (deck: list, lo:int, high:int, query:int) -> int:

    if (lo <= high and deck[lo] >= query and deck[high] <= query):
        print("deck: ",deck)
        if deck[lo] == deck[high]:
            pos = int((lo + high )/2)
        else:
            pos = int(lo + (((query-deck[high])*(high-lo))/(deck[lo]-deck[high])))
        print("Pos: ",pos)

        if deck[pos] == query:
            return pos

        if deck[pos] > query:
            return interpolation_search(deck, pos+1, high, query)

        if deck[pos] < query:
            return interpolation_search(deck, lo, pos-1, query)

        return -1

    else:
        return -1

def interpolation_search_top  (deck: list, query:int) -> int:
    if len(deck) > 0:
        return interpolation_search(deck,0,len(deck)-1,query)
    else:
        return -1

for test in test_list:
    if interpolation_search_top(**test['input']) == test['result']:
        print("PASS")
    else:
        print("FAIL")