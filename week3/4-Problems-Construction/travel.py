def travel_cost(travels):
    allLines = 50
    cost = 0
    start = 0
    end = len(travels) - 1
    while start  <= end:
        if travels[start] < 23:
            cost += travels[start]
        elif travels[start] >= 23 and travels[start] < 50:
            cost += 23
        elif travels[start] >= 50:
            cost += 50
        start += 1
    if cost >= 50:
        return allLines
    else:
        return cost

