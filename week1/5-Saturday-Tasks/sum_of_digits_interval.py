n = input("Enter n: ")
m = input("Enter m: ")

n = int(n)
m = int(m)
if n < m:
    low = n
    up = m
else:
    low = m
    up = n

start = low

while start <= up:
    n = start
    sum = 0
    while n != 0:
        digit = n % 10
        sum += digit
        n = n // 10
    
    print("The total sum of digits of " + str(start) + " = " + str(sum))
    start += 1
