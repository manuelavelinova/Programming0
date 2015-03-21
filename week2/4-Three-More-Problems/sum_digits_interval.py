n = input("Enter n : ")
n = int(n)

m = input("Enter m: " )
m = int(m)

low = 0
up = 0

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
    while n!= 0:
        digit = n % 10
        sum = sum + digit
        n = n // 10

    print("Sum of digits of  " + str(start) + " = " +str(sum))
    start += 1
