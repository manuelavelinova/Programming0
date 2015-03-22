def count_zero_pairs(items):
    n = len(items)
    count = 0
    result = []
    
    for i in range(0,n):
        for j in range(i,n):
            x = items[i]
            y = items[j]

            if x + y == 0:
                count += 1
                result += [x]
                result += [y]

    print(result)
    return count
            

print(count_zero_pairs([2,-2,3,-3,5,10]))
