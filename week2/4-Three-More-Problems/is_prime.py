n = input("Enter n : ")
n = int(n)

start = 2
isPrime = True

if n == 1:
    isPrime = False
while start < n:
    if n % start == 0:
        isPrime = False
        break
    start += 1

if isPrime:
    print("The number is prime")
else:
    print("The number is not prime")
