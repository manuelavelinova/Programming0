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

def sum_divisors(n):
    return sum_ints(divisors(n))

def is_perfect(n):
    if sum_divisors(n) == n:
        return True
    else:
        return False
