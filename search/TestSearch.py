#############################################################
# Assume a simple problem, There is a deck of card arranged in
# decreasing order. Given a query(number), you have to find
# the card position in minimum possible operations.

test_list = []
# If card in center of deck
test1 = {
        'input' : {
                        'deck' : [13,12,11,10,6,5,4,3,2,0],
                        'query': 6
        },
        'result' : 4
}
test_list.append(test1)

# If card in first card of deck
test2 = {
    'input' : {
        'deck' : [13,12,11,10,6,5,4,3,2,0],
        'query': 13
    },
    'result' : 0
}
test_list.append(test2)

# If card in last card of deck
test3 = {
    'input' : {
        'deck' : [13,12,11,10,6,5,4,3,2,0],
        'query': 0
    },
    'result' : 9
}
test_list.append(test3)

# If card in not in card of deck
test4 = {
    'input' : {
        'deck' : [13,12,11,10,6,5,4,3,2,0],
        'query': 15
    },
    'result' : -1
}
test_list.append(test4)

# If card in multiple positions
test5 = {
    'input' : {
        'deck' : [13,12,11,11,11,5,4,3,2,0],
        'query': 11
    },
    'result' : 2
}
test_list.append(test5)

# If list is empty
test6 = {
    'input' : {
        'deck' : [],
        'query': 11
    },
    'result' : -1
}
test_list.append(test6)

#print(test_list)