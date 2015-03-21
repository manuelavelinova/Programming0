n = input("Enter  n: ")
n = int(n)

start = 1
sum = 0

while start < n:
    if n % start == 0:
        sum += start
        start += 1
    else:
        start += 1
print("Sum of divisors is: " + str(sum))
