def count_zero_neighbours(numbers):
    start = 0
    end = len(numbers) - 1
    result = []
    count = 0

    for number in numbers:
        if start < end:
            neighbour = numbers[start + 1]

            if number + neighbour == 0:
                count += 1
                result += [number]
                result += [neighbour]

        start += 1
    print(result)
    return count


res = count_zero_neighbours([1,2,-2,0,0,5,-5])
print(res)


