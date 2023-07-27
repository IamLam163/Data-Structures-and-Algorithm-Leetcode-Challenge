#!/usr/bin/python3
"""Linear Search"""
'''
steps to solve a linear search:
        1. initialize a variable to track position of the iter
        2. define a condition(a loop)
        3. check if the input matches the query
        4. check or return when it reaches the end of the loop
'''
'''
def find_card(cards, query):
        position = 0

        while position < len(cards):
                if cards[position] == query:
                        print(position)
                        break
                
                position += 1

                if position == len(cards):
                        print("Not Found!")
                        return -1
'''

tests = []

#tests.append(test)

tests.append({
        "input": {
                "cards": [13, 11, 10, 7, 4, 3, 1, 0],
                "query": 0
                },
        "output": 7
        })

tests.append({
        "input": {
                "cards": [4, 2, 1, -1],
                "query": 4 
                },
        "output": 0
        })

tests.append({
        "input": {
                "cards": [3, -1, -9, -127],
                "query": -127
                },
        "output": 3
        })

tests.append({
        "input": {
                "cards": [6],
                "query": 6
                },
        "output": 0
        })

tests.append({
        "input": {
                "cards": [5, 6, 1, 4, 9],
                "query": 7
                },
        "output": -1
        })
tests.append({
        "input": {
                "cards": [],
                "query": 6
                },
        "output": 0
        })
tests.append({
        "input": {
                "cards": [8,8,6,6,6,6,5, 3, 3],
                "query": 6
                },
        "output": 2
        })
'''
#print(tests)
for test in tests:
        print(test)
        print()
        find_card(**test["input"]) == test["output"]



BINARY SEARCH
Steps:
        1. Check if the array is sorted. If it is;
        2. divide the array by two by picking the middle element
        3. select the mid element again, do this till you pick your card
'''

def find_card(cards, query):
        start, end = 0, len(cards) - 1

        while start <= end:
                mid = (start + end ) // 2
                mid_card = cards[mid]

                print("start", start, "end", end, "mid", mid, "mid_card", mid_card)

                if mid_card == query:
                        return print(mid) 
                elif mid_card < query:
                        start = mid + 1
                elif mid_card > query:
                        end = mid - 1

        return -1

#tests = []

#tests.append(test)

tests.append({
        "input": {
                "cards": [1, 4, 5, 7, 9, 13, 15, 20],
                "query": 13
                },
        "output": 5
        })
#start 3 end 7 mid 5 mid_card 13


def find_position(cards, query, mid):
        mid_card = cards[mid]
        if mid_card == query:
                if mid - 1 >= 0 and mid_card - 1 == query:
                        return print("Search left")
                else:
                        return ("Mid Found")
        if mid_card < query:
                return print("Search left")
        else:
                return print("Search right")

def locate_card(cards, query):
        start, end = 0, len(cards) -1

        while start <= end:
                mid = (start + end) // 2
                result = find_position(cards, query, mid)

                if result == "found":
                        return print(mid)
                elif result == 'Search left':
                        end = mid -1
                elif result == "Search right":
                        start = mid + 1
        return -1

for test in tests:
        print(test)
        print()
        locate_card(**test["input"]) == test["output"]


