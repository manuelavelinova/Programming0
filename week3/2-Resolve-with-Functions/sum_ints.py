def divisors(n):
    start = 1
    div = []

    while start < n:
        if n % start == 0:
            div += [start]
            start += 1
        else:
            start += 1
        
    return div

def sum_ints(numbers):
    sum = 0
    for number in numbers:
        sum += number
    return sum
