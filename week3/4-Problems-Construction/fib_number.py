def fib(n):
    fibo = [1,1]
    start = 0
    end = n - 3
    if n == 1:
        return [1]
    if n == 2:
        return fibo
    else:
        while start <= end:
            fib = fibo[start] + fibo[start + 1]
            fibo += [fib]
            start += 1
    return fibo
        

def fib_number(n):
    fibonArray = fib(n)
    number = 0
    for fibo in fibonArray:
        if fibo >=0 and fibo <= 9:
            number = number * 10 + fibo
        elif fibo >= 10 and fibo <= 99:
            number = number * 100 + fibo
        elif fibo >99:
            number = number * 1000 + fibo
    return number

