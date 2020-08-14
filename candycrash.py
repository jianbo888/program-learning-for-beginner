def crashCandies(candies):
    candyStack = [[None, 0]]
    candies.append(None)

    curr = 0
    while curr < len(candies):
        lastSeen = candyStack[-1]
        if candies[curr] == lastSeen[0]:
            candyStack[-1][1] += 1;
        elif lastSeen[1] >= 3:
            candyStack.pop()
            continue
        else:
            candyStack.append([candies[curr], 1])
        curr += 1

    if len(candyStack) == 1:
        return []
    else:
        return candyStack[1:-1]


print (crashCandies([1,1,2,2,3,3,3,2]))
print (crashCandies([1,1,2,2,3,3,3,2,1]))

