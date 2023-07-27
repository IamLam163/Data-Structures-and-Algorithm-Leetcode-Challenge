def find_position(cards, query, mid):
    mid_card = cards[mid]
    if mid_card == query:
        if mid - 1 >= 0 and cards[mid - 1] == query:
            return "Search left"
        else:
            return "Mid Found"
    if mid_card < query:
        return "Search left"
    else:
        return "Search right"

def locate_card(cards, query):
    start, end = 0, len(cards) - 1

    while start <= end:
        mid = (start + end) // 2
        result = find_position(cards, query, mid)

        if result == "Mid Found":
            return mid
        elif result == "Search left":
            end = mid - 1
        elif result == "Search right":
            start = mid + 1

    return -1

tests = []

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
    "output": -1
})

tests.append({
    "input": {
        "cards": [8,8,6,6,6,6,5, 3, 3],
        "query": 6
    },
    "output": 2
    })
