n = input("Enter n: ")
n = int(n)

isPrime = True
i = 2
if n == 1:
    isPrime = False

while i < n:
    if n % i == 0:
        isPrime = False
        break
    i = i + 1
if isPrime:
    print("The number is prime.")
else:
    print("The number is not prime.")
